import os
import time

import pytest

if __name__ =='__main__':
    pytest.main(['-vs'])
    time.sleep(3)
    os.system("allure generate ./temps -o ./reports --clean")