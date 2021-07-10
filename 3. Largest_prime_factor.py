"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


def simpleDividers(n):
    answer = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            answer.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        answer.append(n)
    return answer


print(simpleDividers(13195))  # [5, 7, 13, 29]
print(simpleDividers(600851475143))  # [71, 839, 1471, 6857]
print(max(simpleDividers(600851475143)))  # 6857
print(simpleDividers(6857))  # [6857]
