import pytest
from common.yaml_util import read_yaml
from playwright.sync_api import Browser
from common import env_util


# def test_01(api):
#     data = {
#         "operationName": "searchFormValue",
#         "variables": {
#             "form_slug": "vap_douyin_list",
#             "limit": 500,
#             "offset": 0,
#             "order_by": [],
#             "filter_entities": [
#                 {
#                     "filter_key": "status",
#                     "operation": 8,
#                     "filter_value": "[\"1\",\"4\"]"
#                 }
#             ],
#             "relation": 1
#         },
#         "query": "query searchFormValue($form_slug: String, $filters: JSON, $order_by: [OrderByEntity], $limit: Int, $offset: Int, $filter_entities: JSON, $relation: Int, $full_text_search_keyword: String) {\n  searchFormValue(form_slug: $form_slug, filters: $filters, order_by: $order_by, offset: $offset, limit: $limit, filter_entities: $filter_entities, relation: $relation, full_text_search_keyword: $full_text_search_keyword) {\n    items\n    total\n    limit\n    offset\n  }\n}\n"
#     }
#     cookie = {
#         'lang=zh-CN; whalewebjssdk_cross_new_user=1; privacy=true; _t_v2=a9ApXvsKSoSO4T1WVgPr8w; timezone=Asia/Shanghai; resource_id=3785951872649171968; resource_type=res; whale_jssdk_cross={"_distinct_id":"1660102589393-5416562-01ec8ea155f43-10233158","_anonymous_id":"1660102589393-5416562-01ec8ea155f43-10233158","_user_id":"","_is_first_day":true,"_is_first_time":true,"props":{}}'
#     }
#     response = api.post('/graphql', data=data, cookies=cookie)
#     print(response.json())
#     assert response.json().get('code') == '200'


@pytest.mark.parametrize('args', read_yaml('test_test/vap.yaml'))
def test_vap_api(browser: Browser, args):
    context = browser.new_context(storage_state="../data/blankMe_cookie_hyx.json")
    page = context.new_page()
    name = args['name']
    data = args['request']['data']
    res = page.request.post(url=f'https://blankme.{env_util.env}.meetwhale.com/graphql', data=data)
    assert res.status == 200
    print(res.json())


if __name__ == '__main__':
    pytest.main(['-vs', 'test_test/test_alivia_api.py'])
