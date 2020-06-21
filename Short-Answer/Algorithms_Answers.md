#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) Runtime will be O(n) - Along with the loop, only one operation needs to be completed. The time will increase as n increases.

b)Runtime will be O(n log(n)) - There are two nested loops the first running at 0(n) but since the while loops variable 'j' is doubling, it increments exponentially, making it run at log(n) time

c)Runtime will be O(n) - With this recursive function, the time will increase as the size of the input increases. The base case plus the input create n+1, but since the operation is constant get rid of the +1.

## Exercise II

I would solve this is by doing a binary search, which has a runtime of O(lon(n))

1. Making 'f' the number of floors that in the building, we need to divide 'f' in half to find the middle of the building.
2. Once we establish the middle we can throw the egg off from that floor to see if it has broken.
   a -. If it has broken we need to find a new middle in the lower half of floors.
   b -. If the the egg has not broken we need to find the middle of the upper floors .
3. We repeat step two until we find a floor that no longer breaks the egg to find the value for 'f'.
