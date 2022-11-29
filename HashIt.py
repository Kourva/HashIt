#!/usr/bin/env python3

## Hash your text with this tool
## GITHUB: https://github.com/Izolabela/HashIt

# Imports
import threading
import requests
import time
import sys

# Args
if len(sys.argv) < 2:
    print("\033[1;33mUsage: \033[1;37mHashIt.py \033[1;33m--query=\033[1;37mquery \033[1;33m--method=\033[1;37mmethod \033[1;33m--encode=\033[1;37mencoding")
    print("\033[1;33mWhere:")
    print("\033[1;37m  --query  :\033[1;32m \"your text\"")
    print("\033[1;37m  --method :\033[1;32m md5 | sha256 | sha512")
    print("\033[1;37m  --encode :\033[1;32m hex | base64 | base64url")
    print("\n")
    sys.exit()
else:
    for arg in sys.argv:
        if arg.startswith("--query"):
            query = arg.split("=")[1]
        if arg.startswith("--method"):
            method = arg.split("=")[1]
        if arg.startswith("--encode"):
            encode = arg.split("=")[1]

# Global variable
Progress = True

# Hasjing message
def searching():
    global Progress

    while True:
        for msg in ["\r\033[1;31mHashing *  ", "\r\033[1;31mHashing ** ", "\r\033[1;31mHashing ***"]:
            sys.stdout.write(msg)
            sys.stdout.flush()
            time.sleep(0.5)
        if not Progress:
            print("\r\033[1;33mDone!      \n")
            break

# Hashing progress
def HashIt(query, method, encode):
    response = requests.get(f"https://hashable-api.herokuapp.com/hash?str={query}&method={method}&encoding={encode}")
    return response.text

# Main function
def main():
    global Progress, Result, query, method, encode
    
    print(f"\033[1;37mmethod -> \033[1;32m{method}\033[1;37m  |  encoding -> \033[1;32m{encode}")
    thread = threading.Thread(target= searching)
    thread.start()
    Result = HashIt(query, method, encode)
    Progress = False
    time.sleep(2)
    print(f"\033[1;37mResult ->  \033[1;32m{Result}")

# Run
if __name__ == '__main__':
    main()
