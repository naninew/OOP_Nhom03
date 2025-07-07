from nicegui import app as nicegui_app, ui
from Database_controller import (
    get_CardIdList,
    get_CardDetail,
    get_DeckDetail,
    get_CardTagByCardId,
    get_CardIdHavingReviewDateLessThanNowByDeckId,
    get_CardIdNotHavingReviewDateByDeckId,
    get_CardIdHavingReviewDateGreaterThanNowByDeckId,
    get_ConfidentByCardIdAndUserId,
    insert_LearningProgress,
    update_LearningProgress,
    insert_CardTag,
    delete_CardTag,
    delete_AllCardTag,
    delete_LearningProgress,
    delete_Card,
)
from ProtectedData import getTagAllowed


def GetCardIdByPriority():
    CardIdList = list()
    Limit = nicegui_app.storage.user.get("card_per_day")
    CardIdList.extend(
        get_CardIdHavingReviewDateLessThanNowByDeckId(
            nicegui_app.storage.user.get("deckId")
        )
    )
    if len(CardIdList) < Limit:
        CardIdList.extend(
            get_CardIdNotHavingReviewDateByDeckId(
                nicegui_app.storage.user.get("deckId")
            )
        )
    if len(CardIdList) < Limit:
        CardIdList.extend(
            get_CardIdHavingReviewDateGreaterThanNowByDeckId(
                nicegui_app.storage.user.get("deckId")
            )
        )
    if len(CardIdList) < Limit:
        return CardIdList
    return CardIdList[:Limit]


def ApplySetting(CardTag, Tag, cardId: str, dialog, ShowCardTag):
    print(CardTag, "<<<<")
    print(Tag, "<<<<<<")
    for tag in Tag:
        if tag not in CardTag:
            insert_CardTag(cardId, tag)
            print(tag, "<----")
    for tag in CardTag:
        if tag not in Tag:
            delete_CardTag(cardId, tag)
    dialog.close()
    ShowCardTag.refresh()
    ui.notify("Updated card setting", type="positive")


def DeleteCard(cardId: str, settingDialog, dialog):
    delete_AllCardTag(cardId)
    delete_LearningProgress(cardId)
    delete_Card(cardId)
    dialog.close()
    settingDialog.close()
    ui.notification("Deleted card", type="positive")


def DeleteCardDialog(cardId: str, settingDialog):
    with ui.dialog() as dialog, ui.card():
        ui.label("Do you want to delete this card?")
        ui.button(
            "Delete",
            color="red",
            on_click=lambda: DeleteCard(cardId, settingDialog, dialog),
        )
        ui.button("Cancel", on_click=dialog.close)
    dialog.open()


def CardSettingDialog(CardTag: list, cardId: str, ShowCardTag):
    # ui.notification("Not working yet", type="info")
    with ui.dialog() as dialog, ui.card():
        ui.label("Card setting")
        ui.separator()
        TagsAllowed = getTagAllowed()
        with ui.row():
            ui.label("Card tags: ")
            Tag = (
                ui.select(
                    TagsAllowed,
                    multiple=True,
                    value=CardTag,
                    label="Card tags:",
                ).props("use-chips")
            ).style("min-width:300px")
        ui.separator()
        ui.button(
            "Delete this card",
            color="red",
            on_click=lambda: DeleteCardDialog(cardId, dialog),
        )
        ui.separator()
        with ui.row():
            ui.button(
                "Apply setting",
                on_click=lambda: ApplySetting(
                    CardTag, Tag.value, cardId, dialog, ShowCardTag
                ),
            )
            ui.button("Cancel", on_click=dialog.close)
    dialog.open()


@ui.refreshable
def ShowCardDetail(CurrentCardId, ShowFace):
    # ShowFront = ui.label("Front")
    CardDetail = get_CardDetail(CurrentCardId[0])
    # Info = [CardDetail["Front"]]
    CardInfo = ui.label(CardDetail[ShowFace.text])


