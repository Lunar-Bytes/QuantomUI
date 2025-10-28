import tkinter as tk

class Label:
    def __init__(self, text, font_size=20, color="black", bgColor=None):
        self.text = text
        self.font_size = font_size
        self.color = color
        self.bgColor = bgColor  # New background color property

    def _create(self, parent):
        tk.Label(
            parent,
            text=self.text,
            fg=self.color,
            bg=self.bgColor,  # apply bg color if provided
            font=("Arial", self.font_size)
        ).pack(pady=10)
