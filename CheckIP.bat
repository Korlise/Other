@echo off
set /p ip=enter IP for checking: 
for /l %%p in (1,1,100) do (
  timeout /t 1 > nul
  echo Scanning port %%p...
  telnet %ip% %%p 2>nul && echo Port %%p open
)
pause