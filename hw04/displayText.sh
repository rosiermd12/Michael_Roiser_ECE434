#date: 9/24/2018
#Author: Michael Rosier

#discription:
#this program displays text

SIZE=320x240
TMP_FILE=/tmp/text.png

convert -background lightblue -fill red -font Times-Roman -pointsize 42 \
      -size $SIZE \
      label:'Michael Rosier' \
      -draw "text 100,120 'Hello'" \
      $TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE
