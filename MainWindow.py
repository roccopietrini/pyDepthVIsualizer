import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
import os
import numpy as np

class MainWindow():

    def __init__(self, main, image):

        self.cv_img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
        self.height, self.width = self.cv_img.shape
        self.canvas = tk.Canvas(main, width = self.width, height = self.height,  highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=3)
        self.labelDepth = tk.Label(main, text='depth (mm) = ', fg="red", font=("Helvetica", 15))
        self.labelDepth.grid(row=0, column=1, columnspan=1)
        self.labelCoord = tk.Label(main, text='', fg="blue", font=("Helvetica", 15))
        self.labelCoord.grid(row=2, column=1, columnspan=1)
        depth_scale_factor = 255.0 / (np.max(self.cv_img)-np.min(self.cv_img))
        depth_scale_beta_factor = -np.min(depth_scale_factor)*depth_scale_factor
        self.depth_uint8 = self.cv_img*depth_scale_factor+depth_scale_beta_factor
        self.depth_uint8[self.depth_uint8 > 255] = 255
        self.depth_uint8[self.depth_uint8 < 0] = 0
        self.depth_uint8 = self.depth_uint8.astype('uint8')
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.depth_uint8))
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor = tk.NW, image = self.photo)
        self.canvas.bind("<Motion>",self.onMouseOver)


    def onMouseOver(self, event):
        x, y = event.x, event.y
        self.labelDepth.config(text='depth (mm) = ' + str(self.cv_img[y][x]))
        self.labelCoord.config(text='(%s,%s)'%(str(x),str(y)))
