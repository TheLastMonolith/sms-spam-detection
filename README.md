# sms-spam-detection 🔍
## Overview
This project shows how to use a classification model to determine whether an SMS is spam or not (ham). This generates a web application written in Python (3.10) and built with the Flask framework. The classifier is built using Keras' sequential model and embedding layers, yielding an F1 score of **94%** and an accuracy of **98%**.

## Build the classifier model (optional)
1. Clone this github repo in your local machine `git clone https://github.com/TheLastMonolith/sms-spam-detection.git`
2. Move to the sms-spam-detection repositoty `cd sms-spam-detection`
3. Create new virtual python environment and activate it.  
   *using conda*: `conda create --name myenv python=3.10` then `conda activate myenv`
4. Install all necessary libraries using the requirements.txt file. `pip install -r requirements.txt`
5. Build and save the classifier model in the model folder `python keras_model.py`


## Run the Spam Detection App
![](https://github.com/TheLastMonolith/sms-spam-detection/blob/main/assets/spam-app.gif)
1. Pull the [image](https://hub.docker.com/r/jfiguracion94/sms-api) from the docker hub:  
```
docker pull jfiguracion94/sms-api:1.0.0
```
> *Note*: use the tag `1.0.0` when calling the docker image, leaving it blank will call the tag `latest`, which could lead to error
2. Run the docker command below on your local machine:  
```
docker run -p 8080:8080 jfiguracion94/sms-api:1.0.0
```
> *Note*: you can add `-d` for detach mode, this will hide the terminal response
3. Open the application by going to `localhost.8080` in a browser.
4. Submit the SMS message through the text box form.
5. Once you click the predict button, it will show a text if it's a spam or ham.

## [API Documentation](https://thelastmonolith.github.io/sms-spam-api-doc/)

## Directory Tree
### Dataset
The [SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection) is a set of SMS tagged messages that have been collected for SMS Spam research. It contains one set of SMS messages in English of 5,574 messages, tagged acording being ham (legitimate) or spam. 
```bash
data
└── raw   
    ├── SMSSPamCollection
    └── readme
```

### Notebook
Contains the eda and model building result and evaluation.
```bash
notebook
└── eda_and_model_building.ipynb   
```

### Classifier Model
Contains python file to build the and save the classifier model.
```bash
.
├── models    
│   ├── keras_model-0.1.0          # keras model folder
│   └── keras_tokenizer-0.1.0.pkl  # pickled tokenizer 
└── src
    └── keras_model.py             # build and save classifier
```

### Flask and Docker
```bash
app
├── models    
│   ├── keras_model-0.1.0          # keras model folder
│   └── keras_tokenizer-0.1.0.pkl  # pickled tokenizer
├── static
│   └── css
│       └── main.css
├── templates
│   └── index.html
├── Dockerfile                     #  Docker configuration
├── app.py                         # flask app
├── model.py                       # classifier 
├── request.py                     # helper for direct api call
└── requirements.txt

```


### Author  
Joseph Figuracion  
  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/josephfiguracion/)
