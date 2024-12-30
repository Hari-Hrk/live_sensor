# live_sensor


# Work flow

# data ingestion sensor is folder name
- sensor / constant
- sensor / entity == config_entity  &  artifact entity
- sensor/components/data_ingestion
- sensor / pipeline / training_pipeline.py



### mongodb connection 

- .env
- constant/env_variable.py
- configuration/mongodb_db_connection.py
- data_access / sensor_data.py


# data ingestion steps wise
 - 1. collect   -  from mongodb
 - 2. store     -  file/folder etc 2,3 steps  in config
 - 3. split    -   Test,Train 
 - 4. record data  -  in components
 - 5. sequitail arrangement -  pipeline