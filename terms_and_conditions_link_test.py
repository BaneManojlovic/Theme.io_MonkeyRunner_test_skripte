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
while(x<=20):
	x=x+1
	print 'krug:', x
	# klik na link create account
	device.touch(322, 1001, "DOWN_AND_UP")
	MonkeyRunner.sleep(2)
	# klik na link accept Tearms and conditions
	device.touch(396, 1233, "DOWN_AND_UP")
	MonkeyRunner.sleep(2)
	# klik na dugme BACK na telefonu 1 put
	device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(2)
	# klik na dugme BACK na telefonu 2 put
	device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)

	MonkeyRunner.sleep(2)

print('Kraj testa')