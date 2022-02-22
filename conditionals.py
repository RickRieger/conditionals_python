import random

# Conditionals
# 1.	Driving Age
# a.	Declare a variable and assign it the value of the legal driving age in the United States.
driving_age = 16
# b.	Declare a variable to store a user's age. Use the built-in Python input() function to retrieve the user’s age via user input.
age = input('Please provide your age represented by numbers only:  ')
if(age):
  try:
      age = int(age)
  except:
      print('Please provide numbers only.')

# c.	If the user’s age is greater than or equal to the legal driving age in the United States, then print to the console “You are legally able to drive.”
if age >= driving_age:
  print('You are legally able to drive.')
# d.	If the user’s age is less than the legal driving age in the United
else:
  print('You are not old enough to drive yet.')


# 2.	Random Number 
# a.	Declare a variable to store a random number between 0 and 10. You will need to do some research to determine how to generate a random number in Python.
random_num = random.randint(0, 10)
print(random_num)
# i.	A good search term to use: “random number Python”
# b.	If the number is between 0 and 2, print to the console “0 or 1 or 2”
if random_num >= 0 & random_num <= 2:
  print('0 or 1 or 2')
# c.	If the number is between 3 and 5, print to the console “3 or 4 or 5”
elif random_num >= 3 & random_num <= 5:
  print('3 or 4 or 5')
# d.	If the number is between 6 and 8, print to the console “6 or 7 or 8”
elif random_num >= 6 & random_num <= 8:
  print('6 or 7 or 8')
# e.	If the number is equal to 9 or 10, print to the console “9 or 10”
elif random_num == 9 & random_num == 10:
  print('9 or 10')



# 3.	NFL Teams
# a.	Declare a variable to store an NFL team name. Use the built-in Python input() function to retrieve a user’s inputted favorite NFL team.
nfl_team = input('Please provide your favorite NFL team:  ', )
# b.	Build out a conditional for “Bears”, in which if selected it will print to the console “Quarterback much?”
if nfl_team.upper() == 'BEARS':
  print('Quarterback much?')
# c.	Build out a conditional for “Vikings”, in which if selected it will print to the console “Loud noises!”
elif nfl_team.upper() == 'VIKINGS':
  print('Loud noises!')
# d.	Build out a conditional for “Lions”, in which if selected it will print to the console “LOL! They bad!” 
elif nfl_team.upper() == 'LIONS':
  print('LOL! They bad!')
# e.	Build out a conditional for “Packers” in which if selected it will print to the console “Best team in the world! Actually, the universe!” 
elif nfl_team.upper() == 'PACKERS':
  print('Best team in the world! Actually, the universe!')
# f.	Build out a “default” conditional to print to the console “Pick a different team” in the scenario where a user doesn’t input “Bears”, “Vikings”, “Lions”, or “Packers”.
else:
  print('Pick a different team')
