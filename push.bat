@echo off
git init
git add *.*
git commit -m "just another commit"
git branch -M main
git push -u -f origin main
