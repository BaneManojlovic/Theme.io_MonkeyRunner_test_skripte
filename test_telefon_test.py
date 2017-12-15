# Imports
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

device = MonkeyRunner.waitForConnection()
MonkeyRunner.sleep(8)
print('Test poceo\n')
# klik na dugme back na telefonu!!!
device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)

# klik na dugme meny na telefonu!
#device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)

#device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
#MonkeyRunner.sleep(2)

#device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
#MonkeyRunner.sleep(2)

print('Test zavrsen.')