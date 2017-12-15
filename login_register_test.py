# Imports
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

device = MonkeyRunner.waitForConnection()
MonkeyRunner.sleep(8)

# Testiranje Log in ekrana
print('Test poceo\n')
MonkeyRunner.sleep(2)

x=0
while(x<10):
	x = x+1
	print 'krug:', x
	# paket, tj. .apk fajl koji se pokrece
	package = 'com.zesium.android.themeio'
	# pocetna aktivnost koja se pokrece
	activity = '.ui.login_and_register.LoginActivity'
	runComponent = package + '/' + activity

	# Pokrece komponentu, tj. aktivnost
	#print(runComponent)
	device.startActivity(component=runComponent)
	MonkeyRunner.sleep(5)

	# klik na Email and Username
	device.touch(518, 423, "DOWN_AND_UP")
	device.type("bane")
	MonkeyRunner.sleep(2)
	# klik na Password
	device.touch(536, 634, "DOWN_AND_UP")
	device.type("BakiMaki2")
	MonkeyRunner.sleep(2)
	# klik na Log in dugme
	device.touch(518, 842, "DOWN_AND_UP")
	MonkeyRunner.sleep(4)
	# klik na dugme BACK na telefonu 1 put
	device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(2)


print('\nTest zavrsen!')