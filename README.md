# sms-spam-detection
## Overview
This project shows how to use a classification model to determine whether an SMS is spam or not (ham). This generates a web application written in Python (3.10) and built with the Flask framework. The classifier is built using Keras' sequential model and embedding layers, yielding an F1 score of **94%** and an accuracy of **98%**.

## Build the classifier model (optional)
1. Clone this github repo in your local machine `git clone https://github.com/TheLastMonolith/sms-spam-detection.git`
2. Move to the sms-spam-detection repositoty `cd sms-spam-detection`
3. Create new virtual python environment and activate it.  
   *using conda*: `conda create --name myenv python=3.10` then `conda activate myenv`
4. Install all necessary libraries using the requirements.txt file. `pip install -r requirements.txt`
5. Build and save the classifier model in the model folder `python keras_model.py`


## SMS Classification API
You can use this API to classify SMS messages as spam or ham (non-spam). It serves as a single point for rendering results on an HTML GUI.

### Base URL
The base URL for all API endpoints is `localhost.8080`

### Authentication
Authentication is not required for accessing the API.

## Endpoints

### Render Results on HTML GUI

This endpoint renders the classification result on an HTML GUI.

#### Request Parameters
No request parameters are required.

#### Request Example
1. Pull the image from the docker hub:  
```
docker pull jfiguracion94/sms-spam-app
```
2. Run the docker command below on your local machine:  
```
docker run -p 8080:8080 -d jfiguracion94/sms-spam-app
```
3. Open the application by going to `localhost.8080` in a browser.
4. Submit the SMS message through the text box form.
Example:
```
POST localhost:8080/predict OK
Content-Type: application/json

{
  "sms": "Get a free gift now! Call +871297"
}
```

#### Response
The response is an HTML page containing the classification result once you click the **predict** button  
Example:
```
POST localhost:8080/predict OK
Content-Type: application/json

{
  "prediction": "SPAM!"
}
```  

### Conclusion
This API provides am endpoint that allows for rendering results on an HTML GUI. By sending a POST request to the appropriate endpoint, you can obtain the classification result in the response.

### Author  
Joseph Figuracion  
  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/josephfiguracion/)
