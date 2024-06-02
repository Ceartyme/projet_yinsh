import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

class Server:
    def __init__(self):
        self.clients = []
        
        self.root = tk.Tk()
        self.root.title("Serveur")
        
        self.chat_area = scrolledtext.ScrolledText(self.root)
        self.chat_area.pack(padx=20, pady=5)
        self.chat_area.config(state='disabled')
        
        self.msg_entry = tk.Entry(self.root, width=50)
        self.msg_entry.pack(padx=20, pady=5)
        self.msg_entry.bind("<Return>", self.send_message)

    def start(self, host='127.0.0.1', port=5000):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        self.start_server_thread()
        self.root.mainloop()

    def start_server_thread(self):
        threading.Thread(target=self.accept_clients, daemon=True).start()

    def accept_clients(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            self.clients.append(client_socket)
            threading.Thread(target=self.handle_client, args=(client_socket,), daemon=True).start()
            self.display_message(f"Nouvelle connexion entrante !")

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    self.display_message(f"Client : {message}")
                    self.broadcast(f"You : {message}", client_socket)
                else:
                    client_socket.close()
                    self.clients.remove(client_socket)
                    break
            except:
                continue

    def broadcast(self, message, sender_socket):
        for client in self.clients:
            if client != sender_socket:
                client.send(message.encode())

    def send_message(self, event):
        message = self.msg_entry.get().strip()
        if len(message) > 0 :
            self.msg_entry.delete(0, tk.END)
            self.display_message(f"You : {message}")
            self.broadcast(f"Server : {message}", None)

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + '\n')
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

if __name__ == "__main__":
    server = Server()
    server.start(host='127.0.0.1', port=5000)
