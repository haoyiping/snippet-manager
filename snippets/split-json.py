import os, sys, shutil
import json
import glob

def reverse_json(json_file, im_list, im_type="jpg"):
    temp = json_file.split("/")
    last = temp[-1]
    name = last.split("_")
    json_dir = name[0] + "_" + name[1].split(".")[0]
    out_json_dir = ""
    for i in range(len(temp)-1):
        out_json_dir += temp[i]
        out_json_dir += "/"
    out_json_dir += json_dir + "/"

    if not os.path.isdir(out_json_dir):
        os.mkdir(out_json_dir)

    all_data = json.load(open(json_file))
    print len(im_list), len(all_data['JSON_LANES'])

    all_lanes_data = all_data['JSON_LANES']
    for i in range(len(all_data['JSON_LANES'])):
        im_name = im_list[i]
        json_name = out_json_dir + im_name.split('.')[0] + ".json"
        fid_json = open(json_name, 'w')
        curr_data = all_lanes_data[i]
        lanes = curr_data["lanes"]
        json.dump(curr_data, fid_json, indent=4)
        fid_json.close()
