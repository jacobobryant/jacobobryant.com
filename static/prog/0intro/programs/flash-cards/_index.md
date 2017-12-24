+++
title = "flash cards"
subsections = [ "programs" ]
subsections_weight = 10
+++
This program quizzes you on your flash cards. Your flash card terms
and definitions are stored in a text file, like so:

	my cool pack
	entomology: the study of word origins
	entomologists: people who hate that joke^^
	your wife's birthday: 1 jan 1970

	things that float
	small rocks: tiny hard things
	a duck: anything that quacks

You can have multiple "packs" of flash cards. The first line of each
block of text is the name of the pack. Each pack can have as many
term-definition pairs as you like, and the text file can have as many
packs as you like. The packs must be separated by a blank line. Each
term must be followed by a colon and then its definition.

An example run of the program should go like this:

	$ python flashcard.py 
	Packs to choose from:
	0 - my cool pack
	1 - things that float
	Enter a number from 0 to 1: 0

	Think of the definition of "entomology", then press Enter
	The definition is "the study of word origins"

	Think of the definition of "your wife's birthday", then press Enter
	The definition is "1 jan 1970"

	Think of the definition of "entomologists", then press Enter
	The definition is "people who hate that joke^^"

Notice that the program quizzes you on the terms in random order.
Also, the program does indeed wait for you to press Enter before
displaying the definition of a card, although you can't see that from
the example.

This program could use more features, but we'll implement this simple
version first as a starting point.

### Read data file
{{< req "int/file-input"
        "adv/text-parsing" >}}

You need a file for your flashcard data. Download the [example
file](data.txt) I used above. In your program, create a variable
called `packs` and store the flash card data in it. Use this format:

1. `packs` is a list.
2. Each element of `packs` is a dictionary with two keys: "title" and "terms".
1. "title" is the name of the pack.
2. "terms" is a dictionary. Each key in the dictionary is a term in
   the pack. The corresponding value is the term's definition.

The example below should clarify the format. Running the following
code snippet with the example data file should print "PASS":

```python
packs = []

# insert your code here
# ...

expected_packs = [
    {
      "title": "my cool pack",
      "terms": {
        "your wife's birthday": "1 jan 1970",
        "entomologists": "people who hate that joke^^",
        "entomology": "the study of word origins"
      }
    },
    {
      "title": "things that float",
      "terms": {
        "small rocks": "tiny hard things",
        "a duck": "anything that quacks"
      }
    }
]

assert packs == expected_packs
print("PASS")
```

### Choose a pack
The next step is to ask the user which pack they want to use. After the user
chooses a pack, store the dictionary for that pack in a variable called `pack`.
If the user chooses pack 0, the following code snippet should print "PASS":

{{< highlight python >}}
# insert your code here
# ...

expected_pack = {'entomology': 'the study of word origins',
                 "your wife's birthday": '1 jan 1970',
                 'entomologists': 'people who hate that joke^^'}

assert pack == expected_pack
print("PASS")
{{< /highlight >}}

### Quiz the user
Finally, loop through the terms in the selected pack and quiz the user
on them.

{{< req "int/random" >}}

After you complete this section, the program should be done! You
can compare your code to [my code](flashcards.py) to see if we did
anything differently.

### Add features

Try adding these:

 - After quizzing the user on a term, ask them if they got it right.
	 Keep track of the terms they didn't get right. After finishing all
	 the terms, quiz the user again on all the terms they didn't get
	 right. Repeat until they get all the terms right.
 - Create a list of insults. When the user guesses wrong, output a
	 random insult.
