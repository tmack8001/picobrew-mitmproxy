#!/bin/bash

mitmweb --scripts ~/picobrew_firmware_force.py --mode transparent --web-port 9090 --web-host 0.0.0.0 &>> /var/log/mitmweb.log