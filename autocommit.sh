#!/bin/bash
git remote set-url origin https://Warot2534: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@github.com/Warot2534/Don-t-Die-ToGetHer.git
git config --global user.email "warmmy171131@gmail.com"
git config --global user.name "Warot2534"
git branch -M main
git push -u origin main
git fetch
git checkout main
git add .
git commit -m "Auto commit at $(date +'%Y-%m-%d %H:%M:%S')"
git push origin main
git pull origin main