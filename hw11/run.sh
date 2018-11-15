#!/bin/bash

pass="temppwd"

for sysdevpath in $(find /sys/bus/usb/devices/usb*/ -name dev); do
    (
        syspath="${sysdevpath%/dev}"
        devname="$(udevadm info -q name -p $syspath)"
        [[ "$devname" == "bus/"* ]] && continue
        eval "$(udevadm info -q property --export -p $syspath)"
        if [[ "$ID_SERIAL" == "Sony_PLAYSTATION_R_3_Controller" ]]; then 
	  echo "$pass" | sudo -S  ~/sixpair
	fi
    )
done

connect=$(hcitool con)

while [ "$connect" == "Connections:" ]; do
 connect=$(hcitool con)
done

sleep 5

blkid /dev/sr0

sleep 1

cdrom=$(echo $?)
echo "$cdrom"

if [ "$cdrom" == "0" ]; then
 id=$(cd-discid)
 name=${id// /_}
 echo "$name"
 cd ~/psxrip
 if [ $(find "$name".cue | wc -l) -gt 0 ]; then
   echo "$pass" | sudo -S PCSX_WIDTH=600 ~/pixbox-pcsx-rearmed/pcsx -cdfile ~/psxrip/"$name".cue
 else 
   ~/gamerip "$name"
   echo "$pass" | sudo -S PCSX_WIDTH=600 ~/pixbox-pcsx-rearmed/pcsx -cdfile ~/psxrip/"$name".cue
 fi
else
  echo "$pass" | sudo -S PCSX_WIDTH=600 ~/pixbox-pcsx-rearmed/pcsx
fi


