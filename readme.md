# Webhook Utility README

This Python script provides a simple utility to interact with Discord webhooks. It allows you to spam messages to a webhook or delete a webhook based on your choice. Below is an explanation of the code and its functionality.

## Table of Contents

- [Features](#features)
- [Dependencies](#dependencies)
- [Usage](#usage)
  - [Spam a Webhook](#spam-a-webhook)
  - [Delete a Webhook](#delete-a-webhook)
- [How to Run](#how-to-run)
- [Contributing](#contributing)
- [License](#license)

![Display](https://cdn.discordapp.com/attachments/1148256815897915422/1148275191911288872/display.png)

## Features

1. **Spam a Webhook**: Send a repetitive message to a Discord webhook.
2. **Delete a Webhook**: Delete a Discord webhook using its URL.
3. **User-friendly Interface**: The script includes a colorful console interface for ease of use.

## Dependencies

This script uses the following external libraries:

- [requests](https://docs.python-requests.org/en/latest/): For making HTTP requests.
- [colorama](https://pypi.org/project/colorama/): For adding color to console text.

You can install these dependencies using `pip`:

```bash
pip install requests colorama
```

## Usage

### Spam a Webhook

This option allows you to spam a message to a Discord webhook repeatedly.

1. Run the script.
2. Choose option 1 to spam a webhook.
3. Enter the webhook URL when prompted.
4. Enter the message you want to spam.
5. The message will be sent repeatedly until you exit the program.

### Delete a Webhook

This option allows you to delete a Discord webhook using its URL.

1. Run the script.
2. Choose option 2 to delete a webhook.
3. Enter the webhook URL you want to delete.
4. The script will attempt to delete the webhook and provide feedback on the result.

### How to Run

To run the script, follow these steps:

1. Make sure you have Python installed on your system.
2. Install the required dependencies as mentioned in the [Dependencies](#dependencies) section.
3. Save the script to a file with a `.py` extension (e.g., `webhook_utility.py`).
4. Open a terminal or command prompt.
5. Navigate to the directory containing the script.
6. Run the script using the following command:

```bash
python webhook_utility.py
```

7. Follow the on-screen instructions to use the utility.

### Contributing

Feel free to contribute to this script by opening issues or pull requests on the [GitHub repository](https://github.com/ShockxZZx/ShockxZZx-WebHook-Funnier).

## License

This script is provided under the [MIT License](LICENSE). You are free to use and modify it as per the terms of the license.
