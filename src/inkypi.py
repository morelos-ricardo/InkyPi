from config import Config
from display.display_manager import DisplayManager
from refresh_task import RefreshTask
from utils.app_utils import generate_startup_image

device_config = Config()
display_manager = DisplayManager(device_config)
refresh_task = RefreshTask(device_config, display_manager)

if __name__ == '__main__':

    # start the background refresh task
    refresh_task.start()

    # display default inkypi image on startup
    if device_config.get_config("startup") is True:       
        img = generate_startup_image(device_config.get_resolution())
        display_manager.display_image(img)
        device_config.update_value("startup", False, write=True)

    finally:
        refresh_task.stop()


