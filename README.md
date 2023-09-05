# Elektroničko Poslovanje - Radni Nalozi

This project was developed for the "Elektroničko Poslovanje" course at FSRE ([fsre.sum.ba](https://fsre.sum.ba)). The main theme of the project revolves around work orderrs.

## Project Overview

The application is designed to manage and monitor work orders.

For a visual representation of the database schema, you can refer to this [DrawSQL diagram](https://drawsql.app/teams/-b/diagrams/elektronicko-poslovanje-grupa-7).

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. You can verify this by running:
   ```bash
   python --version
   ```
 ### Setting Up the Backend (API)

#### Clone the repository:
```bash
git clone https://github.com/VjekoRezic/EP_API
```
#### Navigate to the project directory:

```bash
cd EP_API
```

#### Create a virtual environment and activate it:

```bash
python -m venv venv
```

```bash
.\venv\Scripts\activate
```

#### Install the required dependencies:

```bash
pip install -r requirements.txt
```

#### Migrate the database:

```bash
python manage.py migrate
```

#### Run the development server:

```bash
daphne EP.asgi:application
```


### Setting Up the Client
The client for this project can be found at this [GitHub repository](https://github.com/akv3sic/ep-grupa-7-client). Follow the instructions in its README to set up and run the client side of the application.