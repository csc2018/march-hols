# Minigame

Arnold wants you to write a game.

**Prerequisites**: Strings, loops


# Task

After CTs are finally over, Arnold is bored with life. He tasks you, the future Python master, to write him a number guessing game because that's all he likes.

The program picks a random number from 1 to 100. The player keeps guessing as long as their guess is wrong **and** they have guessed less than 7 times. If their guess is higher than the number, print "Too high". If their guess is lower than the number, print "Too low". When they guess the correct number, the player wins. If they hit 7 guesses, the player loses.

Two examples of what you can find in the console:
```
I'm thinking of a number between 1-100. You have 7 guesses.
Guess #1: 50
Too low!
Guess #2: 75
Too low!
Guess #3: 87
Too high!
Guess #4: 82
Too low!
Guess #5: 84
You guessed it! What are the odds??
```

```
I'm thinking of a number between 1-100. You have 7 guesses.
Guess #1: 1
Too low!
Guess #2: 2
Too low!
Guess #3: 99
Too high!
Guess #4: 98
Too high!
Guess #5: 3
Too low!
Guess #6: 4
Too low!
Guess #7: 97
Sorry, you didn't guess it in 7 tries! You lose.
```


## Optional extension

You can extend the game in a way that makes it more enjoyable. Here's an example:

```
I'm thinking of a number between 1-100. You have 7 guesses.
Guess #1: 1
Too low!
Guess #2: 2
Too low!
Guess #3: -8
That's not between 1-100! Guess again!
Guess #3: 6969
That's not between 1-100! Guess again!
Guess #4: 3
Too low!
Guess #5: 4
Too low!
Guess #6: 4
You guessed that already! Guess again!
Guess #6: 5
Too low!
Guess #7: 99
Sorry, you didn't guess it in 7 tries! You lose.
```

Save your code as a Python file (with a `.py` extension).

Commit and push your new files to your repo.