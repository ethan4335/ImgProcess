
import os
import shutil

# home = r'D:\work_source\CV_Project\datasets\to_haitu_img\20201218_selected'

path_file = r"D:\work_source\CV_Project\datasets\to_haitu_img\20201216_selected\20201216_takeout.txt"
img_output = r"D:\work_source\CV_Project\datasets\to_haitu_img\8_20201216_takeout"


if not os.path.exists(img_output):
    os.makedirs(img_output)

with open(path_file, 'r') as f1:
    list1 = f1.readlines()
for i in range(0, len(list1)):
    list1[i] = list1[i].rstrip('\n')

for path in list1:
    # path = os.path.join(home,path)
    shutil.copy(path, os.path.join(img_output, os.path.basename(path)))





