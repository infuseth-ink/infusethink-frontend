"""404 Not Found page for Infuseth.ink"""

import asyncio

import flet as ft


@ft.component
def NotFoundPage():
    """404 page with navigation back to home."""

    # Brand colors
    MATCHA_GREEN = "#47905f"
    GOLDEN_OCHRE = "#e1c154"
    PARCHMENT_BEIGE = "#f6f0dd"

    def go_home_click(e):
        asyncio.create_task(ft.context.page.push_route("/"))  # noqa: RUF006

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(height=50),  # Top spacing
                ft.Icon(
                    ft.Icons.ERROR_OUTLINE,
                    size=120,
                    color=GOLDEN_OCHRE,
                ),
                ft.Text(
                    "404",
                    size=72,
                    weight=ft.FontWeight.BOLD,
                    color=MATCHA_GREEN,
                ),
                ft.Text(
                    "Page Not Found",
                    size=32,
                    weight=ft.FontWeight.W_500,
                    color=MATCHA_GREEN,
                ),
                ft.Container(height=20),
                ft.Text(
                    "Oops! The page you're looking for doesn't exist.",
                    size=18,
                    color=ft.Colors.BLACK54,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "It might have been moved, deleted, or you entered the wrong URL.",
                    size=16,
                    color=ft.Colors.BLACK54,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=30),
                ft.Button(
                    "Go Home",
                    on_click=go_home_click,
                    style=ft.ButtonStyle(
                        bgcolor=MATCHA_GREEN,
                        color=ft.Colors.WHITE,
                        text_style=ft.TextStyle(size=16, weight=ft.FontWeight.W_500),
                        shape=ft.RoundedRectangleBorder(radius=8),
                        padding=ft.Padding.symmetric(horizontal=30, vertical=15),
                    ),
                ),
                ft.Container(height=50),  # Bottom spacing
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
        bgcolor=PARCHMENT_BEIGE,
        padding=ft.Padding.all(40),
        expand=True,
    )
