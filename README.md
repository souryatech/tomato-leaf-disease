## **Tomato Leaf Disease Classification**

- Predicts the disease of a tomato leaf plant given an image of one of its tomato leaves
- Classes: Early Blight, Late Blight, Leaf Mold, Yellowleaf Curl Virus, Mosaic Virus, Healthy
- This model has an 89% accuracy

### Installation

- Copy and paste the following into your terminal:

```shell script
git clone https://github.com/souryatech/tomato-leaf-disease.git
cd tomato-leaf-disease
python3.12 -m venv venv
```

If using git bash, unix shell, or mac os, copy and paste the following in your terminal:
```shell script
source venv/bin/activate
pip install -r requirements.txt
```
If using powershell, copy and paste the following in your terminal:
```shell script
venv/Scripts/activate.ps1
pip install -r requirements.txt
```

Tensorflow supports Python versions: 3.9–3.12.

### Running the project

```shell script
python classify.py -i test_images/image.filetype
```


- Drag and drop the image file you want to classify onto the main directory
- Use the command above, replace image.filetype with the name of the image file and its filetype
- Class and confidence would then be outputted

- You could also use one of the test images
- They are numbered 1 through 6, with the order of 1: Early Blight, 2: Late Blight, 3: Leaf Mold, 4: Yellowleaf Curl Virus, 5: Mosaic Virus, 6: Healthy
- Copy and paste the following into your terminal with one of the numbers above
```shell script
python classify.py -i $IMG_NUMBER.jpg
```
