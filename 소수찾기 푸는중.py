from itertools import permutations
from itertools import combinations

def solution(num: str) -> int:
    count_prime = 0
    num_list = list()

    for i in range(1, len(num) + 1):  # make permutations 1
        num_list += permutations(num, i)

    num_list = list(map(''.join, num_list))
    num_list = list(set([int(i) for i in num_list]))
    check_list = [True for i in range(len(num_list))]

    for i in num_list:
        if i >= 2:
            j = 2
            while j <= int(i ** 0.5):
                if i % j == 0:
                    break
                if j == int(i ** 0.5):
                    count_prime += 1
                    break
                j += 1

    for i in num_list:
        if i >= 2:
            pass



    return num_list

print(solution("17"))
print(solution("011"))
print(solution("3"))