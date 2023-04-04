from random import randint

lists = []
nunqLists = []

for each in range(255):
    lists.append([])
    nunqLists.append([])

for each in range(len(lists)):
    lists[each] = [randint(0, 6) for _ in range(5)]
    nunqLists[each] = list(set([elem for elem in lists[each] if lists[each].count(elem) > 1]))

print(f"{lists}\n\n\n{nunqLists}")

