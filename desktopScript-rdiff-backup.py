import time
import os
import datetime
os.system("cls")
def main():
	lineBreak()
	print " |                            Raspberry Pi Backup                             |"
	lineBreak()
	print " +  Before you backup, it is wise to ensure you're not downloading, uploading +"
	print " +  or transferring to/from the RPi. Doing any of those during backup         +"
	print " +  will give you a very slow experience. This is because of the bandwidth    +"
	print " +  limitations that the RPi has when using USB & Ethernet together.          +"
	lineBreak()
	x = raw_input("    Do you wish to backup right now? (y/n): ")
	while x.upper() != "Y" and x.upper() != "N":
		x = raw_input("    Please enter y or n: ")
	lineBreak()
	if x.upper() == "Y":
		print "    Checking if RPi is online...""
		ping = testConnection()
		if ping == 0:
			print '    Connection OK, initiating backup...'
			finishTime = rdiffbackup()
		else:
			print "    Can not establish connection to RPi, quitting..."
	else:
		print "    OK, will try again tomorrow."
	print("Total time: " + str(finishTime))
	deleteOld()
	time.sleep(5)
			
def lineBreak():
	print " +----------------------------------------------------------------------------+"			

def testConnection();
	ping = os.system('powershell.exe "Test-Connection -q 192.168.0.5 | Out-Null"')
	return ping
	
def rdiffbackup();
	startTime = datetime.datetime.now()
	os.system('rdiff-backup --terminal-verbosity=5 --remote-schema "ssh %s -p1019 rdiff-backup --server" C:/Users/Adam/Dropbox username@domain.com::/path/to/directory')
	finishTime = datetime.datetime.now() - startTime
	return finishTime

def deleteOld();
	print("Deleting old archives...")
	os.system('rdiff-backup --remove-older-than 2W --remote-schema "ssh %s -p1019 rdiff-backup --server" username@domain.com::/path/to/directory')
	print("Completed")
	
main()