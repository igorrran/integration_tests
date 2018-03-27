# -*- coding: utf-8 -*-
import pytest

from cfme.utils.appliance.implementations.ui import navigate_to
from cfme.physical.provider.lenovo import LenovoProvider

pytestmark = [pytest.mark.tier(3), pytest.mark.provider([LenovoProvider], scope="module")]


@pytest.fixture(scope="module")
def physical_server(appliance, provider, setup_provider_modscope):
    # Get and return the first physical server
    physical_servers = appliance.collections.physical_servers.find_by(provider, ph_name='cmm-dt1.labs.lenovo.com')
    return physical_servers


def test_network_device_details(physical_server):
    assert physical_server.network_adapters().is_displayed

