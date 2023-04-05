import obsws_python as obs
import base64

class SourceController:
    """
    A class for controlling sources in a given OBS scene.
    """
    
    def __init__(self, obs_controller: obs.ReqClient):
        """
        Initializes the SourceController object with an OBS controller instance.

        :param obs_controller: An instance of the ObsController class.
        """
        self.client = obs_controller
    
    def get_id(self, scene_name: str, source_name: str) -> int:
        """
        Gets the scene item ID for the specified source in the specified scene.

        :param scene_name: The name of the scene the source is in.
        :param source_name: The name of the source.
        :return: The scene item ID for the source.
        """
        return self.client.get_scene_item_id(scene_name, source_name).scene_item_id
    
    def remove(self, scene_name: str, source_name: str):
        """
        Removes the specified source from the specified scene.

        :param scene_name: The name of the scene the source is in.
        :param source_name: The name of the source to remove.
        """
        item = self.get_id(scene_name, source_name)
        self.client.remove_scene_item(scene_name, item)
    
    def get_index(self, scene_name: str, source_name: str):
        """
        Gets the index of the specified source in the specified scene.

        :param scene_name: The name of the scene the source is in.
        :param source_name: The name of the source.
        :return: The index of the source in the scene.
        """
        item = self.get_id(scene_name, source_name)
        return self.client.get_scene_item_index(scene_name, item).scene_item_index
    
    def set_index(self, scene_name: str, source_name: str, index: int):
        """
        Sets the index of the specified source in the specified scene.

        :param scene_name: The name of the scene the source is in.
        :param source_name: The name of the source.
        :param index: The new index for the source in the scene.
        """
        item = self.get_id(scene_name, source_name)
        self.client.set_scene_item_index(scene_name, item, index)
    
    def get_locked(self, scene_name: str, source_name: str):
        """
        Gets the locked status of the specified source in the specified scene.

        :param scene_name: The name of the scene the source is in.
        :param source_name: The name of the source.
        :return: True if the source is locked in the scene, False otherwise.
        """
        item = self.get_id(scene_name, source_name)
        return self.client.get_scene_item_locked(scene_name, item).scene_item_locked
    
    def set_locked(self, scene_name: str, source_name: str, locked: bool):
        """
        Sets the locked status of the specified source in the specified scene.

        :param scene_name: The name of the scene the source is in.
        :param source_name: The name of the source.
        :param locked: True to lock the source in the scene, False to unlock it.
        """
        item = self.get_id(scene_name, source_name)
        self.client.set_scene_item_locked(scene_name, item, locked)
    
    def get_enabled(self, scene_name: str, source_name: str) -> bool:
        """
        Obtains the current enabled status of a source within a scene.

        :param scene_name: The name of the scene that contains the source.
        :param source_name: The name of the source to retrieve the enabled status for.
        :return: A boolean value indicating whether the source is currently enabled within the scene.
        """
        item = self.get_id(scene_name, source_name)
        return self.client.get_scene_item_enabled(scene_name, item).scene_item_enabled
    
    def set_enabled(self, scene_name: str, source_name: str, enabled: bool):
        """
        Sets the enabled status of a source within a scene.

        :param scene_name: The name of the scene that contains the source.
        :param source_name: The name of the source to set the enabled status for.
        :param enabled: A boolean value indicating whether to enable or disable the source.
        """
        item = self.get_id(scene_name, source_name)
        self.client.set_scene_item_enabled(scene_name, item, enabled)
    
    def get_transform(self, scene_name: str, source_name: str) -> dict:
        """
        Retrieves the current transformation properties for a source within a scene.

        :param scene_name: The name of the scene that contains the source.
        :param source_name: The name of the source to retrieve the transformation properties for.
        :return: A dictionary containing the current transformation properties for the source.
        """
        item = self.get_id(scene_name, source_name)
        transform = self.client.get_scene_item_transform(scene_name, item).scene_item_transform
        transform['boundsWidth'] = 1
        transform['boundsHeight'] = 1
        return transform
    
    def set_transform(self, scene_name: str, source_name: str, transform: dict):
        """
        Sets the transformation properties for a source within a scene.

        :param scene_name: The name of the scene that contains the source.
        :param source_name: The name of the source to set the transformation properties for.
        :param transform: A dictionary containing the new transformation properties for the source.
        """
        item = self.get_id(scene_name, source_name)
        self.client.set_scene_item_transform(scene_name, item, transform)

    def get_blend_mode(self, scene_name: str, source_name: str) -> str:
        """
        Retrieves the current blend mode for a source within a scene.

        :param scene_name: The name of the scene that contains the source.
        :param source_name: The name of the source to retrieve the blend mode for.
        :return: A string representing the current blend mode of the source.
        """
        item = self.get_id(scene_name, source_name)
        return self.client.get_scene_item_blend_mode(scene_name, item).scene_item_blend_mode
    
    def set_blend_mode(self, scene_name: str, source_name: str, blend_mode: str):
        """
        Sets the blend mode for a source within a scene.

        :param scene_name: The name of the scene that contains the source.
        :param source_name: The name of the source to set the blend mode for.
        :param blend_mode: A string representing the new blend mode for the source.
        """
        item = self.get_id(scene_name, source_name)
        self.client.set_scene_item_blend_mode(scene_name, item, blend_mode)
    
    def get_screenshot(self, name: str, img_format: str, width: int = None, height: int = None, quality: int = -1) -> bytes:
        """
        Retrieves a screenshot of a source.

        :param name: Name of the source to take a screenshot of
        :param format: Image compression format to use. Use GetVersion to get compatible image formats
        :param width: Width to scale the screenshot to (>= 8, <= 4096). If not specified, full resolution will be used.
        :param height: Height to scale the screenshot to (>= 8, <= 4096). If not specified, full resolution will be used.
        :param quality: Compression quality to use. 0 for high compression, 100 for uncompressed. -1 to use "default"
        :return: A byte array containing the screenshot data, or None if the screenshot cannot be retrieved.
        """
        screenshot_data = self.client.get_source_screenshot(name, img_format, width, height, quality)
        return screenshot_data.image_data

    def save_source_screenshot(self, source_name: str, image_format: str, image_file_path: str, image_width: int = None, image_height: int = None, image_compression_quality: int = -1) -> bool:
        """
        Saves a screenshot of a source to a file.
        
        :param source_name: Name of the source to take a screenshot of
        :param image_format: Image compression format to use. Use GetVersion to get compatible image formats
        :param image_file_path: Path to the file to save the screenshot to
        :param image_width: Width to scale the screenshot to (>= 8, <= 4096). If not specified, full resolution will be used.
        :param image_height: Height to scale the screenshot to (>= 8, <= 4096). If not specified, full resolution will be used.
        :param image_compression_quality: Compression quality to use. 0 for high compression, 100 for uncompressed. -1 to use "default"
        :return: True if the screenshot was saved successfully, False otherwise.
        """
        image_data = self.client.save_source_screenshot(source_name, image_format, image_file_path, image_width, image_height, image_compression_quality)
        with open(image_file_path, "wb") as f:
            f.write(base64.b64decode(image_data))
        return True
    
    