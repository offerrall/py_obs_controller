import obsws_python as obs
from .__utils import get_attributes_as_dict

class StreamController:
    """
    A controller for managing OBS stream. This controller provides methods to
    get status and toggle on/off the stream.
    """

    def __init__(self, obs_controller: obs.ReqClient):
        """
        Initializes the StreamController with a reference to the OBS WebSocket client.
        
        :param obs_controller: An instance of the OBS WebSocket client.
        """
        self.client = obs_controller
        
    def get_status(self) -> dict:
        """
        Gets the current status of the stream.
        
        :return: A dictionary containing the current status of the stream.
        """
        return get_attributes_as_dict(self.client.get_stream_status())

    def toggle(self):
        """
        Toggles the stream on or off.
        """
        self.client.toggle_stream()
        
    def start(self):
        """
        Starts the stream.
        """
        self.client.start_stream()

    def stop(self):
        """
        Stops the stream.
        """
        self.client.stop_stream()