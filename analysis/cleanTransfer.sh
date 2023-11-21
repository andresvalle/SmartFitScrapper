#!/bin/bash

for line in $(cat ~/workshop/smartFitData/analysis/md5sums.txt); 
do
	#echo "$line"
	oldestFile=$(grep -Rl "$line" ~/workshop/smartFitData/dumpSmartFit | xargs stat -c '%Y %n'| sort | cut -d " " -f2 | head -1)
	#echo "$oldestFile"
	cp "$oldestFile" "/home/andres/workshop/smartFitData/analysis/pruned/"
done

#ls -t ~/workshop/smartFitData/dumpSmartFit | grep -Rl "#00f02a7c6f3ced3bbeafd261f155a626" | xargs stat -c '%Y %n'| sort | cut -d " " -f2 | head -1
