from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd

x = [3, 7.5, 10]
y = [3, 6, 9]

output_file("Line.html")
f = figure()
f.line(x, y)
#show(f)

df = pd.read_csv("data.csv")
x1 = df["x"]
y1 = df["y"]
f1 = figure()
f1.line(x1, y1)
show(f1)