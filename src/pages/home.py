"""Home page component with the original counter functionality"""

from dataclasses import dataclass

import flet as ft


@dataclass
@ft.observable
class CounterModel:
    """Observable model for counter state with business logic."""

    counter: int = 0

    def increment(self):
        """Increment counter by 1."""
        self.counter += 1

    def decrement(self):
        """Decrement counter by 1."""
        self.counter -= 1

    def reset(self):
        """Reset counter to 0."""
        self.counter = 0

    @property
    def is_positive(self) -> bool:
        """Check if counter is positive."""
        return self.counter > 0


@ft.component
def CounterView(model: CounterModel):
    """Pure functional counter view component."""
    # Brand colors
    MATCHA_GREEN = "#47905f"
    GOLDEN_OCHRE = "#e1c154"

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
                        ft.IconButton(
                            ft.Icons.REMOVE, on_click=lambda: model.decrement()
                        ),
                        ft.Button(
                            "Reset",
                            on_click=lambda: model.reset(),
                            style=ft.ButtonStyle(
                                color=GOLDEN_OCHRE,
                                text_style=ft.TextStyle(
                                    size=16, weight=ft.FontWeight.W_500
                                ),
                            ),
                        ),
                        ft.IconButton(ft.Icons.ADD, on_click=lambda: model.increment()),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )


@ft.component
def HomePage():
    """Home page container component."""
    model, _ = ft.use_state(CounterModel())
    return CounterView(model)
