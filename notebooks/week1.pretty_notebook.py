# Databricks notebook source

# %pip install loguru pyyaml --quiet
# %restart_python
# COMMAND ----------
import sys
from pathlib import Path

sys.path.append(str(Path.cwd().parent / "src"))

# COMMAND ----------
import sys

import pandas as pd
import yaml
from loguru import logger
from pyspark.sql import SparkSession

from mlops_course.config import ProjectConfig
from mlops_course.data_processor import DataProcessor

config = ProjectConfig.from_yaml(config_path="../project_config.yml", env="dev")

logger.info("Configuration loaded:")
logger.info(yaml.dump(config, default_flow_style=False))

# COMMAND ----------

# Load the white-wine quality dataset
spark = SparkSession.builder.getOrCreate()

filepath = "/Volumes/mlops_dev/floreswo/data/winequality-white.csv"

# Load the data
df = pd.read_csv(filepath, sep=";")


# COMMAND ----------
# Load the white-wine quality dataset

data_processor = DataProcessor(df, config, spark)

# Preprocess the data
data_processor.preprocess()

logger.info("Data preprocessing is completed.")

# COMMAND ----------

# Split the data
X_train, X_test = data_processor.split_data()
logger.info("Training set shape: %s", X_train.shape)
logger.info("Test set shape: %s", X_test.shape)

# COMMAND ----------
# Save to catalog
logger.info("Saving data to catalog")
data_processor.save_to_catalog(X_train, X_test)

# Enable change data feed (only once!)
logger.info("Enable change data feed")
data_processor.enable_change_data_feed()
# COMMAND ----------
