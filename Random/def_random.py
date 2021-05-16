import random

str_1 = '0123456789'
str_2 = '~+-/*!&$#?=@<>'
str_3 = 'abcdefghijklnopqrstuvwxyz'
str_4 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lst_all = [1, 2, 3, 4]

def gen_str (lst):
  lst_type = random.choice(lst)
  return lst_type


def gen_el (res_lst):
  if res_lst == 1:
    res_el = random.choice(str_1)
  elif res_lst == 2:
    res_el = random.choice(str_2)
  elif res_lst == 3:
    res_el = random.choice(str_3)
  else:
    res_el = random.choice(str_4)
  return res_el


def gen_more(sequence):
  str_number = gen_str(sequence)
  password = gen_el(str_number)
  return password


def gen_equal(sequence):
  str_number = gen_str(sequence)
  password = gen_el(str_number)
  if str_number in sequence:
    sequence.remove(str_number)
  return password


def form_pas(lenght):
  pas = ''
  lst_var = lst_all.copy()
  for i in range(lenght): 
      if (lenght-i) == len(lst_var):
        pas += gen_equal(lst_var) 
      else:
        pas += gen_more(lst_all)
  return pas
