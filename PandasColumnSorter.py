#!/usr/bin/python

import sys
import getopt
import pandas as pd
from pandas import DataFrame


class dataFrameMaker:
    def __init__(self):
        self.inFile = ""
        self.df = ""
    def putFile(self, inFile):
        self.inFile = inFile
    def makeDataFrame(self, **kwargs):
        sHeader = kwargs["Header"]
        sSeperator = kwargs["Sep"]
        if sHeader == True:
            self.df = pd.read_csv(self.inFile, sep=sSeperator)
        else:
            self.df = pd.read_csv(self.inFile, sep=sSeperator, header=None)
    def printDataFrame(self):
        print(self.df.to_string(index=False))
    def sortDataFrame(self, **kwargs):
        fGroupFile = kwargs["groupfile"]
        lOrder = []
        with open(fGroupFile,'r') as fr:
            for line in fr:
                lOrder.append(line.strip())
        self.df = self.df[lOrder]
#end: class



if __name__ == "__main__":
    if len(sys.argv) < 7:
        print("#usage: python3 %s -f <txt> -H [true, false] -S [csv, tsv, space]" % sys.argv[0])
        print("Optional arguments:")
        print("  -G <sorting.group.txt>")
        sys.exit()

    opts, args = getopt.getopt(sys.argv[1:], 'f:H:S:G:')

    dOpt = {"file":"", "Header":"", "Separator":"", "groupfile":""}

    for op, p in opts:
        if op == "-f":
            dOpt["file"] = p
        elif op == "-H":
            if p.upper() == "TRUE": dOpt["Header"] = True
            elif p.upper() == "FALSE": dOpt["Header"] = False
            else: print("-H option is not valid. Select between [true or false]");sys.exit()
        elif op == "-S":
            if p.upper() == "CSV": dOpt["Separator"] = ","
            elif p.upper() == "TSV": dOpt["Separator"] = "\t"
            elif p.upper() == "SPACE": dOpt["Separator"] = " "
            else: print("-S option is not valid. Select between [csv or tsv or space]");sys.exit()
        elif op == "-G":
            dOpt["groupfile"] = p
        else:
            print('unknown option',op)
            sys.exit()

    inFile = dOpt["file"]
    cDataFrameMaker = dataFrameMaker()
    cDataFrameMaker.putFile(inFile)
    cDataFrameMaker.makeDataFrame(Header=dOpt["Header"], Sep=dOpt["Separator"])
    if len(dOpt["groupfile"]) != 0:
        cDataFrameMaker.sortDataFrame(groupfile=dOpt["groupfile"])
    cDataFrameMaker.printDataFrame()
#end: if
