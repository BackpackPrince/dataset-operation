from pycocotools.coco import COCO
import os
import shutil
from tqdm import tqdm
import cv2

'''
extract certain category from the coco train and val set to target cofm dataset.
'''

# If the dir is not exists,make it
def mkr(path):
    if os.path.exists(path):
        return
    else:
        os.mkdir(path)


def id2name(coco):
    classes = dict()
    for cls in coco.dataset['categories']:
        classes[cls['id']] = cls['name']
    return classes

def save_imgs(tar_path, dataset, filename):  # save the img into target dir

    print("tar_path:",tar_path + filename)

    img_path = dataDir + '/' + dataset + '/' + filename
    img = cv2.imread(img_path)
    if (img.shape[2] == 1):
        print(filename + " not a RGB image")
        return
    shutil.copy(img_path, tar_path)

if __name__ == '__main__':
    # the path you want to save your results for coco to voc
    savepath = "/home/lab/Projects/multirectangle/dataset/cofm_large_temporary/"
    # img_dir = savepath + 'images/'

    datasets_list = ['train2017', 'val2017']
    tar_datasets_list = ['train2021', 'val2021']


    classes_names = ['cup']
    # classes_names = ['apple','orange', 'banana','scissors','mouse','keyboard', 'tv', 'cup',
    #                  'spoon','fork','knife','bowl','bottle','table','chair','person','book','toothbrush','remote',
    #                  'tennis racket','hair drier']
    # classes_names = ['apple','orange', 'banana', 'mouse','keyboard','tv','spoon','fork','knife','bowl','bottle','remote',
    #                  'tennis racket', 'book','chair','table']

    dataDir = '/home/lab/Projects/multirectangle/dataset/coco/'
    count = 0
    # mkr(img_dir)
    # max_image_number = 2000

    for dataset in datasets_list:
        # ./COCO/annotations/instances_train2014.json
        annFile = '{}/annotations/instances_{}.json'.format(dataDir, dataset)
        tar_dataset = tar_datasets_list[count]
        count += 1
        # COCO API for initializing annotated data
        coco = COCO(annFile)
        '''
        COCO 对象创建完毕后会输出如下信息:
        loading annotations into memory...
        Done (t=0.81s)
        creating index...
        index created!
        至此, json 脚本解析完毕, 并且将图片和对应的标注数据关联起来.
        '''
        # show all classes in coco
        classes = id2name(coco)
        print(classes)
        # [1, 2, 3, 4, 6, 8]
        classes_ids = coco.getCatIds(catNms=classes_names)
        print(classes_ids)



        for cls in classes_names:
            # Get ID number of this class
            cls_id = coco.getCatIds(catNms=[cls])
            img_ids = coco.getImgIds(catIds=cls_id)
            print(cls, len(img_ids))

            category_path = savepath + tar_dataset + r'/' + cls + r'/'
            mkr(category_path)
            # imgIds=img_ids[0:10]
            for imgId in tqdm(img_ids):
                img = coco.loadImgs(imgId)[0]
                filename = img['file_name']
                # print("filename:",filename)
                # print("dataset:",dataset)
                save_imgs(category_path, dataset, filename)
