# import time
# import re
# import allure
# import pytest
# import requests
# from common.yaml_util import read_yaml
# from common.robot import FeishuAlert
# from common import env_util
#
#
# """
# Dev  环境地址：https://aml-api.develop.meetwhale.com
# Stage 环境地址: https://aml-api-public.stage.meetwhale.com
# Production环境：https://aml-api-public.meetwhale.com
# """
#
#
# @allure.feature('算法接口')
# class TestAlgorithmApi:
#
#     @allure.title('prod场控QA')
#     @pytest.mark.parametrize('args', read_yaml('data/qa.yaml'))
#     def test_qa(self, args):
#         method = args['method']
#         url = "https://aml-api-public.meetwhale.com" + '/' + args['url']
#         company_id = args['company_id']
#         comment = args['comment']
#         topk = args['topk']
#         data = {
#             "company_id": company_id,
#             "comment": comment,
#             "topk": topk
#         }
#         res = requests.request(method=method, url=url, json=data)
#         # result = res.json()
#         # print(result)
#         if res.status_code != 200:
#             alert = FeishuAlert()
#             title = "问答接口请求失败"
#             content = f"请求的返回状态为{res.status_code}"
#             alert.post_to_robot(title, content)
#
#     @allure.title('不同环境场控QA')
#     @pytest.mark.parametrize('args', read_yaml('data/qa_env.yaml'))
#     def test_qa_env(self, args):
#         method = args['method']
#         env = args['env']
#         url = args['url']
#         company_id = args['company_id']
#         comment = args['comment']
#         topk = args['topk']
#         data = {
#             "company_id": company_id,
#             "comment": comment,
#             "topk": topk
#         }
#         res = requests.request(method=method, url=url, json=data)
#         # result = res.json()
#         # print(result)
#         if res.status_code != 200:
#             alert = FeishuAlert()
#             title = "问答接口请求失败"
#             content = f"{env}请求的返回状态为{res.status_code}"
#             alert.post_to_robot(title, content)
#
#     @allure.title('不同环境问答库扩充')
#     @pytest.mark.parametrize('args', read_yaml('data/qa_env.yaml'))
#     def test_insertQA_env(self, args):
#         method = args['method']
#         env = args['env']
#         url = args['url'] + '/insertQA'
#         data = {
#             "company_id": "3641588816278531584",
#             "question": "主播干皮适合用什么产品",
#             "question_type": "",
#             "answer": ["小黑盒"],
#             "insert_type": 0,
#             "insert_user": "test1"
#         }
#         res = requests.request(method=method, url=url, json=data)
#         # result = res.json()
#         # print(result)
#         if res.status_code != 200:
#             alert = FeishuAlert()
#             title = "问答库扩充接口请求失败"
#             content = f"{env}请求的返回状态为{res.status_code}"
#             alert.post_to_robot(title, content)
#
#     @allure.title('不同环境问答库修正')
#     @pytest.mark.parametrize('args', read_yaml('data/qa_env.yaml'))
#     def test_updateQA_env(self, args):
#         method = args['method']
#         env = args['env']
#         url = args['url'] + '/updateQA'
#         data = {
#             "company_id": "3641588816278531584",
#             "question": "主播干皮适合用什么产品",
#             "question_type": "",
#             "answer": [],
#             "update_user": "test2"
#         }
#         res = requests.request(method=method, url=url, json=data)
#         # result = res.json()
#         # print(result)
#         if res.status_code != 200:
#             alert = FeishuAlert()
#             title = "问答库修正接口请求失败"
#             content = f"{env}请求的返回状态为{res.status_code}"
#             alert.post_to_robot(title, content)
#
