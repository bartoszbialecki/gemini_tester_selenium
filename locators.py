from selenium.webdriver.common.by import By


class HomePageLocators():
    COOKIES_DIALOG = (By.ID, 'cookies-modal')
    COOKIES_DIALOG_OK_BUTTON = (By.CLASS_NAME, 'cookies-close')

    ACCOUNT_LINK = (By.CSS_SELECTOR, '.nav-button-grid.login')
    REGISTER_LINK = (By.XPATH, '//a[@href="/user/createAccount"]')
    LOGIN_LINK = (By.XPATH, '//a[contains(text(), "Zaloguj się")]')


class RegisterPageLocators():
    FORM = (By.ID, 'user-register-form')
    EMAIL_INPUT = (By.ID, 'st_form-user-email')
    PASSWORD_INPUT = (By.ID, 'st_form-user-password1')
    PASSWORD_CONFIRM_INPUT = (By.ID, 'st_form-user-password2')
    PRIVACY_CHECKBOX = (By.ID, 'st_form-user-privacy')
    REGISTER_BUTTON = (By.XPATH, '//div[@id="st_button-user-account"]/button')


class LoginPageLocators():
    FORM = (By.ID, 'st_application-user-login-new')
    EMAIL_INPUT = (By.ID, 'st_form-user-email')
    PASSWORD_INPUT = (By.ID, 'st_form-user-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.act_button.login')
    ERROR_TOOLTIP = (By.XPATH, '//div[@class="error_tooltip"]/img')
    ERROR_TOOLTIP_MESSAGE_ATTRIBUTE = 'data-tooltip'


class BasketPageLocators():
    BASKET_BOX = (By.ID, 'basket_index')
    ACCOUNT_BUTTON = (By.CLASS_NAME, 'login')
    USER_EMAIL_LINK = (By.CLASS_NAME, 'user_mail')
    LOGOUT_LINK = (
        By.XPATH, '//div[@class="reg"]/a[@href="https://www.aptekagemini.pl/user/logoutUser"]')
    LOGOUT_FORM = (By.ID, 'logout_form')
