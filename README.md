# Forecasting housing prices API
This project consists in dockerizing a Flask API that allows predicting prices by using a previously trained ML model.

## Model presentation
The file Price_pred.py includes the code of several DL or ML models. The dataset used is fetch_california_housing. There are 8 inputs and 1 output. For more info : https://inria.github.io/scikit-learn-mooc/python_scripts/datasets_california_housing.html. The model choosen is the model based on random forest. It is stored in a `.pkl` file and loaded by the API. There are some visualization techniques inside the code.

## API
### Endpoint
- **POST /predict** : It uses the method POST to send the inputs in JSON format and it retrieves the output in JSON format as well.

### Request example with Postman

- URL : `http://localhost:8000/predict` (to test in local on the port 8000)
- Method `POST`
- Body : 
``` JSON
{
    "features": [8.3252, 41.0, 6.984127, 1.023810, 322.0, 2.555556, 37.88, -122.23]
}
```
### Response example
``` JSON

{
    "prediction": [
        4.443321100000003
    ]
}
```
### Use curl
You can use curl to retrieve the output directly in the terminal through the following line :
```
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"features": [8.3252, 41.0, 6.984127, 1.023810, 322.0, 2.555556, 37.88, -122.23]}'
```
## Docker
The dockerfile created an image to install the dependencies required to execute the API. It uses the frameworks in the requirements.txt

### Build an image
```
docker build -t predict-price-api .
```
### Run the container
```
docker run -p 8000:8000 predict-price-api
```
### Test the API
The link to test on Postman in local is : http://localhost:8000/predict

## Deployment on AWS EC2
First, it is required to create an ec2 instance :
 - Image : Amazon Linux AMI
 - Type : t2.micro
 - Stockage : 8Go (Default)
 - Security Group : Inbound rules with SSH (port 22 from you IP or 0.0.0.0/0) to connect to the ec2 server from your computer and a Custom TCP (port 8000 with 0.0.0.0/0) to test the API
 - Create a security key `.pem` if you don't have

### SSH connection
```
ssh -i my_key.pem ec2-user@<ec2-public-ip-adress> on the terminal
```
### Install docker on the instance
```
sudo yum update -y
sudo yum install -y python3 python3-pip
sudo yum install -y docker
```
### Run docker
```
sudo systemctl start docker
sudo systemctl enable docker

sudo docker --version # Verification
```
### Clone git
```
git clone https://github.com/TheoBrln4/Predict_price_API.git
cd Predict_price_API
```
Then you can follow the section "Docker" and test the API with the link : http://<ec2-public-ip-adress>:8000/predict with Postman.

