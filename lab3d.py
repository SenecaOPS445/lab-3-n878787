#!/usr/bin/env python3



# Author ID: nrihani

import subprocess

def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    return output.decode('utf-8').strip()

if __name__ == "__main__":
    print(free_space())
