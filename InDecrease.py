lst = [] 
leng = int(input("lenght of sequence = ")) 
for l in range (leng): 
  numb = float(input("number: ")) 
  for i in lst: 
    if i < numb: 
      lst[lst.index(i)], numb = numb, i     
  lst.append(numb) 
print(f'decrease = {lst}') 
ch = leng //2 
leng = leng-1 
for j in range (ch):
  lst[j], lst[leng - j] = lst[leng - j], lst[j] 
print(f'increase = {lst}') 

