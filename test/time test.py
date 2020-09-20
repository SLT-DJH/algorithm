from itertools import permutations
import time

start = time.time()

team = [2, 3, 4, 5, 6, 7, 8, 9]

permu = permutations(team, 8)

permu = list(permu)

print("time :", time.time() - start)
