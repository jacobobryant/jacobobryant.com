+++
title = "input"
date = "2016-12-28T03:15:42-07:02"
subsections = [ "core" ]
subsections_weight = 2
+++
`input` is the opposite of `print`. We use it to get typed input from the user:

<pre>
>>> number = input("Enter your favorite number: ")
Enter your favorite number: <b>666</b>
>>> print(number)
666
>>> quest = input('What is your quest? ')
What is your quest? <b>To seek the holy grail!</b>
>>> print(quest)
To seek the holy grail!
</pre>

After the user presses Enter, `input` will return whatever the user typed.
