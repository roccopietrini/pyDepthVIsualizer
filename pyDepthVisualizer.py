import tkinter as tk
import os
import argparse
from MainWindow import MainWindow


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the images")
args = vars(ap.parse_args())

image_path = args["image"]

root = tk.Tk()
root.title("PyDepthVisualizer")
MainWindow(root,image_path)
root.mainloop()
