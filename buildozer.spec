[app]

# نام برنامه
title = Mohadeseh Gym App

# نام پکیج (بدون فاصله)
package.name = mohadesehgym

# دامنه پکیج
package.domain = org.mohadeseh

# نسخه برنامه
version = 1.0

# فایل اصلی برنامه
source.main = main.py

# پوشه پروژه
source.dir = .

# فایل‌هایی که باید داخل APK باشند
source.include_exts = py,png,jpg,jpeg,kv,json,ttf,txt

# نیازمندی‌ها
requirements = python3,kivy,arabic-reshaper,python-bidi

# جهت صفحه
orientation = portrait

# اجازه دسترسی فایل‌ها
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# تنظیمات اندروید
android.api = 35
android.minapi = 23

# معماری‌ها
android.archs = arm64-v8a,armeabi-v7a

# نام خروجی
android.entrypoint = org.kivy.android.PythonActivity


[buildozer]

# لاگ ساخت
log_level = 2
