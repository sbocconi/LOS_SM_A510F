#!/bin/bash

# python --version
# Python 3.8.0
python change_mixer.py

# The following is because the output has "value"/> instead of "value" />
# XML-wise it is equivalent but it hampers the diffing of the files
cat mixer_paths_0_python.xml | sed 's/"\/>$/" \/>/g' > mixer_paths_0_proc.xml

# adb --version
# Android Debug Bridge version 1.0.41
# Version 30.0.5-6877874
adb root
adb remount
adb push ./mixer_paths_0_proc.xml /system/vendor/etc/mixer_paths_0.xml
adb reboot