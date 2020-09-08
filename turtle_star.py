from turtle import *

def star(num_vertices, step, side_length):
        for i in range(num_vertices):
                 backward(side_length)
                 left(step*360.0/num_vertices)


star(5, 2, 200)
