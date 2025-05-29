from nicegui import app as nicegui_app, ui
from Pages.Deck_tab import Deck_tab
from Pages.Card_tab import Card_tab
from Pages.Ask_AI_tab import Ask_AI_tab


def logout() -> None:
    nicegui_app.storage.user.clear()
    ui.navigate.to("/login")


def AccountSettingDialog():
    print("Running account setting")
    with ui.dialog() as dialog, ui.card():
        ui.label("Account setting")
        user_name = ui.input(
            label="User name",
            placeholder="your name",
        )
        with ui.row():
            ui.label("Default theme")
            theme = ui.select({1: "Light", 2: "Dark"}, value=1)
        user_email = ui.input(
            label="User email",
            placeholder="your email",
        )
        user_password = ui.input(
            label="User password",
            placeholder="your password",
        )
        with ui.row():
            ui.button("Close", on_click=dialog.close)
            ui.button("Apply")
    dialog.open()
    print("end run account setting")


def Home_page():
    dark_mode = ui.dark_mode()
    with ui.header().classes(replace="row items-center") as header:
        ui.button(on_click=lambda: left_drawer.toggle(), icon="menu").props(
            "flat color=white"
        )
        with ui.tabs() as tabs:
            ui.tab("My Decks")
            ui.tab("My Cards")
            ui.tab("Ask AI")

    with ui.footer(value=False) as footer:
        ui.label("Footer")

    with ui.left_drawer().classes("100") as left_drawer:  # "bg-blue-100"
        ui.menu_item("Light Mode", on_click=dark_mode.disable)
        ui.menu_item("Dark Mode", on_click=dark_mode.enable)
        ui.menu_item("Account type:")
        ui.menu_item("Account setting", on_click=lambda: AccountSettingDialog())
        ui.menu_item(" Logout 𓉘➜", on_click=logout)

    with ui.page_sticky(position="bottom-right", x_offset=20, y_offset=20):
        ui.button(on_click=footer.toggle, icon="contact_support").props("fab")

    CurrentDeckId = [None]
    with ui.tab_panels(tabs, value="My Decks").classes("w-full"):
        with ui.tab_panel("My Decks"):
            Deck_tab(tabs, CurrentDeckId)
        with ui.tab_panel("My Cards"):
            Card_tab(CurrentDeckId)
        with ui.tab_panel("Ask AI"):
            Ask_AI_tab()
