# Dog-Breed-Classifier

## Objectives
- Correctly identify which pet images are of dogs (even if the breed is misclassified) and which pet images aren't of dogs.  
- Correctly classify the breed of dog, for the images that are of dogs.  
- Determine which CNN model architecture (ResNet, AlexNet, or VGG), "best" achieve objectives 1 and 2.  
- Consider the time resources required to best achieve objectives 1 and 2 for each model.
## Usage
Run `sh run_models_batch.sh` on git bash terminal to classify the images inside pet_images directory using Resnet, AlexNet and VGG. 
The classification results are stored in resnet_pet-images.txt, alexnet_pet-images.txt and vgg_pet-images.txt files for each model respectively.

Run `sh run_models_batch_uploaded.sh` if you want to classify your own uploaded images in uploaded_images directory. Similar to before, the results are stored in txt files of {model}_uploaded-images.txt.

The main script file is `check_images.py` which calls functions defined in other scripts in directory. 

## Results
The true labels are extracted from the filename of images in uploaded_images directory. The classifier models give the classifier labels. The dognames.txt is used to check if true label and classifier label
is a dog or not. The results are stored in `results` dictionary. The results dictionary is used to evaluate the model.  
```py
results = {filename: [true_label, classifier label, true_label_dog?, classifier_label_dog?], ...}
```
The model evaluation results are stored in `results_stats` dictionary. Both of them can be accessed through `check_images.py`

After running batch file, the txt files will show how models classified images as dog and not-a-dog along with breed which are objectives 1 and 2. But how much correct was classification?
Using `results_stats`, accuracy and missclassification in breed and dog/not-a-dog is found and mentioned at the end of txt files. The result summary for three models is given as:

|# Total Images|40|
|:----|:----|
|# Dog Images|30|
|# Not-a-Dog Images|10|

|CNN Model Architecture:|% Not-a-Dog Correct|% Dogs Correct|% Breeds Correct|% Match Labels|
|:----|:----|:----|:----|:----|
|ResNet|90.0%|100.0%|90.0%|82.5%|
|AlexNet|100.0%|100.0%|80.0%|75.0%|
|VGG|100.0%|100.0%|93.3%|87.5%|

- For objective 1, notice that both VGG and AlexNet correctly identify images of "dogs" and "not-a-dog" 100% of the time.
- For objective 2, VGG provides the best solution because it classifies the correct breed of dog over 90% of the time

Given our results, the "**best**" model architecture is **VGG** - Objective 3. It outperformed both of the other architectures when considering both objectives 1 and 2. You will notice that ResNet did classify dog breeds better than AlexNet,
but only VGG and AlexNet were able to classify "dogs" and "not-a-dog" at 100% accuracy. The model VGG was the one that was able to classify "dogs" and "not-a-dog" with 100% accuracy and had the best performance regarding breed classification with 93.3% accuracy.

For objective 4, the runtime for these model architectures, as given in txt files, are:

| Model Architecture | Runtime (in seconds) |
|--------------------|---------------------|
| ResNet             | 8                   |
| AlexNet            | 2                   |
| VGG                | 19                  |

which shows that higher the accuracy, higher will be time resources required.

Now, keeping in consider the accuracy of models, these models can be used to classify the uploaded images. For example, if you upload a dog image of unknown breed then there is 93.3% probability that VGG will classify the
breed correctly.
