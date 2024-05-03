import json

def count_annotations(json_file):
    annotation_counts = {}
    
    with open(json_file, "r") as file:
        data = json.load(file)
        annotations = data.get("annotations", [])
        categories = {category["id"]: category["name"] for category in data.get("categories", [])}
        
        for annotation in annotations:
            category_id = annotation.get("category_id")
            if category_id is not None:
                category_name = categories.get(category_id)
                if category_name:
                    annotation_counts[category_name] = annotation_counts.get(category_name, 0) + 1
    
    return annotation_counts

# Replace 'example.json' with the path to your JSON file
# json_file = '/home/xavier/cleaner_ws/src/yolact/data/coco/annotations/filtered_instances_train2017.json'
json_file = '/home/xavier/cleaner_ws/src/yolact/data/coco/annotations/instances_train2017.json'
counts = count_annotations(json_file)

total_count = 0

print("Annotation counts by class:")
for class_name, count in counts.items():
    total_count += count
    print(f"{class_name}: {count}")

print(f"all instances: {total_count}")
