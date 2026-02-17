@echo off

pushd "MOD_files"
call "%NEURONHOME%\bin\mknrndll.bat"
echo.
del "*.tmp" "*.c" "*.o" 2>nul
move nrnmech.dll "..\"
popd
echo.
pause