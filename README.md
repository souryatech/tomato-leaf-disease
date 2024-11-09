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
source venv/bin/activate
pip install -r requirements.txt
```

Tensorflow supports Python versions: 3.9–3.12.

### Running the project

```shell script
python classify.py
```


- Drag and drop the image file you want to classify onto the main directory
- Copy the image file's name from the directory along with .(image's filetype)
- Go to https://github.com/souryatech/tomato-leaf-disease/blob/8f6e43e0c869cddc2abeed16c1c77cf1368162da/classify.py and replace the variable img with the text in quotes ('image.filetype' to '(name you copied).(image's filetype)')
- Then run the file and the class and confidence will then be outputted
