import fauxfactory
import pytest

from cfme.cloud.provider import CloudProvider
from cfme.infrastructure.provider import InfraProvider
from cfme.services.service_catalogs import ServiceCatalogs
from cfme import test_requirements
from cfme.utils.appliance import ViaSSUI
from cfme.utils.providers import ProviderFilter
from cfme.markers.env_markers.provider import providers


pytestmark = [
    pytest.mark.meta(server_roles="+automate"),
    test_requirements.ssui,
    pytest.mark.long_running,
    pytest.mark.ignore_stream("upstream"),
    pytest.mark.provider(gen_func=providers,
                         filters=[ProviderFilter(classes=[InfraProvider, CloudProvider],
                                                 required_fields=['provisioning'])])
]


@pytest.mark.parametrize('context', [ViaSSUI])
def test_service_catalog_crud(appliance, setup_provider,
                              context, provision_request):
    """Tests Service Catalog in SSUI."""

    catalog_item, provision_request = provision_request
    with appliance.context.use(context):
        if appliance.version >= '5.9':
            dialog_values = {'service_name': "ssui_{}".format(fauxfactory.gen_alphanumeric())}
            service = ServiceCatalogs(appliance, name=catalog_item.name,
                                      dialog_values=dialog_values)
        else:
            service = ServiceCatalogs(appliance, name=catalog_item.name)
        service.add_to_shopping_cart()
        service.order()
