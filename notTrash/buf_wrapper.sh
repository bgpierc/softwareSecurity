#!/bin/bash

while getopts ":h:r" opt; do
  case $opt in
    h)
      echo "Usage: python_input.sh -r [INPUT]" >&2
      ;;
    r)
      bash corec.sh
      bash wrapper.sh debugGdb.py
      python3 hackprogram.py
      ;;
    \?)
      echo "Invalid option:" >&2
      ;;
  esac
done

