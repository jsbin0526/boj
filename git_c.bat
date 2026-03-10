@echo off
SET /A n=%1
git.exe add %n%.c
git.exe commit -m "%n%"
git.exe push
exit