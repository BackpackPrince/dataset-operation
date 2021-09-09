import os
import prettytable as pt
'''
Program to visualize the number of images of 
cofm dataset in each category and train or val set
and draw a excel from it. 
'''

dataset_path = '/home/lab/Projects/multirectangle/dataset/cofm/'
train_set_path = dataset_path + 'train2021/'
val_set_path = dataset_path + 'val2021/'

# train_class = os.listdir(train_set_path)
# val_class = os.listdir(train_set_path)
file_list = os.listdir(train_set_path)
file_list.sort()

table = pt.PrettyTable()
table.field_names = ['total  ' + str(len(file_list)), 'train','val']
num = [0,0]
total_num = [0,0]
for class_name in file_list:
    # print(class_name)
    for set in [train_set_path, val_set_path]:
        class_path = set + class_name + '/'
        i = 0 if set is train_set_path else 1
        if os.path.exists(class_path):
            num[i] = len(os.listdir(class_path))
            total_num[i] += num[i]
        else:
            num[i] = None
    table.add_row([class_name, num[0],num[1]])
table.add_row(['total', total_num[0],total_num[1]])
print(table)

