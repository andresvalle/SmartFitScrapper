#!/bin/bash
find ~/workshop/smartFitData/dumpSmartFit -type f -exec sed -n '$p' {} \; -printf "\n" | sort -u > ~/workshop/smartFitData/analysis/md5sums.txt
