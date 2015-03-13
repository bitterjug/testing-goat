from unittest import TestCase
from django.core.management import call_command


def before_all(context):
    context.home_url = context.config.server_url
    context.tc = TestCase()  # for the assert methods


def after_scenario(context, feature):
    try:
        context.browser.quit()
    except AttributeError:
        pass


def before_scenario(context, feature):
    """ Run each scenario in a separate database copy """
    # This is a hack, we really should use transactions and roll back
    # See https://github.com/django-behave/django-behave/issues/43
    call_command('flush', verbosity=0, interactive=False)
