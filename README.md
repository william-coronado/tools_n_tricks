# Tools and Tricks

This project contains various tools and scripts for different purposes I have collected from a number of sites, including data generation, web applications, data validation, and time handling. Below is a brief description of each file and its functionality:

## Scripts

### `arrow_time_handling.py`
This script uses the `arrow` library for handling and manipulating dates and times. It demonstrates creating time objects, date manipulation, human-readable differences, timezone conversion, and date formatting.

### `faker_test_data_gen.py`
This script uses the `faker` library to generate fake user data. It includes examples of generating user profiles, using specific locales, and creating custom providers.

### `hydra_conf_mgnt.py`
This script demonstrates how to use the Hydra framework for managing configurations. It prints the configuration in YAML format and extracts specific configuration values.

### `pydantic_data_val.py`
This script uses the `pydantic` library for data validation. It defines a `User` model with various fields and includes a custom validator for the `age` field.

### `rich_print.py`
This script uses the `rich` library to create a fancy table and a progress bar. It demonstrates how to format and print tables and track progress.

### `streamlit_web_app.py`
This script creates a simple web application using the `streamlit` library. The app displays Uber pickup data in NYC and includes options to load and display raw data.

Run using: *streamlit run streamlit_web_app.py*

### `loguru_logging.py`
This script demonstrates various logging functionalities using the `loguru` library. 

### `psutil_sys_monitoring.py`
This script demonstrates how to use the `psutil` library to monitor system resources and manage processes.

## Directories
### `conf/`
This directory contains configuration files for the Hydra framework.
- `hydra_conf_mgnt.yaml`: Configuration file for managing Hydra configurations.

### `outputs/`
This directory contains output files generated by the project, including logs and configuration files.