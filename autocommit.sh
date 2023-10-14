#!/bin/bash
git remote add origin https://github.com/Warot2534/Don-t-Die-ToGetHer
git config --global credential.https://github.com.token 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
git config --global user.email "warmmy171131@gmail.com"
git config --global user.name "Warot2534"
git add .
git commit -m "Auto commit at $(date +'%Y-%m-%d %H:%M:%S')"
git push origin main
git pull origin main