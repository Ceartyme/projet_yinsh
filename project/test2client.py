import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

class Client:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Client")
        
        self.chat_area = scrolledtext.ScrolledText(self.root)
        self.chat_area.pack(padx=20, pady=5)
        self.chat_area.config(state='disabled')
        
        self.msg_entry = tk.Entry(self.root, width=50)
        self.msg_entry.pack(padx=20, pady=5)
        self.msg_entry.bind("<Return>", self.send_message)

    def start(self, host='127.0.0.1', port=5000):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        self.start_receiving_thread()
        self.root.mainloop()

    def start_receiving_thread(self):
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if message:
                    self.display_message(message)
            except:
                break

    def send_message(self, event):
        message = self.msg_entry.get().strip()
        if len(message) > 0 :
            self.msg_entry.delete(0, tk.END)
            self.client_socket.send(message.encode())
            self.display_message(f"Vous : {message}")

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + '\n')
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

if __name__ == "__main__":
    client = Client()
    client.start(host='127.0.0.1', port=5000)
