# PyOBScontroller WebSocket v5.0

`PyOBScontroller` is a Python package designed to provide a comprehensive abstraction of the OBS Studio WebSocket API. This powerful tool allows you to control OBS Studio in its entirety, using only the documentation and functions provided by this library, without needing to dive into the complexity of the API. It simplifies the interaction with OBS by turning it into a Python object, making it highly accessible to Python developers. This package is based on the [`obsws-python`](https://github.com/aatikturk/obsws-python) library and requires it to be installed beforehand.

> Note: `PyOBScontroller` is not available as a package on PyPI, so it cannot be installed using `pip`. You should copy and paste the provided code into your own project.

## Prerequisites

To use `PyOBScontroller`, you first need to install the [`obsws-python`](https://github.com/aatikturk/obsws-python) library by following the instructions on its GitHub page.

## Control of OBS Studio

`PyOBScontroller` provides a complete set of classes and functions to control every aspect of OBS Studio, offering a seamless experience for users:

- `InputController`: Controls the inputs in OBS Studio.
- `SceneController`: Controls the scenes in OBS Studio.
- `VirtualCameraController`: Controls the virtual camera in OBS Studio.
- `StreamController`: Controls the streaming in OBS Studio.
- `RecordController`: Controls the recording in OBS Studio.
- `SourceController`: Controls the sources in the scenes of OBS Studio.
- `FilterController`: Controls the filters in the sources of OBS Studio.
- `GeneralController`: Provides general functions for getting information and statistics about OBS Studio.

With `PyOBScontroller`, you'll be able to manage your OBS Studio instance effortlessly, using only the library's documentation as a guide.

To use the provided classes and functions, simply access them through the `ObsController` instance. 


## Example Usage

This example demonstrates how to use `PyOBScontroller` to connect to OBS Studio, disable a source, switch to another scene, and mute a microphone input.

```python
from py_obs_controller.obs_controller import ObsController

# Replace these values with your OBS Studio host, port, and password
HOST = '127.0.0.1'
PORT = 4444
PASSWORD = 'your_password_here'

# Create an instance of ObsController with the host, port, and password
obs_controller = ObsController(HOST, PORT, PASSWORD)

# Connect to OBS Studio
obs_controller.client.connect()

# Disable a source
scene_name = 'Scene1'
source_name = 'Source1'
obs_controller.source.set_enabled(scene_name, source_name, False)

# Change to another scene
new_scene_name = 'Scene2'
obs_controller.scenes.set_current(new_scene_name)

# Mute a microphone input
mic_input_name = 'Microphone'
obs_controller.inputs.set_muted(mic_input_name, True)
```


## TODO

1. **Implement all missing API calls:**
   Make sure all OBS Studio WebSocket API functions are implemented in the PyOBScontroller package.

2. **Add usage examples:**
   Provide clear and comprehensive usage examples for users to understand how to use the PyOBScontroller package effectively.

3. **Convert the package into a distributable package:**
   Modify the package structure and configuration so that it can be easily installed and distributed using package managers like `pip`.



