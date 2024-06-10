
### In this repo

- README.md is a basic python crash course in one page
- [learn-python-the-hard-way.md](learn-python-the-hard-way.md) is some notes on learn python the hard way ebook
- [pandas.md](pandas.md) is a crash course on pandas (possibly also numpy)
- [pytorch.md](pytorch.md) is a crash course on pytorch




### Resources

- It's recommended [here](https://www.youtube.com/watch?v=XlvfHOrF26M) to learn assembly, c and python, to get a feel for the abstractions going on when talking to a computer via a typical scripting language. 
- Useful python command-line utilities [here](https://news.ycombinator.com/item?id=40567532). 
  - E.g. `python -m timeit 'sum([list(range(1000))] * 50, [])'` times any python string. Many more.
  - 



# Environment & Setup

From [here](https://news.ycombinator.com/item?id=40568602):

> My favorite and probably most useful? `python3 -m venv ./venv` Honestly, forget about conda, poetry, virtualenvwrapper etc and just use that one.





# Syntax Basics

`l<goes here>`



# Classes

Show how to define a class etc. 

Python supports [multiple inheritance](https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance). When using `super()` in a child of a class which inherits from multiple parent classes, python uses the [Method Resolution Order](http://python-history.blogspot.com/2010/06/method-resolution-order.html) (MRO) to determine which method is called (more [here](https://stackoverflow.com/a/3277407)).  








### List comprehensions

- [Lex](https://www.youtube.com/watch?v=t5CcNJx5qtM): 

> With python when I saw list comprehensions, I just loved it. It was elegant, and made me fall in love with the language. 

[weird personal note] Bizarre coincidence because when I looked up what list comprehensions are, they're the thing I remember seeing when I tutored someone in SIT742 in 2021 and thought the python code was quite amazing (those one-liners to filter lists). Anyway, turns out they were list comprehensions, the same thing that made lex fall in love with python.


Incredibly useful explanation from chatgpt of what a python list comprehension is [here](https://chatgpt.com/c/0873bbd5-b953-444f-8c6c-f2681ff41fc7). But basicaly something of the form `[expression for item in iterable if condition]`.

Examples:

```py
# Create a list of squares:
squares = [x**2 for x in range(10)]

# Filtering to include only even numbers:
evens = [x for x in range(10) if x % 2 == 0]

# Using the expression to perform a complex operation:
formatted = [f"Number: {x}" for x in range(5)]
```

Why are they called list comprehensions (from chatgpt convo above)? 

> The term "list comprehension" comes from the mathematical concept of set comprehension, which is used in set theory to define sets based on existing sets. In mathematics, set comprehensions allow the creation of a new set by applying a condition and/or transformation to each element of an existing set.

> Python's list comprehensions extend this idea to lists, allowing elements to be dynamically generated and optionally filtered by a concise, expressive syntax. By adopting the term "comprehension," Python emphasizes the idea of constructing a new list by comprehensively processing each element of an existing iterable according to specified rules or expressions.





# Quirks and gotchas


- Interesting chat [here](https://news.ycombinator.com/item?id=40630059), [here](https://stackoverflow.com/questions/1132941/the-mutable-default-argument-in-python)

```python
def foo(a=[]):
    a.append(5)
    return a

foo()
# [5]
foo()
# [5, 5]
foo()
# [5, 5, 5]
foo()
# [5, 5, 5, 5]
foo()
```


