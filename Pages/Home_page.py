from nicegui import app as nicegui_app, ui
from Pages.Deck_tab import Deck_tab
from Pages.Card_tab import Card_tab
from Pages.Ask_AI_tab import Ask_AI_tab
from Pages.Learning_Status_tab import Learning_Status_tab
from Database_controller import update_UserDetailById
from Database_controller import get_UserPassword, update_UserEmail, update_UserPassword


def logout() -> None:
    nicegui_app.storage.user.clear()
    ui.navigate.to("/login")


def ApplySetting(user_name, theme, user_email, user_password):
    ThemeDict = {1: "Light", 2: "Dark"}
    theme = ThemeDict[theme]
    if user_name == "":
        user_name = nicegui_app.storage.user.get("userName")
    update_UserDetailById(nicegui_app.storage.user.get("userId"), theme, user_name)
    old_email = nicegui_app.storage.user.get("userEmail")
    old_password = nicegui_app.storage.user.get("password")
    userId = nicegui_app.storage.user.get("userId")
    if old_email != user_email:
        if get_UserPassword(user_email) is not None:
            ui.notification(
                "This email has been registered by another account=>not change email",
                type="warning",
            )
        else:
            nicegui_app.storage.user.update({"userEmail": user_email})
            update_UserEmail(userId, user_email)
    if old_password != user_password:
        nicegui_app.storage.user.update({"password": user_password})
        update_UserPassword(userId, user_password)
    print("Updated account setting")
    ui.notify("Updated account setting", type="positive")
    pass


def AccountSettingDialog():
    print("Running account setting")
    # ui.notify("Change name and theme only", type="warning")
    with ui.dialog() as dialog, ui.card():
        ui.label("Account setting")
        user_name = ui.input(
            label="User name",
            # placeholder=nicegui_app.storage.user.get("userName"),
            value=nicegui_app.storage.user.get("userName"),
        )
        with ui.row():
            ui.label("Default theme")
            if nicegui_app.storage.user.get("theme") == "Light":
                theme_id = 1
            else:
                theme_id = 2
            theme = ui.select({1: "Light", 2: "Dark"}, value=theme_id)
        user_email = ui.input(
            label="User email",
            # placeholder=nicegui_app.storage.user.get("userEmail"),
            value=nicegui_app.storage.user.get("userEmail"),
        )
        user_password = ui.input(
            label="User password",
            # placeholder=nicegui_app.storage.user.get("password"),
            value=nicegui_app.storage.user.get("password"),
            password=True,
            password_toggle_button=True,
        )
        with ui.row():
            ui.button(
                "Apply setting",
                on_click=lambda: ApplySetting(
                    user_name.value, theme.value, user_email.value, user_password.value
                ),
            )
            ui.button("Cancel", on_click=dialog.close)
    dialog.open()
    print("end run account setting")


@ui.page("/home")
def Home_page():
    dark_mode = ui.dark_mode()
    if nicegui_app.storage.user.get("theme") == "Dark":
        dark_mode.enable()
    with ui.header().classes(replace="row items-center") as header:
        ui.button(on_click=lambda: left_drawer.toggle(), icon="menu").props(
            "flat color=white"
        )
        with ui.tabs() as tabs:
            ui.tab("My Decks")
            ui.tab("My Cards")
            ui.tab("Ask AI")
            ui.tab("My learning status")

    with ui.footer(value=False) as footer:
        ui.label("Footer")

    with ui.left_drawer().classes(
        "border"
    ) as left_drawer:  # "bg-blue-100   .classes("100")"
        ui.menu_item(
            "Hello {}".format(nicegui_app.storage.user.get("userName")),
            on_click=lambda: AccountSettingDialog(),
        )
        ui.separator()
        ui.menu_item("Light Mode", on_click=dark_mode.disable)
        ui.menu_item("Dark Mode", on_click=dark_mode.enable)
        ui.separator()
        ui.menu_item(
            "Account type: {}".format(nicegui_app.storage.user.get("accountType"))
        )
        ui.separator()
        ui.menu_item(" Logout 𓉘➜", on_click=logout)

    # with ui.page_sticky(position="bottom-right", x_offset=20, y_offset=20):
    #     ui.button(on_click=footer.toggle, icon="contact_support").props("fab")

    # CurrentDeckId = [None]
    @ui.refreshable
    def Refreshable_Cardtab():
        Card_tab()

    @ui.refreshable
    def Refreshable_Decktab():
        Deck_tab(tabs, Refreshable_Cardtab, Refreshable_Decktab)

    with ui.tab_panels(tabs, value="My Decks").classes("w-full"):
        with ui.tab_panel("My Decks"):
            Refreshable_Decktab()
        with ui.tab_panel("My Cards"):
            Refreshable_Cardtab()
        with ui.tab_panel("Ask AI"):
            Ask_AI_tab()
        with ui.tab_panel("My learning status"):
            Learning_Status_tab()
