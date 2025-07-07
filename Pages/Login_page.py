from nicegui import app as nicegui_app, ui
from typing import Optional
from fastapi.responses import RedirectResponse
from Pages.Menu_bar import Menu_bar
from Database_controller import (
    get_UserPassword,
    get_UserId,
    get_AuthorName,
    get_UserDetailById,
    insert_User,
)
import psycopg2
import ProtectedData

# in reality users passwords would obviously need to be hashed
passwords = {"user1": "pass1", "user2": "pass2"}
unrestricted_page_routes = {"/login"}


def try_login(
    user_email_login, password_login, redirect_to
) -> None:  # local function to avoid passing username and password as arguments
    # print(user_email_login, password_login)
    CheckPassword = get_UserPassword(user_email_login.value)
    if (
        password_login.value == CheckPassword
    ):  # passwords.get(user_email_login.value) ==password_login.value:
        nicegui_app.storage.user.update(
            {
                "userEmail": user_email_login.value,
                "authenticated": True,
                "userId": get_UserId(user_email_login.value),
                "password": CheckPassword,
                "learning_progress": dict(),
            }
        )
        nicegui_app.storage.user.update(
            get_UserDetailById(nicegui_app.storage.user.get("userId"))
        )
        ui.navigate.to(redirect_to)  # go back to where the user wanted to go
    else:
        ui.notify("Wrong username or password", color="negative")


def try_register(userType: str, user_name: str, email: str, pass1: str, pass2: str):
    if pass1 != pass2:
        ui.notification("Wrong confirm password", type="negative")
    elif get_UserPassword(email) is not None:
        ui.notification(
            "This email has been registered\nby another account", type="negative"
        )
    else:
        insert_User(userType, "Light", pass1, user_name, email)
        ui.notification("Created new account", type="positive")


def Login_tab(redirect_to):
    with ui.row().classes("w-full").style("min-width:300px"):
        ui.space()
        with ui.card().classes("items-center").style("min-width:300px"):
            ui.label("Login")
            user_email_login = (
                ui.input(
                    label="Email",
                    placeholder="your email",
                    # validation={"Input too long": lambda value: len(value) < 30},
                ).classes("items-center")
            ).style("min-width:300px")
            password_login = (
                ui.input(
                    label="Password",
                    placeholder="your password",
                    password=True,
                    password_toggle_button=True,
                ).classes("items-center")
            ).style("min-width:300px")
            ui.button(
                "Login",
                on_click=lambda: try_login(
                    user_email_login, password_login, redirect_to
                ),
            ).classes("items-center").style("min-width:300px")
        ui.space()


def Register_tab():
    with ui.row().classes("w-full").style("min-width:300px"):
        ui.space()
        with ui.card().classes("items-center").style("min-width:300px"):
            ui.label("Register")
            user_name = (
                ui.input(
                    label="Your name",
                    placeholder="your name",
                    value="My name",
                    # validation={"Input too long": lambda value: len(value) < 20},
                ).classes("items-center")
            ).style("min-width:300px")

            user_email = (
                ui.input(
                    label="Email",
                    placeholder="your email",
                    # validation={"Input too long": lambda value: len(value) < 20},
                ).classes("items-center")
            ).style("min-width:300px")

            password1 = (
                ui.input(
                    label="Password",
                    placeholder="your password",
                    password=True,
                    password_toggle_button=True,
                ).classes("items-center")
            ).style("min-width:300px")

            password2 = (
                ui.input(
                    label="Confirm password",
                    placeholder="your password",
                    password=True,
                    password_toggle_button=True,
                ).classes("items-center")
            ).style("min-width:300px")
            Type = ["public", "premium"]
            with ui.row():
                ui.label("Account type: ")
                UserType = ui.select(
                    Type,
                    value="public",
                    label="Account type:",
                ).style("min-width:150px")
            ui.button(
                "Register",
                on_click=lambda: try_register(
                    UserType.value,
                    user_name.value,
                    user_email.value,
                    password1.value,
                    password2.value,
                ),
            ).classes("items-center").style("min-width:300px")
        ui.space()


@ui.page("/login")
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
