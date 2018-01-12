#for an N*N grid, to reach the bottom right, we must move right N times and down N times
#since we are only moving right and down, to find a unique path we need to find the unique sets of N-right and N-down
from math import factorial
N = 20
#if we could move right or down indefinitely there would be (N+N)! paths
paths = factorial(N+N)
#however we can only move right N times and down N times, this limits the paths by N! in both right and down
paths /= factorial(N) * factorial(N)
#in this way it is simple to change the dimensions of the grid
print (paths)
#expected result:137846528820