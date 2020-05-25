import os


class Variables:
    VALID_EMAIL = os.getenv("GEMINI_TESTER_USERNAME", "")
    VALID_PASSWORD = os.getenv("GEMINI_TESTER_PASSWORD", "")
    SHORT_PASSWORD = "1234"
    OTHER_PASSWORD = "test1235"
    USER_ALREADY_EXISTS_MESSAGE = "Taki użytkownik już istnieje."
    PASSWORD_TOO_SHORT_MESSAGE = "Podane hasło jest za krótkie min. 6 znaków."
    NO_PASSWORD_MESSAGE = "Brak hasła."
    PASSWORD_NOT_MATCH_MESSAGE = "Hasła nie są takie same."
    ACCEPT_PRIVACY_MESSAGE = "Zaakceptuj regulamin"
    REGISTER_FORM_TITLE = "Rejestracja"

    LOGIN_FORM_TITLE = "Logowanie"
    LOGOUT_MESSAGE = "Pomyślnie wylogowano użytkownika:"

    BASKET_EMPTY_MESSAGE = "Twój koszyk jest pusty"
    BASKET_MESSAGE = "Twój koszyk"
