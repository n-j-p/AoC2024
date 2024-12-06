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


### Parse sample data

sample_orders = []
for s in sample_input:
  st = '('+s.replace('|',',')+')'
  order = eval(st)
  sample_orders += [order,]
#print(sample_orders)

sample_updates = []
for update in sample_input2:
  upd = eval('[' + update + ']')
  sample_updates.append(upd)
#print(sample_updates)

### Parse actual input

fpath = 'C:\\Users\\pot063\\Downloads\\day5_input.txt'
actual_inp = open(fpath).read().split('\n')
orders = []
for line in actual_inp:
  if len(line) > 0:
    st = '('+line.replace('|',',')+')'
    order = eval(st)
    orders += [order,]

  else:
    break
#print(orders)

updates = []
for i,line in enumerate(actual_inp):
  if len(line) > 0:
    pass
  else:
    break
for actual_update in actual_inp[(i+1):]:
  if len(actual_update) == 0:
    break
  upd = eval('[' + actual_update + ']')
  updates.append(upd)
#print(updates)

### Function for part 1
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


### Part 1
c = 0

for update in sample_updates:
  c += check_order(update, sample_orders)
assert c == 143

print("Part 1 test OK")

c = 0 
for update in updates:
  c += check_order(update, orders)
print(f'Part 1 answer is {c}')


### Part 2
### function
def reorder(updatei, oo):
  rupdatei = list(updatei)
  any_swapped = False
  for o in oo:
    try:
      diff = rupdatei.index(o[0]) - rupdatei.index(o[1])
    except ValueError:
      continue
    if diff > 0:
      any_swapped = True
      i = rupdatei.index(o[1])
      a = rupdatei.pop(i+diff)
      b = rupdatei.pop(i)
      rupdatei.insert(i, a)
      rupdatei.insert(i+diff, b)
  if any_swapped:
    return rupdatei

  else:
    return None

## Part 2 test
c = 0
for upd in sample_updates:
  upd0 = list(upd)
  check = check_order(upd, sample_orders)
  if check > 0:
    print(upd, 'already sorted')
    continue
  while check_order(upd,sample_orders) == 0:
    upd = reorder(upd, sample_orders)
  r = check_order(upd, sample_orders)
  print(upd0, upd, r)
  c += r

assert c == 123
print("Part 2 test OK")

c = 0
for upd in updates:
  upd0 = list(upd)
  check = check_order(upd, orders)
  if check > 0:
    print(upd, 'already sorted')
    continue
  while check_order(upd,orders) == 0:
    upd = reorder(upd, orders)
  r = check_order(upd, orders)
  print(upd0, upd, r)
  c += r

print(f'Part 2 answer is {c}')

