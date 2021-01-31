import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def animateTSP(history, points):
    '''
    Animate the solution over time
    
    Parameters
    ----------
    history : list
        history of the solutions chosen by the algorithm
    points: array_like
        points with the coordinates
    '''
    
    # Approx 1500 frames for animation
    key_frames_mult = len(history) // 1500
    
    fig, ax = plt.subplots()
    
    # Path is a line coming through all the nodes
    line, = plt.plot([], [], lw=2)
    
    def init():
        # Initialize node dots on graph
        x = [points[i][0], for i in history[0]]
        y = [points[i][1], for i in history[0]]
        plt.plot(x, y, 'co')
        
        # Draw axes slightly bigger
        extra_x = (max(x) - min(x)) * 0.05
        extra_y = (max(y) - min(y)) * 0.05
        ax.set_xlim(min(x) - extra_x, max(x) + extra_x)
        ax.set_ylim(min(y) - extra_y, max(y) + extra_y)
        
        return line,
        
    def update(frame):
        # For every frame update the solution on the graph
        x = [points[i, 0] for i in history[frame] + [history[frame][0]]]
        y = [points[i, 1] for i in history[frame] + [history[frame][0]]]
        line.set_data(x, y)
        return line
        
    # Animate precalculated solutions
    ani = FuncAnimation(fig, update, frames=range(0, len(history), key_frames_mult),
                        init_func=init, interval=3, repeat=False)
                        
    plt.show()