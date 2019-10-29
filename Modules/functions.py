#! /usr/bin/env python3
""" functions for VirtualHerbarium"""
import csv
import sys
import settings as st
from collections import OrderedDict

def getInputAsDictionary(inputPath, colName=st.colName):
    """read csv file and output a standard dictionary performing some checks"""
    with open(inputPath) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        finalDic = list()
        #test if input is good
        for row in csv_reader:
            try:
                row[colName]
            except KeyError:
                print("no PlantName column in input file %s" % inputPath)
                return
            assert(row[colName] != ""), "missing p§lant name!"
            # transform output to standard dictionary
            normalDic=dict(OrderedDict(row))
            finalDic.append(normalDic)
        return(finalDic)

if __name__ == "__main__":
    print(getInputAsDictionary(st.inputPath, colName=st.colName))
