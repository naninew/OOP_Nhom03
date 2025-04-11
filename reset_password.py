# ResetPassword.py
from nicegui import ui
from Mode import Mode
def reset_password_page():
    @ui.page('/reset_password')
    def reset_password():
        Mode()  
        with ui.card().classes('absolute-center'):
            # Tiêu đề reset mật khẩu
            ui.label('🔑 Quên mật khẩu').classes('text-2xl font-bold mb-4')

            # Nhập email
            email = ui.input('Email của bạn').classes('w-full mb-4')

            # Nút reset mật khẩu
            ui.button('Gửi liên kết khôi phục mật khẩu', color='orange', on_click=lambda: ui.notify(f'Liên kết khôi phục đã gửi đến {email.value}'))

             #Link quay lại trang login
            ui.link('Quay lại Đăng nhập','/')
