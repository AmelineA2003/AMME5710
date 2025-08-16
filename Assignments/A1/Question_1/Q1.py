
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


"""
find_height_map: returns [192x168] numpy array of heights

surface_normals: _________ numpy array of surface normal vectors
"""

def find_height_map(surface_normals, integration_method):
   
   sn_x = surface_normals[:,:,0]
   sn_y = surface_normals[:,:,1]
   sn_z = surface_normals[:,:,2]

   # Computing partial derivatives 
   delta_x = -sn_x/sn_z
   delta_y = -sn_y/sn_z

   # Initialise height_map
   height, width = sn_x.shape
   height_map = np.zeros((height, width)) 
   
   if integration_method == "row wise": 
      None

   elif integration_method == "column wise": 
    None

   elif integration_method == "average": 
    None
   
   

   return height_map
   None



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



