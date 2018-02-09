+++
name = "input"
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


*From a programmer's point of view, the user is a peripheral that types when you issue a read request.*
-- Peter Williams
