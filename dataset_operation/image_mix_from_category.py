import os
import shutil
from tqdm import tqdm
import random

"""
train2021和val2021文件夹下分类好的各个种类的样本，混合到train2021或val2021下，集合成一个不分种类的大数据集。
"""


def mk_dir(path):
    if os.path.exists(path):
        return
    else:
        os.mkdir(path)


dataset_path = r"//AI_LAB_501/Dataset/cofm/"

data_mix_path = r"//AI_LAB_501/Dataset/cofm_mixure/"

for train_val_set in ['train2021', 'val2021']:

    source_path = dataset_path + train_val_set + '/'
    target_save_path = data_mix_path + train_val_set + '/'
    folder_list = os.listdir(source_path)
    mk_dir(target_save_path)

    for class_name in folder_list:
        class_path = source_path + class_name + r'/'
        file_list = os.listdir(class_path)

        for img in tqdm(file_list):
            img_path = class_path + img

            print('moving', img_path, 'to', target_save_path)
            shutil.copy(img_path, target_save_path)
        print(class_name, 'moved to ', target_save_path)
