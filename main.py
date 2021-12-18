### HOW THE GAME WORKS ###
# 
## A commander can do 5 things
# 
# Order a group to contruct a fort
#
# Create a group
#
# Disband a group
#
# Order an assination
#
# Order a move of a group/person

class Person:
  def __init__(self, id, side, ic=False, start=(0, 0)):
    self.id = id
    self.x, self.y = start
    self.side = side
    self.is_commander = ic
    self.alive = True
    self.group = None
    self.current_objective = {'orders': [], 'bloodlust': [], 'heading': None}
  def __repr__(self):
    return f'{self.id}'
  def do_turn():
    pass


def init_battle(sides, army_size):
  locations = {'flags': [], 'forts': [], 'people': []}
  s = 100
  for side in sides:
    i = 0
    while i < army_size:
      p = Person(f'{side}-{i}', side, start=(s, 0))
      locations['people'].append(p)
      i += 1
    c = Person(f'{side}-commander', side, ic=True, start=(s, 10))
    locations['people'].append(c)
    locations['flags'].append({'captured': False, 'loc': (s, 0)})
    
    s *= -1
  return locations

f = init_battle(['red', 'blue'], 10)
print(f)
    
