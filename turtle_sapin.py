#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     10/12/2019
# Copyright:   (c) Administrateur 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
    from  turtle import *
#bgcolor('')

color("green")
begin_fill()
setup (500,700)
position()
backward(100)
goto(-75,60)
backward(130)

color("red")
begin_fill()
circle(-10)
end_fill()
color("green")

goto(-50,150)
backward(90)
color("red")
begin_fill()
circle(-10)
end_fill()
color("green")

goto(-25,230)
backward(60)

color("red")
begin_fill()
circle(-10)
end_fill()
color("green")


goto(0,310)

color("orange")
begin_fill()
goto(-17,320)
forward(34)
goto(-18,300)
goto(0,328)
goto(18,300)
end_fill()

color("green")
goto(0,310)

#register_shape("turtle.gif")
#addshape('turtle')
goto(85,230)

color("red")
begin_fill()
circle(-10)
end_fill()
color("green")

backward(60)
goto(125,150)

color("red")
begin_fill()
circle(-10)
end_fill()
color("green")

backward(90)
goto(200,60)

color("red")
begin_fill()
circle(-10)
end_fill()
color("green")

backward(130)
goto(100,0)
backward(100)
end_fill()



#forward(500)



exitonclick()