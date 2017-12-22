+++
title = "replace"
subsections = ["intermediate"]
+++
What happens if you find yourself in possession of a string that
has forbidden words? Easy, use the `replace` function!

	>>> bad_string = "I like cheese"
	>>> bad_string.replace("cheese", "the Mormon Tabernacle Choir")
	'I like the Mormon Tabernacle Choir'

You can also use it with single characters to make your sentences more
phonetic:

	>>> "caitlyn likes cool coconuts".replace("c", "k")
	'kaitlyn likes kool kokonuts'

You can use the empty string as the replacement if you just want to
delete something. This can help to make your sentences much shorter
and thus faster to read:

	>>> "go hang a salami im a lasagna hog".replace("a", "")
	'go hng  slmi im  lsgn hog'

(Your readers will appreciate it.)
