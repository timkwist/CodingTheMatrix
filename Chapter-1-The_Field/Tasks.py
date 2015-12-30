# Author: Tim Kwist

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
	from plotting import plot
	S = set({2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j})
	plot(S, 4)