+++
title = "file input"
subsections = ["intermediate"]
+++
Use the `open` function to access a file.

	>>> infile = open("foo.txt", "r")

`open` takes two arguments: first, the name of the file; second, the "mode" we're opening the file in.
`"r"` means read-only. We'll talk about the other possible modes later.

`open` returns an object that represents the file we gave it. We can use this object to read the contents
of the file.

	>>> data = infile.read()

`read` will return the contents of the file as a string. Using read to store
the contents of a file in the `data` variable is like using copy-and-paste to
store the contents of a website inside of your text editor.

When we're done reading the file, we need to close it. This will tell the operating system that
we no longer need access to the file.

	>>> infile.close()

If you create a file called `foo.txt` with the contents,

	hello there
	foo bar

the following code will print the contents:

	>>> infile = open("foo.txt", "r")
	>>> data = infile.read()
	>>> infile.close()
	>>> print(data)
	hello there
	foo bar

{{% note %}}
It's actually better to open a file using `with`:

	>>> with open("foo.txt", "r") as infile:
	>>>     data = infile.read()
	>>> print(data)
	hello there
	foo bar

`with` will automatically close the file for you. We haven't covered `with`
yet, so you can wait to use it if you like.
{{% /note %}}
