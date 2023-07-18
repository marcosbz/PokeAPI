# PokeAPI
PokeAPI Challenge

## Local Deployment
#### Build and run a docker image

Use these commands to build the image:

```sh
git clone https://github.com/marcosbz/PokeAPI.git
cd PokeAPI/
docker build --build-arg ARG_POKEAPI_BERRY_BASE_URL=https://pokeapi.co/api/v2/berry/ -t pokeapi:latest .
```

Then run the container:

```sh
docker run --rm -p 5000:5000 pokeapi:latest
```

Call the stats endpoint:

```sh
curl localhost:5000/allBerryStats
```

## Azure Deployment

First an Azure container App has to be created inside a Resource Group and configured. Also create a Service principal with access to the mentioned Resource Group. 
Fork the project to your repository and set the following Vars and Secrets

#### Vars

- AZURE_CREDENTIALS: Json containing the Service Principal credentials with access to the resource group
- DOCKERHUB_TOKEN: Token to access the Dockerhub container registry
- DOCKERHUB_USERNAME: Token to access the Dockerhub container registry

#### Secrets

- ARG_POKEAPI_BERRY_BASE_URL: The base Berry endpoint. Currently https://pokeapi.co/api/v2/berry/
- CONTAINER_APP_NAME: App name set in Azure
- RESOURCE_GROUP: Resource group where the container App resides in Azure
- TARGET_PORT: Port set in azure to be mapped to the port 80
