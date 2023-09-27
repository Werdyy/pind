import turtle


f = open("pindgsis.txt", "r")
sides = f.readline()
directions = f.readline()

print(sides, directions)


def draw_shape(directions):
    t = turtle.Turtle()
    t.begin_fill()
    t.fillcolor("black")
 
    x, y = 0, 0
    angle = 0

    for direction in directions:
               
        if direction == 'N':
                y += 100 
        elif direction == 'S':
                y -= 100  
        elif direction == 'E':
                x += 100  
        elif direction == 'W':
                x -= 100  

        t.goto(x, y)

    t.end_fill()
    turtle.done()

draw_shape(directions)

