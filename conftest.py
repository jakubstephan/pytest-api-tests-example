import pytest


def pytest_addoption(parser):
    """Define param which can be added to the launch test command"""
    parser.addoption("--session", action="store", default="school")


class MasterController:
    """Class used widely within tests, just as example"""

    def __init__(self, session):
        """Get initial value and store it in the class"""
        self.session = session

    def start(self):
        """Example method 1 with this class"""
        print('start for session', self.session)

    def execute(self):
        """Example method 2 with this class"""
        print('execute for session', self.session)

    def finish(self):
        """Example method 3 with this class"""
        print('finish for session', self.session)


@pytest.fixture(scope='session')
def master_controller(request):
    session = request.config.getoption('session')
    master_controller = MasterController(session)
    master_controller.start()
    yield master_controller
    master_controller.finish()
