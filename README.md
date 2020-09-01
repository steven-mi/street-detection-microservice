# Street Situation Detection Microservice

![img](https://images.unsplash.com/photo-1475998776787-d22fa84424b6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1359&q=80)

This repository contains the code for running a microservice for detecting street situations. It is build around the package build around the production model from the [street-situation-detection](https://github.com/steven-mi/street-situation-detection) package. 

## Requirements
- docker
- docker-compose

## Getting started
Run microservice:
```bash
docker-compose up
``` 
Test availability with the example script:
```
python example-requests.py
```
Output should look like this:
```
.../street-situation-microservice/evaluation-images/positive_0.JPG was predicted as 1
.../street-situation-microservice/evaluation-images/positive_1.jpg was predicted as 1
.../street-situation-microservice/evaluation-images/negative_0.jpg was predicted as 0
.../street-situation-microservice/evaluation-images/negative_1.jpg was predicted as 0
```