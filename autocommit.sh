#!/bin/bash

git add .
git commit -m "Auto commit at $(date +'%Y-%m-%d %H:%M:%S')"
git push origin main
git pull origin main