from nicegui import ui
from signup import signup_page
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
