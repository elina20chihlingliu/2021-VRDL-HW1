# 2021-VRDL-HW1

## ✓ ML Code Completeness Checklist

We compiled this checklist by looking at what's common to the most popular ML research repositories. In addition, we prioritized items that facilitate reproducibility and make it easier for others build upon research code.

The ML Code Completeness Checklist consists of five items:

1. **Specification of dependencies**
2. **Training code** 
3. **Evaluation code**
4. **Pre-trained models**
5. **README file including table of results accompanied by precise commands to run/produce those results**

We verified that repositories that check more items on the checklist also tend to have a higher number of GitHub stars. This was verified by analysing official NeurIPS 2019 repositories - more details in the [blog post](https://medium.com/paperswithcode/ml-code-completeness-checklist-e9127b168501). We also provide the [data](notebooks/code_checklist-neurips2019.csv) and [notebook](notebooks/code_checklist-analysis.pdf) to reproduce this analysis from the post. 

NeurIPS 2019 repositories that had all five of these components had the highest number of GitHub stars (median of 196 and mean of 2,664 stars). 

We explain each item on the checklist in detail blow. 

#### 1. Specification of dependencies

If you are using Python, this means providing a `requirements.txt` file (if using `pip` and `virtualenv`), providing `environment.yml` file (if using anaconda), or a `setup.py` if your code is a library. 

It is good practice to provide a section in your README.md that explains how to install these dependencies. Assume minimal background knowledge and be clear and comprehensive - if users cannot set up your dependencies they are likely to give up on the rest of your code as well. 

If you wish to provide whole reproducible environments, you might want to consider using Docker and upload a Docker image of your environment into Dockerhub. 

#### 2. Training code

Your code should have a training script that can be used to obtain the principal results stated in the paper. This means you should include hyperparameters and any tricks that were used in the process of getting your results. To maximize usefulness, ideally this code should be written with extensibility in mind: what if your user wants to use the same training script on their own dataset?

You can provide a documented command line wrapper such as `train.py` to serve as a useful entry point for your users. 
