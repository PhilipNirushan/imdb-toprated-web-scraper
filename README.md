# IMDb Top Rated Movies Web Scraper
A web scraper built using Python to extract information about the top rated movies from IMDb (Internet Movie Database). The information scraped includes movie title, year of release, IMDb rating, and the rank of the movie.

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
### What things you need to install the software and how to install them:

* Python 3.x
* pip

### Use the package manager pip to install the following libraries:

``` py
pip install requests
pip install beautifulsoup4
pip install openpyxl
```

## Usage
Run the following command to execute the script:

``` py
python main.py
```

The script will scrape the top 250 rated movies from IMDb and store the information in a Excel file named IMDB Movie Ratings.xlsx. The Excel file will contain the following columns:

* Title
* Rank
* Year
* IMDb Rating

# Built With

* Python
* Requests - HTTP library for Python
* BeautifulSoup - A library for pulling data out of HTML and XML files
* OpenPyXL - A Python library for reading and writing Excel files 

# License
This project is licensed under the MIT License - see the LICENSE file for details.





