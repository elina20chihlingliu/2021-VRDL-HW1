# 2021-VRDL-HW1

## ✓ ML Code Completeness Checklist

The ML Code Completeness Checklist consists of five items:

1. **Requirements**
2. **Files (images,txt and .py)** 
3. **Training code + Evaluation code** 
4. **Evaluation code + Load the models**
5. **Pre-trained models load links**
6. **README file including table of results accompanied by precise commands to run/produce those results**


#### 1. Requirements

'requirements.txt` contains all python 

#### 2. Files (images,txt and .py)

Please put the following files in the same directory.
1. [training_images]
2. [testing_images]
3. [models]
4. classes.txt
5. testing_img_order.txt
6. training_labels.txt
7. 310706002_main.py
8. 310706002_eval_loadmodels.py

#### 3. Training code + Evaluation code

**310706002_main.py** is full code containing data pre-process, training phase, testing phase and generate answer.txt.\
If you want to retrain models, just run 310706002_main.py (ex: python 310706002_main.py) and you can get answer.txt.\
It may take 1~2 hours to run 310706002_main.py.
    
#### 4. Evaluation code + Load the models 

**310706002_eval_loadmodels.py** only has testing phase to produce answer.txt. It has to load pretrained models in models file.\
In the models file, there are five models parameters that I pretrained and saved which I used to achieve baseline.\
If you want to evaluate test data without training model again, run 310706002_eval_loadmodels.py (ex: python 310706002_eval_loadmodels.py) and you can get answer.txt.\
It may take 1~2 hours to run 310706002_main.py.\\
[models]\
---[my_model0]\
---[my_model1]\
---[my_model2]\
---[my_model3]\
---[my_model4]
    


#### 5. Evaluation code + Load the models

#### 6. Pre-trained models load links




