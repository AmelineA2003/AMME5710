
# Import libraries and packages 
import cv2
import numpy as np 
from matplotlib import pyplot as plt
import pickle
import os

def get_images(img_dir_path):
    images = []
    for i in range(64):
     images.append(cv2.imread(os.path.join(img_dir_path,'image_%03d.png'%(i))))

    return images 

def get_light_directions(light_dirs_path): 
   # Load lighting direction vectors
    light_dirs = pickle.load( open( light_dirs_path, "rb" ) )
    return light_dirs


def display_images():
   # Have a look at some data
    print('lighting direction vectors shape:',light_dirs.shape)
    plt.imshow(imgs[0]) # look at the first face image
    plt.show()



"""
plot_face_3d: produces textured 3D mesh of face data

height_map: [192x168] numpy array of heights
albedo: [192x168] numpy array of albedos (between 0-1)

Note: x-axis displayed in figure is flipped for better viewing
"""
def plot_face_3d(height_map, albedo):

    h, w = albedo.shape[:2]

    X, Y = np.meshgrid(np.arange(w, 0, -1), np.arange(0, h))
    fc = np.empty([h, w, 3])
    fc[:,:,0] = albedo
    fc[:,:,1] = albedo
    fc[:,:,2] = albedo

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surf = ax.plot_surface(X, Y, height_map, facecolors=fc, rstride=1, cstride=1)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.axis('equal')

    plt.show()



