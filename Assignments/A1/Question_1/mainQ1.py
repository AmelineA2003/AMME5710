import Q1
import pickle 
import matplotlib.pyplot as plt

def main():
    
    # Path to images and light direction data 
    img_dir_path = 'yale_face_data/image_dir_B01'
    light_dirs_path = 'yale_face_data/light_dirB01.pkl'

    # Extract images and light direction data 
    images = Q1.get_images(img_dir_path)
    light_directions = Q1.get_light_directions(light_dirs_path)

    B01_data_path = 'yale_face_data/B01_albedo_normals.pkl'
    data = pickle.load( open( B01_data_path, "rb" ) )
    albedo_image = data['albedo_image']
    surface_normals = data['surface_normals']

    integration_method = "row wise"
    height_map = Q1.find_height_map(surface_normals, integration_method)

    Q1.plot_face_3d(height_map, albedo_image)

    # Have a look at some data
    print('lighting direction vectors shape:',light_directions.shape)
    plt.imshow(images[0]) # look at the first face image
    plt.show()











if __name__ == "__main__":
    main()
