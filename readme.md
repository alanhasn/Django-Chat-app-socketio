# Chat Django SocketIO Application

This project implements a real-time chat application using Django and SocketIO.

## Features

- Real-time messaging using SocketIO.
- Django backend.
- Simple chat interface.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/alanhasn/Django-Chat-app-socketio
   ```
2. Navigate to the project directory:
   ```
   cd Django-Chat-app-socketio
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Run the Uvicorn server (for ASGI deployment):
   ```
   uvicorn djchatsocket.asgi:application --reload
   ```

## Usage

- Open your browser and go to `http://localhost:8000` to start chatting.
