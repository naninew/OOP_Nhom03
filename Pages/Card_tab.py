from nicegui import app as nicegui_app, ui
from Database_controller import get_CardIdList, get_CardDetail, get_DeckDetail


def CardSettingDialog():
    with ui.dialog() as dialog, ui.card():
        ui.label("Card setting")
        ui.button("Apply")
        ui.button("Close", on_click=dialog.close)
    dialog.open()


@ui.refreshable
def ShowCardDetail(CurrentCardId, ShowFace):
    # ShowFront = ui.label("Front")
    CardDetail = get_CardDetail(CurrentCardId[0])
    # Info = [CardDetail["Front"]]
    CardInfo = ui.label(CardDetail[ShowFace.text])


def RouteCard(CurrentCardIndex, MaxIndex, step, ShowFace):
    if 0 <= CurrentCardIndex[0] + step <= MaxIndex:
        CurrentCardIndex[0] += step
        ShowFace.text = "Back"  # Do not touch this
        ShowFace.text = "Front"  # Do not touch this
        # print(CurrentCardIndex[0])


def ToggleCard(ShowFace):
    if ShowFace.text == "Front":
        ShowFace.text = "Back"
    else:
        ShowFace.text = "Front"


@ui.refreshable
def Card_tab(CurrentDeckId):
    ui.label("This is my card tab")
    if CurrentDeckId[0] == None:
        ui.label("You haven't choose a deck yet!")
    else:
        CardList = get_CardIdList(CurrentDeckId[0])
        CurrentCardIndex = [0]
        if CardList == None:
            ui.label("This deck have no card!")
        else:
            DeckDetail = get_DeckDetail(CurrentDeckId[0])
            with ui.row():
                ui.label("Title: {}".format(DeckDetail["Title"]))
                ui.label("Back language: {}".format(DeckDetail["BackLanguage"]))
                ui.label("View type: {}".format(DeckDetail["ViewType"]))
            # ShowCardDetail(CurrentCardId)
            ShowFace = ui.label("Front")
            with ui.scroll_area().classes("min-h-96 w-500 border"):
                CardInfo = (
                    (
                        ui.label(
                            get_CardDetail(CardList[CurrentCardIndex[0]])[ShowFace.text]
                        ).bind_text_from(
                            ShowFace,
                            "text",
                            backward=lambda x: get_CardDetail(
                                CardList[CurrentCardIndex[0]]
                            )[x],
                        )
                    ).style("white-space: pre-wrap;")
                ).classes("min-w-fit min-h-fit text-3xl")
            ui.label(
                "Card {} in {}".format(CurrentCardIndex[0] + 1, len(CardList))
            ).bind_text_from(
                ShowFace,
                "text",
                backward=lambda x: "Card {} in {}".format(
                    CurrentCardIndex[0] + 1, len(CardList)
                ),
            )
            with ui.row():
                ui.button(
                    "Back",
                    on_click=lambda: RouteCard(
                        CurrentCardIndex, len(CardList) - 1, -1, ShowFace
                    ),
                )
                ui.button("Toggle Card", on_click=lambda: ToggleCard(ShowFace))
                ui.button(
                    "Next",
                    on_click=lambda: RouteCard(
                        CurrentCardIndex, len(CardList) - 1, 1, ShowFace
                    ),
                )
            ui.button("Card setting", on_click=lambda: CardSettingDialog())
