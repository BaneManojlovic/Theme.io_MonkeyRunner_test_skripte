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

# Testiranje Log in ekrana
print('Test poceo\n')
MonkeyRunner.sleep(2)

device.touch(523, 453, "DOWN_AND_UP")
device.type("bane")
device.touch(544, 657, "DOWN_AND_UP")
device.type("BakiMaki")
device.touch(523, 843, "DOWN_AND_UP")
MonkeyRunner.sleep(3)


print('\nTest zavrsen!')