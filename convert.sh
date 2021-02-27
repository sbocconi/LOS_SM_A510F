#!/bin/bash

python change_mixer.py

# The following is because the output has "value"/> instead of "value" />
# XML-wise it is equivalent but it hampers the diffing of the files
cat mixer_paths_0_python.xml | sed 's/"\/>$/" \/>/g' > mixer_paths_0_proc.xml

adb root
adb remount
adb push ./mixer_paths_0_proc.xml /system/vendor/etc/mixer_paths_0.xml
adb reboot