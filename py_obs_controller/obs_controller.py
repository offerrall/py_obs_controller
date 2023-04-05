import obsws_python as obs

from .input_controller import InputController
from .scene_controller import SceneController
from .virtual_camera_controller import VirtualCameraController
from .stream_controller import StreamController
from .record_controller import RecordController
from .source_controller import SourceController
from .filter_controller import FilterController
from .general_controller import GeneralController


class ObsController:
    """
    The main controller for interacting with OBS. It provides access to various controllers
    for managing different aspects of OBS, such as sources, scenes, inputs, filters,
    recording, streaming, and the virtual camera.
    """

    def __init__(self, host: str, port: int, password: str):
        """
        Initializes the ObsController with a connection to the OBS WebSocket server.
        
        - source: A controller for managing OBS sources.
        - record: A controller for managing OBS recording.
        - stream: A controller for managing OBS streaming.
        - filters: A controller for managing OBS filters.
        - general: A controller for managing general OBS settings.
        - virtual_camera: A controller for managing the OBS virtual camera.
        - scenes: A controller for managing OBS scenes.
        - inputs: A controller for managing OBS input sources.
        
        :param host: The IP address or hostname of the OBS WebSocket server.
        :param port: The port number for the OBS WebSocket server.
        :param password: The password for the OBS WebSocket server.
        """
        self.client = obs.ReqClient(host=host, port=port, password=password)
        
        self.source = SourceController(self.client)
        self.record = RecordController(self.client)
        self.stream = StreamController(self.client)
        self.filters = FilterController(self.client)
        self.general = GeneralController(self.client)
        self.virtual_camera = VirtualCameraController(self.client)
        self.scenes = SceneController(self.client)
        self.inputs = InputController(self.client)
