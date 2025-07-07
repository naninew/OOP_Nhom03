from nicegui import app as nicegui_app, ui, run
from Database_controller import (
    get_DeckIdList,
    get_DeckDetail,
    get_DeckTagByDeckId,
    get_CardIdBackNull,
    get_CardTagByCardId,
    get_CardFrontByCardId,
    update_CardBackByCardId,
    get_BackCardPrompt,
    get_BackCardAIGenerated,
    insert_Deck,
    update_DeckByDeckId,
    update_DeckSetting,
    delete_DeckTag,
    insert_DeckTag,
    insert_Card,
    insert_CardTag,
    delete_AllDeckTag,
    delete_DeckSetting,
    delete_Deck,
    delete_AllCardTag,
    delete_LearningProgress,
    delete_Card,
    get_CardIdList,
)
from Pages.Card_tab import Card_tab
from ProtectedData import getTagAllowed


def ApplySetting(
    Title,
    BackLang,
    ViewType,
    Tag,
    LearningPace,
    CardPerDay,
    DeckDetail,
    Refreshable_Decktab,
    dialog,
):
    userId = nicegui_app.storage.user.get("userId")
    update_DeckByDeckId(DeckDetail["deckId"], Title, ViewType, BackLang)
    update_DeckSetting(DeckDetail["deckId"], userId, LearningPace, CardPerDay)
    for tag in Tag:
        if tag not in DeckDetail["Tag"]:
            insert_DeckTag(DeckDetail["deckId"], tag)
    for tag in DeckDetail["Tag"]:
        if tag not in Tag:
            delete_DeckTag(DeckDetail["deckId"], tag)
    ui.notify("Updated deck setting", type="positive")
    Refreshable_Decktab.refresh()
    dialog.close()


def DeleteCard(cardId: str):
    delete_AllCardTag(cardId)
    delete_LearningProgress(cardId)
    delete_Card(cardId)


def DeleteDeck(deckId: str, settingDialog, dialog, Refreshable_Decktab):
    delete_AllDeckTag(deckId)
    delete_DeckSetting(deckId)
    cardIdList = get_CardIdList(deckId)
    if cardIdList == None:
        cardIdList = []
    for cardId in cardIdList:
        DeleteCard(cardId)
    delete_Deck(deckId)
    dialog.close()
    settingDialog.close()
    Refreshable_Decktab.refresh()
    ui.notification("Deleted deck", type="positive")


def DeleteDeckDialog(deckId: str, settingDialog, Refreshable_Decktab):
    with ui.dialog() as dialog, ui.card():
        ui.label("Do you want to delete this deck?")
        ui.separator()
        ui.button(
            "Delete",
            color="red",
            on_click=lambda: DeleteDeck(
                deckId, settingDialog, dialog, Refreshable_Decktab
            ),
        )
        ui.button("Cancel", on_click=dialog.close)
    dialog.open()


