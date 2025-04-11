from nicegui import ui
from Mode import Mode
@ui.page('/Chatbox')
def chatbox_ui():
    # Giao diện chính
    Mode()  
    with ui.column().style('height: 100vh;width:100vw;justify-content: center; align-items: center; background-color: #2C2C2C; padding: 20px; border-radius: 10px;'):
        
        # Thanh Menu
       

        # Khu vực Chatbot
     with ui.card().style('background-color: #424242; width: 550px; height: 350px; border-radius: 10px; margin: 20px auto; padding: 15px;'):
         ui.label("Chatbot").style("font-size: 24px; font-weight: bold; color: white; margin-bottom: 10px; text-align: center;")
            
                # Row chứa input và button
         with ui.row().style('padding: 10px; gap: 10px; justify-content: center;'):
             search_field = ui.input(label="Nhập từ cần tra...").style("background-color: #757575; color: white; border-radius: 5px; width: 350px;")
             ui.button("Search").style("background-color: #1E88E5; color: white; border-radius: 5px; padding: 10px;").on_click(lambda: ui.notify(f"Tìm kiếm: {search_field.value}"))
            
            # Textarea hiển thị
         ui.textarea().style('background-color: #616161; color: white; border-radius: 5px; height: 150px; width: 100%; padding: 10px;').props("readonly")

        # Khu vực Từ Vựng
     with ui.card().style('background-color: #424242; width: 300px; height: 120px; border-radius: 10px; margin-top: 20px; padding: 15px; display: flex; flex-direction: column; justify-content: center; align-items: flex-start; gap: 5px;'):
        ui.label('Từ:').style('font-size: 18px; color: white; font-weight: bold;')
        ui.label('(Hiển thị từ)').style('font-size: 18px; font-weight: bold; color: #FFEB3B;')
        ui.label('Nghĩa:').style('font-size: 16px; color: white; margin-top: 5px;')
        ui.label('(Hiển thị nghĩa)').style('font-size: 16px; color: #FFEB3B;')

        # Các nút chức năng
     with ui.row().style('justify-content: center; gap: 15px; margin-top: 20px;'):
            ui.button("ADD").style("background-color: #FF9800; color: white; border-radius: 5px; width: 120px; padding: 10px;")
            ui.button("Premium").style("background-color: #D32F2F; color: white; border-radius: 5px; width: 120px; padding: 10px;")
            ui.button("Decks",on_click=lambda:ui.run_javascript('window.location.href="/Decks";')).style("background-color: #4CAF50; color: white; border-radius: 5px; width: 120px; padding: 10px;").on_click(lambda: ui.notify("Decks clicked!"))
