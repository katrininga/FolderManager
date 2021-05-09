import yaml

folder_dict = {1 : "einn", 2 : "Tveir", 3 : "thrir", "nester" : {1 : "one", 2 : "two"}}

parent_folder = list(folder_dict)[-1]

subfolder1 = "I'm a sub"
subfolder2 = "I'm also a sub"

print(folder_dict["nester"][1])

if parent_folder == "nester":

print(parent_folder)