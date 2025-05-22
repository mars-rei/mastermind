from behave import given, when, then, step

@given('they have specified an argument of {number:m}')
def step_impl(context, menu: int):
    pass

@when('they confirm their choice of game option')
def step_impl(context):  
    pass

@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0