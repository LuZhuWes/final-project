import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser( description="" )
parser.add_argument(
    "data_file",
    help="path to the file we want to read",
)
parser.add_argument(
    "xindex",
    type=int,
    help="1-based index of the column containing continuous x-values to plot",
)
parser.add_argument(
    "yindex",
    type=int,
    help="1-based index of the column containing continuous y-values to plot",
)
parser.add_argument(
    "--sindex",
    type=int,
    help="1-based index of the column containing categorical “series” values on which to stratify",
)
args = parser.parse_args( )

fl = open(args.data_file)
a = fl.readline()
if not(args.sindex == None):
    lst = [[float(line.strip().split('\t')[args.xindex-1]),float(line.strip().split('\t')[args.yindex-1]),line.strip().split('\t')[:][args.sindex-1]] for line in fl]


    dic = {}
    for ls in lst:
        if ls[2] in dic.keys():
            dic[ls[2]][0].append(ls[0])
            dic[ls[2]][1].append(ls[1])
        else:
            dic[ls[2]]=[[ls[0]],[ls[1]]]

    plt.figure(1, figsize=(8, 6))
    plt.clf()

    for i in dic.keys():
        plt.scatter(dic[i][0], dic[i][1], label = i)

    plt.legend()
else:
    lst = [[],[]]
    for line in fl:
        lst[0].append(float(line.strip().split('\t')[args.xindex-1]))
        lst[1].append(float(line.strip().split('\t')[args.yindex-1]))
    plt.figure(1, figsize=(8, 6))
    plt.clf()
    plt.scatter(lst[0], lst[1])

plt.xlabel(a.strip().split('\t')[args.xindex-1])
plt.ylabel(a.strip().split('\t')[args.yindex-1])

plt.show()
