from turtle import Turtle, Screen
from random import random

timmy = Turtle()
timmy.shape("arrow")
timmy.color("white")
screen = Screen()
screen.bgcolor("orange")

for i in range(10):
    timmy.forward(5)
    timmy.pu()
    timmy.forward(5)
    timmy.pd()

screen.exitonclick()
