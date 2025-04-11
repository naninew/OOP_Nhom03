from nicegui import ui
from Mode import Mode
@ui.page('/signup')
def signup_page():
    Mode()
    with ui.column().classes('absolute-center'):
        

        ui.label('Sign Up').classes('text-3xl font-bold mb-6')

        email_input = ui.input('Email').props('type=email').classes('w-80')
        username_input = ui.input('Username').classes('w-80')
        password_input = ui.input('Password').props('type=password').classes('w-80')

        def handle_signup():
            email = email_input.value
            username = username_input.value
            password = password_input.value

            if not email or not username or not password:
                ui.notify('Please fill in all fields', color='negative')
                return

            ui.notify(f'Account for {username} created successfully!', color='positive')

        ui.button('Sign Up', on_click=handle_signup).classes(
            'w-40 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4'
        )
       # ui.link('Already have an account? Log in', '/').classes('mt-4 text-blue-500 hover:underline')
        ui.link('Back to Login', '/').classes('mt-4 text-blue-500 hover:underline')
