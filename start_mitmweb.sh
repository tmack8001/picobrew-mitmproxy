#!/bin/bash

mitmweb --scripts ~/picobrew_intercept.py --mode transparent --web-port 9090 --web-host 0.0.0.0 &>> /var/log/mitmweb.log
#mitmweb --scripts ~/picobrew_firmware_force.py --mode transparent --web-port 9090 --web-host 0.0.0.0 &>> /var/log/mitmweb.log
