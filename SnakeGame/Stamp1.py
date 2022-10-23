from re import L
import turtle

#define constants
WIDTH = 500
HEIGHT = 500
#W and H are parameters of our game not the screen
DELAY = 100 #in ms between frame updates

#in order to move
offsets = {
    'up': (0,20),
    'down': (0,-20),
    'right': (20,0),
    'left': (-20,0),
}

def go_up():
    global snake_direction
    if snake_direction != 'down':
        #so that you can't go up from down
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

def move_snake():
    stamper.clearstamps() #rids existing snake thats being drawn

    # a copy of the last segment in the list
    #because we don't want to change the orig
    new_head = snake[-1].copy()
    
    #new_head[0] += 20 #increment x coord
    
    #incrementing x,y based on offsets set above
    #and the direction the snake is heading in (from fxns)
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]


    #add new head to snake body
    snake.append(new_head)

    #remove the last segment
    snake.pop(0)

    #Draw snake
    for segment in snake:
        stamper.goto(segment[0], segment[1]) #x,y coord
        #goes to coord, then stamps
        stamper.stamp()
    
    #need to render (refresh screen)
    screen.update()

    #repeat
    turtle.ontimer(move_snake, DELAY) #intervals of delay

#Create a drawing window
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.title('Snake!')
screen.bgcolor('grey')
screen.tracer(0) #disables auto animation

#event handlers
#here we tell the program to 'listen' for events,
#such as key presses by user to move the snake
screen.listen()
#functions to call when a key is hit
#functin to call, then key (note caps for arrow keys)
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')
screen.onkey(go_right, 'Right')
screen.onkey(go_left, 'Left')

#Creating the turtle
stamper = turtle.Turtle()
stamper.shape('circle')
stamper.color('navy')
stamper.penup() #doesnt trace as it moves

#Create snake as list of coords
snake = [[0,0], [20,0], [40,0], [60,0]]
snake_direction = 'up' #global variable from offsets,
#starts going up when program launches

#Draw snake 
for segment in snake:
    stamper.goto(segment[0], segment[1]) #x,y coord
    #goes to coord, then stamps
    stamper.stamp()

#initial call of fxn
move_snake()

#Finishing statement (required at the end of all turtle programs)
turtle.done()