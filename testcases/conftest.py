import pytest


@pytest.fixture(scope='function',autouse=False,params=(1,2,3))
def connection_sql(request):
    print('连接数据库')
    yield request.param
    print('关闭数据库')