t = int(input())
for test in range(1,t+1):
    n,b = [int(val) for val in input().split(' ')]
    m = [int(s) for s in input().split(' ')]
    m.sort()
    bought_houses =[]
    for house in m:
        if house <= b:
            b = b-house
            bought_houses.append(house)
    print('Case #{} : {}'.format(test, len(bought_houses)))
