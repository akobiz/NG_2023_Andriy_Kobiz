lists = []
nunqLists = []

for each in range(255):
    lists.append(input(f"Enter {each} pack: "))
    nunqLists.append([list(set([elem for elem in lists[each] if lists[each].count(elem) > 1]))])

print(f"{lists}\n\n\n{nunqLists}")

