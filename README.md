## PySpark structured streaming with Tweepy and Kafka
Create, read, write structured stream using twitter api, pyspark and kafka.


## Installation
Install [kafka](https://kafka.apache.org/downloads) locally. Apache Kafka required Java to be installed too.

Install [spark](https://spark.apache.org/downloads.html) locally. Java should be installed during Kafka installation.

```bash
# run Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties
# run Kafka broker(from new terminal)
bin/kafka-server-start.sh config/server.properties
# create topic
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic topic_name
```

Install required Python libs.
```bash
pip install requirements.txt
```
Generate [Twitter's](https://developer.twitter.com/en/apps) keys and tokens from created app.

## Usage

* ```twitter_stream.py``` - provide a stream of tweets and publish as json to Kafka
* ```pyspark_kafka_stream.py``` - read from Kafka, analyze and write to console
```bash
# run locally
$SPARK_HOME/bin/spark-submit --master local[*] pyspark_kafka_stream.py
# then from new window
python twitter_stream.py
# output should be similar
Batch: 0
-------------------------------------------
+---------------+--------------------+---------+-------+
|      user_name|          user_tweet|followers|friends|
+---------------+--------------------+---------+-------+
|   Anon_Snufkin|RT @MikeStuchbery...|     4900|   2934|
|_iamtooprecious|RT @PatrickTimmon...|     1136|   1302|
|  PugilistSteve|FOOTBALL Pinnick...|    11745|  12915|
|   evilbluebird|Chelsea boss Fran...|    23524|   9445|
|  PugilistSteve|FOOTBALL David S...|    11745|  12915|
|       gdmeboss|RT @ManUtdMEN: Ja...|      442|   1426|
|       derr_yck|RT @SaddickAdams:...|     2007|   3269|
| MaybeHeadSouth|@santaspants @Sco...|      565|   1517|
|       ekgmedia|RT @Pismo_B: Poli...|     1483|   2554|
|truebluehatesnp|RT @GordonW092254...|      980|   1548|
|     PoloSpates|RT @Mr_Nance47: I...|      920|   4990|
+---------------+--------------------+---------+-------+

-------------------------------------------
Batch: 1
-------------------------------------------
+---------------+--------------------+---------+-------+
|      user_name|          user_tweet|followers|friends|
+---------------+--------------------+---------+-------+
|kofiwusudedon11|RT @MailSport: Se...|      115|   1303|
+---------------+--------------------+---------+-------+

```
