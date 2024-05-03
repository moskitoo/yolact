import json
import os

def filter_annotations(json_data):
    filtered_annotations = []
    person_images = set()
    
    for annotation in json_data["annotations"]:
        if annotation["category_id"] == 1:
            filtered_annotations.append(annotation)
            person_images.add(annotation["image_id"])
    
    json_data["annotations"] = filtered_annotations
    
    filtered_images = [image for image in json_data["images"] if image["id"] in person_images]
    json_data["images"] = filtered_images
    
    return json_data

def process_json_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".json") and filename.startswith("instances"):
            print(filename)
            input_file = os.path.join(directory, filename)
            output_file = os.path.join(directory, f"filtered_{filename}")
            
            with open(input_file, "r") as file:
                json_data = json.load(file)
                filtered_data = filter_annotations(json_data)
            
            with open(output_file, "w") as file:
                json.dump(filtered_data, file, indent=4)

# Replace 'directory' with the path to the directory containing your JSON files
process_json_files("/home/xavier/cleaner_ws/src/yolact/data/coco/annotations")
