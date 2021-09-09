import os
import shutil
from tqdm import tqdm

'''
Copy the certain number of images from the 
openimages dataset to the target cofm dataset.
'''


def mk_dir(path):   # See if the target dir exists, if does not, create one.
    if os.path.exists(path):
        return
    else:
        os.mkdir(path)
# box  plate  cap  door
# class_name = 'hat'


class_list = ['hat', 'box', 'plate', 'door']
no_limit = True
count = 0

coco_train_path = "/home/lab/Projects/multirectangle/dataset/coco/train2017"
open_images_train_path = "/home/lab/Projects/multirectangle/dataset/openimage/train/"
savepath = "/home/lab/Projects/multirectangle/dataset/cofm_large_temporary/train2021/"

for class_name in class_list:
    class_path = open_images_train_path + class_name + r'/'
    target_class_path = savepath + class_name + r'/'
    file_list = os.listdir(class_path)
    file_list.sort()
    mk_dir(target_class_path)

    if no_limit:
        count = len(file_list)

    for i in range(count):

        file_name = file_list[i]
        if file_name == 'labels':
            continue
        img_path = class_path + r'/' + file_name
        tar_path = target_class_path + r'/' + file_name
        shutil.copy(img_path, tar_path)
        print(tar_path)


