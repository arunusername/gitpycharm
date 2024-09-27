
from pyspark.sql import *
   from pyspark.sql.functions import *
   
   spark = SparkSession.builder.appName("tset").master("local[*]").getOrCreate()
