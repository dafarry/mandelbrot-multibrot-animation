#!/bin/bash
# add end credits

txt='Graphics by Dave Farrance  (CC BY 3.0)\n\n
Music "Frozen Star" by Kevin MacLeod  (CC BY 3.0)\n\n
Creative Commons Attribution 3.0 Unported license'

cd video

# count the number of frames
for ((j=0; j<100000; j++)); do
  printf -v n "file%04d.png" $j
  [[ ! -e "$n" ]] && break
done
echo $j original images

echo "new image: $n"

read w h < <(identify -format "%w %h" file0000.png)

echo "width: $w   height: $h"

# create credit frame
convert -size "${w}x${h}" -pointsize $(( w / 35 )) \
  -background black -fill white -gravity center \
  -font DejaVu-Sans caption:"$txt" "$n"

p=75 # copy to create p credit frames
for ((k=j+1; k<j+p; k++)); do
  printf -v d "file%04d.png" $k
  cp $n $d
done
echo "added $p frame credits, frames $j to $((k-1))"
