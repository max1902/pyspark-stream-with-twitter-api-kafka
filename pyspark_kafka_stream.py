from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import (
    StructType,
    StringType,
    StructField,
    IntegerType,
)

KAFKA_TOPIC = 'tweets'
KAFKA_SERVER = 'localhost:9092'
spark = SparkSession.builder.appName('Tweet-Kafka-Spark-Stream').getOrCreate()
spark.sparkContext.setLogLevel('ERROR')
df = spark \
    .readStream \
    .format('kafka') \
    .option('kafka.bootstrap.servers', KAFKA_SERVER) \
    .option('subscribe', KAFKA_TOPIC) \
    .option('startingOffsets', 'earliest') \
    .load()
MessageSchema = StructType([
    StructField('user_name', StringType(), False),
    StructField('user_tweet', StringType(), False),
    StructField('followers', IntegerType(), False),
    StructField('friends', IntegerType(), False),
])
df = df.selectExpr('CAST(value AS STRING)')
df = df.withColumn('message', from_json(df.value, MessageSchema)) \
    .select('message.user_name',
            'message.user_tweet',
            'message.followers',
            'message.friends') \
    .where('message.friends > 1000')
df.writeStream.outputMode('append').format('console').start().awaitTermination()
