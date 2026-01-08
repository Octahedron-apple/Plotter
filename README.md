# Plotter
A Python-based command-line tool that visualizes straight lines on a Cartesian plane. This script allows users to input parameters for different standard forms of linear equations and renders the resulting graph using matplotlib.
🚀 Features

  Interactive Menu: Simple CLI interface to select the type of equation.
  Multiple Geometric Forms:

        Slope-Intercept Form: Input slope (m) and y-intercept (c).

        Intercept Form: Input x-intercept (a) and y-intercept (b).

        Normal Form: Input perpendicular distance (p) and angle (ω).

  Visualization:
      Plots the line on a grid with x and y axes centered at (0,0).
      Dynamic title updates based on input parameters.

  Save Functionality: Option to save the generated plot as a .png file.

📋 Prerequisites

To run this script, you need Python installed along with the following libraries:

  matplotlib (for plotting)
  numpy (for calculating coordinate arrays)

🛠️ Installation & Setup

  Clone or Download the script to your local machine.

  Install Dependencies: Open your terminal or command prompt and run:
  ```
pip install matplotlib numpy

```
  to run the program
  ```
python3 main.py
```

Mathematical Forms Explained

1. Slope-Intercept Form Plots the line using the equation:
   y=mx+c

    m: The slope (gradient) of the line.

    c: The point where the line crosses the vertical y-axis.

2. Intercept Form Plots the line using the equation:
    ax​+by​=1

    a: The x-intercept (where the line crosses the x-axis).

    b: The y-intercept (where the line crosses the y-axis).

3. Normal Form Plots the line using the equation:
     xcosω+ysinω=p

    p: The length of the perpendicular (normal) from the origin to the line.

    Angle (ω): The angle (in degrees) that the normal makes with the positive x-axis.
