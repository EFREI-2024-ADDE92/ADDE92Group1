# ADDE92Groupe1

This project involves the following steps:

1. Training the model (Iris with scikit-learn KNN) and exporting it (joblib.dump)
2. Integrating the trained model into an API
3. Packaging the API into a Docker image locally
4. Publishing the code on Github
5. Configuring the deployment pipeline with the following elements:
    - Building the Docker image
    - Publishing the Docker image on Azure Container Registry (ACR)
    - Deploying on Azure Container App
    - Configuring autoscaling using the number of simultaneous requests as a parameter
6. Performing a load test with the tool of your choice

## Evaluation

In groups of 6 people, you will have to present your project during a 20-minute defense and provide all the deliverables requested by email. The defense will proceed as follows:

- 15 minutes of presentation
- 5 minutes of questions

Deliverables:

- URL of the Github repository with all the elements (code, Dockerfile, Github workflow configuration)
- Name of the Docker image on Azure Container Registry (ACR)
- Azure Container App API Endpoint
- Report presenting, step by step, the technical choices, the commands used, the load test strategy accompanied by your observations and the difficulties encountered if you have not been able to finish.

## Connection Information

Connection information is available on the Github organization:

- AZURE_CREDENTIALS: service account for authenticating with the Azure API
- REGISTRY_LOGIN_SERVER: link of the registry server (efreibigdata.azurecr.io)
- REGISTRY_USERNAME: registry username
- REGISTRY_PASSWORD: password for the registry
- RESOURCE_GROUP: Azure resource group (ADDE92-CTP)

## Defense

- Deployment on Azure Container Apps
- Code review (API, training method, Dockerfile)
- Local test
- Test of the Azure Container Apps endpoint

## Bonus

- Problems encountered