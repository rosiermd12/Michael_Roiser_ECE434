
# Beaglebone PCSX rearmed console -----------------------

this directory consist of all the code needed to setup and run PCSX reARMed 
on the Beaglebone black (should also work with Beaglebone Green with HDMI
cape) with a bluetooth dongle to read a Playstation 3 controller via bluetooth
and a cd drive to read, convert, and run the content on PS1 game cds.

	equipment used:
	
	cd drive	    https://www.amazon.com/gp/product/B00Y82T6SI/ref=oh_aui_detailpage_o01_s01?ie=UTF8&psc=1
	bluetooth dongle    https://www.amazon.com/gp/product/B009ZIILLI/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1 
	Beaglebone black
	Powered 4-port USB hub
	PS3 controller (not third party)
	HDMI mini to HDMI converter
	HDMI cable
	8GB microSD card

# Setup -------------------------------------------------
for set up just run "setup.sh" and then everything should be downloaded and
boot up at start up.

# Instructions ------------------------------------------

first you need to pair your PS3 controller:
	to do this you should have your ps3 controller connect to your
	beaglebone black before start up. When the beaglebone leds start
	blinking at a constant rate, the controller is paired. for the 
	beaglebone to reconize this change, you have to restart the system. 

configureing controls for PCSX reARMed:
	run the console with no cd in the cd drive. A menu should pop up with
	PCSX shown in the background. using the left ANALOG STICK, SELECT, 
	and L3 to navigate the menu screen, select controls > player1 and edit
	each button by using SELECT and a button on your ps3 controller you
	want to bind it to. exit PCSX and reset the system with a game in the
	cd drive.

running games:
	the way that this console runs games is by checking if you have the 
	inserted PS1 game on your beaglebone. if not, then your beaglebone
	will download and convert to a bin/cue file. (NOTICE: this download 
	will take a few munites to finish so don't panic if you don't see 
	anything on screen for a while). once done downloading the game should
	pop up on your connected screen. 

things to note:
	if you have changed your beaglebone's password, then just make sure
	you do the same for the run.sh file.	 
	  

