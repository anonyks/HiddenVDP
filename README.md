# HiddenVDP

HiddenVDP is a collection of tools designed to assist security researchers and bug bounty hunters in discovering security contact information and vulnerability disclosure policies (VDPs) across various web domains. The repository includes two main scripts, `HiddenVDPv1.py` and `HiddenVDPv2.py`, that automate the process of scanning URLs for relevant security information.

## Features

- **HiddenVDPv1.py**: Automates the process of scanning URLs to discover pages like `.well-known/security.txt` and `security.txt` that might contain keywords indicating the presence of a VDP.
- **HiddenVDPv2.py**: Focuses on detecting and logging URLs that contain direct contact information for security concerns, enhancing the ability to reach out for responsible disclosure.

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/HiddenVDP.git

# Navigate into the repository
cd HiddenVDP

# Install required packages
pip install requests colorama
```

## Usage

To use either of the scripts:

1. Prepare a text file containing the URLs to be scanned, with one URL per line.
2. Run the script and provide the path to your list when prompted.

### Example

```bash
python HiddenVDPv1.py
python HiddenVDPv2.py
```

Follow the prompts to enter the path to your list of URLs.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Contact

If you have any questions or want to connect, please reach out to @AnonyKs_xD on Telegram.
