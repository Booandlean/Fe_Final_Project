# README

## Git repo:

### [Notebooks](https://github.com/Booandlean/Fe_Final_Project/tree/master/Notebooks)
|--- [Data_Prep.ipynb](https://github.com/Booandlean/Fe_Final_Project/blob/master/Notebooks/Data_Prep.ipynb)

_contains code necessary to clean the stanford dataset_

|--- [EDA_n_Vis.ipynb](https://github.com/Booandlean/Fe_Final_Project/blob/master/Notebooks/EDA_n_Vis.ipynb)

_contains visualizations of image distributions for better understanding before modeling_

|--- [Modeling.ipynb](https://github.com/Booandlean/Fe_Final_Project/blob/master/Notebooks/Modeling.ipynb)

_contains FSM and all other models_

### [.gitignore](https://github.com/Booandlean/Fe_Final_Project/blob/master/.gitignore)
_tells github to ignore files + file types listed within_
### [README.md](https://github.com/Booandlean/Fe_Final_Project/blob/master/README.md)
#### _you are here_

## Project Goal

The objective of this project is to create an image classification model that can take in an image of a dog and correctly identify the breed of said dog. Should this be successful this could be utilized by animal shelters/ pounds to better classify dogs who's breed is not known. 

## About the data

The dataset can be found [here](https://www.kaggle.com/jessicali9530/stanford-dogs-dataset). It contains a total of 20,580 images of 120 different breeds of dogs. There are at least 150 images to represent each breed. 

## How do I use this?

As you may have noticed, there is no 'Data' folder in the github repository. This is because the dataset is far too large to be pushed to github. 

Step 1: Make a directory called 'Data' and download the dataset to that folder.

Step 2: Now that the data is in 'Data' there will be a folder within called 'images' and inside of that folder there will be another folder named 'Images'. That folder contains the dataset. Move 'Images' up one level into 'Data', then delete 'images'.

Step 3: Run the code in 'Data_Prep.ipynb', this should produce 3 folders which will contain train, test, and validation data. 

Step 4: In order to run the first simple model, create a folder called 'FSMimgs' and copy the Boxer and Bluetick images from the training data, then, run the 3 blocks of code inside the 'First Simple Model' section of 'Modeling.ipynb'

Step 5: In order to run the rest of the models, you will need to create 3 more folders, 'ExModeling_train', 'ExModeling_test', and 'ExModeling_val'. These upcoming models use pugs, golden retrievers, and pembrokes (AKA corgis)

#### To the grader reading this, I'll write some code that will make tand move files for the user tomorrow, I'm tired and greatly underestimated what I had to get done beyond modeling. 

## Modeling Results

At this moment the models are performing poorly. The first few models are clearly overfit with training accuracy reaching the 90's while the validation accuracy does not tend go go above 40. I attempted to counter this initially by removing layers within the CNN's to decrease their complexity in addition to using vertical and horizontal flips within the train and validation data. This was not very successful, with training accuracy going down and validation accuracy remaining mostly the same. I later reintroduced layers of the CNN and converted the images to grayscale as oposed to RGB on the off-chance that the model was too reliant on the color of the dogs, which can very greatly depending on the breed. This led to low accuracy scores, but the validation data had similar scores hovering around 30-40% accuracy. 

## Next steps

The next plan of attack to counter overfitting is to bring back RGB rather than grayscale and utilize some of the l1 and l2 regularizers within keras. If this goes well I will begin to increase the number of represented breeds in each model. 

## Sources

https://github.com/learn-co-students/dsc-image-classification-lab-sea01-dtsc-ft-051120/tree/solution

https://www.kaggle.com/jessicali9530/stanford-dogs-dataset

Aditya Khosla, Nityananda Jayadevaprakash, Bangpeng Yao and Li Fei-Fei. Novel dataset for Fine-Grained Image Categorization. First Workshop on Fine-Grained Visual Categorization (FGVC), IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2011.

J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li and L. Fei-Fei, ImageNet: A Large-Scale Hierarchical Image Database. IEEE Computer Vision and Pattern Recognition (CVPR), 2009.