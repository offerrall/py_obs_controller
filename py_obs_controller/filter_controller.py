import obsws_python as obs
from .__utils import get_attributes_as_dict

class FilterController:

    def __init__(self, obs_controller: obs.ReqClient):
        self.client = obs_controller

    def get_list(self, source_name: str) -> list:
        """
        Returns a list of filters attached to the specified source.

        :param source_name: The name of the source to retrieve filters for.
        :return: A list of filter objects.
        """
        return self.client.get_source_filter_list(source_name).filters

    def get_default_settings(self, filter_kind: str):
        """
        Retrieves the default settings for a specified filter.

        :param filter_kind: The type of filter to retrieve default settings for.
        :return: A dictionary containing the default settings for the filter.
        """
        return self.client.get_source_filter_default_settings(filter_kind).default_filter_settings

    def create(self, source_name: str, filter_name: str, filter_kind: str, filter_settings: dict = None):
        """
        Creates a new filter and attaches it to the specified source.

        :param source_name: The name of the source to attach the filter to.
        :param filter_name: The name to give the new filter.
        :param filter_kind: The type of filter to create.
        :param filter_settings: Optional. A dictionary containing custom settings for the new filter.
        """
        self.client.create_source_filter(source_name, filter_name, filter_kind, filter_settings)

    def remove(self, source_name: str, filter_name: str):
        """
        Removes the specified filter from the specified source.

        :param source_name: The name of the source the filter is attached to.
        :param filter_name: The name of the filter to remove.
        """
        self.client.remove_source_filter(source_name, filter_name)

    def set_name(self, source_name: str, filter_name: str, new_filter_name: str):
        """
        Renames the specified filter.

        :param source_name: The name of the source the filter is attached to.
        :param filter_name: The current name of the filter.
        :param new_filter_name: The new name to give the filter.
        """
        self.client.set_source_filter_name(source_name, filter_name, new_filter_name)

    def get(self, source_name: str, filter_name: str):
        """
        Retrieves the settings for the specified filter.

        :param source_name: The name of the source the filter is attached to.
        :param filter_name: The name of the filter to retrieve settings for.
        :return: A dictionary containing the current settings for the filter.
        """
        return get_attributes_as_dict(self.client.get_source_filter(source_name, filter_name))

    def set_index(self, source_name: str, filter_name: str, filter_index: int):
        """
        Sets the index of the specified filter within the source's filter list.

        :param source_name: The name of the source the filter is attached to.
        :param filter_name: The name of the filter to set the index for.
        :param filter_index: The new index to give the filter.
        """
        self.client.set_source_filter_index(source_name, filter_name, filter_index)

    def set_settings(self, source_name: str, filter_name: str, filter_settings: dict, overlay: bool = True):
        """
        Sets the settings for the specified filter.
        
        :param source_name: The name of the source the filter is attached to.
        :param filter_name: The name of the filter to set the settings for.
        :param filter_settings: A dictionary containing the new settings for the filter.
        """
        self.client.set_source_filter_settings(source_name, filter_name, filter_settings, overlay)
    
    def get_enabled(self, source_name: str, filter_name: str) -> bool:
        """
        Returns whether the specified filter is enabled.

        :param source_name: The name of the source the filter is attached to.
        :param filter_name: The name of the filter to check.
        :return: True if the filter is enabled, False otherwise.
        """
        data = self.get(source_name, filter_name)
        return data["filter_enabled"]
    
    def set_enabled(self, source_name: str, filter_name: str, enabled: bool):
        """
        Enables or disables the specified filter.

        :param source_name: The name of the source the filter is attached to.
        :param filter_name: The name of the filter to enable or disable.
        :param enabled: True to enable the filter, False to disable it.
        """
        self.client.set_source_filter_enabled(source_name, filter_name, enabled)