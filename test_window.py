import quantom

quantom.window.init(
    quantom.window.size("500x350"),
    quantom.window.title("Quantom UI"),
    quantom.window.bg("gray"),

    quantom.Label(
        "Welcome to Quantom!",
        font_size=50,
        color="white",
        bgColor="gray"
    ),
    quantom.Button(
        "Test button",
        sizeX=120,
        sizeY=60,
        bgColor="black",
        ftColor="yellow",
        on_click=lambda: print("Button Clicked!")
    )
)
