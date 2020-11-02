sequences = [435,3456,456,7687,234,456,5,1,2,4,2,2,5]
ptr_next = map(lambda number: number*number, filter(lambda number: number > 4, sequences))
print(list(ptr_next))
map