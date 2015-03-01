from splinter import Browser
from unittest import TestCase


print("env")


def before_all(context):
    context.browser = Browser()
    context.home_url = context.config.server_url
    context.tc = TestCase() # for the assert methods


def after_all(context):
    context.browser.quit()
