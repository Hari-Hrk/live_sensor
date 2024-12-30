import os 
import sys
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import dump_csv_file_to_mongodb_collection
from sensor.pipeline.training_pipeline import TrainPipeline

# def test_exception():
#     try:
#         logging.info("ki yaha p bhaiaa ek error ayegi diveision by zero wali error ")
#         a=1/0
#     except Exception as e:
#        raise SensorException(e,sys) 



if __name__ == "__main__":

    ##=============== data upload data in mongodb database =============
    # file_path="C:/Users/hi/Desktop/projects/5-project/live_sensor/aps_failure_training_set1.csv"
    # database_name="ineuron"
    # collection_name ="sensor"
    # dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)

    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()


# if __name__ == "__main__":
#     try:
#         test_exception()
#     except Exception as e:
#         print(e)














    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)