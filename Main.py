from nicegui import ui
from Signup import signup_page  # Import trang đăng ký từ file Signup.py
from Login import login_page
from reset_password import reset_password_page
from Chatbox import chatbox_ui
from Decks import flashcard_list_page
# Gọi trang đăng ký
login_page()
signup_page()
reset_password_page()
chatbox_ui()
flashcard_list_page()

ui.run()
