from behave import given, when, then


@given('a user')
def null(context):
    pass


@when('a user visits the site')
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


@then('finish test')
def unfinished(context):
    assert False
