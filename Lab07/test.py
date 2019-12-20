# import os
# from pathlib import Path
#
# for currentpath, folders, files in os.walk('H:\DevelopAlgebra\FlightSchool\src\main'):
#     for file in files:
#         print(os.path.dirname(file))
#         print(os.path.join(currentpath, file))

import glob
import os

root_dir = "H:\DevelopAlgebra\FlightSchool\src\main\java\hr"

for root, subFolders, files in os.walk(root_dir):
    print("Root is: " + root)
    for folder in subFolders:
        print("Folder is: " + folder)
        for file in files:
            print(file)

# for filename in glob.iglob(root_dir + '**/**', recursive=True):
#     if os.path.isfile(filename):
#         with open(filename,'r') as file:
#             print(file.read())
