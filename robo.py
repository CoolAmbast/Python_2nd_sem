'''
a robot move in a plain start from the origin point(0,0),
the robot can move towards up,down,left and right with given steps.
take input from user and then find the distance from origin and direction of robot moving
'''


pos = [0,0]
while True:
  s = input('Enter the robot path ')
  if s == '!':
    break
  direction = s.split()[0]
  steps = int(s.split()[1])

  if direction == 'UP':
    pos[1] = pos[1] + steps
  elif direction == 'DOWN':
    pos[1] = pos[1] - steps
  elif direction == 'LEFT':
    pos[0] = pos[0] - steps
  elif direction == 'RIGHT':
    pos[0] = pos[0] + steps
  else:
    pass

print('new pos',pos)
print((pos[0]*2 + pos[1]*2)*0.5)