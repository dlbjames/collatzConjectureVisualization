# This Program uses the Collatz conjecture
# and visualizes it in an animated graph.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animation

def main():
    graphIt(collatz(313))   # Many Step Numbers:
                            # 989345275647 
                            # 27 54 129 313 649
                            # 1161 2463 3711 6171 

                            # Wavey Numbers:
                            # 127 451 496 
                            # 447 671 703
                            

# Computes the values using the Collatz Conjecture
def collatz(n):
    listX = [n]
    if n < 1:
        return []
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n + 1) // 2
        listX.append(n)
    return listX

# Graphs the computed values using
# matplotlib and animates the points
# using FuncAnimation.
# x-values: Step number
# y-values: Value at a Step
def graphIt(aList):
    x = 0
    listY = []

    fig = plt.figure()
    graph, = plt.plot([], [], 'o') #(listY, aList, 'o')
    
    for y in aList:
        x += 1
        listY.append(x)
        plt.plot(x, y, marker = 'o', markersize = 3)

    def animate(i):
        graph.set_data(listY[:i+1], aList[:i+1])
        return graph
        
    plt.xlabel('Number of Steps')
    plt.ylabel('Value at Step')
    plt.title('Collatz Conjecture')
    ani = animation(fig, animate, frames = len(listY), interval = 50)
    ani.save("collatzConjecture2.gif", writer = 'pillow')
    plt.show()

main()