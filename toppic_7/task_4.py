list_nums = ['9', '42', '19', '35', '10', '70', '32', '12', '98', '37', '91', '25', '28']
for i in list_nums:
    i = int(i)
    if i % 5 == 0 or i % 7 == 0:
        print(i)
