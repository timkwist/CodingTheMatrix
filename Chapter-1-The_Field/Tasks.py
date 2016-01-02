# Author: Tim Kwist

from plotting import plot
from image import file2image
from image import color2gray
from math import e
from math import pi
S = set({2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j})

# Task 1.4.1
# Assign to the variable S a list or set consisting of the complex numbers:
# S = {2 + 2i, 3 + 2i, 1.75 + 1i, 2 + 1i, 2.25 + 1i, 2.5 + 1i, 2.75 + 1i, 3 + 1i, 3.25 + 1i}
# We have provided a module plotting for showing points in the complex plane. The module
# defines a procedure plot. Import this class from the module as follows:
# >>> from pltting import plot
# Next plot the points in S as follows:
# >>>> plot(S, 4)
# Python should open a browser window displaying the points of S in the complex plane. The
# first argument to plot is a collection of complex numbers (or 2-tuples). The second argument
# sets the scale of the plot; in this case, the window can show complex numbers whose real and
# imaginary parts have the absolute value less than 4. The scale argument is optional and
# defaults to 1, and there is another optional argument that sets the size of the dots.
def task141():
	plot(S, 4)

# Task 1.4.3
# Create a new plot using a comprehension to provide a set of points derived from S by adding
# 1 + 2j to each:
# >>> plot({1+2j+z for z in S}, 4)
def task143():
	plot({1+2j+z for z in S}, 4)

# Task 1.4.7
# Create a new plot titled "My scaled points" using a comprehension as in Task 1.4.3.
# The points in the new plot should be halves of the points in S.
def task147():
	plot({0.5*z for z in S}, 4)

# Task 1.4.8
# Create a new plot in which the points of S are rotated by 90 degrees and scaled by 1/2.
# Use a comprehension in which the points of S are multiplied by a single complex numbers
def task148():
	plot({0.5j*z for z in S}, 4)

# Task 1.4.9
# Using a comprehension, create a new plot in which the points of S are rotated by 90 degrees,
# scaled by 1/2, and then shifted down by one unit and the the right two units. Use a
# comprehension in which the points of S are multiplied by one complex number and added to another.
def task149():
	plot({(0.5j*z) + (2+0j) for z in S}, 4)

# Task 1.4.10
# We have provided a module image with a procedure file2image(filename) that reads in an image
# stored in a file in the .png format. Import this procedure and invoke it, providing as argument
# the name of a file containing an image in this format, assigning the returned value to variable
# data. An example grayscale image, img01.png, is available for download.
# The value of data is a list of lists, and data[y][x] is the intensity of pixel (x,y). Pixel (0,0)
# is at the bottom left of the image, and pixel (width-1, height-1) is at the top right. The intensity
# of a pixel is a number between 0 (black) and 255 (white).
# Use a comprehension to assign to a list pts the set of complex numbers x + yi such that the image
# intensity of a pixel (x,y) is less than 120 and plot the list pts.
def task1410(filename):
	# Errata mentions to use color2gray to convert the 3-tuples that file2image gives into a single number
	data = color2gray(file2image(filename))
	# Original Pseudo-code
	# for y = 0; y < len(data); y++
	#	for x = 0; x < len(data[y]); x++
	#		if(data[y][x] < 120)
	#			pts.add(x + yj)
	# pts = {x + yj for {y,x} in data if data[y][x] < 120}
	# Fix this by subtracting the y we get from the height (length of data)
	pts = [x+(len(data)-y)*1j for y, datay in enumerate(data) for x, intensity in enumerate(datay) if data[y][x] < 120]
	plot(pts, 190)
	return pts # Not specified in task, but useful for later manipulation

# Task 1.4.17
# From the module math, import the definitions of e and pi. Let n be the integer 20. Let w be the complex number e^((2*pi*i)/n).
# Write a comprehension yielding the list consisting of w^0, w^1, w^2, ... , w^n-1. Plot these complex numbers
def task1714():
	n = 20
	w = e**((2*pi*1j)/n)
	listW = [w**x for x in range(n)]
	plot(listW, 1)
	# Neat circle!

# Task 1.4.19 Recall from Task 1.4.10 the list pts of points derived from an image. Plot the rotation by pi/4
# of the complex numbers comprimising pts.
def task1419(filename):
	pts = task1410(filename)
	pts = [x * e**((pi/4)*1j) for x in pts]
	plot(pts, 190)