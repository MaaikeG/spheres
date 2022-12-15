import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class AnimatedScatter(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""
    def __init__(self, generator, ax_limits):
        self.stream = generator()
        self.ax_limits = ax_limits

        # Setup the figure and axes...
        self.fig, self.ax = plt.subplots()
        # Then setup FuncAnimation.
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=5, 
                                          init_func=self.setup_plot, blit=True)

    def setup_plot(self):
        """Initial drawing of the scatter plot."""
        data = next(self.stream)
        x, y = data.qs.T

        self.scat = self.ax.scatter(x, y, s=data.radii, vmin=0, vmax=1,
                                    cmap="jet", edgecolor="k")
        self.ax.axis(self.ax_limits)
        # For FuncAnimation's sake, we need to return the artist we'll be using
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,

    def update(self, i):
        """Update the scatter plot."""
        data = next(self.stream)
        coords = data.qs
        
        # Set x and y data...
        self.scat.set_offsets(coords)
        # Set sizes...
        self.scat.set_sizes(300 * abs(data.radii)**1.5 + 100)
        # Set colors..
        self.scat.set_array(data.colors)

        # We need to return the updated artist for FuncAnimation to draw..
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,