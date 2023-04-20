

# Avito Parser with Telegram Bot Integration

This project is a tool designed to track new advertisements on Avito and notify users via a Telegram bot. By integrating with the popular e-commerce platform, Avito, users can easily keep track of new listings for their desired products or services. With the help of the Telegram bot, notifications will be sent to the user as soon as new listings become available, allowing for quick and efficient purchasing decisions. The Avito Parser with Telegram Bot Integration is a useful tool for anyone looking to stay on top of the latest deals and offerings on Avito.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)


## Installation

Instructions on how to install the project and its dependencies.
The four commands are used to create a virtual environment for a Python project and install the necessary dependencies in that environment.
```sh
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Usage

Instructions on how to use the project, including examples and screenshots.

# About the settings in `config.py`

- `TOKEN` - your bot's token
- `TG_USER_ID` - the ID of your Telegram account
- `UPDATE_TIME` - time of automatic viewing of fresh posts
- `url` - a link to a product page (it is important to set the sorting parameters by time of publication for the bot to work correctly)
- `count` - meant to be a number of pages through parser (it hasn't been implemented yet)
- `version_main` - your version of Chrome
- `items` - keywords for selected items (post title or description should have at least one word from this list)
- `max_price` - maximum price of the post

Starting the bot.
```sh
$ python tg_bot.py
```
# How it looks
![image](https://user-images.githubusercontent.com/68539921/233380197-fc7952f0-df56-4a56-b747-8845afaacd97.png)

## Contributing

As the project owner, I welcome all contributions to this project. If you find any issues or bugs, please report them to us via the issues section on our GitHub repository. If you have any ideas for new features or improvements, please share them with us through the same channel. We appreciate any feedback and help to make this project better.

### Issues and Bugs

If you find an issue or a bug in our project, please report it by creating a new issue on our [GitHub repository](https://github.com/waldemarick3/Avito_parse_bot/). Be sure to provide as much detail as possible, including steps to reproduce the issue and any relevant error messages. You can also track the progress on fixing the issue on the same page.

### Feature Requests

If you have a feature request or an idea for how to improve our project, please share it with us by creating a new issue on our [GitHub repository](https://github.com/waldemarick3/Avito_parse_bot/). We encourage you to discuss the feature request with us and other contributors to ensure that it aligns with the goals and vision of the project. You can also track the progress on implementing the feature on the same page.

### Pull Requests

To contribute code changes to our project, please follow these steps:
1. Fork the repository and create a new branch from the `main` branch.
2. Make your changes and ensure that they pass all tests.
3. Create a pull request to merge your branch into the `main` branch of the original repository.
4. Wait for a code review and address any feedback from the reviewers.
5. Once your changes have been approved, they will be merged into the `main` branch.
