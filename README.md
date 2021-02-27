# Introduction
Scripts to manipulate mic settings for Samsung A5 running LineageOS

After I installed LineageOS 17.1 people could not hear my voice well when using the headset with for examle Whatsapp, Signal, Telegram and Skype.
I have seen the this is a common problem but I could not find any practical way to solve it, so I have written some script that automatically change the volume and possibly boost settings on my phone.

# Usage
`python change_mixer.py`
The python script look for the setting with name `MIC1 Volume` and `MIC2 Volume` and multiply the value by a defined constant. I got some results with 7
The script can also increase the boost but this led to distorsion

The shell script `convert.sh` does some corrections to the python output to aid diffing the files, copy the file to the phone (which should be connected via USB with debugging on) and reboots it.

# Remarks

I was trying to find a guide that would explain which settings to change, but I could not find any. I also saw that the LineageOS provided file was the same as the stock Samsung file. I decided to experiment quickly by changing all values, and that was impossible to do manually, that is why I wrote these scripts.

Ideally the script would target particular settings, but I have not had the time not the knowledge yet to see what settings to target

