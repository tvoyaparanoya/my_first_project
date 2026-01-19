age = int(input('Введите возраст '))
if  age >= 18 and age <= 65:
  user_input = int(input('Введите рост '))
  if user_input < 170:
    print('В танкисты')
  elif user_input < 185:
    print('На флот')
  elif user_input < 200:
    print('В десантники')
  else:
    print('В другие войска')
else:
  print('Непризывной возраст')
print('Конец программы')