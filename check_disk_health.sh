#!/bin/bash
DATE=`date +%Y-%m-%d`
OUT="disk_health_info_$DATE.txt"

echo "Getting SDA smart info..." >& $OUT
sudo smartctl -H --all /dev/sda >> $OUT
echo "Getting SDB smart info..." >> $OUT
sudo smartctl -H --all /dev/sdb >> $OUT
echo "Getting SDC smart info..." >> $OUT
sudo smartctl -H --all /dev/sdc >> $OUT
