import pytest
from common.baseDriver import BaseWebdriver


def pytest_addoption(parser):
    parser.addoption(
        "--machine", action="store", default="sanxing_wx", help="选择一个手机和应用"
    )

    parser.addoption(
        "--project", action="store", default="MJLHKWB的接口测试号", help="选择待测试项目"
    )


@pytest.fixture
def machine(request):
    return request.config.getoption("--machine")


@pytest.fixture(scope="session")
def project(request):
    return request.config.getoption("--project")


@pytest.fixture(scope="session")
def driver(request):
    machine = request.config.getoption("--machine")
    driver = BaseWebdriver(machine)

    def end():
        driver.quit()
    request.addfinalizer(end)
    return driver
