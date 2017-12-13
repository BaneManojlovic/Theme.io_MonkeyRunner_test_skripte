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


# klik na Link Create account
device.touch(289, 1005, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
# klik na Username
device.touch(532, 460, "DOWN_AND_UP")
# klik na Email
device.touch(519, 653, "DOWN_AND_UP")
# klik na Password
device.touch(532, 854, "DOWN_AND_UP")
# klik na repeat password
device.touch(519, 1042, "DOWN_AND_UP")
# klik na dugme DONE na tastaturi za unios karaktera
device.touch(933, 1595, "DOWN_AND_UP")
# klik na dugme Register
device.touch(511, 1235, "DOWN_AND_UP")

