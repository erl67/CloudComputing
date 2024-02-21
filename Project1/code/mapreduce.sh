#!/bin/bash
#this script takes a number from 1-10 as an argument
#runs the corresponding mapper and reducer and saves and deletes the output

if [ $# -ne 1 ]; then
    echo "Enter integer from 1 to 10 corresponding to the question"
    exit 1
fi
if ! [[ $1 =~ ^[1-9]$|^10$ ]]; then
    echo "Must be number between 1 and 10"
    exit 1
fi 

mapper="mapper$1.py"
reducer="reducer$1.py"

../hadoop/bin/hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming*.jar \
    -files "$mapper","$reducer" \
    -input input/access_log \
    -output output/output$1 \
    -mapper "/opt/code/$mapper" \
    -reducer "/opt/code/$reducer" \
    2>&1 | tee ./output/out$1hadoop.txt
hdfs dfs -cat output/output$1/* | tee ./output/out$1.txt
hdfs dfs -rm -r output/output$1
