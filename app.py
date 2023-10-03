from flask import Flask, request, json, render_template
import requests
import logging
import os

server_name = os.getenv('SERVER_NAME', 'Unknown Server')

# Set up logging
logging.basicConfig(filename='failed_requests.log', level=logging.INFO, format='%(asctime)s - %(message)s')

app = Flask(__name__)

# Define the Google Books API URL as a global constant
GOOGLE_BOOKS_API_URL = 'https://www.googleapis.com/books/v1/volumes?q=isbn:{}'


@app.route('/')
def index():
    """
    Returns a greeting message along with server information.
    """

    return f"Greetings! You are currently processed on {server_name}"


@app.route('/book/<isbn>')
def get_book(isbn):
    """
    Retrieve metadata information about a book based on its ISBN.
    isbn (str): The ISBN of the book.
    Return: dict: A dictionary that containing metadata information.
    """

    try:
        # Construct the API URL with the provided ISBN
        google_books_api_url = GOOGLE_BOOKS_API_URL.format(isbn)
        response = requests.get(google_books_api_url)
        response.raise_for_status()
        # Convert the response content to JSON format
        book_data = response.json()

        if book_data['totalItems'] == 0:
            # Log an informational message
            info_message = f"No books found for ISBN {isbn}"
            logging.info(info_message)

            # Return a user-friendly page with a message and option to try again
            return render_template('book_not_found.html', isbn=isbn), 404

        return book_data

    # Handle any request exception that may occur during the API call.
    except requests.exceptions.RequestException as e:
        error_message = f"Error fetching book information for ISBN {isbn}: {e}"
        logging.error(error_message)
        return error_message, 500

    # Handle any other type of exception that may occur.
    except Exception as e:
        error_message = f"An error occurred: {e}"
        logging.error(error_message)
        return error_message, 500


@app.route('/cover_image', methods=['GET', 'POST'])
def view_cover_image():
    """
    View the cover image of a book identified by its ISBN.
    Return: str: HTML content with JSON data and cover image.
    """
    if request.method == 'POST':
        isbn = request.form.get('isbn')
        try:
            google_books_api_url = GOOGLE_BOOKS_API_URL.format(isbn)
            response = requests.get(google_books_api_url)
            response.raise_for_status()
            # Convert the response content to JSON format
            book_data = response.json()

            # Check if no books were found for the given ISBN.
            # If so, return a message indicating that no books were found.
            if book_data['totalItems'] == 0:
                return f"No books found for ISBN {isbn}", 404

            # Extract the URL for the book's cover image from the response data.
            cover_image_link = book_data['items'][0]['volumeInfo']['imageLinks']['thumbnail']

            # Generate HTML to display JSON and cover image
            html_content = f'''
            <h1>Book Information</h1>
            <pre>{json.dumps(book_data, indent=4)}</pre>
            <img src="{cover_image_link}" alt="Book Cover">
            '''

            return html_content

        # Handle any request exception that may occur during the API call.
        except requests.exceptions.RequestException as e:
            return f"Error fetching book information for ISBN {isbn}: {e}", 500

        # Handle any other type of exception that may occur.
        except Exception as e:
            return f"An error occurred: {e}", 500

    # If the request method is GET or form submission failed
    return '''
    <form method="post" action="/cover_image">
        <label for="isbn">ISBN:</label>
        <input type="text" id="isbn" name="isbn"><br><br>
        <input type="submit" value="Submit">
    </form>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
