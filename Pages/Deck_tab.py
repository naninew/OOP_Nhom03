from nicegui import app as nicegui_app, ui
from Database_controller import get_DeckIdList, get_DeckDetail
from Pages.Card_tab import Card_tab


def UseThisDeck(deckId, tabs, CurrentDeckId):
    CurrentDeckId[0] = deckId
    Card_tab.refresh()
    tabs.set_value("My Cards")
    print("Change to {}".format(deckId))


def DeckCard(deckId, tabs, CurrentDeckId):
    with ui.card():  # .mark("important"):
        DeckDetail = get_DeckDetail(deckId)
        with ui.row():
            ui.label("Title: {}".format(DeckDetail["Title"]))
            ui.label("Back language: {}".format(DeckDetail["BackLanguage"]))
            ui.label("View type: {}".format(DeckDetail["ViewType"]))
            ui.label("Author: {}".format(DeckDetail["Author"]))
            ui.button(
                "Use this deck",
                on_click=lambda: UseThisDeck(deckId, tabs, CurrentDeckId),
            )
        # ui.button("button {}".format(i))
        # ui.label("label {}".format(i))


def Deck_tab(tabs, CurrentDeckId):
    # Menu_bar()
    DeckList = get_DeckIdList(nicegui_app.storage.user.get("userId"))
    # UsingDeck = 0
    ui.label("This is my deck tab")
    if DeckList == None:
        ui.label("Create my first deck now!")
    else:
        for i in range(len(DeckList)):
            DeckCard(DeckList[i], tabs, CurrentDeckId)
