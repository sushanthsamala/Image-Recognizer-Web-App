# Image-Recognizer-Web-App
This is a image recognizer web application that runs on Kubernetes with 4 replicas, you can upload your image to get a label and confidence.

## Steps to run
 ```
    git clone //https://github.com/sushanthsamala/Image-Recognizer-Web-App
    cd Image-Recognizer-Web-App
    docker build -t image-recognizer .
    kubectl apply -f deployment.yaml
 ```
 Navigate to http://0.0.0.0:5000 on your browser

## Steps to get predictions
1. Upload an image.
2. The web page displays image label and the confidence with which the model has on the prediction.
3. Repeat step 1 until you are satisfied.

## Teardown steps
```
   kubectl delete -f deployment.yaml
   docker rmi -f $(docker images -a -q)
```
