
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
   row, col = sn_x.shape
   height_map_row = np.zeros((row, col)) 
   height_map_col = np.zeros((row, col)) 
   height_map_avg = np.zeros((row, col)) 

   # ------ROW-WISE--------------------------------------------
   # Cumulative sum over first row 
   height_map_row[0,:] = np.cumsum(delta_x[0,:])

   # Summing down each column 
   for i in range(1, row): 
      height_map_row[i, :] = height_map_row[i-1, :] + delta_y[i, :]

   
   # ------COL-WISE--------------------------------------------
   # Cumulative sum down first column 
   height_map_col[:,0] = np.cumsum(delta_y[:,0])

   # Summing across each row
   for i in range(1, col): 
      height_map_col[:, i] = height_map_col[:, i-1] + delta_x[:, i]


   # ------AVERAGE---------------------------------------------
   height_map_avg = (height_map_row+height_map_col)/2
   

   if integration_method == "row wise":
      return height_map_row
   
   elif integration_method == "column wise": 
      return height_map_col
   
   elif integration_method == "average": 
      return height_map_avg

   return None



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
   #  ax.axis('equal')
    ax.axis('auto')

    plt.show()



