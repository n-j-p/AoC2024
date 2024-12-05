sample_input = ['47|53',
'97|13',
'97|61',
'97|47',
'75|29',
'61|13',
'75|53',
'29|13',
'97|29',
'53|29',
'61|53',
'97|53',
'61|29',
'47|13',
'75|47',
'97|75',
'47|61',
'75|61',
'47|29',
'75|13',
'53|13']

sample_input2 = ['75,47,61,53,29',
'97,61,53,29,13',
'75,29,13',
'75,97,47,61,53',
'61,13,29',
'97,13,75,29,47']

orders = []
for s in sample_input:
  st = '('+s.replace('|',',')+')'
  order = eval(st)
  orders += [order,]
print(orders)

def check_order(updatei, oo):
  for o in oo:
    try:
      diff = updatei.index(o[0]) - updatei.index(o[1])
    except ValueError:
      continue
    #print(' ',o,diff)
    if diff > 0:
      return 0
      
  assert len(updatei) % 2 == 1

  return updatei[len(updatei)//2]

c = 0
for update in sample_input2:
  upd = eval('[' + update + ']')
  print(upd)
  test = check_order(upd, orders)
  print(' ',test)
  c += test
print(c)

fpath = 'C:\\Users\\pot063\\Downloads\\day5_input.txt'
actual_inp = open(fpath).read().split('\n')

actual_orders = []
for line in actual_inp:
  if len(line) > 0:
    #print(line)
    st = '('+line.replace('|',',')+')'
    order = eval(st)
    actual_orders += [order,]

  else:
    break
print(actual_orders)

for i,line in enumerate(actual_inp):
  if len(line) > 0:
    pass
  else:
    break
print(i)

c = 0
for actual_update in actual_inp[(i+1):]:
  if len(actual_update) == 0:
    break
  print(actual_update)
  upd = eval('[' + actual_update + ']')
  print(upd)
  test = check_order(upd, actual_orders)
  print(' ',test)
  c += test

print(c)
  

