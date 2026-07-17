[app]

# (str) Title of your application
title = Mohadeseh Gym

# (str) Package name
package.name = mohadesehgym

# (str) Package domain
package.domain = org.mohadeseh

# (str) Source code directory
source.dir = Mohadeseh_Gym_App

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,json,ttf,atlas

# (str) Application version
version = 1.0

# (list) Requirements
requirements = python3,kivy

# (str) Orientation
orientation = portrait

# (bool) Allow fullscreen
fullscreen = 0


# (list) Permissions
android.permissions = INTERNET


# (str) Icon
# icon.filename = %(source.dir)s/icon.png


# (list) Supported architectures
android.archs = arm64-v8a, armeabi-v7a


# (bool) AndroidX
android.enable_androidx = True


# (str) Android API
android.api = 35

# (str) Minimum API
android.minapi = 24


# (str) NDK version
android.ndk = 27c


# (bool) Copy libs
android.copy_libs = 1


# (str) Bootstrap
p4a.bootstrap = sdl2


# (bool) Warn about private storage
android.private_storage = True


# (str) Log level
log_level = 2


[buildozer]

# (int) Log level
log_level = 2

# (str) Warn if running as root
warn_on_root = 1
