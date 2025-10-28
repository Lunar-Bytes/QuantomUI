import tkinter as tk

class Button:
    def __init__(self, text, sizeX=100, sizeY=50, bgColor="lightgray", ftColor="black", on_click=None):
        self.text = text
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.bgColor = bgColor
        self.ftColor = ftColor
        self.on_click = on_click

    def _create(self, parent):
        tk.Button(
            parent,
            text=self.text,
            width=self.sizeX//10,
            height=self.sizeY//20,
            bg=self.bgColor,
            fg=self.ftColor,
            command=self.on_click
        ).pack(pady=5)
