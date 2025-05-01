from nicegui import app as nicegui_app, ui
from LLM_API import FreePrompt


def UpdateAI_Answer(AI_Answer, Prompt):
    AI_Answer.text = FreePrompt(Prompt)


def Ask_AI_tab():
    UserPrompt = ui.textarea(
        label="Ask AI something",
        placeholder="your prompt",
    ).classes("w-full")
    # on_change=lambda e: result_email.set_text(
    #     "you typed: " + e.value
    # ),
    # validation={"Input too long": lambda value: len(value) < 30},
    # ).on(
    #     "keydown.enter",
    #     lambda: UpdateAI_Answer(AI_Answer, UserPrompt.value),
    # )  # .classes("items-center")
    ui.button("Ask AI", on_click=lambda: UpdateAI_Answer(AI_Answer, UserPrompt.value))
    ui.separator()
    AI_Answer = ui.label("AI's answer").style(
        "white-space: pre-wrap;"
    )  # .classes("w-1/2 items-center")
