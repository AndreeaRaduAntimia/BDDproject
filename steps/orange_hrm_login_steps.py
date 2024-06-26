from behave import *


# given reprezinta tag-ul care este scris in fisierul de tip feature pentru un anumit pas
# in cazul de la linia 6, given-ul va identifica pasul de la linia 9 din orange_hrm.feature pe baza textului scris intre paranteze
@given("The user is on the Orange HRM login page")
def step_impl(
        context):  # context este ca un fel de cutiuta care va stoca toate obiectele instantiate din clasele de tip pages
    context.login_page.navigate_to_homepage()  # am apelat metoda care navigheaza catre pagina de login a aplicatiei orangeHRM


@when('The user inserts valid information on the username and password fields')
@when('The user inserts valid username "username" and valid password "password"')
def step_impl(context):
    context.login_page.insert_username()
    context.login_page.insert_password()


# context.login_page.insert_username(username)
# context.login_page.insert_password(password)

@when('The user clicks on the login button')
def step_impl(context):
    context.login_page.click_login_button()


@when('The user clicks on Forgot your password Link')
def step_impl(context):
    context.home_page.try_to_logout()
    context.login_page.click_forgot_your_pass()


@then('The user is redirected forward and the url contains {keyword}')
def step_impl(context, keyword):
    # raise NotImplementedError('Then The user is logged into the application')
    context.login_page.check_current_url(keyword)


@then('The user receives error message: "{error_message}" and cannot login into the application')
def step_impl(context, error_message):
    context.login_page.check_login_error_message(error_message)


# raise NotImplementedError('Then The user receives error message: "Invalid credentials" and cannot login into the application')

# cand avem parametri de introdus este important ca textul sa fie intre apostroafe si parametrii intre ghilimele
@when('The user inserts username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.home_page.try_to_logout()
    context.login_page.insert_username(username)
    context.login_page.insert_password(password)


@given("The user is logged into the application")
def step_impl(context):
    context.login_page.insert_username()
    context.login_page.insert_password()
