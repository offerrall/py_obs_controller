import obsws_python as obs

class InputController:
    """
    A controller for managing OBS input sources. Input sources include various types of
    media sources, such as video, audio, images, and text. This controller provides
    methods to create, modify, and delete input sources, as well as to manage their
    settings and properties.
    """

    def __init__(self, obs_controller: obs.ReqClient):
        """
        Initializes the InputController with a reference to the OBS WebSocket client.
        
        :param obs_controller: An instance of the OBS WebSocket client.
        """
        self.client = obs_controller
    
    def get_list(self) -> list:
        """
        Returns a list of all input sources in the current OBS session.
        
        :return: A list of input sources.
        """
        return self.client.get_input_list().inputs
    
    def get_kind_list(self) -> list:
        """
        Returns a list of all available input source kinds in OBS. Input source kinds
        include types such as video capture devices, audio input/output captures, image
        sources, text sources, and more.
        
        :return: A list of input source kinds.
        """
        return self.client.get_input_kind_list(True).input_kinds

    def create(self, scene_name: str, input_name: str, input_kind: str, input_settings: dict, scene_item_enabled: bool):
        """
        Creates a new input source and adds it to the specified scene. The input source
        will have the provided name, kind, and settings.
        
        :param scene_name: The name of the scene to add the input source to.
        :param input_name: The name of the new input source.
        :param input_kind: The kind of the new input source (e.g., 'video_capture_device', 'audio_input_capture').
        :param input_settings: A dictionary containing the settings for the new input source.
        :param scene_item_enabled: A boolean indicating whether the input source should be enabled in the scene.
        """
        self.client.create_input(scene_name, input_name, input_kind, input_settings, scene_item_enabled)
    
    def remove(self, input_name: str):
        """
        Removes an input source from the current OBS session.

        :param input_name: The name of the input source to remove.
        """
        self.client.remove_input(input_name)
    
    def set_name(self, old_name: str, new_name: str):
        """
        Renames an existing input source.

        :param old_name: The current name of the input source.
        :param new_name: The new name to give the input source.
        """
        self.client.set_input_name(old_name, new_name)
    
    def get_default_settings(self, input_kind: str) -> dict:
        """
        Retrieves the default settings for a particular input source kind.

        :param input_kind: The kind of the input source (e.g., 'video_capture_device', 'audio_input_capture').
        :return: A dictionary containing the default settings for the input source kind.
        """
        return self.client.get_input_default_settings(input_kind).default_input_settings
    
    def get_settings(self, input_name: str) -> dict:
        """
        Retrieves the current settings for an input source.

        :param input_name: The name of the input source to retrieve settings for.
        :return: A dictionary containing the current settings for the input source.
        """
        return self.client.get_input_settings(input_name).input_settings

    def get_kind(self, input_name: str) -> str:
        """
        Retrieves the kind of an input source.

        :param input_name: The name of the input source to retrieve the kind of.
        :return: A string containing the kind of the input source.
        """
        return self.client.get_input_settings(input_name).input_kind

    def set_settings(self, input_name: str, input_settings: dict):
        """
        Updates the settings of an input source.

        :param input_name: The name of the input source to update the settings of.
        :param input_settings: A dictionary containing the new settings for the input source.
        """
        self.client.set_input_settings(input_name, input_settings, True)

    def get_volume(self, input_name: str) -> float:
        """
        Retrieves the current volume multiplier for an input source.

        :param input_name: The name of the input source to retrieve the volume multiplier for.
        :return: A float representing the current volume multiplier for the input source.
        """
        return self.client.get_input_volume(input_name).input_volume_mul

    def set_volume(self, input_name: str, volume: float):
        """
        Sets the volume multiplier for an input source.

        :param input_name: The name of the input source to set the volume multiplier for.
        :param volume: A float representing the new volume multiplier for the input source.
        """
        self.client.set_input_volume(input_name, volume, None)

    def get_volume_decibel(self, input_name: str) -> float:
        """
        Retrieves the current volume multiplier for an input source in decibels.

        :param input_name: The name of the input source to retrieve the volume multiplier for.
        :return: A float representing the current volume multiplier for the input source in decibels.
        """
        return self.client.get_input_volume(input_name).input_volume_db

    def set_volume_decibel(self, input_name: str, volume: float):
        """
        Sets the volume multiplier for an input source in decibels.

        :param input_name: The name of the input source to set the volume multiplier for.
        :param volume: A float representing the new volume multiplier for the input source in decibels.
        """
        self.client.set_input_volume(input_name, None, volume)
    
    def get_muted(self, input_name: str) -> bool:
        """
        Retrieves whether an input source is currently muted or not.

        :param input_name: The name of the input source to retrieve the muted status of.
        :return: A boolean indicating whether the input source is currently muted or not.
        """
        return self.client.get_input_mute(input_name).input_muted

    def set_muted(self, input_name: str, muted: bool):
        """
        Sets the muted status of an input source.

        :param input_name: The name of the input source to set the muted status of.
        :param muted: A boolean indicating whether the input source should be muted or not.
        """
        self.client.set_input_mute(input_name, muted)
    
    def toggle_muted(self, input_name: str):
        """
        Toggles the muted status of an input source.

        :param input_name: The name of the input source to toggle the muted status of.
        """
        self.client.toggle_input_mute(input_name)
    
    def get_audio_balance(self, input_name: str) -> float:
        """
        Retrieves the current audio balance for an input source.

        :param input_name: The name of the input source to retrieve the audio balance for.
        :return: A float representing the current audio balance for the input source.
        """
        return self.client.get_input_audio_balance(input_name).input_audio_balance
    
    def set_audio_balance(self, input_name: str, balance: float):
        """
        Sets the audio balance for an input source.

        :param input_name: The name of the input source to set the audio balance for.
        :param balance: A float representing the new audio balance for the input source.
        """
        self.client.set_input_audio_balance(input_name, balance)
    
    def get_audio_sync_offset(self, input_name: str) -> int:
        """
        Retrieves the current audio sync offset for an input source.

        :param input_name: The name of the input source to retrieve the audio sync offset for.
        :return: An integer representing the current audio sync offset for the input source.
        """
        return self.client.get_input_audio_sync_offset(input_name).input_audio_sync_offset
    
    def set_audio_sync_offset(self, input_name: str, offset: int):
        """
        Sets the audio sync offset for an input source.

        :param input_name: The name of the input source to set the audio sync offset for.
        :param offset: An integer representing the new audio sync offset for the input source.
        """
        self.client.set_input_audio_sync_offset(input_name, offset)
    
    def get_audio_tracks(self, input_name: str) -> dict:
        """
        Retrieves the current audio tracks for an input source.

        :param input_name: The name of the input source to retrieve the audio tracks for.
        :return: A list of dictionaries containing the current audio tracks for the input source.
        """
        return self.client.get_input_audio_tracks(input_name).input_audio_tracks
    
    def set_audio_tracks(self, input_name: str, tracks: dict):
        """
        Sets the audio tracks for an input source.

        :param input_name: The name of the input source to set the audio tracks for.
        :param tracks: A list of dictionaries containing the new audio tracks for the input source.
        """
        self.client.set_input_audio_tracks(input_name, tracks)