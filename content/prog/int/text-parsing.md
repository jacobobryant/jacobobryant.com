+++
title = "text parsing"
subsections = ["intermediate"]
+++
If you have a text file called `my_name.txt` with the following contents,

	George Foreman

it's easy to read the file and store the contents in a variable called `my_name`. However, consider
a more fancy file called `my_kids.txt` with these contents:

	George Jr. (male)
	George III (male)
	George IV (male)
	Georgetta (female)

What if you want to store all that data in separate variables? You need to "parse" the text file; read on
for the juicy details.

{{< req "int/lists"
				"int/dictionaries"
				"int/split"
				"int/strip"
>}}

