from __future__ import print_function
from pyspark import SparkContext
from csv import reader
import sys

if __name__ == "__main__":
    sc = SparkContext()
    parking_lines = sc.textFile(sys.argv[1], 1)
    parking_lines = parking_lines.mapPartitions(lambda x: reader(x)).map(lambda x: ('%s, %s'%(x[14],x[16]),1))
    parking_lines=parking_lines.reduceByKey(lambda x, y: (x+y))
    parking_lines=parking_lines.takeOrdered(20, key = lambda x: -x[1])
    parking_lines=sc.parallelize(parking_lines)
    parking_lines=parking_lines.map(lambda x : '%s\t%s' % (x[0],x[1]))
    parking_lines.saveAsTextFile('task6.out')
    

    

