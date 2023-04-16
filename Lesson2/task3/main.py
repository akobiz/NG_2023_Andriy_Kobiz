from random import randint

lists = []
nunqLists = []

for each in range(255):
    lists.append([randint(0, 6) for _ in range(5)])
    nunqLists.append([list(set([elem for elem in lists[each] if lists[each].count(elem) > 1]))])

print(f"{lists}\n\n\n{nunqLists}")