def DeckSettingDialog(DeckDetail, Refreshable_Decktab):
    # ui.notification("Not working yet", type="info")
    deckId = DeckDetail["deckId"]
    with ui.dialog() as dialog, ui.card():
        ui.label("Deck setting")
        ui.separator()
        if nicegui_app.storage.user.get("userId") == DeckDetail["AuthorId"]:
            Title = ui.input(label="Title", value=DeckDetail["Title"])
            LangAllowed = ["English", "Vietnamese", "Japanese", "Korean", "France"]
            with ui.row():
                ui.label("Back language: ")
                BackLang = ui.select(
                    LangAllowed,
                    value=DeckDetail["BackLanguage"],
                    label="Back language:",
                ).classes("min-w-32")
            Type = ["public", "private"]
            with ui.row():
                ui.label("View type: ")
                ViewType = ui.select(
                    Type,
                    value=DeckDetail["ViewType"],
                    label="View type:",
                ).classes("min-w-32")
            TagsAllowed = getTagAllowed()
            with ui.row():
                ui.label("Deck tags: ")
                Tag = (
                    ui.select(
                        TagsAllowed,
                        multiple=True,
                        value=DeckDetail["Tag"],
                        label="Deck tags:",
                    ).props("use-chips")
                ).classes("min-w-32")
        ui.separator()
        LearningPace = ui.slider(min=1, max=15, value=DeckDetail["learning_pace"])
        with ui.row():
            ui.label("Learning pace: ")
            ui.label().bind_text_from(LearningPace, "value")
        ui.separator()
        CardPerDay = ui.slider(min=1, max=500, value=DeckDetail["card_per_day"])
        with ui.row():
            ui.label("Card per day: ")
            ui.label().bind_text_from(CardPerDay, "value")
        ui.separator()
        if nicegui_app.storage.user.get("userId") == DeckDetail["AuthorId"]:
            with ui.row():
                ui.button(
                    "Create new card",
                    color="deep-purple",
                    on_click=lambda: CreateNewCardDialog(deckId, DeckDetail),
                )
                ui.button(
                    "AI data auto-generator",
                    color="green",
                    on_click=lambda: run.io_bound(
                        AI_DataAutoGenerate, deckId, DeckDetail["BackLanguage"]
                    ),
                )
            ui.button(
                "Delete this deck",
                color="red",
                on_click=lambda: DeleteDeckDialog(deckId, dialog, Refreshable_Decktab),
            )
        ui.separator()
        with ui.row():
            if nicegui_app.storage.user.get("userId") == DeckDetail["AuthorId"]:
                ui.button(
                    "Apply setting",
                    on_click=lambda: ApplySetting(
                        Title.value,
                        BackLang.value,
                        ViewType.value,
                        Tag.value,
                        LearningPace.value,
                        CardPerDay.value,
                        DeckDetail,
                        Refreshable_Decktab,
                        dialog,
                    ),
                )
            else:
                ui.button(
                    "Apply setting",
                    on_click=lambda: ApplySetting(
                        DeckDetail["Title"],
                        DeckDetail["BackLanguage"],
                        DeckDetail["ViewType"],
                        DeckDetail["Tag"],
                        LearningPace.value,
                        CardPerDay.value,
                        DeckDetail,
                        Refreshable_Decktab,
                        dialog,
                    ),
                )
            ui.button("Cancel", on_click=dialog.close)
    dialog.open()


def UseThisDeck(deckId, tabs, Refreshable_Cardtab):  # CurrentDeckId
    # CurrentDeckId[0] = deckId
    nicegui_app.storage.user.update({"deckId": deckId})
    DeckDetail = get_DeckDetail(deckId, nicegui_app.storage.user.get("userId"))
    nicegui_app.storage.user.update(DeckDetail)
    # Card_tab.refresh()
    Refreshable_Cardtab.refresh()
    tabs.set_value("My Cards")
    # print("Change to {}".format(deckId))


def AI_DataAutoGenerate(deckId: str, backLang: str):
    print("--- START LLM GEN ---")
    # ui.notify("Running LLM, pls wait", type="ongoing")
    CardIdList = get_CardIdBackNull(deckId)
    for cardId in CardIdList:
        Tag = ", ".join(get_CardTagByCardId(cardId))
        Front = get_CardFrontByCardId(cardId)
        Back = get_BackCardAIGenerated(Tag, Front, backLang)
        update_CardBackByCardId(Back, cardId)
        print("Done update")
        # ui.notify("Updated a card", type="positive")
    print("--- DONE GEN ---")
    # ui.notify("AI Data Auto-Generation completed", type="positive")


def CreateNewDeck(Title, ViewType, BackLang, Refreshable_Decktab, Tag, dialog):
    userId = nicegui_app.storage.user.get("userId")
    deckId = insert_Deck(userId, Title, ViewType, BackLang)
    for tag in Tag:
        insert_DeckTag(deckId, tag)
    ui.notify("Created new deck", type="positive")
    print("==>", deckId, "<===\n\n")
    Refreshable_Decktab.refresh()
    dialog.close()


