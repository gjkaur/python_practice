"""
Capstone 2: REST Client with GUI Frontend

PCPP Objectives: All sections (1.1-5.2)

Main entry point for the application.
"""

import logging
import sys
from configparser import ConfigParser

# TODO: Import your modules
# from utils.config import load_config
# from utils.logging_config import setup_logging
# from api.client import RESTClient
# from gui.main_window import MainWindow


def main() -> None:
    """Main application entry point."""
    try:
        # TODO: Load configuration
        # config = load_config('config.ini')
        
        # TODO: Setup logging
        # setup_logging(config)
        # logger = logging.getLogger(__name__)
        # logger.info("Application starting")
        
        # TODO: Initialize REST client
        # api_client = RESTClient(config.get('api', 'base_url'))
        
        # TODO: Create and run GUI
        # app = MainWindow(api_client, config)
        # app.run()
        
        print("Capstone 2: Implement your application here!")
        
    except Exception as e:
        logging.error(f"Application error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
