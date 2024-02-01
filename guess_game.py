import random  #random module
answer=random.randint(1,10)
while True:
  try:
    guess=int(input('enter a number:'))
    if  0<guess<11:
      if guess==answer:
        print('good')
        break
    else:
      print('enter a num')
  except ValueError:
    print('pls enter a num')