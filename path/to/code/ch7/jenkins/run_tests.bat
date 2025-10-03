@echo off
REM ================================
REM Windows batch script using Git checkout
REM ================================

REM Project and test directories inside the workspace
set tasks_proj_dir=%WORKSPACE%\ch7\tasks_proj_v2
set start_tests_dir=%tasks_proj_dir%\tests
set results_dir=%WORKSPACE%

REM Activate virtual environment (if you have one inside workspace)
call %WORKSPACE%\venv\Scripts\activate.bat

REM Install project
py -m pip install -e %tasks_proj_dir%

REM Run tests
cd %start_tests_dir%
py -m pytest --junit-xml=%results_dir%\results.xml

echo Tests complete.
