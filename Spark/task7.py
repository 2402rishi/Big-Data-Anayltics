from __future__ import print_function
from pyspark import SparkContext
from csv import reader
import sys

if __name__ == "__main__":
    sc = SparkContext()
    parking_lines = sc.textFile(sys.argv[1], 1)
    parking_lines = parking_lines.mapPartitions(lambda x: reader(x)).map(lambda x: (x[2],1 if int(x[1][-2:]) in [5, 6, 12, 13, 19, 20, 26, 27] else 0))
    count= parking_lines.countByKey()
    parking_lines=parking_lines.reduceByKey(lambda x, y: (x+y))
    parking_lines=parking_lines.map(lambda x: '%s\t%.2f, %.2f' % (x[0],x[1]/float(8), (count[x[0]]-x[1])/float(23))).sortByKey(True)
    parking_lines.saveAsTextFile('task7.out')
    

    

