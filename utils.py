import os
import ast

def load_wildreceipt(dataset_folder):
    ikdataset={'images':[],'metadata':{}}
    files = [os.path.join(dataset_folder,"train.txt"), os.path.join(dataset_folder,"test.txt")]
    id= 1
    for file in files:
        with open(file,"r") as f:
            for line in f.readlines():
                record = {}
                data=ast.literal_eval(line)
                record["id"] = id
                record["filename"] = os.path.join(dataset_folder,data["file_name"])
                record["height"] = data["height"]
                record["width"] = data["width"]
                record["annotations"] = []
                for annot in data["annotations"]:
                    polygon_annot = {}
                    polygon_annot["category_id"] = annot['label']
                    polygon_annot["segmentation_poly"] = [annot["box"]]
                    polygon_annot["text"] = annot['text']
                    record["annotations"].append(polygon_annot)
                ikdataset['images'].append(record)
                id+=1
    class_list = os.path.join(dataset_folder,"class_list.txt")
    dict_file = os.path.join(dataset_folder,"dict.txt")
    with open(class_list,'r') as f:
        classes = {}
        for line in f.readlines():
            k,v = line.replace("\n","").split(' ')
            classes[int(k)]=v
    ikdataset['metadata']['category_names'] = classes
    ikdataset['metadata']['class_list'] = class_list
    ikdataset['metadata']['dict_file'] = dict_file
    # Classes to ignore during evaluation
    ikdataset['metadata']['eval_ignore'] = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 25]
    return ikdataset