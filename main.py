#code goal
#make a program that has basic information of some plants like
#yearly growth, rainfall effects, sunlight, etc. 
#based on user input it will tell you how much your plant should grow

plants = ["Mango Plant", "Avocado Plant", "Tomato Plant", "Cucumber Plant"]
yn = input("Hello. Are you trying to find average growth for a plant of yours?  ")
#using a if else statement to see if they are here for the plants
if yn == "Yes" or yn == "yes" or yn == "yup" or yn == "Yup":
  print("Aright! The options are " + ', '.join(plants))
  choice = input("For which plant will you like to find it's estimated growth for the year? ")
else:
  print("Sorry this website cannot help you as of right now.")
#ask what plant they want to find out about




#mango plant choice
mpoints = []
if choice == "Mango Plant" or choice == "mango plant" or choice == "Mango plant":
  print("Alright, here is some basic information about the Mango Plant.")
#basic mango info
  print("The Mango Plant needs full exposure to the sun, aswell as moist and well drained soil. The reccomended hardiness zone to plant one is 9 through 11.")
#tell and ask user for data
  print("In order to find the estimated yearly growth for your plant, I require some data.")
mango = input("Will your mango plant have full sun exposure? ")
if mango == "Yes" or mango == "yes":
  print("Alright! That's good.")
  mpoints.append(2)
  
else:
  print("Not so great.")
  
mango1 = input("Will the soil be moist and well-drained at all times? ")
if mango1 == "Yes" or mango1 == "yes":
  print("Perfect.")
  mpoints.append(2)
else:
  print("That isn't going to work out well.")

mango2 = int(input("What hardiness zone do you live in?"                ))
if mango2 >= 9 and mango2 < 12:
  print("You are in the perfect hardiness zone!")
  mpoints.append(2)
else:
  print("That's a problem!")

#scoring system to figure out the answer 
total = sum(mpoints)
my_bool = 6 == total
if my_bool == True:
  print("Your plant is ready to grow at it's full potential at 6 feet.")
my_bool = 6
if my_bool > total and total > 2:
  print("Your plant is almost ready to grow at it's full potential but it needs improvement. Based on this it will possibly grow at 3 to 4 feet per year.")
my_bool = 6
if my_bool > total and total <= 2:
  print("You should try looking into different plant as it seems this plant won't work well with your region.")
#avocado plant choice
if choice == "Avocado Plant" or choice == "avocado plant" or choice == "Avocado plant":
  print("Alright, here is some basic information about the Avocado Plant.")
  print("The Avocado Plant needs full or partial exposure to the sun, the soil has to be sandy and well drained. The reccomended hardiness zone to plant one is 9 through 11.")
  
#tomato plant choice
if choice == "Tomato Plant" or choice == "tomato plant" or choice == "Tomato plant":
  print("Alright, here is some basic information on the Tomato Plant.")
  print("The Tomato plant needs full sun exposure and loamy well drained soil. It's reccomended hardiness zone to plant is 3 through 11.")

  
#cucumber plant choice
if choice == "Cucumber Plant" or choice == "cucumber plant" or choice == "Cucumber plant":
  print("Alright, here is some basic information on the Cucumber Plant.")
  print("The Cucumber Plant needs full sun to partial shade and rich, well drained soil. It's reccomended hardiness zone to plant in is 4 through 11.")
#i have to find a fix for the else statement printing regardless of choice
# else:
#   print("Please choose a plant from the list provided.")