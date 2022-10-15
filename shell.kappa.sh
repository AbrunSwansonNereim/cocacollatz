#!/bin/sh

i_set=`seq 1 10`

for i in ${i_set}
do

d=$(( 2**${i} ))
n_set=`seq 1 2 ${d}`
for n in ${n_set}
do

    kappa=`./q.kappa.py ${n} ${d}`
    echo "${n} ${d} ${kappa}" # >> kappa.dat

done

done