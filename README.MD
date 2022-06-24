## Requirements
[Python 3.8](https://www.python.org/downloads/) or higher  
[Allure-commandline](https://docs.qameta.io/allure/#_installing_a_commandline) for generating html-report

## Installing dependencies
```commandline
pip install -r requirements.txt
```

## Running tests
### Only tests without allure-report
```commandline
pytest
```
### Tests with generating allure-report
```commandline
pytest --alluredir=reports/allure
allure serve reports/allure
```