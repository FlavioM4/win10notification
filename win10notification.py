from win10toast import ToastNotifier
import time
from playsound import playsound


def notify(title, desc, dur):
	title = title
	desc = desc
	playsound('beep.wav')
	toaster = ToastNotifier()
	toaster.show_toast(title, desc, duration = dur)

def checkTime(cTime, title, desc, dur):
	cTime = cTime
	title = title
	desc = desc
	dur = dur
	rightTime = time.strftime("%H:%M:%S")
	h = cTime[0:2]
	h1 = rightTime[0:2]
	m = cTime[3:5]
	m1 = rightTime[3:5]
	s = cTime[6:8]
	s1 = rightTime[6:8]
	totalSleep = (int(h) * 3600) + (int(m) * 60) + int(s)
	totalTime = (int(h1) * 3600) + (int(m1) * 60) + int(s1)
	t = totalSleep - totalTime
	print(t, "seconds till the alarm rings!")
	time.sleep(t)
	notify(title, desc, dur)


def inputs():
	chosenTime = input("Choose the time for the notification to be activated (it must be HH:MM:SS): ")
	notificationTitle = input("Choose the desired notification title: ")
	notificationDescription = input("Choose the desired description: ")
	print("Selected time => ", chosenTime)
	print("Selected title => ", notificationTitle)
	print("Selected description => ", notificationDescription)
	checkTime(chosenTime, notificationTitle, notificationDescription, int(notificationTime))


inputs()