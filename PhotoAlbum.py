import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class PhotoAlbum:
    def __init__(self, root):
        self.root = root
        self.root.title("My Photo Album")
        self.root.geometry("950x650")
        self.root.configure(bg="#20232a")

        self.photos = []
        self.current_index = 0
        self.current_image = None

        # Heading
        title = tk.Label(
            root,
            text="📸 My Photo Album",
            font=("Arial", 26, "bold"),
            bg="#20232a",
            fg="white"
        )
        title.pack(pady=15)

        # Image display
        self.image_label = tk.Label(
            root,
            bg="#30343b",
            width=700,
            height=400
        )
        self.image_label.pack(pady=10, expand=True)

        # Filename
        self.filename_label = tk.Label(
            root,
            text="No photo selected",
            font=("Arial", 12),
            bg="#20232a",
            fg="white"
        )
        self.filename_label.pack(pady=5)

        # Buttons
        button_frame = tk.Frame(root, bg="#20232a")
        button_frame.pack(pady=15)

        tk.Button(
            button_frame, text="➕ Add Photos",
            command=self.add_photos,
            width=14, bg="#28a745", fg="white"
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame, text="⬅ Previous",
            command=self.previous_photo,
            width=14, bg="#007bff", fg="white"
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame, text="Next ➡",
            command=self.next_photo,
            width=14, bg="#007bff", fg="white"
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame, text="🗑 Remove",
            command=self.remove_photo,
            width=14, bg="#dc3545", fg="white"
        ).grid(row=0, column=3, padx=5)

    def add_photos(self):
        files = filedialog.askopenfilenames(
            title="Select Photos",
            filetypes=[
                ("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif *.webp")
            ]
        )

        for file in files:
            if file not in self.photos:
                self.photos.append(file)

        if self.photos:
            self.current_index = 0
            self.show_photo()

    def show_photo(self):
        if not self.photos:
            return

        file = self.photos[self.current_index]

        try:
            image = Image.open(file)
            image.thumbnail((750, 430))

            self.current_image = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.current_image)

            self.filename_label.config(
                text=f"{os.path.basename(file)}  |  "
                     f"{self.current_index + 1}/{len(self.photos)}"
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def next_photo(self):
        if self.photos:
            self.current_index = (
                self.current_index + 1
            ) % len(self.photos)
            self.show_photo()

    def previous_photo(self):
        if self.photos:
            self.current_index = (
                self.current_index - 1
            ) % len(self.photos)
            self.show_photo()

    def remove_photo(self):
        if not self.photos:
            return

        self.photos.pop(self.current_index)

        if self.photos:
            self.current_index %= len(self.photos)
            self.show_photo()
        else:
            self.current_index = 0
            self.current_image = None
            self.image_label.config(image="")
            self.filename_label.config(text="No photo selected")


# Run application
if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoAlbum(root)
    root.mainloop()