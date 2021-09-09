import os
import shutil
from tqdm import tqdm
import random

"""
Delete the too much items in the target dir, item left number is defined below, this program will keep the first
image_left_count number of item, and delete the rest, with the order of number first, letter after.
"""


def mk_dir(path):
    if os.path.exists(path):
        return
    else:
        os.mkdir(path)


# class_name_list = ['tennis racket', 'fork', 'knife','bowl','bottle','table','chair', 'book','tennis racket']
class_name_list = ['cup']
image_left_count = 1500
# class_name_number_dict = {'door': 2300, 'monitor': 2000, 'cup': 3000, 'bowl': 2300, 'bottle': 3000,
#                           'chair': 3000, 'person': 10000, 'book': 1000, 'hat': 2000, 'tennis racket': 1500,
#                           }
class_name_number_dict = {'table': 3000}
# train_savepath = "/home/lab/Projects/multirectangle/dataset/cofm/train2021/"
# val_savepath = "/home/lab/Projects/multirectangle/dataset/cofm/val2021/"

train_savepath = r"//AI_LAB_501/Dataset/cofm/train2021/"
val_savepath = "/home/lab/Projects/multirectangle/dataset/cofm/val2021/"
for class_name in class_name_number_dict.keys():
    target_class_path = train_savepath + class_name + r'/'
    file_list = os.listdir(target_class_path)
    file_list.sort()
    mk_dir(target_class_path)

    target_item_number = random.sample(range(len(file_list)), len(file_list)-class_name_number_dict[class_name])
    # print(len(target_item_number))
    # print(file_list)
    for i in target_item_number:
        file_name = file_list[i]
        tar_path = target_class_path + r'/' + file_name
        print(tar_path)
        os.remove(tar_path)
    print(class_name, 'redundant delete complete', len(os.listdir(target_class_path)), 'remain')
