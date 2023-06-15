import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(URL):
    page=requests.get(URL)
    soup=BeautifulSoup(page.content,'html.parser')
    all_post=soup.find_all('a',title="Wikipedia:Citation needed")
    return len(all_post)

print(get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico'))


def get_citations_needed_report(URL):
    counter=0
    all_parag_needed=[]
    page=requests.get(URL)
    soup=BeautifulSoup(page.content,'html.parser')
    all_post=soup.find_all('sup',class_="noprint Inline-Template Template-Fact")
    for parag in all_post:
        counter+=1
        p_needed=parag.find_previous('p').text
        p_needed=f"{counter}" +" . "+ p_needed 
        all_parag_needed.append(p_needed)
    return all_parag_needed

print(get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico'))


