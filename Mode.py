from nicegui import ui
def Mode():
     dark_mode=ui.dark_mode()
     with ui.row().classes("w-full items-center"):
             #result=ui.label().classes("mr-auto")
             with ui.button(icon="menu"):
                 with ui.menu() as menu:    
                      ui.menu_item("Light Mode",on_click=dark_mode.disable)
                      ui.menu_item("Dark Mode",on_click=dark_mode.enable)