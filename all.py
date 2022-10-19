import pytest
import os


if __name__ == '__main__':
    os.system('rm -rf temp')
    os.system('rm -rf report')
    pytest.main(['-n 5'])
    os.system('allure generate ./temp -o ./report --clean')

    # pytest.main(['testcase/test_alivia_blankMe.py::TestAliviaBlankMeChangKong'])
    # pytest.main(['testcase/test_alivia_api.py'])
