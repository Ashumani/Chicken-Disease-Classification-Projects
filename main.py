from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestions import DataIngestionTrainingPipeline

logger.info("welcome to my custom logging")

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
