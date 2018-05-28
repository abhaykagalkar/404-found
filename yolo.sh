#!/bin/bash
$1
$2
cd darknet-modified &&
python yolotest.py -i $1 -o $2