@ui.refreshable
def ShowCardTag():
    CardList = nicegui_app.storage.user.get("CardList")
    CardTagLabel = ui.label(
        "Card tags: {}".format(
            ", ".join(
                get_CardTagByCardId(CardList[nicegui_app.storage.user.get("cardId", 0)])
            )
        )
    )


def RouteCard(MaxIndex, step, ShowFace, Grade_button, ShowCardTag):
    CurrentCardIndex = nicegui_app.storage.user.get("cardId", 0)
    if 0 <= CurrentCardIndex + step <= MaxIndex:
        CurrentCardIndex += step
        # print(CurrentCardIndex[0])
    elif CurrentCardIndex + step > MaxIndex:
        CurrentCardIndex = 0
    else:
        CurrentCardIndex = MaxIndex
    nicegui_app.storage.user.update({"cardId": CurrentCardIndex})
    ShowFace.text = "Back"  # Do not touch this
    ShowFace.text = "Front"  # Do not touch this

    ShowCardTag.refresh()
    Grade_button.set_visibility(False)


def ToggleCard(ShowFace, Grade_button):
    if ShowFace.text == "Front":
        ShowFace.text = "Back"
    else:
        ShowFace.text = "Front"

    Grade_button.set_visibility(True)


def SaveProgress():
    learning_progress = nicegui_app.storage.user.get("learning_progress")
    userId = nicegui_app.storage.user.get("userId")
    learning_pace = nicegui_app.storage.user.get("learning_pace")
    for cardId in learning_progress:
        confident = get_ConfidentByCardIdAndUserId(cardId, userId)
        if confident == None:
            insert_LearningProgress(cardId, userId)
            confident = 0
        grade = learning_progress[cardId][0]
        if grade >= 3.6:
            confident += learning_pace
        elif grade >= 3.2:
            confident += round(learning_pace * 0.5)
        elif grade >= 2.4:
            confident -= learning_pace
        else:
            confident = 1
        if confident > 100:
            confident = 100
        elif confident < 0:
            confident = 0
        update_LearningProgress(cardId, userId, confident)
    nicegui_app.storage.user.update({"learning_progress": dict()})
    ui.notification("Saved learning progress", type="positive")


def CardGradeCal(cardId: str, grade: int, Grade_button):
    Grade_button.set_visibility(False)
    learning_progress = nicegui_app.storage.user.get("learning_progress")
    if cardId not in learning_progress:
        learning_progress[cardId] = [grade, 1]
    else:
        counter = learning_progress[cardId][1]
        learning_progress[cardId][0] = (
            learning_progress[cardId][0] * counter + grade
        ) / (counter + 1)
        learning_progress[cardId][1] += 1
    ui.notification("Updated learning progress", type="positive", position="top-right")
    print("--- --- --- ---")
    print(nicegui_app.storage.user.get("learning_progress"))


