print('welcome to James Heaton ATM')
restart = ('Y')
changes = 3
balance = 100.145

while changes >= 0:
  pin = int(input('Please enter your pin:'))
  if pin == (1234):
    print('YOU ENTERED THE CORRECT PIN\n')
    while restart is not ('N','n','No','no'):
      print('1 for balance\n')
      print('2 for withdrawal\n')
      print('3 to pay in\n')
      print('4 return card\n')
      option = int(input('please select: '))
      if option == 1:
        print('your balance is',balance,'\n')
        restart = input('would you like to go back?')
        if restart in ('N','n','No','no'):
          print('thank you')
          break
      elif option == 2:
          option2 = ('y')
          withdrawal = float(input('how much would you like to withdrawal? \n £10,£20,£40,£60,£80,£100'))
          if withdrawal in [10,20,40,60,80,100]:
            balance = balance - withdrawal
            print('your balance is now £',balance)
            restart = input('would you like to go back?')
            if restart in ('N','n','No','no'):
              print ('thank you')
              break
          elif withdrawal != [10,20,40,60,80,100]:
            print('invalid amount, please retry \n')
            restart = ('y')
          elif withdrawal ==1:
            withdrawal = float(input('please enter amount'))

      elif
