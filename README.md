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

### Running the Application
Build the Docker images:

```
docker-compose up --build
```

This command will build the Docker images for Server A, Server B, Nginx and start the containers.

Once the containers are running, open your web browser and navigate to:

http://0.0.0.0:8000

You should see a greeting message indicating which server is currently processing your request.

## Endpoints

### 1. /

Access the application at [http://localhost:8000](http://localhost:8000). 

This endpoint provides a greeting message indicating which server is currently processing your request.

### 2. /book/{ISBN}

Use this endpoint to retrieve metadata information about a book by providing its ISBN number in the URL.

Replace **`<ISBN>`** with the actual ISBN number.

Example:
```plaintext
[GET] http://localhost:8000/book/1503222683

### 3. /cover_image/

 To view the cover image of a book, use the **`/cover_image endpoint`**.

 The cover image will be displayed along with the metadata information.


## Logging
Failed requests are logged in the failed_requests.log file.
