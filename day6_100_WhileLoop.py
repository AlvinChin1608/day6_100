#Will be cover the While Loop, Functions and Karel
#Here is a simple example where a function was created by Python

print("Hello")
num_char = len("Hello")
print(num_char)

#But what if we want to create our own function? here's how
# We start by using def to define our function
# The thing that differentiate function() and variable is the ()

def my_function(): # define the function
  print("test hello") # it did not print, because we need to call the function
#Here is how we trigger the function
my_function()

"""
Function() to bundle a set of repeatative instruction, we don't have type again and again 
Just call the function when needed
"""
# note
"""
For 
for item in list_items:
  #Do something to each list

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

for number in range(a,b):
  print(number)

While Loop

while something_is_true: #condition 
  #Do something repeatedly
  #only when something became false, loop stop

i = 1
while i < 6:
  print(i)
  i += 1

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
"""
#Hurdle 1
"""
def over_wall():
  move()
  turn_left()
  move()
  turn_left()
  turn_left()
  turn_left()
  move()
  turn_left()
  turn_left()
  turn_left()
  move()
  move()
  turn_left()
  
# Repeat the process exactly 5 times
for _ in range(5):
  over_wall()

"""
#Hurdle 2
"""
def over_wall():
  move()
  turn_left()
  move()
  turn_left()
  turn_left()
  turn_left()
  move()
  turn_left()
  turn_left()
  turn_left()
  move()
  turn_left()
# Initialize a counter variable
count = 0

# Repeat the process until count reaches 5
while count < 6 and not at_goal():
  over_wall()
  count += 1
"""
#Note - when best use based on scenario
"""
For Loop: Use a for loop when you know the number of iterations beforehand, such as iterating over a sequence (like a list or a range of numbers). It's particularly useful when you want to iterate a specific number of times.

While Loop: Use a while loop when you want to repeat a block of code as long as a condition is true. It's useful when the number of iterations is not known beforehand, or when you want to repeat until a certain condition is met.

But if you condition is always true, then your while loop will become infinite loop. 

"""
#Hurdle 3
"""
def turn_right():
  turn_left()
  turn_left()
  turn_left()

def jump():
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()

while not at_goal():
  if wall_in_front():
      jump()
  else:
      move()
"""
# Hurdle 4
"""
def turn_right():
  turn_left()
  turn_left()
  turn_left()

def jump():
  turn_left()
  while wall_on_right():
      move()
  turn_right()
  move()
  while front_is_clear():
      move()
  turn_left()

while not at_goal():
  if wall_in_front():
      jump()
  else:
      move()
"""

#Maze problem 1 - Fixed
"""
def turn_right():
  for i in range(3):
      turn_left()

count = 0

while not at_goal():
  if right_is_clear():
      turn_right()
      move()
      count += 1
      if count > 3: #added a track counter to performed additional step it would not stuck in infinite loop
          move()
          count = 0  # Reset the counter after moving
  elif front_is_clear():
      move()
  else:
      turn_left()
"""

