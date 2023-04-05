import obsws_python as obs
from .__utils import get_attributes_as_dict

class GeneralController:

    def __init__(self, obs_controller: obs.ReqClient):
        self.client = obs_controller

    def get_version(self):
        """
        Returns the version of the OBS server.
        
        :return: A dictionary containing the version information.
        """
        atributes = get_attributes_as_dict(self.client.get_version())
        del atributes["available_requests"]
        return atributes

    def get_stats(self):
        """
        Returns statistics about the OBS instance.
        
        :return: A dictionary containing the statistics information.
        """
        return get_attributes_as_dict(self.client.get_stats())
    
    def get_studio_mode_enabled(self):
        """
        Returns whether studio mode is currently enabled or not.
        
        :return: A boolean indicating whether studio mode is currently enabled.
        """
        return self.client.get_studio_mode_enabled().studio_mode_enabled
    
    def set_studio_mode_enabled(self, enabled: bool):
        """
        Enables or disables studio mode.
        
        :param enabled: A boolean indicating whether studio mode should be enabled.
        """
        self.client.set_studio_mode_enabled(enabled)
    
    def create_profile(self, profile_name: str):
        """
        Creates a new profile in OBS.
        
        :param profile_name: The name of the new profile.
        """
        self.client.create_profile(profile_name)
    
    def remove_profile(self, profile_name: str):
        """
        Removes a profile from OBS.
        
        :param profile_name: The name of the profile to remove.
        """
        self.client.remove_profile(profile_name)
    
    def get_profile_list(self):
        """
        Returns a list of all profiles in OBS.
        
        :return: A list of profiles.
        """
        return self.client.get_profile_list().profiles
    
    def set_current_profile(self, profile_name: str):
        """
        Sets the current profile in OBS.
        
        :param profile_name: The name of the profile to set as the current profile.
        """
        self.client.set_current_profile(profile_name)
    
    def get_scene_collection_list(self):
        """
        Returns a list of all scene collections in OBS.
        
        :return: A list of scene collections.
        """
        return self.client.get_scene_collection_list().scene_collections
    
    def create_scene_collection(self, scene_collection_name: str):
        """
        Creates a new scene collection in OBS.
        
        :param scene_collection_name: The name of the new scene collection.
        """
        self.client.create_scene_collection(scene_collection_name)
    
    def set_current_scene_collection(self, scene_collection_name: str):
        """
        Sets the current scene collection in OBS.
        
        :param scene_collection_name: The name of the scene collection to set as the current scene collection.
        """
        self.client.set_current_scene_collection(scene_collection_name)
    
    def get_profile_parameters(self, category: str, name: str):
        """
        Returns the value of a profile parameter.
        
        :param category: The category of the parameter.
        :param name: The name of the parameter.
        :return: The value of the parameter.
        """
        return self.client.get_profile_parameter(category, name).parameterValue
    
    def set_profile_parameters(self, category: str, name: str, value: str):
        """
        Sets the value of a profile parameter.
        
        :param category: The category of the parameter.
        :param name: The name of the parameter.
        :param value: The value to set the parameter to.
        """
        self.client.set_profile_parameter(category, name, value)
    
    def get_video_settings(self):
        """
        Returns the current video settings.
        
        :return: A dictionary containing the video settings.
        """
        return get_attributes_as_dict(self.client.get_video_settings())
    
    def set_video_settings(self, video_settings: dict):
        """
        Sets the video settings.
        
        :param video_settings: A dictionary containing the video settings.
        """
        settings = {}
        settings["base_width"] = video_settings["base_width"]
        settings["base_height"] = video_settings["base_height"]
        settings["out_width"] = video_settings["output_width"]
        settings["out_height"] = video_settings["output_height"]
        settings["numerator"] = video_settings["fps_numerator"]
        settings["denominator"] = video_settings["fps_denominator"]
        
        self.client.set_video_settings(**settings)
    
    def get_stream_settings(self) -> tuple:
        """
        Returns the current stream settings.
        
        :return: A tuple containing a dictionary containing the stream settings and a string containing the stream type.
        """
        
        data = self.client.get_stream_service_settings()
        
        return data.stream_service_settings, data.stream_service_type
    
    def set_stream_settings(self, stream_settings: dict, stream_type: str):
        """
        Sets the stream settings.
        
        :param stream_settings: A dictionary containing the stream settings.
        :param stream_type: A string containing the stream type.
        """
        self.client.set_stream_service_settings(stream_type, stream_settings)
        
        
        