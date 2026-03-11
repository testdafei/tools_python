# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "10"
caps["deviceName"] = "W4XUT20515002938"
caps["appPackage"] = "com.kmxs.reader"
caps["appActivity"] = "com.km.app.home.view.LoadingActivity"
caps["unicodeKeyboard"] = False
caps["noReset"] = True
caps["newCommandTimeout"] = "6000"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
time.sleep(6)
driver.tap([(357, 1300)])
# el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup[2]")
# el2.click()
time.sleep(5)
# el2.click()
# activity_name = driver.current_activity

driver.quit()