# @ui.refreshable
def Card_tab():
    if nicegui_app.storage.user.get("deckId", None) == None:
        ui.label("This is my card tab")
        ui.label("You haven't choose a deck yet!")
    else:
        # CardList = get_CardIdList(CurrentDeckId[0])
        CardList = GetCardIdByPriority()
        nicegui_app.storage.user.update({"CardList": CardList})
        # CurrentCardIndex = [0]
        nicegui_app.storage.user.update({"cardId": 0})
        if len(CardList) == 0:  # CardList == None:
            ui.label("This deck have no card!")
        else:
            # DeckDetail = get_DeckDetail(CurrentDeckId[0])
            with ui.row():
                if nicegui_app.storage.user.get(
                    "userId"
                ) == nicegui_app.storage.user.get("AuthorId"):
                    ui.button(
                        "Card setting",
                        on_click=lambda: CardSettingDialog(
                            get_CardTagByCardId(
                                CardList[nicegui_app.storage.user.get("cardId", 0)]
                            ),
                            CardList[nicegui_app.storage.user.get("cardId", 0)],
                            ShowCardTag,
                        ),
                    )
                ui.button("Save my progress", color="green", on_click=SaveProgress)
            ui.separator()
            with ui.row():
                ui.label("Title: {}".format(nicegui_app.storage.user.get("Title")))
                ui.label(
                    "Back language: {}".format(
                        nicegui_app.storage.user.get("BackLanguage")
                    )
                )
                ui.label(
                    "View type: {}".format(nicegui_app.storage.user.get("ViewType"))
                )

            # ShowCardDetail(CurrentCardId)
            ShowFace = ui.label("Front")
            # with ui.scroll_area().classes(
            #     "border w-full h-96"
            # ):  # "min-h-96 w-500 border"
            #     CardInfo = (
            #         (
            #             ui.label(
            #                 get_CardDetail(CardList[CurrentCardIndex[0]])[ShowFace.text]
            #             ).bind_text_from(
            #                 ShowFace,
            #                 "text",
            #                 backward=lambda x: get_CardDetail(
            #                     CardList[CurrentCardIndex[0]]
            #                 )[x],
            #             )
            #         ).style("white-space: pre-wrap;")
            #     ).classes("min-w-fit min-h-fit text-3xl")
            ui.label(
                "Card {} in {}".format(
                    nicegui_app.storage.user.get("cardId", 0) + 1, len(CardList)
                )
            ).bind_text_from(
                ShowFace,
                "text",
                backward=lambda x: "Card {} in {}".format(
                    nicegui_app.storage.user.get("cardId", 0) + 1, len(CardList)
                ),
            )
            # CardTagLabel = ui.label(
            #     "Tags: {}".format(
            #         ", ".join(
            #             get_CardTagByCardId(
            #                 CardList[nicegui_app.storage.user.get("cardId", 0)]
            #             )
            #         )
            #     )
            # )
            ShowCardTag()
            ui.separator()
            with ui.row():
                ui.button(
                    "Back",
                    on_click=lambda: RouteCard(
                        len(CardList) - 1, -1, ShowFace, Grade_button, ShowCardTag
                    ),
                )
                Toggle_button = ui.button(
                    "Toggle Card",
                    color="indigo",
                    on_click=lambda: ToggleCard(ShowFace, Grade_button),
                )
                ui.button(
                    "Next",
                    on_click=lambda: RouteCard(
                        len(CardList) - 1, 1, ShowFace, Grade_button, ShowCardTag
                    ),
                )
            with ui.row() as Grade_button:
                ui.button(
                    "Again",
                    color="red",
                    on_click=lambda: CardGradeCal(
                        CardList[nicegui_app.storage.user.get("cardId", 0)],
                        0,
                        Grade_button,
                    ),
                )
                ui.button(
                    "Hard",
                    color="deep-orange",
                    on_click=lambda: CardGradeCal(
                        CardList[nicegui_app.storage.user.get("cardId", 0)],
                        2,
                        Grade_button,
                    ),
                )
                ui.button(
                    "Good",
                    color="teal",
                    on_click=lambda: CardGradeCal(
                        CardList[nicegui_app.storage.user.get("cardId", 0)],
                        3,
                        Grade_button,
                    ),
                )
                ui.button(
                    "Easy",
                    color="green",
                    on_click=lambda: CardGradeCal(
                        CardList[nicegui_app.storage.user.get("cardId", 0)],
                        4,
                        Grade_button,
                    ),
                )
            Grade_button.set_visibility(False)
            CardInfo = (
                (
                    ui.markdown(
                        get_CardDetail(
                            CardList[nicegui_app.storage.user.get("cardId", 0)]
                        )[ShowFace.text]
                    ).bind_content_from(
                        ShowFace,
                        "text",
                        backward=lambda x: get_CardDetail(
                            CardList[nicegui_app.storage.user.get("cardId", 0)]
                        )[x],
                    )
                ).style("white-space: pre-wrap;")
            ).classes(
                "min-w-fit min-h-fit border p-2 text-2xl"
            )  # text-3xl
