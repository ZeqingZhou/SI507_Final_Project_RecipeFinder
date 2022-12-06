from bs4 import BeautifulSoup
import requests
import time
import json

CACHE_FILE_NAME = 'recipe_cache.json'

def load_cache(CACHE_FILE_NAME):
    try:
        cache_file = open(CACHE_FILE_NAME, 'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache


def save_cache(CACHE_FILE_NAME, cache):
    cache_file = open(CACHE_FILE_NAME, 'w')
    contents_to_write = json.dumps(cache)
    cache_file.write(contents_to_write)
    cache_file.close()

class Recipe:
    def __init__(self, name,ingre=[], cooktime={}, url = ''):
        self.name = name
        self.ingre = ingre
        self.cooktime = cooktime
        self.url = url
    
    def json(self):
        return {
            'url' : self.url,  
            'name' : self.name, 
            'ingredient': self.ingre,
            'cooktime': self.cooktime,
        }


        
def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup
    
        
def get_recipe_time(url):
    try:
        soup = get_soup(url)

        recipe_time_tag= soup.find('div', class_='wprm-recipe-block-container wprm-recipe-block-container-separated wprm-block-text-normal wprm-recipe-time-container wprm-recipe-cook-time-container')
        # print(recipe_time_tag)
        cook_time_compose = recipe_time_tag.find_all('span', recursive=False)
        # cook_time = {cook_time_compose[0].text.strip(): cook_time_compose[1].text.strip()}
        cook_time = cook_time_compose[1].text.strip()
        return(cook_time)
    except:
        return ''

def get_recipe_ingre(url):
    try:
        soup = get_soup(url)

        recipe_ingre_tag_list = soup.find_all('ul', class_='wprm-recipe-ingredients')
        recipe_ingre_list = []
        for tag_list in recipe_ingre_tag_list:
            recipe_ingre_list_in = tag_list.find_all('li', class_='wprm-recipe-ingredient')
            recipe_ingre_list = recipe_ingre_list + recipe_ingre_list_in

        ingredient_list = []
        for i in recipe_ingre_list:
            ingre = i.find('span', class_='wprm-recipe-ingredient-name').text.strip().lower()
            ingredient_list.append(ingre)
        return ingredient_list
    except:
        return []

def get_recipe_name(url):
    try:
        soup = get_soup(url)

        recipe_name = soup.find('h1', class_='entry-title').text.strip()

        return recipe_name
    except:
        return ""

def convert_time(time):
    """
    convert a string to a int with unit of minutes
    """
    time_dict = {}
    time_list = time.split()
    time = 0
    
    try:
        
        for i in range(len(time_list)):
            try:
                time_list[i] = int(time_list[i])
            except:
                continue

        for i in time_list:
            if isinstance(i, int):
                position = time_list.index(i) + 1
                if 'm' in time_list[position]:
                    time = time+i
                elif 'h' in time_list[position]:
                    time = time + i * 60

            else:
                continue

        # print(time)
        return time
    
    except:
        return 0

def create_recipe(url):
    
    name = get_recipe_name(url)
    ingre = get_recipe_ingre(url)
    cooktime_str = get_recipe_time(url)
    # print(type(cooktime_dic['Cook Time']))
    cooktime = convert_time(cooktime_str)
    
    recipe_class = Recipe(name, ingre, cooktime, url)
    
    return recipe_class

def get_kind_url(base_recipe_url):
    soup = get_soup(base_recipe_url)
    recipe_url_tag = soup.find('div', class_='kt-row-column-wrap kt-has-6-columns kt-gutter-default kt-v-gutter-default kt-row-valign-top kt-row-layout-equal kt-tab-layout-two-grid kt-m-colapse-left-to-right kt-mobile-layout-two-grid')
    url_div_list = recipe_url_tag.find_all('div', recursive=False)
    
    url_list = []
    for div in url_div_list:
        url_a = div.find('a')
        # print(url_a)
        url = url_a['href']
        url_list.append(url)     
    return url_list

def get_recipe_url(base_url):
    soup = get_soup(base_url)
    recipe_list_parent = soup.find('div', class_='content-wrap grid-cols post-archive grid-sm-col-2 grid-lg-col-3 item-image-style-above')
    # print(recipe_list_parent)
    recipe_list_article = recipe_list_parent.find_all('article')
    # print(len(recipe_list_article))
    url_list = []
    for recipe in recipe_list_article:
        recipe_block = recipe.find('a')
        recipe_url = recipe_block['href']
        url_list.append(recipe_url)
    return url_list


def get_recipe_using_cache(url, cache):
    url_list = [recipe['url'] for recipe in cache]

    if url in url_list: # the url is our unique key
        print("Using cache")
        recipe = cache[url_list.index(url)]
        return recipe
    
    else:
        print("Fetching")
        # time.sleep(1)
        recipe = create_recipe(url).json()
        cache.append(recipe)
        save_cache(cache)
        return recipe

def get_results(ingr1, ingr2, cache):
    while True:
        count_str = input('Enter the maximum number of recipes to retrieve: ')
        try:
            count_int = int(count_str)
        except:
            print("Please enter a valid number greater than 0.")
            continue
        if count_int < 1 or count_int > 30:
            print("Please enter a valid number between 1 and 30, inclusive.")
            continue
        break
         
    result_list = []
       
    for recipe in cache:
        ingr_str = ''
        for ingr in recipe['ingredient']:
            ingr_str = ingr_str + ingr
            
        if ingr1 in ingr_str and ingr2 in ingr_str:
            result_list.append(recipe)
            
            if len(result_list) == count_int:
                break

    return result_list





def main():
    

    base_recipe_url = 'https://www.indianhealthyrecipes.com/recipes/'
    category_url = get_kind_url(base_recipe_url)
    # print(category_url)

    # recipe_list_total = []
    # for url in category_url:
    #     recipe_list = get_recipe_url(url)
    #     recipe_list_total = recipe_list_total + recipe_list


    # recipe_json_list = []
    # for url in recipe_list_total:
    #     recipe_class = create_recipe(url).json()
    #     recipe_json_list.append(recipe_class)


        
    # save_cache('recipe_cache_2.json', recipe_json_list)

    cache = load_cache('recipe_cache.json')

    recipe_list_new = []
    while True:
        
        keyword1 = input('Please enter a ingredient you have, or "exit" to quit: ').lower()
        
        if keyword1 == 'exit':
            print('Bye!')
            break
            
        else: 
            keyword2 = input('Please enter another ingredient you have: ').lower()
            recipe_list = get_results(keyword1, keyword2, cache)
            
        if recipe_list == []:
            print("Sorry, we can't find any recipe that contains these ingredients. Please try something else.")

        else:
            print('We have found some recipes for you! Now please tell us more information to shorten the list.')
            while True:
                time_input = input('Do you want recipes that take less than or equal to 20 min to cook? (y/n) ')
                if time_input.lower() in ['y', 'yes', 'yep'] :
                    recipe_list_new = [recipe for recipe in recipe_list if recipe['cooktime'] == 20 or recipe['cooktime'] < 20]
                    # break
                elif time_input.lower() in ['no', 'n', 'nope']:
                    recipe_list_new = [recipe for recipe in recipe_list if recipe['cooktime'] > 20]
                    # break
                else:
                    print("Please input 'y' or 'n': ")

                if recipe_list_new == []:
                    print("Sorry, we couldn't find any recipes that fit the time requirement. Please try a different option.")
                else:
                    break

            number = 0
            for recipe in recipe_list_new:
                number = number + 1 
                print(str(number) + '. ' + recipe['name'])
            
            # while True:
            #     term = input('Please enter a number to get the full recipe: ')
            #     try:
            #         number_int = int(term)
            #         if number_int < 1:
            #             print('Please enter a number larger than 0.')
            #         elif number_int > len(recipe_list_new):
            #             print('Please enter a valid number less than the largest number in the list above.')
            #         else:
            #             break
            #     except:
            #         print('Please enter a valid number.')

            while True:
                term = input('Please enter a number to get the full recipe: ')
                try:
                    number_int = int(term)
                    if number_int < 1 or number_int > len(recipe_list_new):
                        print('Please enter a valid number between 1 and', len(recipe_list_new), 'inclusive.')
                    else:
                        position = number_int - 1
                        result = recipe_list_new[position]
                        break
                except:
                    print('Please enter a valid number.')

            
            
            position = number_int - 1
            result = recipe_list_new[position]
            
            # print(result['ingredient'])
            print('Ingredient List:')
            for ingr in result['ingredient']:
                print(ingr)
            
            print('Launching ' + result['url'] + ' in web broswer...')
            # break

    



if __name__ == '__main__':
    main()