+++
title = "import"
subsections = ["intermediate"]
+++
Python comes with a lot of helpful functions out of the box like
`print`, `input` and `launch_ze_missiles`, but there's a lot of stuff
you don't get out of the box. The `import` statement allows you to
access extra functions and other code.

For instance, if you're pining to do some trigonometry, you can import
the `math` package:

	>>> import math
	>>> math.sin(666)
	-0.01764164581327013
	>>> math.pi
	3.141592653589793
	>>> math.cos(math.pi)
	-1.0

(This is more pleasant than the alternative of taking a year of
calculus and then writing your own `sin` function.)

There are many more packages at your disposal. Try importing
the `antigravity` package some time.
