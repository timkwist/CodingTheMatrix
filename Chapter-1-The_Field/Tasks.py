# Author: Tim Kwist

from plotting import plot
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