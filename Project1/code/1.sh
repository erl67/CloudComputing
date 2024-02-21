../hadoop/bin/hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming*.jar \
    -files mapper1.py,reducer1.py \
    -input input/access_log \
    -output output/output1 \
    -mapper /opt/code/mapper1.py \
    -reducer /opt/code/reducer1.py
hdfs dfs -cat output/output1/*
hdfs dfs -rm -r output/output1