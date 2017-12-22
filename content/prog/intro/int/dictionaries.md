+++
title = "dictionaries"
subsections = ["intermediate"]
+++
{{% req "int/lists" %}}

Suppose you're writing a program that has a bunch of settings. You could make
a separate variable for each setting:

	>>> chopping_speed = 4
	>>> saltiness = "very salty"
	>>> self_destruct_time = 10

But that could be inconvenient if you have lots of settings. What if you want to store them
all in a single variable? You could use a list:

	>>> settings = [4, "very salty", 10]

But this has a big problem: you have to remember what each setting is! To get
the saltiness level, you'd have to type `settings[1]`. Besides being ugly,
someone else who looks at your code will have no idea what in the heck
`settings[1]` is supposed to mean without digging deeper. And what if you got
`chopping_speed` mixed up with `self_destruct_time`? *shudder*...

What if instead of using number indices (like `settings[1]`), you could instead use a string as an index,
like `settings['saltiness']`? That's what a dictionary is for!

	>>> settings = {'chopping_speed': 4,
	                'saltiness': 'very salty',
	                'self_destruct_time': 10}
	>>> settings['chopping_speed']
	4
	>>> settings['saltiness']
	'very salty'
	>>> settings['self_destruct_time']
	10
	>>> settings['self_destruct_time'] = 9
	>>> settings['self_destruct_time']
	9

A dictionary lets you store a bunch of "key-value pairs". The dictionary has a set
of keys (in our case, `'chopping_speed'`, `'saltiness'` and `'self_destruct_time'`).
Each of those keys has a value assigned to it. The keys actually don't have to be strings:

	>>> my_dict = {4: "hello"}

But usually strings are what you want for keys. 

{{% note %}}
It's called a "dictionary" because a dictionary has a set of keys (words) and a
value (a definition) for each key.
{{% /note %}}
