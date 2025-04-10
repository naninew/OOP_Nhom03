from nicegui import ui

# Danh sách các thẻ flashcard
deck = [
    {'front': 'Hello', 'back': 'Xin chào'},
    {'front': 'Thank you', 'back': 'Cảm ơn'},
    {'front': 'Goodbye', 'back': 'Tạm biệt'},
]

@ui.page('/Decks')
def flashcard_list_page():
    selected_index = {'value': None}  # Lưu chỉ số của thẻ được chọn
    card_info_text = ui.label('Card Info Here').classes('text-lg q-mt-md')  # Hiển thị thông tin thẻ

    # Hàm làm mới danh sách thẻ
    def refresh_list():
        list_view.clear()
        for index, card in enumerate(deck):
            def on_click(i=index):
                selected_index['value'] = i
                card_info_text.text = f"Front: {deck[i]['front']}"  # Hiển thị mặt trước của thẻ
            with list_view:
                ui.button(f"{index + 1}. {card['front']}", on_click=on_click).props('flat').classes('text-left w-full')

    # Hàm thêm thẻ mới
    def add_card():
        with ui.dialog() as dialog, ui.card():
            ui.label('➕ Add New Card').classes('text-h6')
            front_input = ui.input('Front')
            back_input = ui.input('Back')
            with ui.row().classes('justify-end'):
                ui.button('Save', on_click=lambda: save_card(front_input, back_input, dialog)).props('color=primary')
                ui.button('Cancel', on_click=dialog.close)

    def save_card(front_input, back_input, dialog):
        front = front_input.value.strip()
        back = back_input.value.strip()
        if not front or not back:
            ui.notify("Please enter both front and back.")
            return
        deck.append({'front': front, 'back': back})
        refresh_list()
        dialog.close()

    # Hàm xóa thẻ
    def delete_card():
        i = selected_index['value']
        if i is None:
            ui.notify("Please select a card to delete.")
            return
        deck.pop(i)
        selected_index['value'] = None
        card_info_text.text = "Card Info Here"  # Xóa thông tin thẻ
        refresh_list()
        ui.notify("Card deleted.")

    # Hàm hiển thị mặt trước của thẻ
    def show_card_front():
        i = selected_index['value']
        if i is None:
            ui.notify("Please select a card to view.")
            return
        card_info_text.text = f"Front: {deck[i]['front']}"

    # Hàm hiển thị mặt sau của thẻ
    def show_card_back():
        i = selected_index['value']
        if i is None:
            ui.notify("Please select a card to view.")
            return
        card_info_text.text = f"Back: {deck[i]['back']}"

    # Giao diện chính
    with ui.column().classes('q-pa-md q-gutter-md max-w-3xl mx-auto'):
        ui.label('📘 My Decks').classes('text-h4 text-center')

        # Khung hiển thị danh sách thẻ
        list_view = ui.column().classes('q-pa-md bg-white rounded shadow-md max-h-64 overflow-auto')

        # Các nút chức năng
        with ui.row().classes('q-mt-md justify-center'):
            ui.button('➕ Add', on_click=add_card).props('color=primary')
            ui.button('❌ Delete', on_click=delete_card).props('color=negative')

        # Hiển thị thông tin thẻ
        card_info_text

        # Các nút chuyển đổi mặt trước/mặt sau
        with ui.row().classes('q-mt-md justify-center'):
            ui.button('Front', on_click=show_card_front).props('color=primary')
            ui.button('Back', on_click=show_card_back).props('color=primary')

    # Làm mới danh sách thẻ khi khởi chạy
   # refresh_list()