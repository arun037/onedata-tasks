**Task-3: Kubernetes Deployment Using ARGOCD**
Step 1: Create a namespace and apply the manifests

![alt text](images/image.png)

step 2: Patch the argocd-server to node-port

![alt text](images/image-1.png)

step 3: Install argocd cli, get initial admin password and add cluster

![alt text](images/image-2.png)

login to the cluster

![alt text](images/image-3.png)

step 4: Add the repo to argocd

![alt text](images/image-4.png)

step 5: Create a new app and select the repo 

![alt text](images/image-5.png)

the deployment happens to the cluster by argocd

![alt text](images/image-6.png)

this was the image version first used

![alt text](images/image-7.png)

And if auto-sync is enabled argocd watches github for any changes and if it detects it sync with respect to github

![alt text](images/image-8.png)