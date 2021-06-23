Case 1

mapper.py and reducer.py used for experiment 1 with mapper_top100.py and reducer_top100.py to get final output.
mapper6.py and reducer.py used for experiment 2 with mapper_top100.py and reducer_top100.py to get final output.

Case A

$HADOOP_HOME/bin/hadoop jar hadoop-streaming-2.2.0.jar \
-file /HADOOP/hdfs/user/bigdata16/mapper.py -mapper mapper.py \
-file /HADOOP/hdfs/user/bigdata16/reducer.py -reducer reducer.py \
-input BigData.txt -output BDOutput1

$HADOOP_HOME/bin/hadoop jar hadoop-streaming-2.2.0.jar \
-file /HADOOP/hdfs/user/bigdata16/mapper6.py -mapper mapper6.py \
-file /HADOOP/hdfs/user/bigdata16/reducer.py -reducer reducer.py \
-input BigData.txt -output BDOutput1b

Case B

$HADOOP_HOME/bin/hadoop jar hadoop-streaming-2.2.0.jar \
-file /HADOOP/hdfs/user/bigdata16/mapper.py -mapper mapper.py \
-file /HADOOP/hdfs/user/bigdata16/reducer.py -reducer reducer.py \
-file /HADOOP/hdfs/user/bigdata16/reducer.py -combiner reducer.py \
-input BigData.txt -output BDOutput2

$HADOOP_HOME/bin/hadoop jar hadoop-streaming-2.2.0.jar \
-file /HADOOP/hdfs/user/bigdata16/mapper6.py -mapper mapper6.py \
-file /HADOOP/hdfs/user/bigdata16/reducer.py -reducer reducer.py \
-file /HADOOP/hdfs/user/bigdata16/reducer.py -combiner reducer.py \
-input BigData.txt -output BDOutput2b

Case C

$HADOOP_HOME/bin/hadoop jar hadoop-streaming-2.2.0.jar \
-D mapreduce.partition.keypartitioner.options=-k1,2 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-file /HADOOP/hdfs/user/bigdata16/mapper.py -mapper mapper.py \
-file /HADOOP/hdfs/user/bigdata16/reducer.py -reducer reducer.py \
-file /HADOOP/hdfs/user/bigdata16/reducer.py -combiner reducer.py \
-input BigData.txt -output BDOutput3


$HADOOP_HOME/bin/hadoop jar hadoop-streaming-2.2.0.jar \
-D mapreduce.partition.keypartitioner.options=-k1,1 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-file /HADOOP/hdfs/user/bigdata16/mapper6.py -mapper mapper6.py \
-file /HADOOP/hdfs/user/bigdata16/reducer.py -reducer reducer.py \
-file /HADOOP/hdfs/user/bigdata16/reducer.py -combiner reducer.py \
-input BigData.txt -output BDOutput3b 

Case D

$HADOOP_HOME/bin/hadoop jar hadoop-streaming-2.2.0.jar \
-D mapreduce.compress.map.output=true \
-D mapreduce.output.compress=true \
-D mapreduce.map.output.compression.codec=org.apache.hadoop.io.compress.DefaultCodec \
-D mapreduce.output.compression.codec=com.hadoop.compression.lzo.LzopCodec \
-file /HADOOP/hdfs/user/bigdata16/mapper.py -mapper mapper.py \
-file /HADOOP/hdfs/user/bigdata16/reducer.py -reducer reducer.py \
-file /HADOOP/hdfs/user/bigdata16/reducer.py -combiner reducer.py \
-input BigData.txt -output BDOutput4

$HADOOP_HOME/bin/hadoop jar hadoop-streaming-2.2.0.jar \
-D mapreduce.compress.map.output=true \
-D mapreduce.output.compress=true \
-D mapreduce.map.output.compression.codec=org.apache.hadoop.io.compress.DefaultCodec \
-D mapreduce.output.compression.codec=com.hadoop.compression.lzo.LzopCodec \
-file /HADOOP/hdfs/user/bigdata16/mapper6.py -mapper mapper6.py \
-file /HADOOP/hdfs/user/bigdata16/reducer.py -reducer reducer.py \
-file /HADOOP/hdfs/user/bigdata16/reducer.py -combiner reducer.py \
-input BigData.txt -output BDOutput4b 

To get Output File
Where input will be the output file of the above commands

