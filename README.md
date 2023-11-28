# AMR-Capstone-Server
## Project Overview

The AMR project involves an autonomous mobile robot that navigates from QR code to QR code using a REST API. The Spring Boot server acts as a communication hub, receiving and processing data from the robot and providing updated information and destinations for the robot's navigation.

### Prerequisites

- Java 11
- Spring Boot 3.1.5 with the Spring Web and Spring Boot Starter Validation dependencies.
- Python3 (UI)

### Endpoints and APIs

#### `/qr` (GET) - Get a list of all QR codes
- **Description:** Retrieve a list of all available QR codes.
- **HTTP Method:** GET
- **Request URL:** `/qr`
- **Response:** A list of QR codes in JSON format, including information like name, status, image, code, and position.

#### `/robot` (GET) - Retrieve information about the robot
- **Description:** Provides information about the robot, including its current status, position, rotation, destination, QR code scan, log, and image capture.
- **HTTP Method:** GET
- **Request URL:** `/robot`
- **Response:** A JSON representation of the robot's current state, including details like ID, status, position, rotation, destination, QR code scan, log, and image data.

#### `/robot` (PUT) - Update the robot's information
- **Description:** Update the robot's information, including status, message, position, rotation, destination, QR code scan, log, and image capture.
- **HTTP Method:** PUT
- **Request URL:** `/robot`
- **Request Body:** A JSON object with updated robot information.
- **Response:** A response typically including a float[] representing updated destination and position based on the qrScan.

#### `/robot/user` (GET) - Receive user commands for the robot
- **Description:** Receive user commands for the robot, such as moving forward, rotating left/right, or stopping.
- **HTTP Method:** GET
- **Request URL:** `/robot/user`
- **Response:** A user command as a string, used to control the robot's behavior.
  

### Server Communication with Jetson Nano Robot

The server, based on Spring Boot, serves as the central communication hub in the AMR project, facilitating interactions with the Jetson Nano robot through HTTP requests.

#### HTTP Request Handling
- The server listens for HTTP requests from the Jetson Nano robot.
- Requests may include robot status updates, sensor data, image captures, and QR code scans.

#### Data Processing
- Received data is processed and interpreted by the server.

#### Sending Commands and Information
- The server responds with commands or updated navigational information.
- Responses might include new destinations, path corrections, or operational commands (start, stop, pause).

#### Error Handling and Logging
- The server manages communication errors and execution issues.
- All interactions and transactions are logged for debugging and record-keeping.

### Server Communication with User Interface

The user interface (UI) is a standalone Python program that interacts with the server via HTTP requests.

#### Feedback and Data Visualization
- The server sends responses from Jetson Nano robot to the UI.
- The UI visualizes this data, offering an interactive platform for robot control and monitoring.

#### Real-Time Updates
- The UI receives real-time updates from the server.
- These updates ensure users are constantly informed about the robot's status and environment.

This architecture enables a robust, flexible system where the server acts as an intermediary between the Jetson Nano robot and the standalone Python-based UI. The use of HTTP requests ensures ease of integration and compatibility with various technologies.

