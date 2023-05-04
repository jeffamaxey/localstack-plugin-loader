import pytest

from plugin.discovery import ModuleScanningPluginFinder
from tests.plugins import sample_plugins


@pytest.fixture
def sample_plugin_finder():
    yield ModuleScanningPluginFinder(modules=[sample_plugins])
