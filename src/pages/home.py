"""Home page component with the original counter functionality"""

import flet as ft


@ft.component
def HomePage():
    """Home page with the counter functionality."""

    # Brand colors
    MATCHA_GREEN = "#47905f"
    GOLDEN_OCHRE = "#e1c154"

    text_size, set_text_size = ft.use_state(10)
    counter, set_counter = ft.use_state(0)

    def minus_click(e):
        set_counter(counter - 1)

    def plus_click(e):
        set_counter(counter + 1)

    def text_size_minus_click(e):
        set_text_size(max(10, text_size - 1))

    def text_size_plus_click(e):
        set_text_size(min(200, text_size + 1))

    return ft.SelectionArea(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Infuseth.ink Demo",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color="MATCHA_GREEN",
                ),
                ft.Text("Welcome to our counter app!", size=18, color=GOLDEN_OCHRE),
                ft.Text("You clicked this many times:", size=text_size),
                ft.Text(
                    str(counter),
                    size=text_size,
                    weight=ft.FontWeight.BOLD,
                    color=MATCHA_GREEN,
                ),
                ft.Row(
                    controls=[
                        ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                        ft.IconButton(ft.Icons.ADD, on_click=plus_click),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Text(f"Text size: {text_size}"),
                ft.Row(
                    controls=[
                        ft.IconButton(
                            ft.Icons.ZOOM_OUT, on_click=text_size_minus_click
                        ),
                        ft.IconButton(ft.Icons.ZOOM_IN, on_click=text_size_plus_click),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )
