import os
import json
import requests
import random


#Read all the data links in the json files in the direcotry into single file named links.txt
jsons_path = "./jsons"
output_file = open("links.txt", "a")

for json_file in os.listdir(jsons_path):
    label = json_file.split(".")[0]
    input_file = open(os.path.join(jsons_path, json_file), "r")

    for line in input_file.readlines():
        item = json.loads(line)
        item_url = item["content"]
        
        try:
            item_label = item["annotation"]["labels"]

            if len(item_label) != 1:                       ## Skip the item if it has no label or more than one label
                continue
            else:
                output_file.write(item_url + "\t" + label + "\t" + item_label[0] + "\n")          # Print the label with bridges class
        
        except:
            continue
    input_file.close()

soutput_file.close()
