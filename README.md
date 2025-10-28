# Quantom

Quantom is a modern Python GUI library built on Tkinter.  
It supports windows, buttons, labels, themes, and simple layouts.

## Installation

Install from Pypi (pip):
pip install quantom

## Syntax example

Example file:

import quantom

quantom.window = quantom.window.Window()

quantom.window.init(
    quantom.window.size("400x300"),

    quantom.window.title("Test Window"),

    quantom.window.bg("gray"),

    quantom.label("Welcome to Quantom!", font_size=30, color="yellow"),

    quantom.button("Click Me!", sizeX=120, sizeY=50, bgColor="black", ftColor="yellow", on_click=lambda: print("Button clicked!"))
)
