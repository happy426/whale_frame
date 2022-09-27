import pytest
from common.yaml_util import read_yaml
# import requests


class TestApi:

    @pytest.mark.parametrize('args', read_yaml('test_test/test.yaml'))
    def test_access_token(self, args):
        # print(args)
        method = args['request']['method']
        url = args['request']['url']
        data = args['request']['data']
        result = [method, url, data]
        print(result)


if __name__ == '__main__':
    pytest.main(['test_test/test_yaml.py'])
