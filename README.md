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
python classify.py -i image.filetype
```


- Drag and drop the image file you want to classify onto the main directory
- Use the command above, replace image.filetype with the name of the image file and its filetype
- Class and confidence would then be outputted