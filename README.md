# PayPal_Home_assignment
 
This project is a simple web application that provides metadata information about books when given their ISBN number. It consists of three components:

1. **Server A:** Responsible for processing 60% of the incoming requests.
2. **Server B:** Responsible for processing 40% of the incoming requests.
3. **Nginx:** Orchestrates the requests, directing them to either Server A or Server B.
   
## Getting Started
Follow these steps to run the application on your local machine:

### Installation
Clone this repository:

```
git clone https://github.com/orelevi/PayPal_Home_assignment.git
```

Change to the project directory:

```
cd PayPal_Home_assignment
```

Build the Docker images:

```
docker-compose up --build
```

This command will build the Docker images for Server A, Server B, Nginx and start the containers.

### Installation with bash script

I've provided a convenient bash script (`run_application.sh`) to streamline the process of updating your application and starting the Docker containers. This script automates three essential steps: pulling the latest changes from the repository, navigating to the project directory and initiating the Docker-compose process.

**How to Run the Script**

1. Make the script executable with the command: `chmod +x run_application.sh`
2. Execute the script by running: `./run_application.sh`

Once the containers are running, open your web browser and navigate to:

http://0.0.0.0:8000

You should see a greeting message indicating which server is currently processing your request.

## Endpoints

### 1. /

Access the application at [http://0.0.0.0:8000](http://localhost:8000). 

This endpoint provides a greeting message indicating which server is currently processing your request.

### 2. /book/{ISBN}

Use this endpoint to retrieve metadata information about a book by providing its ISBN number in the URL.

Replace **`<ISBN>`** with the actual ISBN number.

Example:

http://0.0.0.0:8000/book/1503222683

### 3. /cover_image/

 To view the cover image of a book, use the **`/cover_image endpoint`**.

 After you will enter the ISBN number in the box, the cover image will be displayed along with the metadata information.


## Logging
Failed requests are logged in the failed_requests.log file.
