import pytest

class TestApi_1:
    @pytest.mark.smoke
    def test_login(self,):
        print('登录用例')

    def test_register(self,):
        print('注册用例')

class TestApi_2:
    @pytest.mark.smoke
    def test_add(self,connection_sql):
        print('增加用例')