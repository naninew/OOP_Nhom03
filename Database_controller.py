Fake_UserEmailPass = {"user1": "pass1", "user2": "pass2"}
Fake_UserEmailID = {"user1": "1", "user2": "2"}
Fake_DeckIdList = {"1": ["1D0", "1D1", "1D2"]}  # , "2": ["2D0", "2D1"]}
Fake_CardIdList = {"1D0": ["1D0C0", "1D0C1", "1D0C2"], "1D1": ["1D1C0", "1D1C1"]}
Fake_DeckDetail = {
    "1D0": {"BackLanguage": "English", "Title": "N5 vocab", "ViewType": "public"},
    "1D1": {"BackLanguage": "English", "Title": "N4 vocab", "ViewType": "public"},
    "1D2": {"BackLanguage": "English", "Title": "N3 vocab", "ViewType": "private"},
}
Fake_CardDetail = {
    "1D0C0": {
        "Front": """青い, 蒼い, 碧い, あおい""",
        "Back": """1. blue, azure
mostly archaic or in ref. to fruits, vegetables and traffic lights
2. green
Only 青い, Only 蒼い
3. pale (facial color), gray, grey
4. unripe, inexperienced""",
    },
    "1D0C1": {
        "Front": """明るい, あかるい""",
        "Back": """1. light, bright, well-lit, well-lighted
2. bright (colour)
3. cheerful, spirited, sunny (e.g. disposition)
4. bright (future, prospects, etc.), rosy, encouraging, promising
as ...に明るい
5. knowledgeable (about), familiar (with), well versed (in), well acquainted (with)""",
    },
    "1D0C2": {
        "Front": """厚い, 篤い, あつい""",
        "Back": """1. thick, deep, heavy
2. kind, cordial, hospitable, warm, faithful
Only 篤い
3. serious (of an illness)
4. abundant""",
    },
    "1D1C0": {
        "Front": """謝る, あやまる""",
        "Back": """Godan verb, Transitive
1. to apologize, to apologise
dated term
2. to refuse, to decline
Intransitive
3. to be unable to bear, to be defeated (by), to be at a loss""",
    },
    "1D1C1": {
        "Front": """以上, 已上, いじょう""",
        "Back": """Noun, used as a suffix, Antonym: 以下・1
1. not less than ..., ... and over, ... and above, ... and upwards, ... or more
2. beyond (e.g. one's expectations), more than, further than
May take 'no'
3. the above, the above-mentioned, the aforementioned, the foregoing
Conjunction, after a verb
4. since ..., seeing that ..., now that ..., once ...
Expression
5. that's all, that is the end""",
    },
}


def get_UserPassword(email: str):
    return Fake_UserEmailPass.get(email, None)


def get_UserId(email: str):
    return Fake_UserEmailID.get(email, None)


def get_DeckIdList(userId: str):
    return Fake_DeckIdList.get(userId, None)


def get_CardIdList(deckId: str):
    return Fake_CardIdList.get(deckId, None)


def get_DeckDetail(deckId: str):

    return Fake_DeckDetail.get(deckId, None)


def get_CardDetail(cardId: str):
    return Fake_CardDetail.get(cardId, None)


def set_UserAccount(email: str, password: str):
    pass


def set_DeckDetail(deckId: str, BackLanguage: str, Title: str, ViewType: str):
    if deckId in Fake_DeckDetail:
        Fake_DeckDetail[deckId]["BackLanguage"] = BackLanguage
        Fake_DeckDetail[deckId]["Title"] = Title
        Fake_DeckDetail[deckId]["ViewType"] = ViewType


def set_CardDetail(cardID: str, Front: str, Back: str):
    if cardID in Fake_CardDetail:
        Fake_CardDetail[cardID]["Front"] = Front
        Fake_CardDetail[cardID]["Back"] = Back
