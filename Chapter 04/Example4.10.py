set1 = {11,21,33,44,53}
set2 = set([35,44,56,67,75])
union = set1|set2
print(union)
intersection = set1&set2
print(intersection)
difference = set1-set2
print(difference)
set1.add(68)
print(set1)
set2.remove(35)
print(set2)
