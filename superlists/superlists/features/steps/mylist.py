from behave import given, when, then


@given('a user')
def null(context):
    pass


@when('a user visits the site')
def visit(context):
    context.browser.visit(context.home_url)


@then('the page title contins \'{text}\'')
def title_content(context, text):
    assert text in context.browser.title.decode()

@then('finish test')
def unfinished(context):
    assert false
