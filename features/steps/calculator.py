from behave import *

@given('I power on the calculator')
def step_impl(context):
	context.power_on = True 

@given('I take the calculator')
def step_impl(context):
	context.current_value = 0

@when("I add {first_value:d} and {second_value:d}")
def step_impl(context, first_value, second_value):
	context.current_value = first_value + second_value

@when("I subtract {first_value:d} and {second_value:d}")
def step_impl(context, first_value, second_value):
	context.current_value = first_value - second_value

@when("I multiply {first_value:d} and {second_value:d}")
def step_impl(context, first_value, second_value):
	context.current_value = first_value * second_value

@when("I divide {first_value:d} and {second_value:d}")
def step_impl(context, first_value, second_value):
	context.current_value = first_value / second_value

@when("I potentiate {first_value:d} and {second_value:d}")
def step_impl(context, first_value, second_value):
	context.current_value = first_value ** second_value

@then("the result should be {expected_value:d}")
def step_impl(context, expected_value):
    assert context.current_value == expected_value
