#! /bin/sh

sudo apt install libsdl1.2-dev
sudo apt install libsdl2-dev
sudo apt install oss4-dev
sudo apt install cdrdao
sudo apt install bluez
sudo apt install checkinstall
sudo apt install libusb-dev
sudo apt install libbluetooth-dev
sudo apt install libpng-dev

#setting up pcsx-rearmed
mkdir ~/pixbox-pcsx-rearmed
git clone httpshttps://github.com/alban-rochel/pixbox-pcsx-rearmed ~/pixbox-pcsx-rearmed

#---------patch files------------
cd ./pcsx_patches
cp MENU.patch configure.patch ~/pixbox-pcsx-rearmed
cd -
cd ~/pixbox-pcsx-rearmed

patch < MENU.patch
patch < configure.patch
#--------------------------------

chmod +x configure
./configure
make

cd -

#setting up dualshock 3 bluetooth support

cd ~
wget http://www.pabr.org/sixlinux/sixpair.c 
gcc -o sixpair sixpair.c -lusb

wget http://sourceforge.net/projects/qtsixa/files/QtSixA%201.5.1/QtSixA-1.5.1-src.tar.gz
tar xfvz QtSixA-1.5.1-src.tar.gz

cd -
cd bluetooth_patches
#------patch files---------
cp -a ./ ~/QtSixA-1.5.1/sixad
cd -
cd ~/QtSixA-1.5.1/sixad
patch < uinput.patch
patch < sixad-bin.patch
patch < bluetooth.patch
patch < remote.patch
patch < shared.patch
patch < sixad-3in1.patch
patch < sixad-raw.patch
patch < sixad-sixaxis.patch
patch < sixaxis.patch
patch < textfile.patch
patch < sixad-remote.patch
#--------------------------
make
sudo mkdir -p /var/lib/sixad/profiles
sudo checkinstall

cd -

#copy over gamerip file
cp gamerip ~/
cd ~
chmod +x gamerip
cd -

#set to run during boot time
sixad --boot-yes

cp run.sh /usr/bin
cp systemd_pcsx.service /lib/systemd

cd /etc/systemd/system/
ln /lib/systemd/systemd_pcsx.service systemd_pcsx.service

systemctl daemon-reload

sudo reboot

