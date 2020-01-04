import os
import random
import sys
import shutil

if __name__ == "__main__":
    data_path =    sys.argv[1]  
    train_ratio =  int(sys.argv[2])
    val_ratio   =  int(sys.argv[3])  
    test_ratio  =  int(sys.argv[4])

    # Create the train, test, val direcotries
    os.mkdir("./train")
    os.mkdir("./test")
    os.mkdir("./val")

    # create a text file contain links to all the data in the data_path
    items = open("items.txt", "a")

    
    # Loop over each image in each image direcotry (building_low, builidng_high, etc) and write the path of the image and its label
    # To a file
    for image_category in os.listdir(data_path):
        for image in os.listdir(os.path.join(data_path, image_category)):
            items.write(os.path.join(data_path, image_category, image))
            items.write("\t")
            items.write(image_category)
            items.write("\n")

    items.close()	
    items = open("items.txt", "r")
    # Read the links of all the imags
    items.seek(0)
    total_data_size = len(items.readlines())

    # Create the splitings
    train_data_size =       int((train_ratio * total_data_size) / 100)
    test_data_size =        int((test_ratio * total_data_size) / 100)
    validation_data_size =  int((val_ratio * total_data_size) / 100)

    train_start = 0
    train_end   = train_data_size

    test_start  = train_end
    test_end    = test_start + test_data_size

    val_start = test_end
    val_end   = total_data_size

    print("Training   data size:", train_data_size)
    print("Testing    data size: ", test_data_size)
    print("Validation data size: ", validation_data_size)


    indcies = {
        "train" : [train_start, train_end],
        "val"   : [val_start, val_end],
        "test"  : [test_start, test_end]
    }


    # Suffle the data
    items.seek(0)
    lines =  items.readlines()
    random.shuffle(lines)

    for data_type in indcies.keys():
        dirs = set()

        data_type_start = indcies[data_type][0]
        data_type_end =   indcies[data_type][1]

        item_counter = 0

        for line in lines[data_type_start: data_type_end]:
            label = line.split("\t")[1]
            if label not in dirs:
                os.mkdir(os.path.join("./", data_type, label))
                dirs.add(label)
                shutil.copy(line.split("\t")[0], os.path.join("./", data_type, label))
            else:
                shutil.copy(line.split("\t")[0], os.path.join("./", data_type, label))


    items.close()
