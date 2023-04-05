
def example_used():
    """
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
    """
    pass
