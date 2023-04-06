import requests  # Import the requests library to make HTTP requests

downloadUrl = 'example.com'  # Define the base URL for downloading files
for count in range(m, n):  # Loop over a range of integers
    urls = (downloadUrl + str(count) + '.jpg')  # Concatenate the count to the URL to form the complete URL for each file
    req = requests.get(urls, verify=False)  # Send a GET request to the URL to download the file
    filename = req.url[urls.rfind('/') + 1:]  # Extract the filename from the URL

    with open(filename, 'wb') as f:  # Open the file in binary mode for writing
        for chunk in req.iter_content(chunk_size=8192):  # Iterate over the response content in chunks of 8192 bytes
            if chunk:  # Check if the chunk is not empty
                f.write(chunk)  # Write the chunk to the file

def download_file(url, filename=''):  # Define a function that downloads a file from a URL and saves it to a file
    try:
        if filename:  # If a filename is specified
            pass  # Do nothing
        else:
            filename = req.url[downloadUrl.rfind('/') + 1:]  # Extract the filename from the URL

        with requests.get(url) as req:  # Send a GET request to the URL to download the file
            with open(filename, 'wb') as f:  # Open the file in binary mode for writing
                for chunk in req.iter_content(chunk_size=8192):  # Iterate over the response content in chunks of 8192 bytes
                    if chunk:  # Check if the chunk is not empty
                        f.write(chunk)  # Write the chunk to the file
            return filename  # Return the filename of the downloaded file
    except Exception as e:  # Catch any exceptions that may occur
        print(e)  # Print the exception message
        return None  # Return None to indicate that the download failed
