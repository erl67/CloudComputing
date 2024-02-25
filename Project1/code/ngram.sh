#!/bin/bash
#this script takes a number from 1-10 as an argument for the ngram length
#and the second argument is the input file

if [ $# -ne 2 ]; then
    echo "Usage: Enter the ngram length followed by the input file [input/hello.txt or input/rand.txt]"
    exit 1
fi
if ! [[ $1 =~ ^[1-9]$|^10$ ]]; then
    echo "Must be number between 1 and 10"
    exit 1
fi

ngram_length=$1
input_file=$2

mapper="mapper-ngram.py"
reducer="reducer-ngram.py"

../hadoop/bin/hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming*.jar \
    -files "$mapper","$reducer" \
    -input "$input_file" \
    -output output/outputn \
    -mapper "/opt/code/$mapper $ngram_length" \
    -reducer "/opt/code/$reducer" \
    2>&1 | tee ./output/outnhadoop.txt
hdfs dfs -cat output/outputn/* | tee ./output/outn.txt
hdfs dfs -rm -r output/outputn