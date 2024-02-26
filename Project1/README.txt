All code is located in the /code folder and all outputs are located in the /output folder

1. Part 1 was setting up the local docker file and running a single node hadoop. This was done using the Dockerfile
contained in the /local_demo folder, and starting hadoop with the bootstrap.sh file. The output of the console was saved to hadoop_docker_test.txt which verifies
that the hadoop node was running by executing the command:
root@fa8638416a92:/opt/hadoop# bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.1.jar pi 2 5


Part 2 and 3 were both done using the book Hadoop With Python from O'Reilly which uses Hadoop Streaming to run MapReduce from python files.
I used the commands in the book to call each program and wrote shell scripts that would run hadoop with the corresponding inputs, 
then save both the MapReduce output and the hadoop terminal output to a designated folder. This saved a lot of time instead of having
to copy and past the command line and output and change the inputs for each run. All the programming was done in Vim.
One thing I tried for the ngram program (which was done last) was to create the MapReduce program using the MRJob python class
which was mentioned in the book. However, I kept running into errors getting it to read the test data and ran out of time.


2. Part 2 was running the ngram program. I tested it with a test file containing "hello world" and with a RandomTextWriter
output of 1MB. The program is run via the script ngram.sh which controls the n-gram size and the input file.
The output is stored in the /output folder as outn.txt and the results of the hadoop runtime output is outnhadoop.txt

The command for the test is:
root@fa8638416a92:/opt/code#  ./ngram.sh 2 input/test.txt

The command for the random text is:
root@fa8638416a92:/opt/code#  ./ngram.sh 5 input/rand.txt



3. Part 3 was the ten questions on the common log file. For this part I used 10 different map/reduce programs which
are all callable from the same shell script. The script calls the corresponding program and saves the output along with the
hadoop runtime output. The command to run each program is as follows, where the number is a number from 1 to 10 of which question to answer.

root@fa8638416a92:/opt/code# ./mapreduce.sh 1


For a few of them I had to sort the output afterwards because the reducer that was done with the following commands:
cat output4.txt | sort -k2,2nr > output4sorted.txt
cat out9.txt | sort -k2,2nr | head -n 10 > out9sorted.txt


The shell scripts look like this to run hadoop streaming:
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



The results of all 10 are as follow:
1:
/images/smilies/	330592

2:
96.32.128.5	1959647

3:
ASDE	1
DEBUG	5
DELETE	6
FLURP	6
GET	3542440
HEAD	5696259
INDEX	1
OPTIONS	26
POST	471552
PROPFIND	23
PUT	11
SEARCH	1
TRACE	10
TRACK	6
VIMF	1
get	1

4:
/apache-log/access.log	630006
/administrator/index.php	453910
/	37687
/index.php?option=com_contact&view=contact&id=1	22248
/index.php	20330
/robots.txt	12987
/index.php?option=com_easyblog&view=dashboard&layout=write	11873
/administrator/index.php?option=com_plugins	11554
/templates/_system/css/general.css	11534
/favicon.ico	8888

5:
47.39.156.135	4305147
96.32.128.5	1959647
73.169.232.206	1572800
193.106.31.130	340874
82.209.218.4	333838
95.208.160.29	220496
14.139.110.137	95069
198.137.18.192	58916
113.14.181.185	51503
197.52.128.37	40777

6:
POST	471552

7:
404	7209055

8:
19/Dec/2020	10337151

9:
47.39.156.135	1191486857
73.169.232.206	565279763
96.32.128.5	2672374057

10:
16/Jan/2022	2465568761

Sources:
https://www.oreilly.com/content/hadoop-with-python/
https://docs.docker.com/engine/reference/builder/
https://stackoverflow.com/questions/17569423/what-is-best-way-to-start-and-stop-hadoop-ecosystem-with-command-line
https://hadoop.apache.org/docs/r1.2.1/streaming.html
https://www.geeksforgeeks.org/what-is-hadoop-streaming/
https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/
https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HDFSCommands.html
https://hadoop.apache.org/docs/r1.2.1/api/org/apache/hadoop/examples/RandomTextWriter.html
https://mrjob.readthedocs.io/en/latest/