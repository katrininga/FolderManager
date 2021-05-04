import yaml

folder_dict = dict()

folder_dict["blah"] = 1
folder_dict["blu"] = 2

folder_dict["slab"] = ""
folder_dict["flab"] = ""
folder_dict["ham"] = ""
last = list(folder_dict)[-1]

folder_dict[last] = 5

with open("Test.yaml", "w") as yaml_file:
    yaml.dump(folder_dict,yaml_file, default_flow_style=False)


print(folder_dict)