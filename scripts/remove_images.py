import json
import numpy
import os

input_file = "./my_duplicates.json"
images_dir = "/home/malek/ml/project/unlabeled_data/data/data"

to_delete_images = json.load(open(input_file, "r"))

print(len(to_delete_images))

for image in os.listdir(images_dir):
    if image in to_delete_images:
        os.remove(os.path.join("/home/malek/ml/project/unlabeled_data/data/data", image))

