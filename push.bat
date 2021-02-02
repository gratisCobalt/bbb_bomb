@echo off
git init
git add *.*
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/gratisCobalt/bbb_bomb.git
git push -u -f origin main
