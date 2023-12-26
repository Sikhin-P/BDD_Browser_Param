from behave import *
from POM.MyDriver import MyDriver
from POM.Base import Base
from POM.ResultsPage import ResultsPage
from POM.HomePage import HomePage


@given('Open a browser')
def open_browser(context):
    context.user = Base(context)


@given('Navigate to "{url}"')
def navigate(context, url):
    context.user.driver.get(url)


@when('Search with "{word}"')
def search(context, word):
    HomePage(context.user).search_for(word)
    context.results = ResultsPage(context.user).top_results(5)


@then('Save search results to text file')
def verify_and_save(context):
    assert context.results is not None, 'Failed to get results'
    with open('output.txt', 'w') as file:
        for result in context.results:
            for item in result:
                file.write(item + ": ")
            file.write('\n')
