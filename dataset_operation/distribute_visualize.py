import matplotlib.pyplot as plt
import os

dataset_path = '/home/lab/Projects/multirectangle/dataset/cofm/'
train_set_path = dataset_path + 'train2021/'
val_set_path = dataset_path + 'val2021/'
ignore_list = ['person','table',]

# train_class = os.listdir(train_set_path)
# val_class = os.listdir(train_set_path)
file_list = os.listdir(train_set_path)
file_list.sort()
for class_name in ignore_list:
    file_list.remove(class_name)

train_set_data = []
val_set_data = []
for class_name in file_list:
    if class_name in ['person', 'table']:
        continue
    for set in [train_set_path, val_set_path]:
        class_path = set + class_name + '/'
        i = 0 if set is train_set_path else 1
        if os.path.exists(class_path):
            if not i:
                train_set_data.append(len(os.listdir(class_path)))
            # total_num[i] += num[i]
            else:
                val_set_data.append(len(os.listdir(class_path)))
        else:
            continue

labels = file_list
# plt.bar(range(len(train_set_data)), train_set_data, tick_label=labels)
# plt.tick_params(axis='x', labelsize=8)
plt.figure(1)
plt.bar(range(len(train_set_data)), train_set_data, tick_label=labels)
plt.xticks(rotation=-45)
plt.title('cofm train set')
plt.show()

plt.figure(2)
plt.bar(range(len(val_set_data)), val_set_data, tick_label=labels)
plt.xticks(rotation=-45)
plt.title('cofm val set')
plt.show()
