import tkinter as tk
from .label import Label
from .button import Button

class Window:
    def __init__(self):
        self._root = tk.Tk()
        self._widgets = []

    # Config methods
    def size(self, geom):
        return ("size", geom)

    def title(self, text):
        return ("title", text)

    def bg(self, color):
        return ("bg", color)

    def icon(self, path):
        return ("icon", path)

    # Init method
    def init(self, *args):
        width, height = 400, 300
        title_text = "Quantom App"
        bg_color = "#ffffff"

        for item in args:
            if isinstance(item, tuple):
                key, val = item
                if key == "size":
                    w, h = val.lower().split("x")
                    width, height = int(w), int(h)
                elif key == "title":
                    title_text = val
                elif key == "bg":
                    bg_color = val
                elif key == "icon":
                    try:
                        self._root.iconphoto(True, tk.PhotoImage(file=val))
                    except Exception as e:
                        print(f"Warning: Could not load icon: {e}")
            else:
                self._widgets.append(item)

        self._root.geometry(f"{width}x{height}")
        self._root.title(title_text)
        self._root.configure(bg=bg_color)

        for w in self._widgets:
            w._create(self._root)

        self._root.mainloop()

# ✅ Singleton instance
window = Window()
