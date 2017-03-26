from __future__ import print_function
from pyspark import SparkContext
from csv import reader
import sys

if __name__ == "__main__":
    sc = SparkContext()
    parking_lines = sc.textFile(sys.argv[1], 1)
    parking_lines = parking_lines.mapPartitions(lambda x: reader(x)).map(lambda x: ('Other' if x[16] not in 'NY' else x[16],1))
    parking_lines=parking_lines.reduceByKey(lambda x, y: (x+y)).sortByKey(True)
    parking_lines=parking_lines.map(lambda x: '%s\t%s' % (x[0],x[1]))
    parking_lines.saveAsTextFile('task4.out')
    

    

