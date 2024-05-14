import tkinter as tk

class TestLocal:
    def __init__(self, root):
        self.root = root
        self.root.title("Zone de texte avec texte grisé")

        self.placeholder_text = "Entrez votre texte ici"
        self.history = []

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=10, pady=10)

        self.history_frame = tk.Frame(self.main_frame, width=200, height=200, bg="lightgrey")
        self.history_frame.pack(side=tk.TOP)

        self.text_label = tk.Label(self.history_frame, text="", bg="lightgrey", padx=10, pady=5, justify="left")
        self.text_label.pack(padx=10, pady=(0, 10))

        self.entry = tk.Entry(self.main_frame, fg='grey')
        self.entry.insert(0, self.placeholder_text)
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.restore_placeholder)
        self.entry.bind("<Key>", self.display_text)
        self.entry.pack(padx=10, pady=10)

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
            input_text = self.entry.get().strip()  # Supprimer les espaces en début et fin de texte
            if input_text:  # Vérifier si le texte n'est pas vide après suppression des espaces
                if len(self.history) >= 10:
                    self.history.pop(0)  # Supprimer le premier message
                self.history.append(input_text)
                self.update_label()
                self.entry.delete(0, tk.END)  # Effacer le texte de la zone de texte après l'envoi
            else:
                # Si le texte est vide après suppression des espaces, ne rien faire
                pass

    def update_label(self):
        self.text_label.config(text="\n".join(self.history))

def main():
    root = tk.Tk()
    root.geometry('600x600')
    app = TestLocal(root)
    root.mainloop()

if __name__ == "__main__":
    main()
