import sys
import os
from PIL import Image

# Grab the first and second argument

# Folder path
path_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new folder exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through images folder
for filename in os.listdir(path_folder):
    img = Image.open(f'{path_folder}{filename}')
    # replace filename to then save it with the new format
    clean_name = os.path.splitext(filename)[0]
    # save the img as png
    img.save(f'{output_folder}{clean_name}.png', 'png')

print('success')


