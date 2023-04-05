import obsws_python as obs
from .__utils import get_attributes_as_dict

class VirtualCameraController:
    """
    A controller for managing OBS virtual camera. This controller provides methods to
    get status and toggle on/off the virtual camera.
    """

    def __init__(self, obs_controller: obs.ReqClient):
        """
        Initializes the VirtualCameraController with a reference to the OBS WebSocket client.
        
        :param obs_controller: An instance of the OBS WebSocket client.
        """
        self.client = obs_controller
        
    def get_status(self) -> dict:
        """
        Gets the current status of the virtual camera.
        
        :return: A dictionary containing the current status of the virtual camera.
        """
        return get_attributes_as_dict(self.client.get_virtual_cam_status())

    def toggle(self):
        """
        Toggles the virtual camera on or off.
        """
        self.client.toggle_virtual_cam()
        
    def start(self):
        """
        Starts the virtual camera.
        """
        self.client.start_virtual_cam()

    def stop(self):
        """
        Stops the virtual camera.
        """
        self.client.stop_virtual_cam()