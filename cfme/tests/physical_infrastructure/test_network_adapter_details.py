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


@pytest.fixture(scope="module")
def guest_device(appliance, physical_server):
    network_adapter = appliance.rest_api.collections.guest_devices.find_by(device_name=physical_server.guest_devices_id()[0]['guest_name'])
    return network_adapter


"""def test_network_device_all(physical_server):
    view = navigate_to(physical_server, "AllNetworkAdapter")
    assert view.is_displayed"""


def test_network_device_detail(physical_server, guest_device):
    view = navigate_to(physical_server, "DetailsNetworkAdapter")
    assert view.is_displayed(guest_device[0].device_name)


