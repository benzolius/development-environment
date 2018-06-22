#!/usr/bin/env python

import subprocess
import os


subprocess.call(['byobu-tmux', 'new-session', '-d', '-s', 'green', '-n', 'run'])
subprocess.call(['byobu-tmux', 'new-session', '-d', '-s', 'red', '-n', 'run'])
subprocess.call(['byobu-tmux', 'new-session', '-d', '-s', 'blue', '-n', 'run'])
subprocess.call(['byobu-tmux', 'new-session', '-d', '-s', 'log', '-n', 'general'])

subprocess.call(['byobu-tmux', 'new-window', '-t', 'green', '-n', 'edit'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'green', '-n', 'git'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'green', '-n', 'test'])

subprocess.call(['byobu-tmux', 'new-window', '-t', 'red', '-n', 'edit'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'red', '-n', 'git'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'red', '-n', 'test'])

subprocess.call(['byobu-tmux', 'new-window', '-t', 'blue', '-n', 'edit'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'blue', '-n', 'git'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'blue', '-n', 'test'])

# subprocess.call('byobu-tmux send-keys -t log "xrandr --output eDP-1 --off" ENTER', shell=True)
subprocess.call('byobu-tmux send-keys -t log "setxkbmap -layout us" ENTER', shell=True)
subprocess.call('byobu-tmux send-keys -t log "setxkbmap -variant norman -option misc:extend,lv5:caps_switch_lock" ENTER', shell=True)
subprocess.call('byobu-tmux send-keys -t log "nohup firefox &" ENTER', shell=True)
subprocess.call('byobu-tmux send-keys -t log "nohup thunderbird &" ENTER', shell=True)

subprocess.call(['byobu-tmux', 'new-window', '-t', 'log', '-n', 'leo'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'log', '-n', 'vpn'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'log', '-n', 'history'])

# subprocess.call('byobu-tmux send-keys -t log "mkdir /dev/shm/ramdisk1" ENTER', shell=True)
# subprocess.call('byobu-tmux send-keys -t log "ln -s /dev/shm/ramdisk1 /ramdisk/ramdisk1" ENTER', shell=True)
