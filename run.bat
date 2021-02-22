pytest -s -v -m "sanity" --html=./Reports/report1.html TestCases/ --browser chrome
REM pytest -s -v -m "regression" --html=./Reports/report1.html TestCases/ --browser chrome
REM pytest -s -v -m "regression and sanity" --html=./Reports/report1.html TestCases/ --browser chrome
REM pytest -s -v -m "regression or sanity" --html=./Reports/report1.html TestCases/ --browser chrome
REM - rem is comment