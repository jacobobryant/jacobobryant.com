+++
title = "the python shell"
subsections = ["introduction"]
subsections_weight = 4
date = "2016-12-28T03:15:42-06:04"
+++

Try typing `python` without anything else after it. You should see something like this:

```
$ python
Python 3.5.2 (default, Jun 28 2016, 08:46:01) 
[GCC 6.1.1 20160602] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You're now in a new kind of command line interface, the Python command line
interface. We call it the Python shell. Why do we call it a shell? It would
take me more than ten words to explain, so don't worry about it. In general, it
may help you be less confused if whenever you see a word that seems out of
place, assume it's like that because of historical reasons and don't worry
about why they called it that (they had to call it something). That's what I do
a lot.

Remember the "prompt" from the command line? See that `>>>` up there? That's your new prompt!
As long as it's there, the terminal/Command Prompt is expecting Python commands, not regular
ones. So try typing this command and see what happens ;)

```
>>> print('I like cheese')
```

That's a basic command. They can get more complicated, like this:

```
>>> pairs = [(6, 's'), (2, 'r'), (1, 'u'),
...          (4, 'r'), (8, '!'), (7, 'e'),
...          (0, 's'), (3, 'p'), (5, 'i')]
>>> print(''.join([char for num, char in
...                sorted(pairs, key=lambda x: x[0])]))
surprise!
```

But there's no need to worry about that for now. The Python shell will be a
valuable tool for you. You can use it to interactively try out new Python
commands as you learn them. When you start writing complete programs, then you
can save the commands in a text file like in `hilo.py`.

When you're done, type `quit()` to exit the Python shell and go back to the normal
command line:

```
>>> quit()
$
```

You've finished the introduction! Tune in next time to see our dashing hero
learn more about their first Python command, `print`.
