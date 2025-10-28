from Quantom import Window, Button, Label, Theme

def test_window_creation():
    win = Window(title="Test Window", size=(200, 100))
    assert win._root.title() == "Test Window"

def test_button_label_creation():
    win = Window(title="Test Window")
    btn = Button(win, text="Test Button")
    lbl = Label(win, text="Test Label")
    assert btn._widget.cget("text") == "Test Button"
    assert lbl._widget.cget("text") == "Test Label"

def test_themes():
    win = Window(title="Theme Test", theme="DARK")
    assert win.theme["bg"] == "#2e2e2e"

if __name__ == "__main__":
    test_window_creation()
    test_button_label_creation()
    test_themes()
    print("All tests passed!")
