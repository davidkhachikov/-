# Microservices Project

This project consists of two microservices: a recommendation service and a marketplace service. Both services communicate via gRPC.

## Services Overview

### Recommendation Service
The recommendation service provides book recommendations based on categories. It uses a predefined list of books categorized by genre.

### Marketplace Service
The marketplace service serves as a frontend for users to interact with the recommendation service. It displays recommended books and allows users to select them.

## Running the Services Locally

To run the services locally, you need to have Docker installed on your machine.

### Prerequisites

- Docker
- Docker Compose

### Steps to Run Locally

1. **Clone the Repository:**
   First, clone the repository to your local machine.
2. **Navigate to the Project Directory:**
   Change directory to where the `docker-compose.yml` file is located
3. **Start the Services:**
   Use the following `docker-compose up` command to start all services defined in `docker-compose.yml`.
4. **Stop the Services:**
   To stop the running services, use the command: `docker-compose down`


Работа по предмету "Архитектура бизнес-приложений". Четвёртый семестр заочной формы обучения, кафедра САиТ, группа  КТбз2-9.
