# End-to-End-ML-with-MLFLOW

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update parmas.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/kumarraj585/End-to-End-ML-with-MLFLOW
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```
```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui


### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/kumarraj585/End-to-End-ML-with-MLFLOW.mlflow \
MLFLOW_TRACKING_USERNAME=kumarraj585 \
MLFLOW_TRACKING_PASSWORD=5a9c9ac10d202f3f2761c73bc264e235a536e0d1 \
python script.py

Run this to export as env variables:


```bash

$env:MLFLOW_TRACKING_URI="https://dagshub.com/kumarraj585/End-to-End-ML-with-MLFLOW.mlflow"

$env:MLFLOW_TRACKING_USERNAME="kumarraj585"

$env:MLFLOW_TRACKING_PASSWORD="5a9c9ac10d202f3f2761c73bc264e235a536e0d1"

```
