# Open the file and load the file
with open('justfile') as f:
    lines = f.readlines()

# there can only be one place in justfile called default which calls other recipes
default_recipe = [x for x in lines if "default" in x][-1]
steps = default_recipe.split("default: ")[-1].replace("-","_")
steps = steps.split(" ")

text_file = open("flow.dot", "w")
text_file.write("graph { \n")
for i in range(len(steps)-1):
    row = steps[i] + " -- " + steps[i+1] + " \n"
    n = text_file.write("\t" + row) 

text_file.write("}")
text_file.close()