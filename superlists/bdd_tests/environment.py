from unittest import TestCase
from django.core.management import call_command


def browser_for(self, user):
    """ Convenience function to look up a given user's
    browser, or the current one if a more general term is used.
    """
    if user in ['she', 'he', 'user']:
        return self.browser
    else:
        return self.browsers[user]


def before_all(context):
    context.home_url = context.config.server_url
    context.tc = TestCase()  # for the assert methods

    # dict of user -> browser
    context.browsers = {}
    context.__class__.browser_for = browser_for


def after_all(context):
    # Close all users' browsers
    for browser in context.browsers.values():
        browser.quit()


def before_scenario(context, feature):
    """ Run each scenario in a separate database copy """
    # This is a hack, we really should use transactions and roll back
    # See https://github.com/django-behave/django-behave/issues/43
    call_command('flush', verbosity=0, interactive=False)
