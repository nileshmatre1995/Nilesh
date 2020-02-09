def calcuate_min_cost(number_of_villagers, cost):
    total_cost = 0
    cost.sort()
    for i in range(0, number_of_villagers - 1):
        if cost is not None:
            total_cost += max(cost)
            if i < (number_of_villagers - 2):
                total_cost += min(cost)
            cost = cost[:-1]
    return total_cost

t = input()
n = int(input())
a = input().split(' ')
A=[]
for i in a:
    A.append(int(i))
print(calcuate_min_cost (n,A))