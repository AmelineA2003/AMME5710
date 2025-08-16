import Q1

def main():
    
    # Path to images and light direction data 
    img_dir_path = 'yale_face_data/image_dir_B01'
    light_dirs_path = 'yale_face_data/light_dirB01.pkl'

    # Extract images and light direction data 
    images = Q1.get_images(img_dir_path)
    light_directions = Q1.get_light_directions(light_dirs_path)

    Q1.display_images()



if __name__ == "__main__":
    main()
