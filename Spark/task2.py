from __future__ import print_function
from pyspark import SparkContext
from csv import reader
import sys

if __name__ == "__main__":
    sc = SparkContext()
    parking_lines = sc.textFile(sys.argv[1], 1)
    parking_lines = parking_lines.mapPartitions(lambda x: reader(x)).map(lambda x: (x[2],1)).reduceByKey(lambda x, y: x + y).sortByKey(True)
    parking_lines= parking_lines.map( lambda x: '%s\t%d' % (x[0],x[1]))
    parking_lines.saveAsTextFile('task2.out')
    

    
