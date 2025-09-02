# Email & SMS Usage Warning Notifier

This application monitors email account storage usage and sends SMS notifications when usage exceeds a predefined threshold. It uses an AI to generate a friendly and informative warning message.

## Features

- Monitors email mailbox size for a list of users.
- Sends an SMS alert if mailbox usage is over 90%.
- Uses Google's Gemini AI to generate the content of the SMS message.
- Runs as a background service using Docker.

## Prerequisites

- [Docker](https://www.docker.com/get-started) must be installed on your system.

## Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/4lvin67/RTSP-Email-Usage-Warning.git
    cd RTSP-Email-Usage-Warning
    ```

2.  **Create a `.env` file:**
    Create a file named `.env` in the root of the project and add the necessary environment variables. Use the `.env.example` as a template.

    ```env
    # Email Server API
    SERVER_ADDRESS=https://your-server-api.com/
    USERNAME=your_api_username
    PASSWORD=your_api_password

    # 8x8 SMS API
    SMS_API_URL=https://sms.8x8.com/api/v1/subaccounts/your_subaccount/messages
    SMS_API_KEY=your_sms_api_key

    # List of users to monitor (JSON format)
    PEOPLE_INFO=[{"email":"user1@example.com","number":"+1234567890"},{"email":"user2@example.com","number":"+0987654321"}]

    # Google Gemini API Key
    GEMINI_API_KEY=your_gemini_api_key
    ```

## Usage

The application is designed to be run inside a Docker container.

1.  **Build the Docker image:**
    ```sh
    docker build -t email-usage-warning .
    ```

2.  **Run the container:**
    Run the container in detached mode. It will restart automatically unless it is stopped.
    ```sh
    docker run -d --restart unless-stopped --name email-warning-app --env-file .env email-usage-warning
    ```

## Viewing Logs

To see the application's output and check for errors, you can view the container's logs.

-   **View all logs:**
    ```sh
    docker logs email-warning-app
    ```

-   **Follow logs in real-time:**
    ```sh
    docker logs -f email-warning-app
    ```

## Stopping the Container

To stop the application, run:
```sh
docker stop email-warning-app
```

## Environment Variables

| Variable         | Description                                                                                             |
| ---------------- | ------------------------------------------------------------------------------------------------------- |
| `SERVER_ADDRESS` | The base URL of your email server's API.                                                                |
| `USERNAME`       | The username for authenticating with the email server API.                                              |
| `PASSWORD`       | The password for authenticating with the email server API.                                              |
| `SMS_API_URL`    | The URL for the 8x8 SMS API endpoint.                                                                   |
| `SMS_API_KEY`    | Your API key for the 8x8 SMS service.                                                                   |
| `PEOPLE_INFO`    | A JSON string containing an array of user objects, each with an `email` and a phone `number`.           |
| `GEMINI_API_KEY` | Your API key for the Google Gemini service, used to generate notification messages.                     |