import matplotlib.pyplot as plt
import time
import random
import os

plt.show()
fig, axs = plt.subplots(2, 3)
fig.suptitle('Positional and Orientational Views')

# Set limits for each subplot
axs[0, 0].set_xlim(-1, 1)
axs[0, 0].set_ylim(-1, 1)
axs[0, 1].set_xlim(-1, 1)
axs[0, 1].set_ylim(-1, 1)
axs[0, 2].set_xlim(-1, 1)
axs[0, 2].set_ylim(-1, 1)

axs[1, 0].set_xlim(-0.1, 0.1)
axs[1, 0].set_ylim(-0.1, 0.1)
axs[1, 1].set_xlim(-0.5, 0.5)
axs[1, 1].set_ylim(-0.5, 0.5)
axs[1, 2].set_xlim(-0.01, 0.01)
axs[1, 2].set_ylim(-0.01, 0.01)

# Position Graphs
line1, = axs[0, 0].plot([], [], '.')
axs[0, 0].set_title("Position - Top View (x vs. y) (meters)")
line2, = axs[0, 1].plot([], [], '.')
axs[0, 1].set_title("Position - Side View (z vs. x) (meters)")
line3, = axs[0, 2].plot([], [], '.')
axs[0, 2].set_title("Position - Side View (z vs. y) (meters)")

# Orientation Graphs
line4, = axs[1, 0].plot([], [], '.')
axs[1, 0].set_title("Orientation - 1 (meters)")
line5, = axs[1, 1].plot([], [], '.')
axs[1, 1].set_title("Orientation - 2 (meters)")
line6, = axs[1, 2].plot([], [], '.')
axs[1, 2].set_title("Orientation - 3 (meters)")

fig.tight_layout()

def plot_data(positional_data, x_orientation, y_orientation, z_orientation):
    x_position, y_position, z_position = positional_data
    x_orientation_x, x_orientation_y, x_orientation_z = x_orientation
    y_orientation_x, y_orientation_y, y_orientation_z = y_orientation
    z_orientation_x, z_orientation_y, z_orientation_z = z_orientation

    # Update Positional Data
    line1.set_xdata(x_position)
    line1.set_ydata(y_position)
    line2.set_xdata(z_position)
    line2.set_ydata(x_position)
    line3.set_xdata(z_position)
    line3.set_ydata(y_position)

    # Update Orientational Data
    line4.set_xdata(x_orientation_x)
    line4.set_ydata(x_orientation_y)
    line5.set_xdata(y_orientation_x)
    line5.set_ydata(y_orientation_y)
    line6.set_xdata(z_orientation_x)
    line6.set_ydata(z_orientation_y)

    fig.suptitle('Positional and Orientational Views\n[Time: %s]' % time.asctime())

    plt.draw()
    plt.pause(1e-17)

if __name__ == '__main__':
    # Get data from tool_tip_*.txt file
    file_path_position = os.path.dirname(os.getcwd()) + '/build/tool_tip_position.txt'
    file_path_X_orientation = os.path.dirname(os.getcwd()) + '/build/tool_tip_X_orientation.txt'
    file_path_Y_orientation = os.path.dirname(os.getcwd()) + '/build/tool_tip_Y_orientation.txt'
    file_path_Z_orientation = os.path.dirname(os.getcwd()) + '/build/tool_tip_Z_orientation.txt'

    while True:
        # Positional data
        tool_tip_file = open(file_path_position, "r")

        # If position data present
        first_line = tool_tip_file.readline()
        if first_line != '':
            # Plot marker positional data
            tool_tip_position_x = float(first_line)
            tool_tip_position_y = float(tool_tip_file.readline())
            tool_tip_position_z = float(tool_tip_file.readline())
        else:
            tool_tip_position_x = 0
            tool_tip_position_y = 0
            tool_tip_position_z = 0
        tool_tip_file.close()

        # X orientation data
        tool_tip_file = open(file_path_X_orientation, "r")

        # If position data present
        first_line = tool_tip_file.readline()
        if first_line != '':
            # Plot marker positional data
            tool_tip_X_orientation_x = float(first_line)
            tool_tip_X_orientation_y = float(tool_tip_file.readline())
            tool_tip_X_orientation_z = float(tool_tip_file.readline())
        else:
            tool_tip_X_orientation_x = 0
            tool_tip_X_orientation_y = 0
            tool_tip_X_orientation_z = 0
        tool_tip_file.close()

        # Y orientation data
        tool_tip_file = open(file_path_Y_orientation, "r")

        # If position data present
        first_line = tool_tip_file.readline()
        if first_line != '':
            # Plot marker positional data
            tool_tip_Y_orientation_x = float(first_line)
            tool_tip_Y_orientation_y = float(tool_tip_file.readline())
            tool_tip_Y_orientation_z = float(tool_tip_file.readline())
        else:
            tool_tip_Y_orientation_x = 0
            tool_tip_Y_orientation_y = 0
            tool_tip_Y_orientation_z = 0
        tool_tip_file.close()

        # Z orientation data
        tool_tip_file = open(file_path_Z_orientation, "r")

        # If position data present
        first_line = tool_tip_file.readline()
        if first_line != '':
            # Get marker positional data
            tool_tip_Z_orientation_x = float(first_line)
            tool_tip_Z_orientation_y = float(tool_tip_file.readline())
            tool_tip_Z_orientation_z = float(tool_tip_file.readline())
        else:
            tool_tip_Z_orientation_x = 0
            tool_tip_Z_orientation_y = 0
            tool_tip_Z_orientation_z = 0
        tool_tip_file.close()

        plot_data((tool_tip_position_x, tool_tip_position_y, tool_tip_position_z),
                  (tool_tip_X_orientation_x, tool_tip_X_orientation_y, tool_tip_X_orientation_z),
                  (tool_tip_Y_orientation_x, tool_tip_Y_orientation_y, tool_tip_Y_orientation_z),
                  (tool_tip_Z_orientation_x, tool_tip_Z_orientation_y, tool_tip_Z_orientation_z))
