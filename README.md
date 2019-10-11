# Multibrot video generator

This is the python script for generating the multibrot images
as a sequence of png files. A Python 3 script requiring the
installation of the "numpy" and "pillow" libraries.
Tested on Ubuntu -- and uses a Linux font that will need to be
changed to something else if used on Windows:

**multibrot-make-images.py**

Bash script to add the reversed sequence to the images, created
from the existing images:

**add-reverse.sh**

Bash script uses ImageMagick's "convert" to add credits to the
end of the image sequence:

**add-credits.sh**

Not included here. CC by 3.0 licensed music file..
Find this file by web-searching with something like:
"Kevin Macleod Frozen Star free mp3 download":

**Frozen_Star.mp3**

Bash script to convert png image sequence to mp4 video and adds
music file.  Requires "ffmpeg" to make the mp4 video:

**make-vid.sh**
