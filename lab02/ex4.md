1. Describe the algorithm you will use to find the room. Assume all the information you have is the one given by the sign; you have no knowledge of the floor plan.

If the room number is between 100 and 130 (inclusive), go left and walk clockwise. Otherwise, go right and walk counterclockwise. Check the rooms one by one until you find the room. 

In this case, to find EY128 according to this algorithm, you would go left and continue until you find it.

2. How many ”steps” it will take to find room EY128? And what is “step” in this case?

It will take 15 "steps" to find EY128. In this case, one "step" is checking one room, and following the algorithm, EY128 would be the 15th room checked.

3. Is this a best-case scenario, worst-case scenario, or neither?

This is neither a best-case not a worst-case scenario.

4. With this particular sign and floor layout, explain what a worst-case or best-case scenario would look like.

The worst-case scenario would be if you're looking for the last room on the cutoff written on the sign (EY130), which would take 16 steps. The best-case scenario would be if the room you're looking for is the first room on either end (EY100 or EY138), which would only take 1 step.

5. Suppose after a few weeks in the term you memorize the layout of the floor. How would you improve the algorithm to make it more efficient?

The algorithm could be changed so that you go left if the room number is between 100 and 118 (inclusive), and you go right if the room number is larger than this. Since 118 is around the middle in the range of room numbers, you reduce the number of steps in the worse-case scenario.