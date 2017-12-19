# Imports
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

device = MonkeyRunner.waitForConnection()
MonkeyRunner.sleep(8)

# paket, tj. .apk fajl koji se pokrece
package = 'com.zesium.android.themeio'
# pocetna aktivnost koja se pokrece
activity = '.ui.login_and_register.LoginActivity'
runComponent = package + '/' + activity

# Testiranje Create account ekrana
print('Test poceo\n')
MonkeyRunner.sleep(2)
	
x=0
while(x<10):
	x = x+1
	print 'krug:', x
	
	# Pokrece komponentu, tj. aktivnost
	print(runComponent)
	device.startActivity(component=runComponent)
	MonkeyRunner.sleep(5)

	#klik na Login via Google dugme
	#device.touch(526, 1261, "DOWN_AND_UP")
	device.touch(508, 1323, "DOWN_AND_UP")
	MonkeyRunner.sleep(8)
	# klik na potvrdu korisnickog Google profila
	device.touch(423, 936, "DOWN_AND_UP")
	MonkeyRunner.sleep(8)
	# klik na dugme back na telefonu!!!
	device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(2)

print('\nTest zavrsen.')