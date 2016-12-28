+++
title = "input"
subsections = [ "beginner" ]
subsections_weight = 2
+++
`input` is the opposite of `print`. We use it to get typed input from the user:

	>>> number = input("Enter your favorite number: ")
	Enter your favorite number: 666
	>>> print(number)
	666
	>>> quest = input('What is your quest? ')
	What is your quest? To seek the holy grail!
	>>> print(quest)
	To seek the holy grail!

After the user presses Enter, `input` will return whatever the user typed.
