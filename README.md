
# URL Health Checker

A Python script to check the status of a list of URLs and optionally report their ping times.

## Table of Contents

-   [Installation](https://github.com/daazer/LinkHealthChecker#installation)
-   [Usage](https://github.com/daazer/LinkHealthChecker#usage)
-   [Features](https://github.com/daazer/LinkHealthChecker#features)
-   [Contributing](https://github.com/daazer/LinkHealthChecker#contributing)
-   [License](https://github.com/daazer/LinkHealthChecker#license)

## Installation

1.  Ensure you have Python installed. This script is compatible with Python 3.6+.
2.  Install required packages:
    
    bashCopy code
    
    `pip install requests` 
    

## Usage

To use the URL Health Checker, run the script `check_urls.py` with required and optional arguments:

bashCopy code

`python check_urls.py -L <path_to_file_with_urls> [options]` 

### Arguments:

-   **-L, --list**: (Required) Path to the file containing a list of URLs to check.
    
-   **-T, --threads**: (Optional) Number of threads to use. Default is 10.
    
-   **--only-up**: (Optional) If provided, only display URLs that are up.
    
-   **--show-ping**: (Optional) If provided, display the ping time for URLs.
    

Example:

bashCopy code

`python check_urls.py -L urls.txt --show-ping` 

## Features

-   **URL Health Checking**: Determine if a URL is up or down based on HTTP status codes.
    
-   **Ping Reporting**: Optional feature to display the ping time for each URL.
    
-   **Multithreading**: Speed up the checking process by running checks in parallel.
    

## Contributing

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/fooBar`).
3.  Commit your changes (`git commit -am 'Add some fooBar'`).
4.  Push to the branch (`git push origin feature/fooBar`).
5.  Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
