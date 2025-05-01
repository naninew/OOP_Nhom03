from nicegui import app as nicegui_app, ui
from Pages.Deck_tab import Deck_tab
from Pages.Card_tab import Card_tab
from Pages.Ask_AI_tab import Ask_AI_tab


# def logout() -> None:
#     nicegui_app.storage.user.clear()
#     ui.navigate.to("/login")
def logout() -> None:
    nicegui_app.storage.user.clear()
    ui.navigate.to("/login")


def Home_page():
    # Menu_bar()
    # with ui.column().classes("absolute-center items-center"):
    #     ui.label(f'Hello {nicegui_app.storage.user["user_email"]}!').classes("text-2xl")
    #     ui.button(on_click=logout, icon="logout").props("outline round")
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
        # ui.label("Side menu")
        ui.menu_item("Light Mode", on_click=dark_mode.disable)
        ui.menu_item("Dark Mode", on_click=dark_mode.enable)
        ui.menu_item(" Logout 𓉘➜", on_click=logout)

    with ui.page_sticky(position="bottom-right", x_offset=20, y_offset=20):
        ui.button(on_click=footer.toggle, icon="contact_support").props("fab")

    CurrentDeckId = [None]
    with ui.tab_panels(tabs, value="My Decks").classes("w-full"):
        with ui.tab_panel("My Decks"):
            # ui.label("Content of A")
            Deck_tab(tabs, CurrentDeckId)
        with ui.tab_panel("My Cards"):
            # ui.label("Content of B")
            Card_tab(CurrentDeckId)
        with ui.tab_panel("Ask AI"):
            # ui.label("Content of C")
            Ask_AI_tab()
