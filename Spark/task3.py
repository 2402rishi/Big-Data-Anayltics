from __future__ import print_function
from pyspark import SparkContext
from csv import reader
import sys

if __name__ == "__main__":
    sc = SparkContext()
    parking_lines = sc.textFile(sys.argv[1], 1)
    parking_lines = parking_lines.mapPartitions(lambda x: reader(x)).map(lambda x: '%s,%f'%(x[2],float(x[12])))
    parking_lines=parking_lines.map(lambda x: (x.split(',')[0],float(x.split(',')[1])))
    count=parking_lines.countByKey()
    parking_lines=parking_lines.reduceByKey(lambda x, y: (x+y)).sortByKey(True)
    parking_lines= parking_lines.map( lambda x: '%s\t%.2f, %.2f' % (x[0],x[1], x[1]/count[x[0]]))
    parking_lines.saveAsTextFile('task3.out')
    

    

