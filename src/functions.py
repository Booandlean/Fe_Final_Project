import shutil
import os
import numpy as np

data_path = os.path.join('..', 'Data')
images_path = os.path.join(data_path, 'Images')


test_path = os.path.join(data_path, 'test_images')
train_path = os.path.join(data_path, 'train_images')
val_path = os.path.join(data_path, 'val_images')

split_paths =  (test_path, train_path, val_path)

def clean_target_file_name(name):
    return ''.join(name.split('-')[1:])
#takes messy filenames such as 'n02085620-Chihuahua', and returns all text after '-'

def train_test_val_split(lst, train=.90, test=.09, val=.01):
    #lst is the list from directory made from the OG images folder
    train_size = int(train * len(lst))
    test_size = int(test * len(lst))
    val_size = int(val * len(lst))
    #determines distribution of images to train, test, and validation folders based on decimals given. 
    train_split = list(np.random.choice(lst, size=train_size, replace=False))
    #adds a number of random images to train list equal to specified distribution
    no_train = [x for x in lst if x not in train_split]
    #makes a list of each image not in the train list
    test_split = list(np.random.choice(no_train, size=test_size, replace=False))
    #adds a number of random images to test list equal to specified distribution
    val_split = [x for x in no_train if x not in test_split]
    #adds all leftover images not in test or train lists ti validation list
    return train_split, test_split, val_split

def move_files(destination, origin, file_names):
    os.mkdir(destination)
    #creates a directory if it doesn't exist already
    for file in file_names:
    #iterates through images in dog files
        file_path = os.path.join(origin, file)
        #creates a path from specified path to the OG image file
        destination_path = os.path.join(destination, file)
        #creates a path from the new dir to the OG image file
        shutil.copyfile(file_path, destination_path)
        #copies OG image file to the new dir 
        
def split_data(train=.90, test=.09, val=.01):
    
    create_folders()
    images_folders = os.listdir(images_path)
    images_folders = [folder for folder in images_folders if folder != '.DS_Store']

       
        
    for folder in images_folders:
        target_name = clean_target_file_name(folder)
        #each img goes through ^^^ to remove all before '-'
        target_path = os.path.join(images_path, folder)
        #makes a path from the images folder to the dog folder inside being worked on
        target_images = os.listdir(target_path)
        #makes a list of the names of the images from the 'target folder'
        train_split, test_split, val_split = train_test_val_split(target_images, train=train, test=test, val=val)
        #splits up the images from the OG image folder to a test, train, and val folder
        target_train_path = os.path.join(train_path, target_name)
        target_test_path = os.path.join(test_path, target_name)
        target_val_path = os.path.join(val_path, target_name)
        #makes paths to respective train, test, and validation folders
        move_files(target_train_path, target_path, train_split)
        move_files(target_test_path, target_path, test_split)
        move_files(target_val_path, target_path, val_split)
        #makes copies of images and sends them to appropirate folders

def create_folders():
    for path in split_paths:
        if os.path.isdir(path):
            shutil.rmtree(path)
    for path in split_paths:
        os.mkdir(path)
        
def model_prep(breed):
    
    test_breed = os.path.join(test_path, breed)
    train_breed = os.path.join(train_path, breed)
    val_breed = os.path.join(val_path, breed)
    
    Ex_test_breed = os.path.join(Ex_test_path, breed)
    Ex_train_breed = os.path.join(Ex_train_path, breed)
    Ex_val_breed = os.path.join(Ex_val_path, breed)
    
    shutil.copytree(test_breed, Ex_test_breed)
    shutil.copytree(train_breed, Ex_train_breed)
    shutil.copytree(val_breed, Ex_val_breed)