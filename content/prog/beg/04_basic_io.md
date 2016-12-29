+++
title = "basic io"
date = "2016-12-28T03:15:42-07:03"
subsections = [ "beginner" ]
subsections_weight = 3
+++
Create a file called `basic_io.py` ("io" is short for input/output). In it, write a program
that displays a friendly greeting:

	$ python basic_io.py
	What is your name? kevin
	Go away kevin

<a href="#demo" class="btn btn-info" data-toggle="collapse">Show solution</a>
<div id="demo" class="collapse">
`basic_io.py`:

	name = input("What is your name? ")
	print("Go away", name)

</div>
