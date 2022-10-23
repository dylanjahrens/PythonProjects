from re import L
import turtle
import random

WIDTH = 500
HEIGHT = 500
FOOD_SIZE = 20

offsets = {
    'up': (0,20),
    'down': (0,-20),
    'right': (20,0),
    'left': (-20,0),
}

#replaces 4 fxns with these next 2
def bind_direction_keys():
    screen.onkey(lambda: set_snake_dir('up'), 'Up')
    screen.onkey(lambda: set_snake_dir('down'), 'Down')
    screen.onkey(lambda: set_snake_dir('left'), 'Left')
    screen.onkey(lambda: set_snake_dir('right'), 'Right')

def set_snake_dir(direction): 
    global snake_direction
    #global because we might change its value
    if direction == 'up':
        if snake_direction != 'down':
            snake_direction = 'up'
    elif direction == 'down':
        if snake_direction != 'up':
            snake_direction = 'down'
    elif direction == 'right':
        if snake_direction != 'left':
            snake_direction = 'right'
    elif direction == 'left':
        if snake_direction != 'right':
            snake_direction = 'left'

def game_loop():

    stamper.clearstamps()

    new_head = snake[-1].copy()
    
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    if (new_head in snake or new_head[0] < -WIDTH/2 or 
        new_head[0] > WIDTH /2 or new_head[1] < -HEIGHT /2
        or new_head[1] > HEIGHT /2):
        #turtle.bye() 
        reset()
        #instead of ending program we call reset
    
    else: 

        snake.append(new_head)

        if not food_collision():
            snake.pop(0) 

        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()
        
        screen.title(f'Snake Game! Score: {score}')
        screen.update()

        turtle.ontimer(game_loop, delay) 

def food_collision():
    global food_position, score, delay
    #need to make score global becuase we aren't 
    #just reading it we are updating it too
    #bring it into the scope of the fxn
    if get_distance(snake[-1], food_position) < 20:
        score +=1
        food_position = get_food_pos() 
        food.goto(food_position)
        if delay >=60:
            delay -= 10
        return True
    return False

def get_food_pos():
    x = random.randint(-WIDTH /2 +FOOD_SIZE, WIDTH /2 -FOOD_SIZE)
    y = random.randint(-HEIGHT /2 +FOOD_SIZE, HEIGHT /2 -FOOD_SIZE)
    return (x,y)

def get_distance(pos1,pos2):
    x1,y1 = pos1
    x2,y2 = pos2
    distance = ((y2-y1) **2 + (x2-x1) **2) **0.5
    return distance

#to reset game after you lose, don't have to run prog again
def reset():
    global score, snake, snake_direction, food_position, delay
    #these were in program but moved to here and made global
    snake = [[0,0], [20,0], [40,0], [60,0]]
    snake_direction = 'up'
    score = 0
    delay = 200
    food_position = get_food_pos()
    food.goto(food_position)    
    game_loop()
    #now at the end of the program instead of calling
    #game loop we call reset fxn

screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.title('Snake!')
screen.bgcolor('silver')
screen.tracer(0) 

screen.listen()
bind_direction_keys()
#replaces old clunky repetative code

stamper = turtle.Turtle()
stamper.shape('circle')
stamper.color('navy')
stamper.penup() 

#for segment in snake:
    #stamper.goto(segment[0], segment[1])
    #stamper.stamp()

food = turtle.Turtle()
food.shape('turtle')
food.color('forest green')
food.shapesize(FOOD_SIZE / 20) 
food.penup() 

reset()

turtle.done()