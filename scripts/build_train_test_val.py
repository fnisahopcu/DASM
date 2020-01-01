input_file = open("links.txt", "r")
total_data_size = len(input_file.readlines())

input_file.seek(0)

# Create the splitings
train_data_size =       int((65 * total_data_size) / 100)
test_data_size =        int((20 * total_data_size) / 100)
validation_data_size =  int((15 * total_data_size) / 100)

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



lines =  input_file.readlines()
random.shuffle(lines)

for data_type in indcies.keys():
    dirs = set()

    data_type_start = indcies[data_type][0]
    data_type_end =   indcies[data_type][1]

    item_counter = 0

    for line in lines[data_type_start: data_type_end]:
        item_url = line.split("\t")[0]
        item_category = line.split("\t")[1]
        item_label = line.split("\t")[2]

        label = item_category + "_" + item_label

        print(item_url)
        print(label)

        if label not in dirs:
            os.mkdir(os.path.join("./", data_type, label))
            dirs.add(label)

        try:
            response = requests.get(item_url, timeout = 10)
            if response.status_code == 200:
                file_path = os.path.join( "./", data_type, label ,  str(item_counter) + ".jpg")
                item_counter += 1
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                    print (file_path)
            else:
                raise ValueError( "Not a 200 response")
        except Exception as e:
            print("Failed to download image at " + item_url + " \n" + str(e) + "\nignoring....")
