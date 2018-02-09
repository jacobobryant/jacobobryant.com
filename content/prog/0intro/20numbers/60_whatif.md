+++
name = "what if"
+++
Pretend you're taking CS 101 at Wossamotta University. During the
semester there are two midterm exams and a final exam. Your grade
breakdown is:

 - 25% -- midterm 1 score
 - 25% -- midterm 2 score
 - 50% -- final exam score

You got 85% and 95% on the two midterms, respectively. So if you got
75% on the final, your grade would be
0.25 * 85 + 0.25 * 95 + 0.5 * 75 = 82.5%.


Now write the following program:

<pre>
>>> %Run what_if.py
Enter a final exam score: <b>87</b>
If you get 87 percent on the final exam, your grade will be 88.5 percent.
</pre>

<a href="#demo" class="btn btn-info" data-toggle="collapse">Show solution</a>
<div id="demo" class="collapse">
```python
# what_if.py
final = int(input("Enter a final exam score: "))
midterm1 = 85
midterm2 = 95
grade = 0.25 * midterm1 + 0.25 * midterm2 + 0.5 * final
print("If you get", final,
      "percent on the final exam, your grade will be",
      grade, "percent.")
```
</div>

After you finish that, create a new file, `calc.py`, which does the
following:

<pre>
>>> %Run calc.py 
Enter a number: <b>665</b>
Enter another number: <b>1</b>
665 plus 1 is 666
</pre>
