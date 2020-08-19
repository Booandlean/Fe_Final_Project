# README

## Git repo:

### [Notebooks](https://github.com/Booandlean/Fe_Final_Project/tree/master/Notebooks)
|--- [Data_Prep.ipynb](https://github.com/Booandlean/Fe_Final_Project/blob/master/Notebooks/Data_Prep.ipynb)

_contains code necessary to clean the stanford dataset_

|--- [EDA_n_Vis.ipynb](https://github.com/Booandlean/Fe_Final_Project/blob/master/Notebooks/EDA_n_Vis.ipynb)

_contains visualizations of image distributions for better understanding before modeling_

|--- [Modeling.ipynb](https://github.com/Booandlean/Fe_Final_Project/blob/master/Notebooks/Modeling.ipynb)

_contains FSM and all other models other than final notebook_

|--- [Modelig_2.ipynb](https://github.com/Booandlean/Fe_Final_Project/blob/master/Notebooks/Modeling_2.ipynb)

_contains final model and test data evaluation_

|--- [Final_Notebook](https://github.com/Booandlean/Fe_Final_Project/blob/master/Notebooks/Final_Notebook.ipynb)

_contains final notebook_

### [.gitignore](https://github.com/Booandlean/Fe_Final_Project/blob/master/.gitignore)
_tells github to ignore files + file types listed within_
### [README.md](https://github.com/Booandlean/Fe_Final_Project/blob/master/README.md)
#### _you are here_
### [Presentation_Slides](https://github.com/Booandlean/Fe_Final_Project/tree/master/Presentation_Slides)
_contains a .pdf copy of the presentation slides_
### [src](https://github.com/Booandlean/Fe_Final_Project/tree/master/src)
_contains a .py file of the methods used to set up the data for modeling_
### [Vis_Files](https://github.com/Booandlean/Fe_Final_Project/tree/master/Vis_Files)
_contains images of visualizations used in the presentation and within the notebooks_
### [dogs.yml](https://github.com/Booandlean/Fe_Final_Project/blob/master/dogs.yml)
_the enviorment file_
## Project Goal

The objective of this project is to create an image classification model that can take in an image of a dog and correctly identify the breed of said dog. Should this be successful this could be utilized by animal shelters/ pounds to better classify dogs who's breed is not known. 

## About the data

The dataset can be found [here](https://www.kaggle.com/jessicali9530/stanford-dogs-dataset). It contains a total of 20,580 images of 120 different breeds of dogs. There are at least 150 images to represent each breed. 

## How do I use this?

As you may have noticed, there is no 'Data' folder in the github repository. This is because the dataset is far too large to be pushed to github. 

Step 0: Before you use jupyer notebook to look at the .ipynb notebooks the environment needs to be set up. Open your terminal and navigate to the folder which contains dogs.yml. Run:

'conda env create -f dogs.yml' 

Then run: 

'conda activate dogs'

to activate the environment. If you do not have pykernel installed, run: 

'pip install --user ipykernel' 

in the terminal. Once this is done, run: 

'python -m ipykernel install --user --name=dogs' 

Upon opening jupyer notebook, go to the 'new' button with the down arrow. You should see 'dogs' under the 'notebook' tab. Once you click 'dogs' the environment will be set up, and you can now run the code within the notebooks. 

Step 1: Make a directory called 'Data' and download the dataset to that folder.

Step 2: Now that the data is in 'Data' there will be a folder within called 'images' and inside of that folder there will be another folder named 'Images'. That folder contains the dataset. Move 'Images' up one level into 'Data', then delete 'images'.

Step 3: Open 'Data_Prep.ipynb', it contains the methods which will be moving the data around for you from now on. 

Step 4: Run The imports cell, then run the 'Data Split' cell of your choice. If you are doing this for the very first time, run 'split_data(.9, .09, .01)' as it will be used for the first couple models.

Step 5: Run every cell in 'Pathways and Image Directories' to make the necessary file paths and folders.

Step 6: For the 'Methods' section, you only need to run 'model_prep()' at the bottom. All of the other methods are for 'split_data()' which was already imported from 'functions.py'. 

Step 7: The first cell you will see in 'Model Perperation' resets the folders used for modeling and only needs to be run if you are changing the split and/or breeds being used. It is noted in the 'Model Preperation' which breeds are used in which models as headers for the 'model_prep()' cells. 

You should now be ready to run models within the modeling notebooks. To make it easier, here's a list of which splits are used on which models:

#### 90 9 1: 
First Simple Model - model 2
#### 70 15 15:
model 3 - model d
#### 90 5 5:
All remaining models plus Final Model in the 'Modeling_2' notebook. 


## Modeling Results

The final and best performing model was model_1 from the 'Modeling_2' notebook with a train accuracy of .850 and a test accuracy of 0.854. Overfitting was a big problem early on in the modeling process so I am glad to see evidence of overcoming it. This certainly isn't enough to handle all 120 breeds, but it is a good start. 

## Future Improvments

- A limitation of this project was processing power. My models could only get so complex or else they would take too long to run and it was evident that the internal temperatures of my mac book were getting high while running them. 
- Once processing power is no longer a problem, the next step would be to run more advanced models over more epochs. Most models run in this project only had 10 or 15 epochs. 
- One improvment that could only make the project better would be to add more dog images beyond those provided by the Stanford dataset. Many dog breeds only had 150 images representing them, and more would have been prefered. 

## Presentation:
You can find a .pdf of the slides [here.](https://github.com/Booandlean/Fe_Final_Project/blob/master/Presentation_Slides/Dog_Breed_Identification.pdf)

## Sources

https://github.com/learn-co-students/dsc-image-classification-lab-sea01-dtsc-ft-051120/tree/solution

https://www.kaggle.com/jessicali9530/stanford-dogs-dataset

Aditya Khosla, Nityananda Jayadevaprakash, Bangpeng Yao and Li Fei-Fei. Novel dataset for Fine-Grained Image Categorization. First Workshop on Fine-Grained Visual Categorization (FGVC), IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2011.

J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li and L. Fei-Fei, ImageNet: A Large-Scale Hierarchical Image Database. IEEE Computer Vision and Pattern Recognition (CVPR), 2009.