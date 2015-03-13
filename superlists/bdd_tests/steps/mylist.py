from splinter import Browser
from behave import given, when, then


@given('a user')
def set_up_session(context):
    try:
        context.browser.quit()
    except AttributeError:
        pass
    context.browser = Browser()


@when('a new user')
def set_up_new_session(context):
    set_up_new_session(context)


@when('user visits the site')
def visit(context):
    context.browser.visit(context.home_url)


@then('the header text contins \'{text}\'')
def header_content(context, text):
    assert text in context.browser.find_by_tag('h1').text


@then('the page title contins \'{text}\'')
def title_content(context, text):
    assert text in context.browser.title.decode()


@then('user is taken to a new URL')
def at_list_url(context):
    context.tc.assertRegex(
        context.browser.url,
        '/lists/.+'
    )


@then('the page title and header contins \'{text}\'')
def title_and_header_contain(context, text):
    title_content(context, text)
    header_content(context, text)


@then('user is invited to enter an item')
def input_box_present(context):
    inputbox = context.browser.find_by_id('id_new_item').first
    assert inputbox['placeholder'] == 'Enter a to-do item'


@when('user enters \'{text}\'')
def enter_todo(context, text):
    context.browser.find_by_id('id_new_item').type(text + '\n')


@given('user has entered \'{text}\'')
def previously_entered(context, text):
    visit(context)
    enter_todo(context, text)


@then('\'{text}\' is in to-do list')
def verify_todo_content(context, text):
    table = context.browser.find_by_id('id_list_table')
    rows = table.find_by_tag('tr')
    context.tc.assertIn(text, [row.text for row in rows])


@then('\'{text}\' is not in to-do list')
def verify_not_in_page(context, text):
    page_text = context.browser.find_by_tag('body')
    context.tc.assertNotIn(text, page_text)


@then('finish test')
def unfinished(context):
    assert False
