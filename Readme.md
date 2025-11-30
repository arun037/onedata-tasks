**Task-2: Kubernetes Deployment with Minikube**

Prerequsites:
    Minikube
    docker 


Step 1: Customize the nginx deployment with custom index.html file and placed in root folder and Create a Dockerfile

step 2: Build the docker image and push it to repository

docker build -t arunagri03/myapp .

![alt text](images/image.png)

docker push arunagri03/myapp

![alt text](images/image-1.png)

step 3: Create a deployment.yaml and service.yaml with image as arunagri03/myapp inside deploy-files folder and deploy it using

Kubectl deploy -f deployment.yaml
kubectl deploy -f svc.yaml

![alt text](images/image-2.png)

step 4: Verify deployment using kubectl get pods,svc

![alt text](images/image-3.png)

step 5: Creating an ingress.yaml to use custom domain

    Minikube comes with default ingrss addon and to enable it 
    
    minikube addons enable ingress

   curl arunm.online  --->  ingress ---> myapp-svc ---> myapp

step 6: curl using domain name: 

![alt text](images/image-4.png)