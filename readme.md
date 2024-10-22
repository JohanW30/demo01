# Kubernetes Demo01
## DOCKER

### Konfigurera ett gemensamt nätverk för frontend och backend
skapa nätverket my-network `docker network create my-network`
\
kontrollera vilka nätverk som finns `docker network ls`

### Backend
kör kommando i samma katalog som docker backend-filen
- `docker build -t johwi30/random-facts-backend  .`
- `docker run --name backend-service.backend-namespace.svc.cluster.local --network my-network -p 5001:5000 johwi30/random-facts-backend`

### Frontend
kör kommando i samma katalog som docker frontend-filen 
- `docker build -t johwi30/random-facts-frontend .`
- `docker run --network my-network -p 81:80 johwi30/random-facts-frontend`


### Pusha till docker-hub
loggga in `docker login`\
pusha frontend `docker push johwi30/random-facts-frontend`\
pusha backend `docker push johwi30/random-facts-backend`


## MINIKUBE
`minikube start`
\
`minikube dashboard`

## KUBECTL COMMANDS

### Installera docker-image från docker hub
#### FRONTEND
`kubectl delete -f .\frontend-deployment.yaml`
\
`kubectl apply -f frontend-deployment.yaml`
#### BACKEND
`kubectl delete -f .\backend-deployment.yaml`
\
`kubectl apply -f backend-deployment.yaml`

### Testa backend (port-forward)
`kubectl port-forward svc/backend-service 5001:5000 -n backend-namespace`

### Testa frontend (port-forward)
Alt 1 - `kubectl port-forward svc/frontend-service 81:80 -n frontend-namespace`
\
(Alt 2 - `minikube service frontend-service --namespace=frontend-namespace`)

### Testa API-anrop från en pod till en annan
Vad heter poden? `kubectl get pods -n frontend-namespace`
\
Gör anropet `kubectl exec -it PODNAMNET -n frontend-namespace -- curl -s http://backend-service.backend-namespace.svc.cluster.local:5000/fact`