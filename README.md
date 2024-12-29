## **Tomato Leaf Disease Classification**

- Predicts the disease of a tomato leaf plant given an image of one of its tomato leaves
- Classes: Early Blight, Late Blight, Leaf Mold, Yellowleaf Curl Virus, Mosaic Virus, Healthy
- This model has an 89% accuracy

## Requirements

- Make sure [uv](https://github.com/astral-sh/uv) is installed

### Installation

- Run `uv sync`

### Running

- Run `uv run start`
- You can also check the streamlit app here: <project-url>

- Drag and drop the image file you want to classify onto the main directory
- Use the command above, replace image.filetype with the name of the image file and its filetype
- Class and confidence would then be outputted

- You could also use one of the test images
- They are numbered 1 through 6, with the order of 1: Early Blight, 2: Late Blight, 3: Leaf Mold, 4: Yellowleaf Curl Virus, 5: Mosaic Virus, 6: Healthy
- Copy and paste the following into your terminal with one of the numbers above

```shell script
python classify.py -i $IMG_NUMBER.jpg
```

## Todo

- fix pyproject.toml to install tensorflow
- get railway deployment with streamlit to function
