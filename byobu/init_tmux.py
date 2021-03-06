#!/usr/bin/env python

import subprocess
import os


subprocess.call(['byobu-tmux', 'new-session', '-d', '-s', 'green', '-n', 'run'])
subprocess.call(['byobu-tmux', 'new-session', '-d', '-s', 'red', '-n', 'run'])
subprocess.call(['byobu-tmux', 'new-session', '-d', '-s', 'blue', '-n', 'run'])
subprocess.call(['byobu-tmux', 'new-session', '-d', '-s', 'pink', '-n', 'run'])
subprocess.call(['byobu-tmux', 'new-session', '-d', '-s', 'log', '-n', 'run'])

subprocess.call(['byobu-tmux', 'new-window', '-t', 'green', '-n', 'edit'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'green', '-n', 'git'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'green', '-n', 'search'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'green', '-n', 'test'])

subprocess.call(['byobu-tmux', 'new-window', '-t', 'red', '-n', 'edit'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'red', '-n', 'git'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'red', '-n', 'search'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'red', '-n', 'test'])

subprocess.call(['byobu-tmux', 'new-window', '-t', 'blue', '-n', 'edit'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'blue', '-n', 'git'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'blue', '-n', 'search'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'blue', '-n', 'test'])

subprocess.call(['byobu-tmux', 'new-window', '-t', 'pink', '-n', 'edit'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'pink', '-n', 'git'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'pink', '-n', 'search'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'pink', '-n', 'test'])

# subprocess.call('byobu-tmux send-keys -t log "xrandr --output eDP-1 --off" ENTER', shell=True)
subprocess.call('byobu-tmux send-keys -t log "nohup firefox &" ENTER', shell=True)
subprocess.call('byobu-tmux send-keys -t log "pwd" ENTER', shell=True)

subprocess.call(['byobu-tmux', 'new-window', '-t', 'log', '-n', 'leo'])

subprocess.call(['byobu-tmux', 'new-window', '-t', 'log', '-n', 'vpn'])

subprocess.call(['byobu-tmux', 'new-window', '-t', 'log', '-n', 'search'])
subprocess.call(['byobu-tmux', 'new-window', '-t', 'log', '-n', 'old'])
