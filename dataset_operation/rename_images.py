import os
import csv
import math
import shutil
from tqdm import tqdm

'''
用于将一个文件夹中的样本按照顺序重新命名， 并按照数量重新分配子文件夹

'''


def write_csv(file_path, info):
    row = info
    out = open(file_path, "a+")
    csv_writer = csv.writer(out, dialect="excel")
    csv_writer.writerow(row)
    out.close()


def mk_dir(path):
    if os.path.exists(path):
        return
    else:
        os.mkdir(path)


dataset_path = r"//AI_LAB_501/Dataset/cofm_mixure/"
original_present_name_relation_csv = r"//AI_LAB_501/Dataset/cofm_mixure/original_present_name_val.csv"

with open(original_present_name_relation_csv, 'a+') as file:
    writer = csv.writer(file)
    file.close()

file_number_per_folder = 5000

def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]

def get_imname(path):
    return [f for f in os.listdir(path) if f.endswith('.jpg')]

for train_val_set in ['val2021']:
    subset_path = dataset_path + train_val_set + '/'
    # file_list = os.listdir(subset_path)
    # file_list.sort()
    img_count = 0
    start_number = img_count
    file_list = get_imname(subset_path)
    file_list.sort()

    for i in tqdm(range(img_count, img_count + len(file_list))):

        original_img_path = subset_path + file_list[i-start_number]
        image_name = str(i).zfill(6) + '.jpg'
        target_img_path = subset_path + image_name

        print(original_img_path, 'will be renamed as', target_img_path)
        img_count = img_count + 1
        os.rename(original_img_path, target_img_path)
        write_csv(original_present_name_relation_csv, [file_list[i-start_number], image_name])

        folder_number = math.ceil(img_count / file_number_per_folder)

        folder_name = str(folder_number).zfill(2)
        folder_path = subset_path + folder_name
        mk_dir(folder_path)
        print(target_img_path, 'will be moved to ', folder_path)
        shutil.move(target_img_path, folder_path)

