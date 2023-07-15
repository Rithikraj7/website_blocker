import platform
import os


def block_websites(websites):
    system = platform.system()

    if system == "Windows":
        host_path = r"C:\Windows\System32\drivers\etc\hosts"
    elif system == "Linux" or system == "Darwin":
        host_path = "/etc/hosts"
    else:
        print("Unsupported operating system.")
        return

    # Add website entries to the host file
    try:
        with open(host_path, "a") as host_file:
            host_file.write("\n")
            for website in websites:
                host_file.write(f"127.0.0.1 {website}\n")
    except PermissionError:
        print("Permission denied. Please run the program as an administrator or with sudo.")
    except FileNotFoundError:
        print("Host file not found.")
    else:
        print("Websites blocked successfully.")


# List of websites to be blocked
websites_to_block = ["google.com",
                     "facebook.com",
                     "twitter.com"
                     ]

# Call the Function block_websites to Block the websites
block_websites(websites_to_block)
