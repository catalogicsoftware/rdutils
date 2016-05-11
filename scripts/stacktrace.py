#!/usr/bin/env python

import re
import sys

def collapse_dots(trace):
    if not trace:
        return trace

    newtrace = []
    lastline = None
    for line in trace:
        if (line.find("...") == -1) or (lastline.find("...") == -1):
            newtrace.append(line)
            lastline = line
            continue

    return newtrace

STLINE_PAT = re.compile("^(\s*)at (\S*)\(")

# Change the value to your package prefix. The script will keep lines
# containing classes with that prefix. 
OUR_PKG = "com.example"

stacktrace = []
for line in sys.stdin:
    m = STLINE_PAT.match(line)
    if m:
        class_name = m.group(2)

        if class_name.find(OUR_PKG) != -1 or class_name.find(".") == -1 or not stacktrace:
            stacktrace.append(line)
        else:
            stacktrace.append("        ...\n")

        continue

    if stacktrace:
        for x in collapse_dots(stacktrace):
            print x,

        stacktrace = []

    print line,

if stacktrace:
    for x in collapse_dots(stacktrace):
        print x,

    
    
