+++
name = "calculator"
+++
Create a new file, `calc.py`, which does the following:

<pre>
>>> %Run calc.py 
Enter a number: <b>665</b>
Enter another number: <b>1</b>
665 plus 1 is 666
</pre>

<a href="#demo" class="btn btn-info" data-toggle="collapse">Show solution</a>
<div id="demo" class="collapse">
```python
# calc.py
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print(x, "plus", y, "is", x + y)
```
</div>
