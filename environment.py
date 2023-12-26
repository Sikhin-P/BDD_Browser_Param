from selenium.webdriver import Chrome, Firefox


def before_all(context):
    context.driver = {
        'Chrome': Chrome,
        'Firefox': Firefox
    }[context.config.userdata['browser']]()
