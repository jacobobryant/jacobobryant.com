+++
title = "installing python"
subsections = ["introduction"]
subsections_weight = 3
date = "2016-12-28T03:15:42-06:03"
+++
For Windows or OS X, you can get python from [the Python
website](https://www.python.org/downloads/). You have a choice between
Python 2 and Python 3. Choose Python 3; it's what I use.

On Ubuntu Linux, you can probably use this command:

```
sudo apt-get install python3
```

If you're on some other flavor of Linux or you're having trouble with my
detailed instructions, just do an internet search for how to install Python 3
on whatever operating system you're using.

Once you have it installed, open the command line interface and run `python
--version`. On Windows, you might need to run `py --version` instead. If you're
on Linux and it doesn't work, try `python3 --version`. You should get something
like this:

```
$ python --version
Python 3.5.2
```

If it doesn't work, you'll need to figure out what's wrong before moving on. If
you're having trouble fixing it, feel free to email me
(contactme@jacobobryant.com). I can afford to do that since my website doesn't
have any regular readers as of writing this, other than perhaps my mother.
You're probably reading this because I asked you to try the course and give me
feedback, so feel free to ask me for help in person.

Now download [this Python program](/files/hilo.py). Use the `cd` command to
move to the same folder where you saved the program and then run `python
hilo.py` (or `py hilo.py`, or ...).

```
$ cd my_programs/
$ python hilo.py 
I'm thinking of a number between 1 and 100, sucka
You have 7 guesses left.
Pick a number:
```

{{% tip %}}
Press Control-C to stop a program that hasn't finished yet.
{{% /tip %}}

Now that you know how to run a Python program, the only thing left is
to learn how to make the programs in the first place (how hard could it be?).
In the next episode, you'll learn how to mess around with your first Python
commands.
