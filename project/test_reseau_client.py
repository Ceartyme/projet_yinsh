import socket
import threading
import tkinter as tk

class TestLocal:
    def __init__(self, root):
        self.root = root
        self.root.title("Test Client")
        
        self.placeholder_text = "Entrez votre message ici"
        self.history = []

        self.entry = tk.Entry(self.root, fg='grey')
        self.entry.insert(0, self.placeholder_text)
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.restore_placeholder)
        self.entry.bind("<Key>", self.display_text)
        self.entry.pack(padx=10, pady=10)

        self.text_label = tk.Label(self.root, text="", bg="lightgrey", padx=10, pady=5, justify="left")
        self.text_label.pack(padx=10, pady=(0, 10))

    def clear_placeholder(self, event):
        if self.entry.get() == self.placeholder_text:
            self.entry.delete(0, tk.END)
            self.entry.config(fg='black')

    def restore_placeholder(self, event):
        if not self.entry.get():
            self.entry.insert(0, self.placeholder_text)
            self.entry.config(fg='grey')

    def display_text(self, event):
        if event.keysym == "Return":
            input_text = self.entry.get().strip()
            if input_text:
                if len(self.history) >= 10:
                    self.history.pop(0)
                self.history.append(input_text)
                self.update_label()
                self.entry.delete(0, tk.END)
            else:
                pass

    def update_label(self):
        self.text_label.config(text="\n".join(self.history))

def receive_message(client_socket):
    while True:
        try:
            response = client_socket.recv(1024)
            print(f"\nHôte : {response.decode('utf-8')}")
        except ConnectionResetError:
            break

def connect():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9999))

    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
    receive_thread.start()

    while True:
        try:
            message = input("Entrez votre message : ")
            print(f"Invité : {message}")
            client_socket.send(message.encode('utf-8'))
        except ConnectionResetError:
            break

    client_socket.close()

main()