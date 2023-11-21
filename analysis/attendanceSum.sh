#!/bin/bash

#sed 's/#.*//' < pruned/mix_2022-08-16T12\:02\:06-06\:00.tsv | grep -Ev '^$' | awk '{sum+=$4} END {print sum}'
#sed 's/#.*//' < pruned/mix_2022-08-16T12\:02\:06-06\:00.tsv | grep -Ev '^$' | head -n 1 | awk '{ print strftime("%Y/%m/%d" , $2) }'

#Mix
rm -f "/home/andres/workshop/smartFitData/analysis/results/attendanceMix.tsv"

for file in /home/andres/workshop/smartFitData/analysis/pruned/mix*
do
	dateStamp=$(sed 's/#.*//' < $file | grep -Ev '^$' | head -n 1 | awk '{ print strftime("%Y-%m-%d" , $2) }')
	year=$(date -d $dateStamp +%G)
	dayOfTheWeek=$(date -d $dateStamp +%u)
	weekTemp=$(date -d $dateStamp +%-V)
	weekOfTheYear=$(( $weekTemp + 100 * ($year  - 2022 ) ))
	#weekOfTheYear=$(date -d $dateStamp +%V)
	sumData=$(sed 's/#.*//' < $file | grep -Ev '^$' | awk '{sum+=$4} END {print sum}')
	#Solo datos de 13 a 15
	#sumData=$(sed 's/#.*//' < $file | grep -Ev '^$' | head -n 12 | tail -n 3 | awk '{sum+=$4} END {print sum}')
	printf "%s\t%s\t%s\t%s\n" $dateStamp $dayOfTheWeek $sumData $weekOfTheYear >> "/home/andres/workshop/smartFitData/analysis/results/attendanceMix.tsv"
done

#Tikal
rm -f "/home/andres/workshop/smartFitData/analysis/results/attendanceTikal.tsv"

for file in /home/andres/workshop/smartFitData/analysis/pruned/tikal*
do
	dateStamp=$(sed 's/#.*//' < $file | grep -Ev '^$' | head -n 1 | awk '{ print strftime("%Y-%m-%d" , $2) }')
	dayOfTheWeek=$(date -d $dateStamp +%u)
	weekOfTheYear=$(date -d $dateStamp +%V)
	sumData=$(sed 's/#.*//' < $file | grep -Ev '^$' | awk '{sum+=$4} END {print sum}')
	printf "%s\t%s\t%s\t%s\n" $dateStamp $dayOfTheWeek $sumData $weekOfTheYear >> "/home/andres/workshop/smartFitData/analysis/results/attendanceTikal.tsv"
done
