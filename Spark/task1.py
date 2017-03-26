from __future__ import print_function
from pyspark import SparkContext
from csv import reader
import sys

if __name__ == "__main__":
    sc = SparkContext()
    parking_lines = sc.textFile(sys.argv[1], 1)
    open_lines=sc.textFile(sys.argv[2],1)
    parking_lines = parking_lines.mapPartitions(lambda x: reader(x)).map(lambda x: (x[0],x))
    open_lines=open_lines.mapPartitions(lambda x: reader(x)).map(lambda x: (x[0],x))
    result=parking_lines.subtractByKey(open_lines)
    result=result.map(lambda x: '%s\t%s, %s, %s, %s' %(x[1][0], x[1][14], x[1][6], x[1][2], x[1][1]))
    #parking_lines=parking_lines.map(lambda x: list(reader(x.split('\t')[1])))
    #.map(lambda x: '%s\t%s, %s, %s, %s' % (x[0],x[15],x[7],x[3],x[2]))
    result.saveAsTextFile('task1.out')
    

    
