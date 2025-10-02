from random import randint

print('=' * 36)
print('| Rock Paper Scissors Lizard Spock |')
print('=' * 36)

print('1) ✊ Rock')
print('2) ✋ Paper')
print('3) ✌️ Scissors')
print('4) 🦎 Lizard')
print('5) 🖖 Spock')

pick = int(input('Pick a number: '))
cpu = randint(1,5)

while True: 
  if pick == 1:
    print('You chose: ✊')
    break
  elif pick == 2:
    print('You chose: ✋')
    break
  elif pick == 3:
    print('You chose: ✌️')
    break
  elif pick == 4:
    print('You chose: 🦎')
    break
  elif pick == 5:
    print('You chose: 🖖')
    break
  else: 
    print('Invalid choice.')
    pick = int(input('Pick a number: '))

if cpu == 1:
  print('CPU chose: ✊')
elif cpu == 2:
  print('CPU chose: ✋')
elif cpu == 3:
  print('CPU chose: ✌️')
elif pick == 4:
  print('CPU chose: 🦎')
elif pick == 5:
  print('CPU chose: 🖖')

if pick == 3 and cpu == 2:
  print('The player won!')
elif pick == 2 and cpu == 1:
  print('The Player won!')
elif pick == 1 and cpu == 4:
  print('The Player won!')
elif pick == 4 and cpu == 5:
  print('The Player won!')
elif pick == 5 and cpu == 3:
  print('The Player won!')
elif pick == 3 and cpu == 4:
  print('The Player won!')
elif pick == 4 and cpu == 2:
  print('The Player won!')
elif pick == 2 and cpu == 5:
  print('The Player won!')
elif pick == 5 and cpu == 1:
  print('The Player won!')
elif pick == 1 and cpu == 3:
  print('The Player won!')
elif pick == cpu:
  print("It's a tie")
else:
  print('CPU won!')
