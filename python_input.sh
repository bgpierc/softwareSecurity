#!/bin/bash

while getopts ":h" opt; do
  case $opt in
    h)
      echo "Usage: python_input.sh [STRING]" >&2
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done
