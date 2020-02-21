#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

a = 0 is constant time (assignment) => O(1)
while (a < n * n * n) is a loop => O(n)
a = a + n * n is constant time (assignment) => O(1)

If n = 0 the program exits.
If n = 1 the loop runs, a is assigned 1 and the program exits.
If n = 2 the loop runs, a is assigned 4
         the loop runs, a is assigned 8 and the program exits.
If n = 3 the loop runs, a is assigned 9
         the loop runs, a is assigned 18
         the loop runs, a is assigned 27 and the program exits.

Therefore the number of runs is proportional to n and the algorithm has an overall Big O of n.

b)

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

sum = 0 is constant time (assignment) => O(1)
for i in range(n) is a loop => O(n)
j = 1 is constant time (assignment) => O(1)
while j < n is a loop => O(n)
j *= 2 is constant time (assignment) => O(1)
sum += 1 is constant time (assignment) => O(1)

The first loop runs n times. The second loop runs n - 1 times. 
They're nested, so we multiply them together leading to a Big O for the algorithm of n^2.

c)

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

Recursion creates a loop which runs until n = 0 and then returns, so the Big O of this algorithm is n.

## Exercise II


