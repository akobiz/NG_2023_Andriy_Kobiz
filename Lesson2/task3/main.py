lst1, lst2, lst3 = input('First pack: '), input('Second pack: '), input('Third pack: ')

unqLst1 = set([each for each in lst1 if lst1.count(each) > 1])
unqLst2 = set([each for each in lst2 if lst2.count(each) > 1])
unqLst3 = set([each for each in lst3 if lst3.count(each) > 1])

print(f"Non-unique elements from each packs:\n{unqLst1}\n{unqLst2}\n{unqLst3}")