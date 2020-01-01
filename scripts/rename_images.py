import os

# Rename each image in the passed foleder to its id starting from zero
for directory_name in os.listdir("/home/malek/ml/project/unlabeled_data/data/unnamed_images"):
    count = 0
    for image in os.listdir("/home/malek/ml/project/unlabeled_data/data/unnamed_images/{0}".format(directory_name)):
        
        os.rename(os.path.join("/home/malek/ml/project/unlabeled_data/data/unnamed_images", directory_name, image), "./renamed_images/" + "_new_"+ directory_name + "-" +  str(count) + ".jpg")
        count += 1
