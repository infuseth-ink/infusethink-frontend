"""Footer component for navigation"""

import asyncio

import flet as ft


@ft.component
def Footer():
    """Footer with navigation links using routing."""

    # Brand colors
    MATCHA_GREEN = "#47905f"
    GOLDEN_OCHRE = "#e1c154"

    def on_home_click(e):
        asyncio.create_task(ft.context.page.push_route("/"))  # noqa: RUF006

    def on_brand_story_click(e):
        asyncio.create_task(ft.context.page.push_route("/brand-story"))  # noqa: RUF006

    return ft.Container(
        content=ft.Row(
            controls=[
                ft.TextButton(
                    "Home",
                    on_click=on_home_click,
                    style=ft.ButtonStyle(
                        color=MATCHA_GREEN,
                        text_style=ft.TextStyle(size=16, weight=ft.FontWeight.W_500),
                    ),
                ),
                ft.Text("•", size=16, color=GOLDEN_OCHRE),
                ft.TextButton(
                    "Brand Story",
                    on_click=on_brand_story_click,
                    style=ft.ButtonStyle(
                        color=MATCHA_GREEN,
                        text_style=ft.TextStyle(size=16, weight=ft.FontWeight.W_500),
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        ),
        padding=ft.Padding.symmetric(vertical=20, horizontal=20),
        bgcolor=ft.Colors.with_opacity(0.05, MATCHA_GREEN),
        border=ft.Border.only(top=ft.BorderSide(1, MATCHA_GREEN)),
    )
