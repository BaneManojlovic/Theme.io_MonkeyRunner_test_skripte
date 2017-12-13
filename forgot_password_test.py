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
	# klik na Forgot password link
	device.touch(745, 1005, "DOWN_AND_UP")
	MonkeyRunner.sleep(2)
	# klik na polje Email or Username
	device.touch(527, 925, "DOWN_AND_UP")
	device.type("bane1manojlovic@gmail.com")
	# klik na dugme Send
	device.touch(540, 1076, "DOWN_AND_UP")
	
print('Kraj testa')