$HADOOP_HOME/bin/hadoop jar hadoop-streaming-2.2.0.jar \
-D mapred.reduce.tasks=1 \
-file /HADOOP/hdfs/user/bigdata16/mapper_top100.py -mapper mapper_top100.py \
-file /HADOOP/hdfs/user/bigdata16/reducer_top100.py -reducer reducer_top100.py \
-file /HADOOP/hdfs/user/bigdata16/reducer_top100.py -combiner reducer_top100.py \
-input BDOutput1 -output BDOutputFinal100

Case 2

mapper.py and reducer_top100.py used for experiment 1.

Case A

$HADOOP_HOME/bin/hadoop jar hadoop-streaming-2.2.0.jar \
-D mapred.reduce.tasks=1 \
-file /HADOOP/hdfs/user/bigdata16/mapper.py -mapper mapper.py \
-file /HADOOP/hdfs/user/bigdata16/reducer_top100.py -reducer reducer_top100.py \
-input BigData.txt -output BDOutput1

Case B

$HADOOP_HOME/bin/hadoop jar hadoop-streaming-2.2.0.jar \
-D mapred.reduce.tasks=1 \
-file /HADOOP/hdfs/user/bigdata16/mapper.py -mapper mapper.py \
-file /HADOOP/hdfs/user/bigdata16/reducer_top100.py -reducer reducer_top100.py \
-file /HADOOP/hdfs/user/bigdata16/reducer_top100.py -combiner reducer_top100.py \
-input BigData.txt -output BDOutput2

Case C

$HADOOP_HOME/bin/hadoop jar hadoop-streaming-2.2.0.jar \
-D mapred.reduce.tasks=1 \
-D mapreduce.partition.keypartitioner.options=-k1,2 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-file /HADOOP/hdfs/user/bigdata16/mapper.py -mapper mapper.py \
-file /HADOOP/hdfs/user/bigdata16/reducer_top100.py -reducer reducer_top100.py \
-file /HADOOP/hdfs/user/bigdata16/reducer_top100.py -combiner reducer_top100.py \
-input BigData.txt -output BDOutput3

Case D

$HADOOP_HOME/bin/hadoop jar hadoop-streaming-2.2.0.jar \
-D mapred.reduce.tasks=1 \
-D mapreduce.compress.map.output=true \
-D mapreduce.output.compress=true \
-D mapreduce.map.output.compression.codec=org.apache.hadoop.io.compress.DefaultCodec \
-D mapreduce.output.compression.codec=com.hadoop.compression.lzo.LzopCodec \
-file /HADOOP/hdfs/user/bigdata16/mapper.py -mapper mapper.py \
-file /HADOOP/hdfs/user/bigdata16/reducer_top100.py -reducer reducer_top100.py \
-file /HADOOP/hdfs/user/bigdata16/reducer_top100.py -combiner reducer_top100.py \
-input BigData.txt -output BDOutput4

Case 3

$HADOOP_HOME/bin/hadoop jar hadoop-streaming-2.2.0.jar \
-D mapred.reduce.tasks=30 \
-file /HADOOP/hdfs/user/bigdata16/mapper.py -mapper mapper.py \
-file /HADOOP/hdfs/user/bigdata16/reducer.py -reducer reducer.py \
-file /HADOOP/hdfs/user/bigdata16/reducer.py -combiner reducer.py \
-input BigData.txt -output BDOutput2_30

$HADOOP_HOME/bin/hadoop jar hadoop-streaming-2.2.0.jar \
-D mapred.reduce.tasks=60 \
-file /HADOOP/hdfs/user/bigdata16/mapper.py -mapper mapper.py \
-file /HADOOP/hdfs/user/bigdata16/reducer.py -reducer reducer.py \
-file /HADOOP/hdfs/user/bigdata16/reducer.py -combiner reducer.py \
-input BigData.txt -output BDOutput2_60

To get Output File
Where input will be the output file of the above commands

$HADOOP_HOME/bin/hadoop jar hadoop-streaming-2.2.0.jar \
-D mapred.reduce.tasks=1 \
-file /HADOOP/hdfs/user/bigdata16/mapper_top100.py -mapper mapper_top100.py \
-file /HADOOP/hdfs/user/bigdata16/reducer_top100.py -reducer reducer_top100.py \
-file /HADOOP/hdfs/user/bigdata16/reducer_top100.py -combiner reducer_top100.py \
-input BDOutput1 -output BDOutputFinal100
