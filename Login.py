from nicegui import ui
from Mode import Mode

# Hàm xử lý đăng nhập
def handle_login(username, password):
    if username == 'admin' and password == '123':  # Kiểm tra tài khoản/mật khẩu
        ui.notify('Đăng nhập thành công!')  # Thông báo thành công
        ui.run_javascript('window.location.href="/Chatbox";')
    else:
        ui.notify('❌ Sai tài khoản hoặc mật khẩu!')  # Thông báo lỗi

# Tạo trang login
def login_page():
    @ui.page('/')  # Đây là trang chính (route '/')
    def login():
         Mode()
         with ui.card().classes('absolute-center'):
            # Tiêu đề login
            ui.label('🔐 Đăng nhập').classes('text-2xl font-bold mb-4')

            # Nhập tên đăng nhập
            username = ui.input('Tên đăng nhập').classes('w-full mb-4')

            # Nhập mật khẩu
            password = ui.input('Mật khẩu').props('type=password').classes('w-full mb-4')

            # Nút đăng nhập
            ui.button('Đăng nhập', color='blue', on_click=lambda: handle_login(username.value, password.value))

            # Link đăng ký và quên mật khẩu
            ui.link('Quên mật khẩu', '/reset_password')
            ui.link('Đăng ký', '/signup')
        


        

