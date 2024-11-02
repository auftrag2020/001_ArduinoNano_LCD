@echo off
@REM cls

echo.
echo.
echo **********************************************************************************************
echo **********************************************************************************************
echo **                                                                                          **
echo **                                                                                          **
echo **                                     Rebuild Project                                      **
echo **                                                                                          **
echo **                                                                                          **
echo **********************************************************************************************
echo **********************************************************************************************


@echo off
setlocal

REM Get the directory of the batch file
set SCRIPT_DIR=%~dp0

REM Run the Python script with the provided argument
python "%SCRIPT_DIR%\swBuild\pyScript\main.py" %1

endlocal
