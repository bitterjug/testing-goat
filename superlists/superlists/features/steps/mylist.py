from behave import given, when, then


@given('a user')
def null(context):
    pass


@when('user visits the site')
def visit(context):
    context.browser.visit(context.home_url)


@then('the header text contins \'{text}\'')
def header_content(context, text):
    assert text in context.browser.find_by_tag('h1').text


@then('the page title contins \'{text}\'')
def title_content(context, text):
    assert text in context.browser.title.decode()


@then('the page title and header contins \'{text}\'')
def title_and_header_contain(context, text):
    title_content(context, text)
    header_content(context, text)


@then('user is invited to enter an item')
def input_box_present(context):
    inputbox = context.browser.find_by_id('id_new_item')
    self.assertEqual(
        inputbox.get_attribute('placeholder'),
        'Enter a to-do item'
    )


@when('user enters \'{text}\'')
def enter_todo(context, text):
    context.browser.find_by_id('id_new_item').fill(text)


@then('\'{text}\' is in to-do list')
def verify_todo_content(context, text):
    rows = context.browser.find_by_id('id_list_table').table.find_by_tag('tr')
    self.assertTrue(any(row.text == '1. Buy peacock feathers') for row in rows)


@then('finish test')
def unfinished(context):
    assert False
