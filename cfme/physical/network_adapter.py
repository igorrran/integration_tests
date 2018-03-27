import attr

from cfme.modeling.base import BaseCollection

@attr.s
class NetworkAdapter():


@attr.s
class NetworkAdapterCollection(BaseCollection):



    def all(self, provider, physical_server):
        guest_device_table = appliance.db.client['guest_devices']
        physical_server_table = self.appliance.db.client['physical_servers']
        ems_table = self.appliance.db.client['ext_management_systems']
        computer_system_table = self.appliance.db.client['computer_systems']
        hardware_table = self.appliance.db.client['hardwares']

        guest_device_query = (
            self.appliance.db.client.session
                .query(guest_device_table.device_name, physical_server_table.name, ems_table.name)
                .join(ems_table, physical_server_table.ems_id == ems_table.id)
                .join(computer_system_table, (computer_system_table.managed_entity_id == physical_server_table.id)
                      & (computer_system_table.managed_entity_type == 'PhysicalServer'))
                .join(hardware_table, hardware_table.computer_system_id == computer_system_table.id)
                .join(guest_device_table, (guest_device_table.hardware_id == hardware_table.id)
                      & (guest_device_table.device_type == 'ethernet')))

        guest_devices = []

        for name, ps_name, ems_name in guest_device_query.all():
            guest_devices.append(self.instantiate(name=name, physical_server=physical_server, provider=provider))

        return guest_devices
