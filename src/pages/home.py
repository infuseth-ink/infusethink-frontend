"""Home page component with the original counter functionality"""

from dataclasses import dataclass

import flet as ft


@dataclass
@ft.observable
class CounterModel:
    """Observable model for counter state."""

    counter: int = 0


@ft.component
def HomePage():
    """Home page with the counter functionality."""

    # Brand colors
    MATCHA_GREEN = "#47905f"
    GOLDEN_OCHRE = "#e1c154"

    model, _ = ft.use_state(CounterModel())

    def minus_click(e):
        model.counter -= 1

    def plus_click(e):
        model.counter += 1

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
                ft.Text(
                    str(model.counter),
                    size=24,
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
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )
