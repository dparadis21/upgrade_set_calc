#!/bin/bash
python /home/mike/Documents/upgrade_set_calc/update.py /home/mike/Documents/upgrade_set_calc/sets > /home/mike/Documents/upgrade_set_calc/.tmp
cat /home/mike/Documents/upgrade_set_calc/.tmp > /home/mike/Documents/upgrade_set_calc/current_prices
rm /home/mike/Documents/upgrade_set_calc/.tmp
