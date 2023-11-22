#!/bin/bash

/home/andres/workshop/smartFitData/analysis/extractMD5.sh
/home/andres/workshop/smartFitData/analysis/cleanTransfer.sh
/home/andres/workshop/smartFitData/analysis/attendanceSum.sh

cd /home/andres/workshop/smartFitData/analysis/results
./histogram.py
cd "$OLDPWD"
