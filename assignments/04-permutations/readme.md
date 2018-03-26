# Permutations

Arnold needs help hacking into Ivy.

**Prerequisites**: Strings, loops, conditions, functions


# Task

After you wrote the guessing game for Arnold, he still finds no meaning to his existence. Bored, Arnold now wants to hack into his archnemesis' Ivy account. He knows his archnemesis' password is just a scrambled version of his archnemesis' favourite word, but he isn't too sure which permutation of the word it is. He wants you, the Future Python Master, to write a program to generate all permutations of the characters to obtain the password.

Assuming the length of the password to find is the same as the keyword, Arnold wants you to write a function that accepts **1 string argument, `keyword`**, and returns **a list of possible permutations**.

1. All characters are taken as lowercase.
2. The permutations must have the same length as the string.
3. No repeated strings are allowed.
4. The output is printed in console.

See the following examples.

**Generating permutations**:

Given string: `Fins`

```
[ 'fin', 'fni', 'nif', 'nfi', 'ifn', 'inf' ]
```

**No repeats**:

Given string: `Saws`

```	
[ 'assw', 'asws', 'awss', 'wass' ]
```

In `assignment.py`, find the line saying `def gen_passcode(keyword)` and add your code below.