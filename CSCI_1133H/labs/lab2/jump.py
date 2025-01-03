from turtle import *
draw_finish_line = Turtle()
draw_finish_line.penup()
draw_finish_line.setpos(150,-20)
draw_finish_line.pendown()
draw_finish_line.left(90)
draw_finish_line.forward(60)

turtle1 = Turtle()
turtle2 = Turtle()

turtle1.setpos(0,0)
turtle2.setpos(0,20)

p1_jump1 = int(input("PLAYER 1 Enter your first jump: "))
turtle1.forward(p1_jump1)
p2_jump1 = int(input("PLAYER 2 Enter your first jump: "))
turtle2.forward(p2_jump1)

p1_jump2 = int(input("PLAYER 1 Enter your second jump: "))
turtle1.forward(p1_jump2)
p2_jump2 = int(input("PLAYER 2 Enter your second jump: "))
turtle2.forward(p2_jump2)


p1_jump3 = int(input("PLAYER 1 Enter your third jump: "))
turtle1.forward(p1_jump3)
p2_jump3 = int(input("PLAYER 2 Enter your third jump: "))
turtle2.forward(p2_jump3)

print("GAME OVER :(")


