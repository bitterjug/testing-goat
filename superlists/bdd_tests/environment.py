from splinter import Browser
from unittest import TestCase
from django.core.management import call_command


print("env")


def before_all(context):
    context.browser = Browser()
    context.home_url = context.config.server_url
    context.tc = TestCase() # for the assert methods


def after_all(context):
    context.browser.quit()

def before_scenario(context, feature):
    """ Run each scenario in a separate database copy """
    # This is a hack, we really should use transactions and roll back
    # See https://github.com/django-behave/django-behave/issues/43
    call_command('flush', verbosity=0, interactive=False)
