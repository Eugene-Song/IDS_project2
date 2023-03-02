## Flask microservice for looking up zipcode

# Introduction
This is a course project which is a simple microservice for looking up detail information of a zipcode based on Flask. This project image will be pushed to DockerHub, or Cloud based Container Registery (ECR), and it is deployed to App Runner from AWS. 

For minikube testing, user can just use the image which I pushed to dockerhub to create the local cluster.

In the future, this project can be deployed to EKS.

# Usage
For local testing, just use ```python3 app.py``` to start the service. 
Then user can go to ```localhost:8080``` to check the result.

# Test with minikube
1.  Push container to DockerHub
2. ```minikube start```
3. ```minikube dashboard --url```
4. Hover over link and "follow link"
5. Create a deployment: ```kubectl create deployment proj2 --image=registry.hub.docker.com/wadqq/project2```
6. View deployment: `kubectl get deployments`
7. Create service and expose it: ```kubectl expose deployment proj2 --type=LoadBalancer --port=8080```
8. View services:  ```kubectl get service proj2```
9.  ```minikube service proj2 --url```
10. Curl web service: i.e. ```curl <URL>```
11.  Cleanup
```kubectl delete service proj2```
```kubectl delete deployment proj2```
```minikube stop```

# Deploy to APP Runner
For test, user can just go to https://b6smt2eihv.us-east-1.awsapprunner.com/zip/<zipcode> to test the usage of it.

# Project plan
Week1: Finish the project planning, and finish the basic fucntion of the project.

Week2: Add an interactive page for this application and add more features. And finish the dockerfile and other containerized steps. 

Week3: Finish the automatically deployment to App Runner.

# Screemshots
For app runner testing result:
![alt text](img1.png)
For minikube testing result:
![alt text](img2.png)

## Reference

1. [Applied Kubernetes by Noah Gift on Github](https://github.com/nogibjj/coursera-applied-de-kubernetes-lab)
2. [Rust Template by Noah Gift on Github](https://github.com/noahgift/rust-new-project-template)