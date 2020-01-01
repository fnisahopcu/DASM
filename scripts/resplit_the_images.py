import math
import os
import shutil

image_classes = set()

images_dir = "/home/malek/ml/project/unlabeled_data/data/data"

for image in os.listdir(images_dir):
    image_type =  image.split("_")[1]
    print(image_type)
    
    # Just consider the new images
    if image_type != "new":
       continue
    
    image_category = image.split("-")[0]

  
    if image_category in image_classes:
        shutil.move(os.path.join("/home/malek/ml/project/unlabeled_data/data/data", image), os.path.join("./", image_category))
    else:
        image_classes.add(image_category)
        os.mkdir(image_category)        # Create a directory for the image depending on the image directory
        shutil.move(os.path.join("/home/malek/ml/project/unlabeled_data/data/data", image), os.path.join("./", image_category))

