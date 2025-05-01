from nicegui import app as nicegui_app, ui
from typing import Optional
from fastapi.responses import RedirectResponse
from Pages.Menu_bar import Menu_bar
from Database_controller import get_UserPassword, get_UserId

# in reality users passwords would obviously need to be hashed
passwords = {"user1": "pass1", "user2": "pass2"}
unrestricted_page_routes = {"/login"}


def try_login(
    user_email_login, password_login, redirect_to
) -> None:  # local function to avoid passing username and password as arguments
    # print(user_email_login, password_login)
    if password_login.value == get_UserPassword(
        user_email_login.value
    ):  # passwords.get(user_email_login.value) ==password_login.value:
        nicegui_app.storage.user.update(
            {
                "userEmail": user_email_login.value,
                "authenticated": True,
                "userId": get_UserId(user_email_login.value),
            }
        )
        ui.navigate.to(redirect_to)  # go back to where the user wanted to go
    else:
        ui.notify("Wrong username or password", color="negative")


def Login_tab(redirect_to):
    with ui.row().classes("w-full items-center"):
        ui.space()
        with ui.card().classes("w-1/2 items-center"):
            ui.label("Login")
            user_email_login = (
                ui.input(
                    label="Email",
                    placeholder="your email",
                    # on_change=lambda e: result_email.set_text(
                    #     "you typed: " + e.value
                    # ),
                    validation={"Input too long": lambda value: len(value) < 30},
                ).on(
                    "keydown.enter",
                    lambda: try_login(user_email_login, password_login, redirect_to),
                )
            ).classes("w-1/2 items-center")

            result_email = ui.label()

            password_login = (
                ui.input(
                    label="Password",
                    placeholder="your password",
                    # on_change=lambda e: result_password.set_text(
                    #     "you typed: " + e.value
                    # ),
                    validation={"Input too long": lambda value: len(value) < 30},
                    password=True,
                    password_toggle_button=True,
                ).on(
                    "keydown.enter",
                    lambda: try_login(user_email_login, password_login, redirect_to),
                )
            ).classes("w-1/2 items-center")
            result_password = ui.label()
            # ui.button(
            #     "Login", on_click=lambda: ui.label("Login success")
            # ).classes("w-1/2 items-center")
            ui.button(
                "Login",
                on_click=lambda: try_login(
                    user_email_login, password_login, redirect_to
                ),
            ).classes("w-1/2 items-center")
            # ui.timer(1.0, lambda: ui.label("Tick!"), once=True)
        ui.space()


def Register_tab():
    with ui.row().classes("w-full"):
        ui.space()
        with ui.card().classes("w-1/2 items-center"):
            ui.label("Register")
            user_email = ui.input(
                label="Email",
                placeholder="your email",
                on_change=lambda e: result_email.set_text("you typed: " + e.value),
                validation={"Input too long": lambda value: len(value) < 20},
            ).classes("w-1/2 items-center")
            result_email = ui.label()

            password1 = ui.input(
                label="Password",
                placeholder="your password",
                on_change=lambda e: result_password.set_text("you typed: " + e.value),
                validation={"Input too long": lambda value: len(value) < 20},
                password=True,
                password_toggle_button=True,
            ).classes("w-1/2 items-center")
            result_password = ui.label()

            password2 = ui.input(
                label="Confirm password",
                placeholder="your password",
                on_change=lambda e: result_confirm_password.set_text(
                    "you typed: " + e.value
                ),
                validation={"Input too long": lambda value: len(value) < 20},
                password=True,
                password_toggle_button=True,
            ).classes("w-1/2 items-center")
            result_confirm_password = ui.label()

            ui.button(
                "Register", on_click=lambda: ui.label("Register Success!")
            ).classes("w-1/2 items-center")
            # ui.timer(1.0, lambda: ui.label("Tick!"), once=True)
        ui.space()


def Login_page(redirect_to: str = "/home") -> Optional[RedirectResponse]:

    if nicegui_app.storage.user.get("authenticated", False):
        return RedirectResponse("/home")

    Menu_bar()

    with ui.tabs().classes("w-full") as tabs:
        Login = ui.tab("Login")
        Register = ui.tab("Register")

    with ui.tab_panels(tabs, value=Login).classes("w-full"):
        with ui.tab_panel(Login):
            Login_tab(redirect_to)
        with ui.tab_panel(Register):
            Register_tab()
