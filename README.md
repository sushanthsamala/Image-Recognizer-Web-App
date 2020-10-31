# Image-Recognizer-Web-App
This is a image recognizer web application that runs on Kubernetes with 4 replicas, you can upload your image to get a label and confidence.
## Prerequisites
1. Install [Docker](https://docs.docker.com/get-docker/)
2. Install [Kubernetes](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
3. Open Docker desktop and run docker daemon.
4. Navigate to Kubernetes tab in Docker desktop and select 'Enable Kubernetes' option. 
## Steps to run
 ```
    git clone //https://github.com/sushanthsamala/Image-Recognizer-Web-App
    cd Image-Recognizer-Web-App
    docker build -t image-recognizer .
    kubectl apply -f deployment.yaml
 ```
## Steps to get predictions
1. Navigate to http://0.0.0.0:5000 in your browser
2. Upload an image.
3. The web page displays image label and the confidence with which the model has on the prediction.
4. Repeat step 2 until you are satisfied.
## Teardown steps
```
   kubectl delete -f deployment.yaml
   docker rmi -f $(docker images -a -q)
```
