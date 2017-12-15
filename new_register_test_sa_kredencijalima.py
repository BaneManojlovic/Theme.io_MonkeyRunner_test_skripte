# Imports
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

device = MonkeyRunner.waitForConnection()
MonkeyRunner.sleep(8)

# paket, tj. .apk fajl koji se pokrece
package = 'com.zesium.android.themeio'
# pocetna aktivnost koja se pokrece
activity = '.ui.login_and_register.LoginActivity'
runComponent = package + '/' + activity

# Pokrece komponentu, tj. aktivnost
print(runComponent)
device.startActivity(component=runComponent)
MonkeyRunner.sleep(5)

# Testiranje Create account ekrana
print('Test poceo\n')
MonkeyRunner.sleep(2)

x=0
while(x<10):
	x = x+1
	print 'krug:', x
	# klik na Link Create account
	device.touch(289, 1005, "DOWN_AND_UP")
	MonkeyRunner.sleep(2)
	# klik na Username
	device.touch(532, 460, "DOWN_AND_UP")
	device.type("TestTest")
	MonkeyRunner.sleep(2)
	# klik na dugme BACK na telefonu 1 put
	device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(2)
	# klik na Email
	device.touch(519, 653, "DOWN_AND_UP")
	device.type("testtest@gmail.com")
	MonkeyRunner.sleep(2)
	# klik na dugme BACK na telefonu 1 put
	device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(2)
	# klik na Password
	device.touch(532, 854, "DOWN_AND_UP")
	device.type("testtest")
	MonkeyRunner.sleep(2)
	# klik na dugme BACK na telefonu 1 put
	device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(2)
	# klik na repeat password
	device.touch(519, 1042, "DOWN_AND_UP")
	device.type("testtest")
	MonkeyRunner.sleep(2)
	# klik na dugme BACK na telefonu 1 put
	device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(2)
	# klik na button za stikliranje terms and conditions 
	device.touch(297, 1228, "DOWN_AND_UP")
	MonkeyRunner.sleep(2)
	# klik na dugme Register
	#device.touch(536, 1400, "DOWN_AND_UP")
	MonkeyRunner.sleep(2)
	# klik na dugme BACK na telefonu 1 put
	device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(2)

print('Test zavrsio')