def CreateNewDeckDialog(Refreshable_Decktab):
    # ui.notification("Not working yet", type="info")
    DeckDetail = {
        "BackLanguage": "English",
        "Title": "Your deck's title",
        "ViewType": "private",
        "Tag": list(),
        "AuthorId": nicegui_app.storage.user.get("userId"),
        "learning_pace": 5,
        "card_per_day": 5,
    }
    with ui.dialog() as dialog, ui.card():
        ui.label("Create new deck")
        if nicegui_app.storage.user.get("userId") == DeckDetail["AuthorId"]:
            Title = ui.input(label="Title", value=DeckDetail["Title"])
            LangAllowed = ["English", "Vietnamese", "Japanese", "Korean", "France"]
            with ui.row():
                ui.label("Back language: ")
                BackLang = ui.select(
                    LangAllowed,
                    value=DeckDetail["BackLanguage"],
                    label="Back language:",
                ).classes("min-w-32")
            Type = ["public", "private"]
            with ui.row():
                ui.label("View type: ")
                ViewType = ui.select(
                    Type,
                    value=DeckDetail["ViewType"],
                    label="View type:",
                ).classes("min-w-32")
        TagsAllowed = getTagAllowed()
        with ui.row():
            ui.label("Deck tags: ")
            Tag = (
                ui.select(
                    TagsAllowed,
                    multiple=True,
                    value=[],
                    label="Deck tags:",
                ).props("use-chips")
            ).classes("min-w-32")
        with ui.row():
            ui.button(
                "Create",
                on_click=lambda: CreateNewDeck(
                    Title.value,
                    ViewType.value,
                    BackLang.value,
                    Refreshable_Decktab,
                    Tag.value,
                    dialog,
                ),
            )
            ui.button("Cancel", on_click=dialog.close)
    dialog.open()


def CreateNewCard(deckId: str, Front: str, Back: str, Tag, dialog):
    cardId = insert_Card(deckId, Front, Back)
    for tag in Tag:
        insert_CardTag(cardId, tag)
    dialog.close()
    ui.notify("Created new card", type="positive")


def CreateNewCardDialog(deckId: str, DeckDetail):
    # ui.notification("Not working yet", type="info")
    with ui.dialog() as dialog, ui.card():
        ui.label("Create new card")
        TagsAllowed = getTagAllowed()
        with ui.row():
            ui.label("Card tags: ")
            Tag = (
                ui.select(
                    TagsAllowed,
                    multiple=True,
                    value=DeckDetail["Tag"],
                    label="Card tags:",
                ).props("use-chips")
            ).classes("min-w-32")
        Front = ui.input(
            label="Front", placeholder="This is the front of my card", value=""
        ).style("min-width:300px")
        Back = ui.input(
            label="Back",
            placeholder="Leave this empty for AI-auto-generate function",
            value="",
        ).style("min-width:300px")
        with ui.row():
            ui.button(
                "Create",
                on_click=lambda: CreateNewCard(
                    deckId, Front.value, Back.value, Tag.value, dialog
                ),
            )
            ui.button("Cancel", on_click=dialog.close)
    dialog.open()


def DeckCard(deckId, tabs, Refreshable_Cardtab, Refreshable_Decktab):  # , CurrentDeckId
    with ui.card():  # .mark("important"):
        DeckDetail = get_DeckDetail(deckId, nicegui_app.storage.user.get("userId"))
        nicegui_app.storage.user.update(DeckDetail)
        with ui.row():
            ui.label("Title: {}".format(DeckDetail["Title"]))
            ui.label("Back language: {}".format(DeckDetail["BackLanguage"]))
            ui.label("View type: {}".format(DeckDetail["ViewType"]))
            ui.label("Author: {}".format(DeckDetail["Author"]))
        with ui.row():
            ui.label("Learning pace: {}".format(DeckDetail["learning_pace"]))
            ui.label("Card per day: {}".format(DeckDetail["card_per_day"]))

        ui.label("Tags: {}".format(", ".join(DeckDetail["Tag"])))
        with ui.row():
            ui.button(
                "Deck setting",
                on_click=lambda: DeckSettingDialog(DeckDetail, Refreshable_Decktab),
            )
            ui.button(
                "Use this deck",
                color="green",
                on_click=lambda: UseThisDeck(deckId, tabs, Refreshable_Cardtab),
            )
            # if (
            #     nicegui_app.storage.user.get("userId") == DeckDetail["AuthorId"]
            #     and nicegui_app.storage.user.get("accountType") == "premium"
            # ):


def Deck_tab(tabs, Refreshable_Cardtab, Refreshable_Decktab):  # CurrentDeckId
    # Menu_bar()
    DeckList = get_DeckIdList(nicegui_app.storage.user.get("userId"))
    # UsingDeck = 0
    ui.label("This is my deck tab")
    ui.button(
        "Create new deck",
        color="deep-purple",
        on_click=lambda: CreateNewDeckDialog(Refreshable_Decktab),
    )
    if DeckList == None:
        ui.label("Create my first deck now!")
    else:
        for i in range(len(DeckList)):
            DeckCard(DeckList[i], tabs, Refreshable_Cardtab, Refreshable_Decktab)
