# Course:CS 2302 MW 1:30-2:50, Author:David Ayala
# Assignment:Lab #1, Instructor: Olac Fuentes
# Teaching Assistant: Maliheh Zargaran, Date of last Modification: 2/8/2019
# Purpose of program: will print(draw) using recursion to draw interesting figures.

import numpy as np
import matplotlib.pyplot as plt
import math

#figure one
#this method will attempt to draw multiple squares recusively
def draw_squares(axis,count,points,w):
     axis.plot(points[:, 0], points[:, 1], color='k')
     if count > 0:
         temp = points*w
         axis.plot(count[:,0],count[:,1],color='k')
         draw_squares(axis, count-1, temp+750, w)
         draw_squares(axis, count-1, temp-250, w)

#plt.close("all")
size = 1000

points = np.array([[0, 0], [0, size], [size, size], [size,0],[0,0]])
fig, axis = plt.subplots()
draw_squares(axis,3,points,.5)
axis.set_aspect(1.0)
axis.axis('on')
plt.show()
fig.savefig('square.png')

#figure two
def circle(center, radi):
    x_axis = center[0] + radi
    y_axis = center[1] + radi
    return x_axis, y_axis
#this method will attempt to draw multiple circles recusively
def draw_circles(axis, n, center, radius, w):
     if n > 0:
          x_axis, y_axis = circle(center, radius)
          axis.plot(x_axis+radius, y_axis, color='k')
          draw_circles(axis, n - 1, center, radius * w, w)


#plt.close("all")
fig, axis = plt.subplots()
draw_circles(axis, 50, [100, 0], 100, .9)
axis.set_aspect(1.0)
axis.axis('on')
plt.show()
fig.savefig('circle.png')

#figure three
#this method will attempt to draw multiple binary trees recusively
def draw_trees_and_mountians(axis,n,count,x_axis,y_axis):
    if count>0:
        axis.plot([n[1],n[1]-x_axis],[n[0],n[0]-y_axis], color='k')
        axis.plot([n[1],n[1]+x_axis],[n[0],n[0]-y_axis], color='k')
        if count>0:
            draw_trees_and_mountians(axis,[n[1]-x_axis,n[0]-y_axis],count-1,x_axis/2,y_axis*.6)
            draw_trees_and_mountians(axis,[n[1]+x_axis,n[0]-y_axis],count-1,x_axis/2,y_axis*.6)

#plt.close("all")
fig, axis = plt.subplots()
n = np.array([[0,0],[0,500],[500,500],[500,0],[0,0]])
draw_trees_and_mountians(axis,n,7,1000 ,1000)
axis.set_aspect(1.0)
axis.axis('on')
plt.show()
fig.savefig('tree.png')


#figure four
def circle(center, rad):
      n = int(4 * rad * math.pi)
      t = np.linspace(0, 6.3, n)
      x_axis = center[0] + rad * np.sin(t)
      y_axis = center[1] + rad * np.cos(t)
      return x_axis, y_axis

#this method will attempt to draw multiple squares recusively
def draw_circles2(axis, n, center, radius, w):
      x_axis, y_axis = circle(center, radius)
      axis.plot(x_axis, y_axis, color='k')
      if n > 0:
           x_axis, y_axis = circle(center, radius*1/4)
           axis.plot(x_axis, y_axis, color='k')
           draw_circles2(axis, n - 1, center, radius * 1/3, w*1/3)
           draw_circles2(axis, n - 1, center*5, radius * 1/3, w*1/3)

plt.close("all")
fig, axis = plt.subplots()
draw_circles(axis, 5, [100, 0], 100, 1)
axis.set_aspect(1.0)
axis.axis('on')
plt.show()
fig.savefig('circles.png')

