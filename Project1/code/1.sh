../hadoop/bin/hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -input /opt/hadoop/access_log \
    -output 3_1_output.txt \
    -mapper mapper1.py \
    -reducer reducer1.py \
    -file mapper1.py \
    -file reducer1.py
                            