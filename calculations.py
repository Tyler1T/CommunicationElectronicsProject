import numpy as np
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import matplotlib

matplotlib.use("TkAgg")

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

frequency = np.double(5*10**9)
omega = np.double(frequency*2*math.pi)
mew = np.double(.05928)
tox = np.double(2.25*10**-9)
Eox = np.double(3.9*8.854*10**-12)
Cox = np.double(Eox/tox)
Vth = np.double(.3782)
Vgs = np.double(1)
Id = np.double(.003)

fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 1000, .1)
fig.add_subplot(111).plot(t,  .5 * mew * Cox * t * (Vgs - Vth)**2)
fig.ylabel("Id ()")
fig.xlabel("W/L")


# Define the window layout
layout = [
    [sg.Text("Plot test")],
    [sg.Canvas(key="-CANVAS-")],
    [sg.Button("Ok")],
]

# Create the form and show it without the plot
window = sg.Window(
    "Matplotlib Single Graph",
    layout,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
)

# Add the plot to the window
draw_figure(window["-CANVAS-"].TKCanvas, fig)

event, values = window.read()

window.close()
