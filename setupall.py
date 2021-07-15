from SDL_DS3231 import SDL_DS3231 as RTC
rtc=RTC()
print("Before setting")
print(rtc.read_all())

rtc.write_now()
print("After setting")
print(rtc.read_all())