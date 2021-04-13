import turtle
import time
import random

# Width and Height of the canvas/screen
WIDTH, HEIGHT = 500, 500

# A list of colors for the turtle racers
COLORS = ["red", "green", "blue", "orange", "yellow", "black", "purple", "pink", "brown", "cyan"]

# A function that asks the User for the number of turtles to race
def get_number_of_racers():
  racers = 0

  while True:
    racers = input("Enter the number of racers (2 - 10): ")

    if racers.isdigit():
      racers = int(racers)
    else:
      print("Input is not numeric... Try again!")
      continue 

    if 2 <= racers <= 10:
      return racers
    else:
      print("Number not in range 2 - 10. Try again!")


# A function that creates the entered number of turtles and evenly places them on the canvas in their starting positions
def create_turtles(colors):
  turtles = []
  spacing_x = WIDTH // (len(colors) + 1)

  for i, color in enumerate(colors):
    racer = turtle.Turtle()
    racer.color(color) 
    racer.shape("turtle")
    racer.left(90)
    racer.penup()
    racer.setpos(-WIDTH//2 + (i + 1) * spacing_x, -HEIGHT//2 + 20)
    racer.pendown()
    turtles.append(turtle)

  return turtles


def init_turtle():
  # Declaration and setup of the canvas/screen
  screen = turtle.Screen()
  screen.setup(WIDTH, HEIGHT)
  screen.title("Ninja Turtle Racing!")

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
create_turtles(colors)