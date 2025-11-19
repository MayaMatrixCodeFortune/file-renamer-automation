import os

folder = "files/"

for index, filename in enumerate(os.listdir(folder)):
    new_name = f"file_{index}.txt"
    os.rename(folder + filename, folder + new_name)

print("Renaming complete!")
