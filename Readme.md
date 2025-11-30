**Task-4: Kubernetes Deployment with Github-Actions**

Step 1: creating a github actions file under .git/workflow/main.yaml


Step 2: i have used two stages build and deploy
        build stage - code checkout happens and docker image is build and for everybuild it modifies the image tag.
        deploy stage - deploy the manifest file into the minikube cluster.

Step 3: Build stage runs-on Github-runner
    - code checkout happens
    - Install dependencies
    - Run testcases
    - Build the docker image
    - Push the docker image. use of secrets for storing the credentials of docker hub
    - update deployment file. - for every code push a new docker image is build and pushed to repository and the image tag on deployment file was modified by using sed command and pushed to repo.

    note: for this we have give permission for content as write

Step 4: Deploy-stage runs-on Self-hosted runner
    - To perform deploy action to the minikube cluster 
    - Apply the yaml files located inside deploy-files folder
    - check the rollout status of deployment

    