import turtle

# Настройка окна
turtle.setup(800, 600)
turtle.speed(0)
turtle.bgcolor('white')

# Тело танка
turtle.color('green')
turtle.begin_fill()
turtle.forward(200)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(50)
turtle.end_fill()

# Башня танка
turtle.penup()
turtle.goto(100, 50)
turtle.pendown()
turtle.color('brown')
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# Опция для сохранения рисунка
ts = turtle.getscreen()
ts.getcanvas().postscript(file="tank.eps")

turtle.done()
