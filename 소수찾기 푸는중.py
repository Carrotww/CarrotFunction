from itertools import permutations
from itertools import combinations

def solution(num: str) -> int:
    count_prime = 0
    num_list = list()
    for i in range(1, len(num) + 1):
        # num_list.append(combinations(num, i))
        num_list += combinations(num, i)
    num_list = set(num_list)
    num_list = list(map(''.join, num_list))
    num_list = [int(i) for i in num_list]
    check_list = [True for i in range(len(num_list))]

    for i in range(len(num_list)):
        sqrt = int(num_list[i] ** 0.5) + 1
        for j in range(2, sqrt):
            if num_list[i] % j == 0:
                check_list[i] = False
                continue

    for i in check_list:
        if i == True:
            count_prime += 1

    return num_list

print(solution("17"))
print(solution("011"))