from re import L
import turtle
import random

WIDTH = 500
HEIGHT = 500
DELAY = 200
FOOD_SIZE = 20

offsets = {
    'up': (0,20),
    'down': (0,-20),
    'right': (20,0),
    'left': (-20,0),
}

def go_up():
    global snake_direction
    if snake_direction != 'down':
        snake_direction = 'up'

def go_down():
    global snake_direction
    if snake_direction != 'up':
        snake_direction = 'down'

def go_right():
    global snake_direction
    if snake_direction != 'left':
        snake_direction = 'right'

def go_left():
    global snake_direction
    if snake_direction != 'right':
        snake_direction = 'left'

def game_loop():
    #changed from move_snake

    stamper.clearstamps()

    new_head = snake[-1].copy()
    
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    #check collisions with itself or the walls
    if (new_head in snake or new_head[0] < -WIDTH/2 or 
        new_head[0] > WIDTH /2 or new_head[1] < -HEIGHT /2
        or new_head[1] > HEIGHT /2):
        #half the negative width is left hand wall, so on
        turtle.bye() #end program, can restart also
    
    else: # if no collision game plays normal

        snake.append(new_head)

        #check for food collision
        if not food_collision():
            snake.pop(0) #keeps snake same len unless it gets food

        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()
        
        screen.update()

        turtle.ontimer(game_loop, DELAY) 

#returns True and sets a new food position if we are within
#a specified distance from the food
def food_collision():
    global food_position
    if get_distance(snake[-1], food_position) < 20:
        food_position = get_food_pos() #make a new food spot
        food.goto(food_position)
        return True
    return False

#generates a point on the grid to put food
def get_food_pos():
    x = random.randint(-WIDTH /2 +FOOD_SIZE, WIDTH /2 -FOOD_SIZE)
    y = random.randint(-HEIGHT /2 +FOOD_SIZE, HEIGHT /2 -FOOD_SIZE)
    return (x,y) 

#function to get the snake to eat food,
#hard to get exact point when snake collides with food
#so we use the pathagorean theorem to determine when it is
#within a set number of pixels away (hypotenus)
def get_distance(pos1,pos2):
    x1,y1 = pos1
    x2,y2 = pos2
    distance = ((y2-y1) **2 + (x2-x1) **2) **0.5 #theorem
    #**0.5 is same as taking sq root
    return distance

screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.title('Snake!')
screen.bgcolor('silver')
screen.tracer(0) 

screen.listen()
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')
screen.onkey(go_right, 'Right')
screen.onkey(go_left, 'Left')

stamper = turtle.Turtle()
stamper.shape('circle')
stamper.color('navy')
stamper.penup() 

snake = [[0,0], [20,0], [40,0], [60,0]]
snake_direction = 'up'

for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

#food dots
food = turtle.Turtle()
food.shape('turtle')
food.color('forest green')
food.shapesize(FOOD_SIZE / 20) #/20 generally to get pixel control
food.penup() #to not leave a trail when it moves
food_position = get_food_pos()
#this variable is used as a global in the food collision fxn
food.goto(food_position)

game_loop()

turtle.done()