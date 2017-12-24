+++
title = "split"
subsections = ["intermediate"]
+++
{{< req "int/lists"
        "int/file-input" >}}

`split` takes a string and returns a list of all the words:

	>>> phrase = "I like cheese"
	>>> phrase.split()
	['I', 'like', 'cheese']

This is handy for reading from a file, because you can split the contents
into a list of lines:


