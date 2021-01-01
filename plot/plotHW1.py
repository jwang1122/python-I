import matplotlib.pyplot as plt
n = 51

X = range(n)
Y = [(value) * 3 for value in X]
print("Values of X:")
print(*range(n))
print("Values of Y (thrice of X):")
print(Y)
# Plot lines and/or markers to the Axes.
plt.plot(X, Y)
# Set the x axis label of the current axis.
plt.xlabel("x - axis")
# Set the y axis label of the current axis.
plt.ylabel("y - axis")
# Set a title
plt.title("Draw a line.")
# Display the figure.
plt.show()