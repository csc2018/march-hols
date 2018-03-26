# Arcade

Aaron and Xuanchun are at an arcade.

**Prerequisites**: Binary search, loops, conditions, functions



# Task

After CTs are finally over, Aaron and Xuanchun have decided to hang out at an arcade to play the best game ever - _Vermintide_. After a few hours of hard work, they eventually managed to arrive at the final boss stage. Aaron can deal a point of damage to the boss every `a` seconds, while Xuanchun can do so every `x` seconds. The boss is a tough one, and can take a total of `b` points of damages before it dies. Aaron and Xuanchun want you, the future python master, to help them figure out a few things before they start on this quest.



## Part 1

Let **t** be the number of seconds elapsed after the game starts. Aaron deals a damage at the start of t=0, a, 2a, 3a, ..., and Xuanchun deals a damage at the start of t=0, x, 2x, 3x,… . Given t, a, b, x, help them figure out what is the total amount of damage done to the boss at time t, and whether the boss has been killed.

In `assignment.py`, find the line saying `def boss_dead(t, a, x, b):` and add your code below. The function should return `True` if the boss is dead at time t, and `False` otherwise.



### Sample Inputs and Outputs

| Input                        | Return Value | Explanation                                                  |
| ---------------------------- | ------------ | ------------------------------------------------------------ |
| `boss_dead(0, 1, 1, 10)` | `False`  | Aaron and Xuanchun each dealt 1 point of damage to the boss at t=0. However, the boss is still not dead as it can take 10 points of damage before dying and only 2 has been dealt. |
| `boss_dead(4, 1, 1, 10)` | `True`   | Aaron and Xuanchun each dealt 1 point of damage to the boss at t=0, 1, 2, 3, 4, totalling to 10 points of damage. Hence, the boss is dead. |
| `boss_dead(4, 1, 6, 7)`  | `False`  | Aaron dealt 5 points of damage while Xuanchun dealt 1. Hence the boss is not dead. |

### Hints

You may want to consider using the function `math.floor`. If you are not sure what it does, remember Google is your friend!



## Part 2

Aaron and Xuanchun now want to know how long it takes for the game to end, since they both have pretty strict curfews. A easy way to do this is to guess when the boss is dead. To do so, you start guessing at t=0. If the boss is dead, return 0 as the answer. If the boss is not dead, try t=1, t=2 and so on. Assume that the game will take no longer than 10<sup>18</sup> seconds to complete.



In `assignment.py`, find the line saying `def game_length(a, x, b):` and complete this function. Your function should return the time it takes for the game to end.



## Part 3

This part does not require any code to be written. Suppose that we have a=1000, x=1000, b=10<sup>9</sup>, how long does it take for the game to end? Will your code for Part 2 give a satisfactory running time for this case?



Another important observation to make: if the boss is dead at t=t<sub>0</sub>, will it be alive at t = t<sub>0</sub> + 1? How about t = t<sub>0</sub> + 10<sup>9</sup>?



## Part 4

​Your observation in the previous part directly leads to a much more optimal solution to the problem, namely binary search. The game can end anytime between 0 to 10<sup>18</sup> seconds, so we maintain 2 variables, `l = -1` and `r = 1000000000000000000`, representing the starting and ending point of our search space (starting point is exclusive). We guess the number in the middle of `l` and `r`, `m`, each time. If the boss is already dead at t=m, we do not have to care about any value of t greater than m, so we update `r=m`. Similarly, if the boss is not dead at t = m, then we do not have to care about any value of t smaller than m, and we update `l=m` . This continues until `r=l+1`, at which point `r` contains the write answer.



In the file `assignment.py`, find the line saying `def game_length_opt(a, x, b):` and complete the function using the algorithm described above. A template has already been given.
