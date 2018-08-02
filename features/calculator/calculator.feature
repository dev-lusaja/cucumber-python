Feature: Calculator
	As a user
	I want to use a Calculator
	So that I  dont need  to calculate myself

	Background: Power On
		Given I power on the calculator 

	Scenario: Add two numbers
		Given I take the calculator
		When I add 2 and 3
		Then the result should be 5

	Scenario: Subtract two numbers
		Given I take the calculator
		When I subtract 5 and 3
		Then the result should be 2

	Scenario: Multiply two numbers
		Given I take the calculator
		When I multiply 1 and 3
		Then the result should be 3

	Scenario: Divide two numbers
		Given I take the calculator
		When I divide 6 and 2
		Then the result should be 3

	Scenario Outline: Potentiate two numbers
		Given I take the calculator
		When I potentiate <base> and <potence>
		Then the result should be <result>

		Examples:
			| base | potence | result |
			|	6  |	2	 |	36	  |