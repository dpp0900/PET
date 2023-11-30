#!/bin/bash

touch /tmp/capture.pcap
chmod 777 /tmp/capture.pcap

tshark -i eth0 -f 'tcp port 80' -w /tmp/capture.pcap -F pcap > /dev/null 2>&1