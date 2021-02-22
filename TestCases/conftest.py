from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome(executable_path="C:\Softwares\chromedriver.exe")
        print("Launching Chrome Browser")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        driver = webdriver.Chrome(executable_path="C:\Softwares\chromedriver.exe")
        print("Launching Chrome Browser")
    return driver


#to get the parameter from command line
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the browser method to the setup method
    return request.config.getoption("--browser")

# To run from Command prompt
# pytest -v -s TestCases/test_login.py --browser chrome

# To run test cases in parallel in the same browser
# To run parallelly , need to include pytest-xdist in the python interpreter (File->Settings)
# pytest -v -s -n=2 TestCases/test_login.py --browser chrome
# -n=2 here 2 shows number of testcases to run parallelly in the browser

#It is a hook for adding Environmental Variables to the HTML Report (This function is optional)
def pytest_configure(config):
    config._metadata['Project Name']='nop commerce'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='Varsha'

# It is a hook for deleting/modifying Environmental Variables from the HTML Report (This function is optional)
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)

#For generating HTML report, 'pytest-html' should be added in the python interpreter (File->Settings)
# pytest -v -s -n=2 --html=Reports\report.html TestCases/test_login.py --browser chrome

# For running testcases by grouping
# pytest -s -v -m "regression" --html=./Reports/report1.html TestCases/ --browser chrome
# pytest -s -v -m "sanity" --html=./Reports/report1.html TestCases/ --browser chrome
# pytest -s -v -m "sanity or regression" --html=./Reports/report1.html TestCases/ --browser chrome
# pytest -s -v -m "sanity and regression" --html=./Reports/report1.html TestCases/ --browser chrome