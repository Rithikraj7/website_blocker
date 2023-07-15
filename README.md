# Website Blocker

This Python program allows you to block access to specific websites by modifying the host file on your operating system.

## Prerequisites

- Python 3 installed on your system

## Getting Started

1. Clone the repository or download the source code.

2. Open the `block_websites.py` file in a text editor.

3. Modify the `websites_to_block` list to include the domain names of the websites you want to block. For example:

    ```python
    websites_to_block = ["google.com", "facebook.com", "twitter.com"]
    ```

4. Save the changes to the file.

5. Run the script:

    - On Windows: Open the command prompt as an administrator, navigate to the directory containing the `block_websites.py` file, and run:

        ```bash
        python block_websites.py
        ```

    - On Linux or macOS: Open the terminal and run:

        ```bash
        sudo python3 block_websites.py
        ```

6. The program will modify the host file on your operating system to block access to the specified websites by redirecting them to `127.0.0.1`.

7. To unblock the websites, open the `block_websites.py` file again and remove the corresponding entries from the `websites_to_block` list. Save the changes and run the script again.

## Compatibility

- Windows
- Linux
- macOS

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The program modifies the host file to block websites. Please use it responsibly and respect the legal and ethical considerations of blocking websites.
