+++
title = "fix filenames"
shorttitle = "filenames"
subsections = [ "programs" ]
subsections_weight = 0
draft = true
+++

You have just procured a directory full of mp3 files. Much to your
dismay, you find that they have names like `My Cool Song.mp3` and
`O'Bryant's theme SONG.mp3`. Spaces in file names are an abomination,
and it's also nice to have everything be lowercase so that it's all
uniform. Your mission: write a program to help you rename these files
automatically. The program should:

1. Replace spaces with underscores.
2. Remove apostrophes.
3. Convert all characters to lower case.
4. Print out the new file names in alphabetical order.

You should be able to pass in file names as command line arguments,
and then the program will print each fixed name on a separate line.
Here's an example:

<pre>
$ <b>python fix_names.py "O'Bryant's theme SONG.mp3" "My Cool Song.mp3"</b>
my_cool_song.mp3
obryants_theme_song.mp3
</pre>

{{% req "int/command-line-arguments"
	"int/replace"
	"int/case"
	"int/list-comprehensions"
	"int/sorted"
%}}

<a href="#demo" class="btn btn-info" data-toggle="collapse">Show solution</a>
<div id="demo" class="collapse">
```python
# fix_names.py
import sys
transform = lambda s: s.replace(" ", "_").replace("'", "").lower()
new_names = sorted([transform(filename) for filename in sys.argv[1:]])
for name in new_names:
    print(name)
```
</div>
