import turtle

# создаем черепаху
t = turtle.Turtle()

# вывод надписи "Win!"
win = turtle.Turtle()
win.hideturtle()
win.color("yellow")

# задаем цвета
turtle.bgcolor("black")
t.color("white")
walls_color = "purple"

# задаем размеры объектов класса "walls"
wall_size = 20

# перемещение через портал
def return_to_start():
    t.goto(0,0)


# создаем класс "walls", "portal", "coin"
class Walls(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.penup()
        self.goto(x, y)
        self.shape("square")
        self.color(walls_color)
        self.shapesize(wall_size / 20, wall_size / 20)

class Portal(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.penup()
        self.goto(x, y)
        self.shape("square")
        self.color("red")
        self.shapesize(wall_size / 20, wall_size / 20)

class Coin(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.penup()
        self.goto(x, y)
        self.shape("circle")
        self.color("yellow")
        self.shapesize(wall_size / 20, wall_size / 20)

# создаем объекты класса "walls", "portal", "coin"
walls = []
walls.append(Walls(0, 100))
walls.append(Walls(-20, 100))
walls.append(Walls(-40, 100))
walls.append(Walls(-60, 100))
walls.append(Walls(-80, 100))
walls.append(Walls(-100, 100))
walls.append(Walls(-120, 100))
walls.append(Walls(-140, 100))
walls.append(Walls(-160, 100))
walls.append(Walls(-180, 100))
walls.append(Walls(-200, 100))
walls.append(Walls(-200, 80))
walls.append(Walls(-200, 60))
walls.append(Walls(-200, 40))
walls.append(Walls(-200, 20))
walls.append(Walls(-200, 0))
walls.append(Walls(-200, -20))
walls.append(Walls(-200, -40))
walls.append(Walls(-200, -60))
walls.append(Walls(-200, -80))
walls.append(Walls(-200, -100))
walls.append(Walls(-180, -100))
walls.append(Walls(-160, -100))
walls.append(Walls(-140, -100))
walls.append(Walls(-120, -100))
walls.append(Walls(-100, -100))
walls.append(Walls(-80, -100))
walls.append(Walls(-60, -100))
walls.append(Walls(-40, -100))
walls.append(Walls(-20, -100))
walls.append(Walls(0, -100))
walls.append(Walls(20, -100))
walls.append(Walls(40, -100))
walls.append(Walls(60, -100))
walls.append(Walls(80, -100))
walls.append(Walls(100, -100))
walls.append(Walls(120, -100))
walls.append(Walls(140, -100))
walls.append(Walls(160, -100))
walls.append(Walls(180, -100))
walls.append(Walls(200, -100))
walls.append(Walls(200, -80))
walls.append(Walls(200, -60))
walls.append(Walls(200, -40))
walls.append(Walls(200, -20))
walls.append(Walls(200, 0))
walls.append(Walls(200, 20))
walls.append(Walls(200, 40))
walls.append(Walls(200, 60))
walls.append(Walls(200, 80))
walls.append(Walls(200, 100))
walls.append(Walls(180, 100))
walls.append(Walls(160, 100))
walls.append(Walls(140, 100))
walls.append(Walls(120, 100))
walls.append(Walls(100, 100))
walls.append(Walls(80, 100))
walls.append(Walls(60, 100))
walls.append(Walls(40, 100))
walls.append(Walls(20, 100))
walls.append(Walls(-140, 80))
walls.append(Walls(-140, 30))
walls.append(Walls(-120, 30))
walls.append(Walls(-180, -30))
walls.append(Walls(-160, -30))
walls.append(Walls(-140, -30))
walls.append(Walls(-100, -30))
walls.append(Walls(-100, -50))
walls.append(Walls(-80, -30))
walls.append(Walls(-80, -10))
walls.append(Walls(-80, 10))
walls.append(Walls(-80, 60))
walls.append(Walls(-80, 80))
walls.append(Walls(-60, -10))
walls.append(Walls(-40, -10))
walls.append(Walls(-40, -60))
walls.append(Walls(-20, -60))
walls.append(Walls(0, -60))
walls.append(Walls(0, -40))
walls.append(Walls(0, 40))
walls.append(Walls(-20, 60))
walls.append(Walls(60, -60))
walls.append(Walls(60, -40))
walls.append(Walls(60, 60))
walls.append(Walls(60, 40))
walls.append(Walls(80, 40))
walls.append(Walls(120, 40))
walls.append(Walls(120, 20))
walls.append(Walls(120, 0))
walls.append(Walls(120, -20))
walls.append(Walls(180, 80))
walls.append(Walls(140, 40))
walls.append(Walls(120, -80))
walls.append(Walls(140, -80))


portals = []
portal.append(Portal(-100, -80))
portal.append(Portal(140, 20))

coins = []
coin_1 = Coin(-180,-80)
coins.append(coin_1)
# функции для перемещения черепахи
def move_up():
    if (t.heading() != 270) and (not check_collision(t.xcor(), t.ycor() + 20)):
        t.setheading(90)
        t.forward(20)

def move_down():
    if (t.heading() != 90) and (not check_collision(t.xcor(), t.ycor() - 20)):
        t.setheading(270)
        t.forward(20)

def move_left():
    if (t.heading() != 0) and (not check_collision(t.xcor() - 20, t.ycor())):
        t.setheading(180)
        t.forward(20)

def move_right():
    if (t.heading() != 180) and (not check_collision(t.xcor() + 20, t.ycor())):
        t.setheading(0)
        t.forward(20)

# функция для проверки столкновения с объектами класса "walls", "portal", "coin"    
def check_collision(x, y):
    for wall in walls:
        if (wall.distance(x, y) < wall_size):
            return True
    for portal in portals:
        if (portal.distance(x, y) < wall_size):
            return_to_start()
    for coin_1 in coins:
        if (coin_1.distance(x, y) < wall_size):
            coin_1.hideturtle()
            win.write("1/2", True, align="center")
            coin_2 = Coin(140,-20)
            win.penup()
            win.goto(0,-20)
            win.pendown()
            coins.append(coin_2)
            coins.remove(coin_1)
            break
    for coin_2 in coins:
        if (coin_2.distance(x, y) < wall_size):
            coin_2.hideturtle()
            win.write("WIN!", True, align="center")
            coins.remove(coin_2)
            break
        
# назначаем клавиши перемещения
turtle.listen()
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(return_to_start, "r")
# отображаем окно
turtle.mainloop()
