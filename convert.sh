#!/bin/bash

is_dryrun=n
do_mic1=n
do_mic2=n

while getopts "a:b:dt" options
do
    case "${options}" in
        a)
            re_isanum='^[0-9]+$'
            if ! [[ ${OPTARG} =~ $re_isanum ]]
            then
                echo "Error: gain must be a positive, whole number."
                exit 1
            fi
            mic1_gain=${OPTARG}
            do_mic1=y
        ;;
        
        b)
            re_isanum='^[0-9]+$'
            if ! [[ ${OPTARG} =~ $re_isanum ]]
            then
                echo "Error: gain must be a positive, whole number."
                exit 1
            fi
            mic2_gain=${OPTARG}
            do_mic2=y
        ;;
        d)
            do_diff=y
        ;;
        t)
            is_dryrun=y
        ;;
        :)
            echo "Error: -${OPTARG} requires an argument."
            exit 1
        ;;
        *)
            exit 1
        ;;
    esac
done

# python --version
# Python 3.8.0
params=""
if [ "${do_mic1} " == 'y ' ]
then
    params="${params} --mic1_gain ${mic1_gain}"
fi

if [ "${do_mic2} " == 'y ' ]
then
    params="${params} --mic2_gain ${mic2_gain}"
fi

python change_mixer.py ${params}

orig_file=mixer_paths_0.xml
py_file=mixer_paths_0_python.xml
proc_file=mixer_paths_0_proc.xml

# The following is because the output has "value"/> instead of "value" />
# XML-wise it is equivalent but it hampers the diffing of the files
cat ${py_file} | sed 's/"\/>$/" \/>/g' > ${proc_file}

if [ "${do_diff} " == 'y ' ]
then
    diff ${orig_file} ${proc_file} | more
fi

# adb --version
# Android Debug Bridge version 1.0.41
# Version 30.0.5-6877874
if [ "${is_dryrun} " != 'y ' ]
then
    echo "Pushing file to phone"
    adb root
    adb remount
    adb push ./mixer_paths_0_proc.xml /system/vendor/etc/mixer_paths_0.xml
    adb reboot
else
    echo "Not pushing file to phone"
fi