FROM ubuntu:22.04

#MAINTAINER 

USER root
ENV JAVA_HOME /usr/java/default
ENV PATH $PATH:$JAVA_HOME/bin
ENV hadoop_path /opt/hadoop
ENV java_path /usr/lib/jvm/java-8-openjdk-amd64


RUN \
   apt-get update && apt-get install -y \
   ssh \
   rsync \
   vim \
   openjdk-8-jdk

RUN \
   wget https://archive.apache.org/dist/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz \
    && \
    tar -xzf hadoop-3.2.1.tar.gz && \
    mv hadoop-3.2.1 $hadoop_path && \
    echo "export JAVA_HOME=$java_path" >> $hadoop_path/etc/hadoop/hadoop-env.sh && \
    echo "PATH=$PATH:$hadoop_path/bin" >> ~/.bashrc

ADD /*xml $hadoop_path/etc/hadoop/
ADD /*jar $hadoop_path
ADD bootstrap.sh bootstrap.sh

# ADD file, hdfs-site.xml in the current directory, to the directory, $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml, in the image
ADD hdfs-site.xml $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml

EXPOSE 8088 50070 50075
cmd bash bootstrap.sh




#docker build .
#sudo docker images
#sudo docker run -it -d name /bin/bash
#
#sudo docker ps
#sudo docker exec -it name

