import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
from numpy import typing as npt

def animate(data:npt.NDArray, interval: int = 50, **plot_args):
    """Make a nice widget for animations."""
    fig, ax = plt.subplots()
    ax.imshow(data[0], vmin=plot_args.pop('vmin', np.percentile(data, 1)), vmax=plot_args.pop('vmax', np.percentile(data, 99)))
    ax.set(xlabel=plot_args.pop('xlabel', ''),
           ylabel=plot_args.pop('ylabel', ''))
    title = plot_args.pop('title', '')
    def animate(frame):
        ax.images[0].set_data(data[frame])
        ax.set_title(f"{title}\nFrame {frame}")
        return ax.images

    plt.close(ax.figure)  # prevent figure from showing up in interactive mode

    # `blit=True` means only re-draw the parts that have changed.
    frames = len(data) 
    anim = FuncAnimation(
        ax.figure,
        animate,
        frames=frames,
        interval=interval,
        blit=True,
    )
    return HTML(anim.to_jshtml())