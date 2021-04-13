import turtle

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


def init_turtle():
  # Width and Height of the canvas/screen
  WIDTH, HEIGHT = 500, 500

  # Declaration and setup of the canvas/screen
  screen = turtle.Screen()
  screen.setup(WIDTH, HEIGHT)
  screen.title("Ninja Turtle Racing!")

racers = get_number_of_racers()
init_turtle()