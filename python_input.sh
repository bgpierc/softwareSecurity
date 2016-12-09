#!/bin/bash

while getopts ":h:r" opt; do
  case $opt in
    h)
      echo "Usage: python_input.sh -r [INPUT]" >&2
      ;;
    r)
      python python_to_write_python.py $2
      python newpython.py
      ;;
    \?)
      echo "Invalid option:" >&2
      ;;
  esac
done

