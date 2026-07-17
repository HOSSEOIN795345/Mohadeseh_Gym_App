[app]

# نام برنامه
title = Mohadeseh Gym

# نام پکیج (بدون فاصله)
package.name = mohadesehgym

# دامنه سازنده
package.domain = org.mohadeseh

# مسیر اصلی پروژه (جایی که main.py هست)
source.dir = .

# فایل‌های پایتون و منابع
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf

# نسخه برنامه
version = 1.0

# نیازمندی‌ها
requirements = python3,kivy,arabic-reshaper,python-bidi

# حالت صفحه
orientation = portrait

# پشتیبانی اندروید
fullscreen = 0


[buildozer]

# سطح لاگ
log_level = 2

# هشدارهای کمتر
warn_on_root = 1


[android]

# حداقل نسخه اندروید
android.minapi = 23

# نسخه API
android.api = 35

# معماری‌ها
android.archs = arm64-v8a,armeabi-v7a

# قبول لایسنس‌ها
android.accept_sdk_license = True

# NDK سازگار
android.ndk = 25b


# فعال کردن پشتیبانی پایتون
p4a.branch = master


[python-for-android]

# استفاده از SDL2 برای Kivy
android.bootstrap = sdl2
