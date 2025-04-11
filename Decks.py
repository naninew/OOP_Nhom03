from nicegui import ui

deck = [
    {'front': 'Hello', 'back': 'Xin chào'},
    {'front': 'Thank you', 'back': 'Cảm ơn'},
    {'front': 'Goodbye', 'back': 'Tạm biệt'},
]

@ui.page('/Decks')
def flashcard_list_page():
    selected_index = {'value': None}
    card_info_text = ui.label('Card Info Here').classes('text-lg q-mt-md text-center')

    list_view = ui.column().classes('q-pa-md bg-white rounded shadow-md max-h-64 overflow-auto w-full')

    # Dialog thêm
    add_card_dialog = ui.dialog()
    with add_card_dialog, ui.card():
        ui.label('➕ Add New Card').classes('text-h6')
        add_front_input = ui.input('Front')
        add_back_input = ui.input('Back')
        with ui.row().classes('justify-end'):
            ui.button('Save', on_click=lambda: save_new_card(add_front_input, add_back_input)).props('color=primary')
            ui.button('Cancel', on_click=add_card_dialog.close)

    # Dialog sửa
    edit_card_dialog = ui.dialog()
    with edit_card_dialog, ui.card():
        ui.label('✏️ Edit Card').classes('text-h6')
        edit_front_input = ui.input('Front')
        edit_back_input = ui.input('Back')
        with ui.row().classes('justify-end'):
            ui.button('Save', on_click=lambda: save_edited_card(edit_front_input, edit_back_input)).props('color=primary')
            ui.button('Cancel', on_click=edit_card_dialog.close)

    def refresh_list():
        list_view.clear()
        for index, card in enumerate(deck):
            def on_click(i=index):
                selected_index['value'] = i
                card_info_text.text = f"Front: {deck[i]['front']}"
            with list_view:
                ui.button(f"{index + 1}. {card['front']}", on_click=on_click).props('flat').classes('text-left w-full')

    def add_card():
        add_front_input.value = ''
        add_back_input.value = ''
        add_card_dialog.open()

    def save_new_card(front_input, back_input):
        front = front_input.value.strip()
        back = back_input.value.strip()
        if not front or not back:
            ui.notify("Please enter both front and back.")
            return
        deck.append({'front': front, 'back': back})
        add_card_dialog.close()
        refresh_list()
        ui.notify("Card added!")

    def delete_card():
        i = selected_index['value']
        if i is None:
            ui.notify("Please select a card to delete.")
            return
        deck.pop(i)
        selected_index['value'] = None
        card_info_text.text = "Card Info Here"
        refresh_list()
        ui.notify("Card deleted.")

    def edit_card():
        i = selected_index['value']
        if i is None:
            ui.notify("Please select a card to edit.")
            return
        edit_front_input.value = deck[i]['front']
        edit_back_input.value = deck[i]['back']
        edit_card_dialog.open()

    def save_edited_card(front_input, back_input):
        i = selected_index['value']
        if i is None:
            ui.notify("No card selected.")
            return
        deck[i]['front'] = front_input.value.strip()
        deck[i]['back'] = back_input.value.strip()
        edit_card_dialog.close()
        refresh_list()
        ui.notify("Card updated!")
        card_info_text.text = f"Front: {deck[i]['front']}"

    def show_card_front():
        i = selected_index['value']
        if i is None:
            ui.notify("Please select a card.")
            return
        card_info_text.text = f"Front: {deck[i]['front']}"

    def show_card_back():
        i = selected_index['value']
        if i is None:
            ui.notify("Please select a card.")
            return
        card_info_text.text = f"Back: {deck[i]['back']}"

    # 🧩 Tất cả giao diện nằm giữa màn hình
    with ui.column().classes('items-center justify-center min-h-screen q-gutter-md max-w-xl mx-auto'):
        ui.label('📘 My Decks').classes('text-h4 text-center')

        list_view

        with ui.row().classes('q-mt-md justify-center'):
            ui.button('➕ Add', on_click=add_card).props('color=primary')
            ui.button('✏️ Edit', on_click=edit_card).props('color=secondary')
            ui.button('❌ Delete', on_click=delete_card).props('color=negative')

        card_info_text

        with ui.row().classes('q-mt-md justify-center'):
            ui.button('Front', on_click=show_card_front).props('color=primary')
            ui.button('Back', on_click=show_card_back).props('color=primary')

    refresh_list()


