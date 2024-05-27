## Project overview

This project utilizes the Concrete Slump Test dataset, which is imported using the `ucimlrepo` library, to develop a machine learning model for predicting the compressive strength of the concrete.

## Dataset

The dataset comprises the following independent variables:
- **Cement**
- **Blast Furnace Slag**
- **Fly Ash**
- **Water**
- **Superplasticizer**
- **Coarse Aggregate**
- **Fine Aggregate**
- **Age**

These variables are used for predicting the compressive strength of the concrete.


## Model development

Script `ml_model.py` was used to develop a Gradient Boosting regression model. The dataset was divided, with 80% of the data allocated for model training. 


## Model performance

Model's performance was evaluated using mean absolute error (MAE) and root mean squared error (RMSE) metrics:
- **MAE:** 4.094.
- **RMSE:** 5.699.

## Model saving

The trained model was saved in a file named `trained_pipeline.pkl` using the `pickle` module.

## Project implementation

- **main.py:** contains the necessary Python code to implement the project's functionality. The code includes the implementation of a FastAPI application for predicting concrete compressive strength using a pre-trained machine learning model.
- **requirements.txt:** lists the external libraries or dependencies that the Python code relies on.
- **Dockerfile:** includes instructions to build a Docker image.

## Running the project

To run the project code from the main directory the following commands were used:
- `docker build .` to build the Docker image. 
- `docker image list` to investigate the image ID.
- `docker run -d -p 8000:8000 8780d6ef443f` to un the Docker container in the background with the image ID 8780d6ef443f.

## Verify API health check:

After launching the Docker container, go to http://localhost:8000/ in web browser. This should show a health check response: {"healthcheck": "OK"}, confirming that the API is functioning properly.

## Using the API for predictions:

The API enables users to input values for independent variables to receive predictions for cement compressive strength. API can be accessed and viewed the available endpoints by visiting the documentation at http://localhost:8000/docs#/.

## Pushing docker image to a container registry:

Here are the steps taken to push a Docker image to a container registry:
- `docker login` command to log into Docker Hub.
- `docker tag 8780d6ef443f matassepikas/bd_individual_project:v1.0` command to tag a local Docker image with a new name and version.
- `docker push matassepikas/bd_individual_project:v1.0` command to push the tagged image to Docker Hub.

The Docker image tag: `matassepikas/bd_individual_project:v1.0`