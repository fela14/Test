@echo off
REM ================================
REM Windows batch script using Git and WORKSPACE
REM ================================

REM Paths relative to workspace
set tasks_proj_dir=%WORKSPACE%\path\to\code\ch7\tasks_proj_v2
set start_tests_dir=%WORKSPACE%\path\to\code\ch7\tasks_proj_v2\tests
set results_file=%WORKSPACE%\results.xml

REM Install project
py -m pip install -e %tasks_proj_dir%

REM Run tests
cd %start_tests_dir%
py -m pytest --junit-xml=%results_file%

echo Tests complete.
exit /b %errorlevel%

