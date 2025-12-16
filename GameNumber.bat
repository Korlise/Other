@echo off
set /a num=%random% %% 10+1
:guess
set /p guess=Guess number (1-10)
if %guess% equ %num% goto win
echo Wrong! Try again
goto guess
:win
echo Congratulations!
pause