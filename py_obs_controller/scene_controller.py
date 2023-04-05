import obsws_python as obs

class SceneController:
    """
    A controller for managing OBS scenes. This controller provides methods to create, modify, and delete scenes,
    as well as to manage the current scene and its items.
    """

    def __init__(self, obs_controller: obs.ReqClient):
        """
        Initializes the SceneController with a reference to the OBS WebSocket client.
        
        :param obs_controller: An instance of the OBS WebSocket client.
        """
        self.client = obs_controller
    
    def get(self) -> list:
        """
        Returns a list of all scenes in the current OBS session.
        
        :return: A list of scene names.
        """
        return self.client.get_scene_list().scenes
    
    def get_group(self, group_name: str) -> list:
        """
        Returns a list of all scenes in the specified group.
        
        :param group_name: The name of the group to get scenes for.
        :return: A list of scene names.
        """
        return self.client.get_group_list().groups
    
    def get_current(self) -> str:
        """
        Returns the name of the current program scene in OBS.
        
        :return: The name of the current program scene.
        """
        return self.client.get_scene_list().current_program_scene_name

    def set_current(self, scene_name: str):
        """
        Sets the current program scene in OBS to the specified scene.
        
        :param scene_name: The name of the scene to set as the current program scene.
        """
        self.client.set_current_program_scene(scene_name)

    def set_name(self, old_name: str, new_name: str):
        """
        Renames an existing scene in OBS.
        
        :param old_name: The current name of the scene.
        :param new_name: The new name for the scene.
        """
        self.client.set_scene_name(old_name, new_name)
    
    def remove(self, scene_name: str):
        """
        Deletes an existing scene from OBS.
        
        :param scene_name: The name of the scene to remove.
        """
        self.client.remove_scene(scene_name)
    
    def create(self, scene_name: str):
        """
        Creates a new scene in OBS with the specified name.
        
        :param scene_name: The name for the new scene.
        """
        self.client.create_scene(scene_name)
    
    def get_items(self, scene_name: str) -> list:
        """
        Returns a list of all items in the specified scene.
        
        :param scene_name: The name of the scene to get items for.
        :return: A list of scene items.
        """
        return self.client.get_scene_item_list(scene_name).scene_items
    
    def get_current_preview(self) -> str:
        """
        Returns the name of the current preview scene in OBS.
        if the preview scene is not set, raises an exception.
        
        :return: The name of the current preview scene.
        """
        return self.client.get_current_preview_scene().current_preview_scene_name
    
    def set_current_preview(self, scene_name: str):
        """
        Sets the current preview scene in OBS to the specified scene.
        
        :param scene_name: The name of the scene to set as the current preview scene.
        """
        self.client.set_current_preview_scene(scene_name)
    
    def set_scene_transition_override(self, scene_name: str, transition_name: str, duration: int = 0):
        """
        Sets the transition override for the specified scene.
        
        :param scene_name: The name of the scene to set the transition override for.
        :param transition_name: The name of the transition to use for the scene.
        """
        self.client.set_scene_scene_transition_override(scene_name, transition_name, duration)
    
    def get_scene_transition_override(self, scene_name: str) -> dict:
        """
        Returns the transition override for the specified scene.
        
        :param scene_name: The name of the scene to get the transition override for.
        :return: A dictionary containing the transition override for the specified scene.
        """
        return self.client.get_scene_scene_transition_override(scene_name)