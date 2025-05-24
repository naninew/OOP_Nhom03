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


def get_UserPassword_Fake(email: str):
    return Fake_UserEmailPass.get(email, None)


def get_UserId_Fake(email: str):
    return Fake_UserEmailID.get(email, None)


def get_DeckIdList_Fake(userId: str):
    return Fake_DeckIdList.get(userId, None)


def get_CardIdList_Fake(deckId: str):
    return Fake_CardIdList.get(deckId, None)


def get_DeckDetail_Fake(deckId: str):

    return Fake_DeckDetail.get(deckId, None)


def get_CardDetail_Fake(cardId: str):
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


# -----------------------------------------------------------------------------------------------
# from mysqlx import Row
import psycopg2
import ProtectedData


def RunQuery(query: str):
    DB_info = ProtectedData.getDatabaseKey()
    conn = psycopg2.connect(
        database=DB_info["DB_NAME"],
        password=DB_info["DB_PASS"],
        user=DB_info["DB_USER"],
        host=DB_info["DB_HOST"],
        port=DB_info["DB_PORT"],
    )
    print("Connected successfully")
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    print(rows)
    # for data in rows:
    #     print(data)
    #     print("\n----------------\n")
    conn.close()
    return rows


def get_UserPassword(email: str):
    rows = RunQuery(
        """SELECT password 
            FROM user_account 
            WHERE email='{}'""".format(
            email
        )
    )
    if len(rows) == 0:
        return None
    return rows[0][0]


def get_UserId(email: str):
    rows = RunQuery(
        """SELECT user_id 
            FROM user_account 
            WHERE email='{}'""".format(
            email
        )
    )
    if len(rows) == 0:
        return None
    return rows[0][0]


def get_AuthorName(userId: str):
    rows = RunQuery(
        """SELECT user_name 
            FROM user_account 
            WHERE user_id='{}'""".format(
            userId
        )
    )
    if len(rows) == 0:
        return "Unknown author"
    return rows[0][0]


def get_DeckIdList(userId: str):
    rows = RunQuery(
        """SELECT deck_id 
            FROM deck 
            WHERE author_id='{}' OR public=true""".format(
            userId
        )
    )
    if len(rows) == 0:
        return None
    return list(i[0] for i in rows)


def get_CardIdList(deckId: str):
    rows = RunQuery(
        """SELECT card_id      
        FROM card 
        WHERE deck_id='{}'""".format(
            deckId
        )
    )
    if len(rows) == 0:
        return None
    return list(i[0] for i in rows)


def get_DeckDetail(deckId: str):
    rows = RunQuery(
        """SELECT deck_name,author_id,public,back_lang 
            FROM deck 
            WHERE deck_id='{}'""".format(
            deckId
        )
    )
    if len(rows) == 0:
        return None
    Output = dict()
    Output["BackLanguage"] = rows[0][3]
    Output["Title"] = rows[0][0]
    Output["ViewType"] = "public" if rows[0][2] else "private"
    Output["Author"] = get_AuthorName(rows[0][1])
    return Output


def get_CardDetail(cardId: str):
    rows = RunQuery(
        """SELECT front,back 
            FROM card
            WHERE card_id='{}'""".format(
            cardId
        )
    )
    if len(rows) == 0:
        return None
    Output = dict()
    Output["Front"] = rows[0][0]
    Output["Back"] = rows[0][1]
    return Output
