import os

class Config:
    """
    Minimal configuration class for the simple e-ink slideshow.
    Stores image folder path, display resolution, and startup flag.
    """

    def __init__(self):
        # Path to the folder where images are stored
        self.IMAGE_DIR = "/usr/local/inkypi/images"

        # Display resolution of your e-ink screen (width, height)
        self.RESOLUTION = (800, 600)  # adjust to your actual display

        # Startup flag: if True, display a startup image once on boot
        self.STARTUP = True

    def get_image_dir(self):
        """Returns the image directory path."""
        return self.IMAGE_DIR

    def get_config(self, key=None, default={}):
        """Gets the value of a specific configuration key or returns the entire config if none provided."""
        if key is not None:
            return self.config.get(key, default)
        return self.config

    def update_value(self, key, value, write=False):
        """Updates a specific key in the configuration with a new value and optionally writes it to the config file."""
        self.config[key] = value
        if write:
            self.write_config()

    def get_resolution(self):
        """Returns the display resolution as a tuple (width, height)."""
        return self.RESOLUTION

    def get_startup_flag(self):
        """Returns True if startup image should be displayed."""
        return self.STARTUP

    def disable_startup_flag(self):
        """Disable the startup image flag after first use."""
        self.STARTUP = False
