import flet as ft


@ft.component
def App():
    count, set_count = ft.use_state(0)

    return ft.View(
        appbar=ft.AppBar(
            title=ft.Text("Counter App"),
            bgcolor=ft.Colors.GREEN,
            center_title=True,
            actions=[
                ft.IconButton(ft.Icons.SETTINGS),
                ft.IconButton(ft.Icons.INFO),
            ],
        ),
        floating_action_button=ft.FloatingActionButton(
            icon=ft.Icons.ADD, on_click=lambda: set_count(count + 1)
        ),
        controls=[
            ft.SafeArea(
                ft.Container(
                    ft.SelectionArea(content=ft.Text(value=f"{count}", size=50)),
                    alignment=ft.Alignment.CENTER,
                ),
                expand=True,
            )
        ],
    )


ft.run(lambda page: page.render_views(App))
