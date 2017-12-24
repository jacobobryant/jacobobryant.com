+++
title = "nested data"
subsections = ["advanced"]
+++
{{< req "int/lists"
        "int/dictionaries" >}}

So you know about lists and dictionaries. It turns out that you
can have a list inside of a dictionary:

	>>> foom = {'acceptable_foods': ['mice', 'fish', 'spaghetti'],
	            'favorite_humans': ['ghandi', 'gen. patton']}
	>>> foom['acceptable_foods']
	['mice', 'fish', 'spaghetti']
	>>> foom['acceptable_foods'][1]
	'fish'

And you can have a dictionary inside of a list:

	>>> cats = [{'name': 'foom', 'occupation': 'web developer'},
	            {'name': 'fluffy', 'occupation': 'meter maid'}]
	>>> cats[1]['name']
	'fluffy'

You can have lists inside of lists inside of dictionaries inside of lists
inside of... In other words, lists and dictionaries can be "nested" inside of
each other. This allows us to store a lot of information about something all in
one place.
