

"""
Course:  Training YOLO v3 for Objects Detection with Custom Data

Section-3
Labelling new Dataset in YOLO format
File: creating-files-data-and-name.py
"""


# Creating files labelled_data.data and classes.names
# for training in Darknet framework
#
# Algorithm:
# Setting up full paths --> Reading file classes.txt -->
# --> Creating file classes.names -->
# --> Creating file labelled_data.data
#
# Result:
# Files classes.names and labelled_data.data needed to train
# in Darknet framework


"""
Start of:
Setting up full path to directory with labelled images
"""

# Full or absolute path to the folder with images
# Find it with Py file getting-full-path.py
# Pay attention! If you're using Windows, yours path might looks like:
# r'C:\Users\my_name\Downloads\video-to-annotate'
# or:
# 'C:\\Users\\my_name\\Downloads\\video-to-annotate'
full_path_to_images = '/home/zerosec/Downloads/Model_Files/yolov3/dataset/images'
full_path_to_directory = '/home/zerosec/Downloads/Model_Files/yolov3'

"""
End of:
Setting up full path to directory with labelled images
"""


"""
Start of:
Creating file classes.names
"""

# Defining counter for classes
c = 0

# Creating file classes.names from existing one classes.txt
# Pay attention! If you're using Windows, it might need to change
# this: + '/' +
# to this: + '\' +
# or to this: + '\\' +
with open(full_path_to_directory + '/' + 'classes.names', 'w') as names, \
     open(full_path_to_images + '/' + 'classes.txt', 'r') as txt:

    # Going through all lines in txt file and writing them into names file
    for line in txt:
        names.write(line)  # Copying all info from file txt to names

        # Increasing counter
        c += 1

"""
End of:
Creating file classes.names
"""

