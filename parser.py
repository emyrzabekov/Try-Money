import requests

from bs4 import BeautifulSoup


def find(url, class_, third):

    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text, "html.parser")

    link = soup.find(class_, {'class': third})

    print(link.text)
find('https://limon.kg/news:74133', 'h1', 'title')
find('https://www.eurosport.ru/football/liga/2020-2021/story_sto8212170.shtml', 'h1', 'ArticleHeroBlack__title--olympics mb-3 sm:mb-5 lg:mb-3 font-bold text-br-2-90 olympics:text-br-2-20 olympics:font-neoTokyo olympics:font-normal caps-s2-rs sm:text-32 sm:leading-38 lg:text-48 lg:leading-58 lg:w-3/4')
find('https://limon.kg/news:74133', 'h4', 'news-title')
