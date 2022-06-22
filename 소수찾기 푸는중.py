from itertools import permutations
from itertools import combinations

def solution(num: str) -> int:
    count_prime = 0
    commpare_list = []
    for i in range(1, len(num) + 1):
        commpare_list += combinations(num, i)
    return commpare_list

print(solution("17"))
print(solution("011"))