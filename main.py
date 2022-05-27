from random import random, randint
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
f = open('movies.csv', 'w', encoding='utf-8_sig', newline='\n')
file = csv.writer(f)
file.writerow(['Title', 'Describe'])
ind = 1
while ind<150:
    url = 'https://www.qartulad.ge/category/filmebi?page=1' + str(ind)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    sub_soup = soup.find('div', class_='row actorMoviesCont mainMoveCont')
    all_movies = sub_soup.find_all('div', class_='item defMov-box movie-box lazy boxRight')
    for movie in all_movies:
        title = movie.p.text
        describe = movie.find('p', class_='mainTxt').text
        file.writerow([title, describe])
    ind+=30
    sleep(randint(15,20))
f.close()