#!/bin/bash
# add reversed sequence of images

cd video

# count the number of frames
for ((j=0; j<100000; j++)); do
  printf -v n "%04d" $j
  [[ ! -e "file$n.png" ]] && break
done
echo $j original images

p=${1:-20}
printf -v s "file%04d.png" $((j-1))
for ((k=j; k<j+p; k++)); do
  printf -v d "file%04d.png" $k
  cp $s $d
done
echo "added a $p frame pause, frames $j to $((k-1))"

for ((m=k; m<k+j; m++)); do
  printf -v s "file%04d.png" $((j+j+p-m-1))
  printf -v d "file%04d.png" $m
  cp $s $d
done
echo "added a reverse sequence, frames $k to $((m-1))"
