from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("Operations").setMaster("local")
sc = SparkContext(conf)

data = spark.parallelize(
    [('Amber', 22), ('Alfred', 23), ('Skye',4), ('Albert', 12),
     ('Amber', 9)])