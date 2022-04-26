#!/bin/bash

# Store the number of lines of the file
lines=$(wc -l < $1)

if [[ $lines -lt 10001 ]]
then
    echo Error : The input file must a least have 10000 lines.
    exit 1
fi

echo $lines
echo $(head -n 1 $1)
echo $(tail -10000 $1 | grep -ic 'potus') 
echo $(sed -n '100,200p' $1 | grep -c 'fake')




