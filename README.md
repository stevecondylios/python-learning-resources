

### Why python?

Lex ([here](https://www.youtube.com/watch?v=pdJQ8iVTwj8&t=10m20s)):

> what do I love about python? how intuitive it is, how it feels like natural language, how I can read and understand other people's code, it's more condenced than c++ and c, there's a bunch of little features (e.g. list comprehensions), it's package ecosystem and the humans involved.

Chris lattner:

> python is the universal connector




### In this repo

- README.md is a basic python crash course in one page
- [learn-python-the-hard-way.md](learn-python-the-hard-way.md) is some notes on learn python the hard way ebook
- [pandas.md](pandas.md) is a crash course on pandas (possibly also numpy)
- [pytorch.md](pytorch.md) is a crash course on pytorch




### Resources

- It's recommended [here](https://www.youtube.com/watch?v=XlvfHOrF26M) to learn assembly, c and python, to get a feel for the abstractions going on when talking to a computer via a typical scripting language.
- Useful python command-line utilities [here](https://news.ycombinator.com/item?id=40567532).
  - E.g. `python -m timeit 'sum([list(range(1000))] * 50, [])'` times any python string. Many more.
- Random reading on duckdb vs pandas/polars [here](https://www.pgrs.net/2024/11/01/duckdb-over-pandas-polars/)



# Installation

- Derek recommends installing via brew.
    - More specifics on my learnings under [Environment & Setup](#environment--setup)
- `python3` to run
- Note that [Brew](https://docs.brew.sh/Homebrew-and-Python) also installs pip3
- so tl;dr: install via brew, then you'll have python3 and pip3 available via the command line




# Environment & Setup


- Note: a newish tool called 'uv' (made in rust) is apparently great.
  - It lets you skip the whole process of setting up a virtual env / pip by placing a shebang a the top of the python script and a /// script /// section to denote which packages and python version to use, and uv sets up the environment automatically with minimal fuss, caching, etc).
- sc: I think you can install python packages via brew (just as you can with pip), but for whatever reason python could never find them ie. `import xyz` would fail. So my 'go to' is a virtual env every time and then use pip.
- sc: if you want to use a python version other than the latest installed via brew, try running `brew search python@` to see what python versions are installed via brew. Then you can run commands (or start the interpreter) using `python3.11` (or whatever version you have, note no @ symbol when using it in the terminal). (also note, you can install any specific python version with brew by `brew install python@3.14` - I'm 99% sure)
  - I then used `python3.11 -m venv .venv` etc to create the virtual env as per below but using `python3.11` in place of `python`.
    - This approach was handly when I was getting errors using `openai-whisper` package with the latest python version `3.13`
    - Here's a guide to which version of python is most recent and which are getting old: https://devguide.python.org/versions/


### How to set up a virtual environment


From [here](https://news.ycombinator.com/item?id=40568602):

<hr>

> My favorite and probably most useful? `python3 -m venv ./venv` Honestly, forget about conda, poetry, virtualenvwrapper etc and just use that one.

<hr>

Start a python [virtual env](https://docs.python.org/3/library/venv.html). The reason is because macOS comes with python and the virtual env stops them messing with eachother. My first impression is python virtual envs seem similar to ruby's bundler in that it will use the ruby (python) installation it finds for the project and only if it doesn't see one will it use the system one.


```sh
# the last argument is the directory name where the virtual env will go

python -m venv .venv

# Note: might be python3 depending on the system

python3 -m venv .venv

# Check that it worked (should see a hidden directory called .venv)

ls -a

# activate it
source .venv/bin/activate
# Should see command prompt change to (.venv) (base)


# now that it's activated, run this to confirm
which python

# It should return something like
# /Users/st/python/myproject/.venv/bin/python
# and not any other python installation like
# /Users/st/opt/anaconda3/bin/python


# You can tell a python virtual environment is active because the command prompt will look like this
# (venv) (base)
# You can deactivate it with
deactivate

# Now when you use pip or pip3, it will use the correct (vitual env) version of python
# Note that you'll have to install things for each new virtual environment
```



Notes

- Don't commit .venv to git. Instead use `pip freeze > requirements.txt` (**note*: venv has to be activated or else `pip freeze` will include very package on your *system* python, which you don't want).
- Omit .venv from git with `echo "**/.venv" >> .gitignore`
- Install packages from requirement.txt with `pip install --requirement requirements.txt`
- Note that `source .venv/bin/activate` seems to contain some paths which had to be modified manually when I rearranged a repo.




# Tooling

- A couple of times in [this](https://www.youtube.com/watch?v=l8pRSuU81PU) video, Karpathy uses 'break' which I think is a vscode command pallet item (as opposed to code like `binding.pry` or `browser()`)






# Syntax Basics





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


