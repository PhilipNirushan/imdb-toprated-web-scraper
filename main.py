import requests
from bs4 import BeautifulSoup
import openpyxl

# Create a new Excel file
excel = openpyxl.Workbook()
# Knowing How many sheets are in this Excel file
print(excel.sheetnames)
# Make the sheet as active - To load the data into that sheet
sheet = excel.active
# Giving name to the sheet
sheet.title = 'Top Rated Movies'
# Giving column names
sheet.append(['Movie Rank', 'Movie Name', 'Year of Release', 'IMDB Rating'])


# Creating a function which contains the program to retrieve the information of top-rated movies from imdb website
def find_topRatedMovies():
    # Getting Response - html code of the website
    html_text = requests.get('https://www.imdb.com/chart/top/').text
    # Using BeautifulSoup and parsing HTML
    soup = BeautifulSoup(html_text, 'html.parser')
    movies = soup.find('tbody', class_="lister-list").find_all('tr')
    for movie in movies:
        # Getting name of the movie
        movie_name = movie.find('td', class_="titleColumn").a.text
        # Getting rank of the movie
        movie_rank = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
        # Getting year of the movie
        movie_year = movie.find('td', class_="titleColumn").span.text.strip('()')
        # Getting rating of the movie
        movie_rating = movie.find('td', class_="ratingColumn imdbRating").strong.text
        # Saving all the data into particular columns accordingly
        sheet.append([movie_rank, movie_name, movie_year, movie_rating])


if __name__ == "__main__":
    # Calling the function
    find_topRatedMovies()
    # To save Excel file
    excel.save('IMDB Movie Ratings.xlsx')
