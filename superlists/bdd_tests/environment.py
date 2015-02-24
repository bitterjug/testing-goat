from splinter import Browser


print("env")


def before_all(context):
    print("before all")
    import ipdb; ipdb.set_trace();
    context.browser = Browser()
    context.home_url = context.config.server_url


def after_all(context):
    print("after all")
    context.browser.quit()
