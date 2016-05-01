#!/bin/bash

date_str=`date +%Y-%m-%d`

function usage
{
    echo "usage: mycalendar [[-d 2016-04-01] | [-h]]"
}

while [ "$1" != "" ]; do
    case $1 in
        -d | --date )
            shift
            if [ ! -z "$1" ]; then
                date_str=$1
            fi
            ;;
        -h | --help )
            usage
            exit
            ;;
        * )
            usage
            exit 1
    esac
    shift
done

PYTHON=`which python`
$PYTHON ~/Programming/Python/terminalcalendar/mycalendar.py "$date_str"
