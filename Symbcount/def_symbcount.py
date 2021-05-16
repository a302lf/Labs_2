import string
str_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
str_eng = 'abcdefghijgklmnopqrstuvwxyz'

def count_eng (string, numb_eng):
  for i in string:
    if i.isupper():
      i = i.lower()
    if i in str_eng:
      if i in numb_eng:
        numb_eng[i]+=1
      else:
        numb_eng[i]=1
  return numb_eng


def count_rus (string, numb_rus): 
  for i in string:
    if i.isupper():
      i = i.lower()
    if i in str_rus:
      if i in numb_rus:
        numb_rus[i]+=1
      else:
        numb_rus[i]=1
  return numb_rus

def common(count_string):
  numb_rus = {}
  numb_eng = {}
  for i in range(count_string):
    string = input("Input your line:")
    count_rus(string, numb_rus)
    count_eng(string, numb_eng)
  return numb_rus, numb_eng

def out (dct_rus, dct_eng):
  print("Rus:")
  for i in dct_rus:
    if dct_rus[i] != 1:
      print(f'{i} = {dct_rus[i]}')
  print("Eng:")
  for i in dct_eng:
    if dct_eng[i] != 1:
      print(f'{i} = {dct_eng[i]}')


 



        
  



