import obsws_python as obs
from .__utils import get_attributes_as_dict

class RecordController:
    
    def __init__(self, obs_controller: obs.ReqClient):
        """
        Constructor for the RecordController class.

        :param obs_controller: An instance of the obs.ReqClient class for communicating with the OBS WebSocket server.
        """
        self.client = obs_controller
        
    def get_status(self) -> dict:
        """
        Retrieves the current status of the recording.

        :return: A dictionary containing the status of the recording.
        """
        return get_attributes_as_dict(self.client.get_record_status())

    def toggle(self):
        """
        Toggles the recording on/off.
        """
        self.client.toggle_record()
        
    def start(self):
        """
        Starts the recording.
        """
        self.client.start_record()

    def stop(self):
        """
        Stops the recording.
        """
        self.client.stop_record()

    def toggle_pause(self):
        """
        Toggles pausing the recording on/off.
        """
        self.client.toggle_record_pause()

    def pause(self):
        """
        Pauses the recording.
        """
        self.client.pause_record()

    def resume(self):
        """
        Resumes the recording after it has been paused.
        """
        self.client.resume_record()
    
    def get_directory(self) -> str:
        """
        Retrieves the directory where the recordings are being saved.

        :return: The directory where the recordings are being saved.
        """
        return self.client.get_record_directory().record_directory
    