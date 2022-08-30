num = [2,5,9,1]
num [2] = 36
num.append(9)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
  num.remove(5)
else:
    print('não Achei o numero 4')

print(num)
print(f'Essa lista tem {len(num)} elementos')