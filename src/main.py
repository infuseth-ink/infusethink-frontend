"""Infuseth.ink main application with navigation"""

from collections.abc import Callable
from dataclasses import dataclass
import logging

import flet as ft

from components.footer import Footer
from pages.brand_story import create_brand_story_page
from pages.home import HomePage
from pages.not_found import NotFoundPage

logging.basicConfig(level=logging.INFO)
logging.getLogger("flet_components").setLevel(logging.INFO)


@dataclass(frozen=True)
class ThemeContextValue:
    mode: ft.ThemeMode
    toggle: Callable[[], None]


ThemeContext = ft.create_context(ThemeContextValue(ft.ThemeMode.LIGHT, lambda: None))


@ft.observable
@dataclass
class AppModel:
    route: str
    theme_mode: ft.ThemeMode = ft.ThemeMode.LIGHT

    def route_change(self, e: ft.RouteChangeEvent):
        print("Route changed from:", self.route, "to:", e.route)
        self.route = e.route

    async def view_popped(self, e: ft.ViewPopEvent):
        print("View popped")
        views = ft.unwrap_component(ft.context.page.views)
        if len(views) > 1:
            await ft.context.page.push_route(views[-2].route)

    def toggle_theme(self):
        self.theme_mode = (
            ft.ThemeMode.DARK
            if self.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )


@ft.component
def ThemeToggle():
    theme = ft.use_context(ThemeContext)
    return ft.Switch(
        label="Dark mode" if theme.mode == ft.ThemeMode.LIGHT else "Light mode",
        value=theme.mode == ft.ThemeMode.DARK,
        on_change=lambda _: theme.toggle(),
    )


@ft.component
def AppBar():
    MATCHA_GREEN = "#47905f"
    return ft.AppBar(
        title=ft.Text("Infuseth.ink", size=20, weight=ft.FontWeight.BOLD),
        bgcolor=MATCHA_GREEN,
        color=ft.Colors.WHITE,
        center_title=True,
        actions=[ThemeToggle()],
    )


@ft.component
def InfusethApp():
    app, _ = ft.use_state(AppModel(route=ft.context.page.route))

    # subscribe to page events as soon as possible
    ft.context.page.on_route_change = app.route_change
    ft.context.page.on_view_pop = app.view_popped

    # stable callback (doesn't change identity each render)
    toggle = ft.use_callback(lambda: app.toggle_theme(), dependencies=[app.theme_mode])

    # memoize the provided value so its identity changes only when mode changes
    theme_value = ft.use_memo(
        lambda: ThemeContextValue(mode=app.theme_mode, toggle=toggle),
        dependencies=[app.theme_mode, toggle],
    )

    ft.on_mounted(
        lambda: print("Page size:", ft.context.page.width, ft.context.page.height)
    )

    def update_theme_mode():
        print("Theme mode changed to:", app.theme_mode)
        ft.context.page.theme_mode = app.theme_mode

    ft.on_updated(update_theme_mode, [app.theme_mode])

    # Get current page content based on route
    def get_page_content():
        match app.route:
            case "/":
                return HomePage()
            case "/brand-story":
                return create_brand_story_page()
            case _:
                return NotFoundPage()

    return ThemeContext(
        theme_value,
        lambda: [
            ft.View(
                route=app.route,
                appbar=AppBar(),
                controls=[
                    ft.Container(
                        content=get_page_content(),
                        expand=True,
                    ),
                    Footer(),
                ],
                spacing=0,
                padding=0,
            ),
        ],
    )


ft.run(lambda page: page.render_views(InfusethApp))
