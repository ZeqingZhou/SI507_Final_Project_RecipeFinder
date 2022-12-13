# SI507_Final_Project_RecipeFinder

RecipeFinder is a tool for finding delicious recipes. With RecipeFinder, you can easily search for recipes using the ingredients you have on hand, and quickly find recipes that match your preferences. All of the recipes in RecipeFinder are scraped from a popular Indian recipe website https://www.indianhealthyrecipes.com/ , so you can be sure you're getting authentic and delicious recipes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to have the following libraries installed:

- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)
- [Requests](https://pypi.org/project/requests/)

You can install these libraries using `pip`:
`pip install beautifulsoup4`
`pip install requests`

### Installing

To download and set up the project on your local machine, follow these steps:

Download `Final_proj_RecipeFinder.py` and `recipe_cache.json`. Put them in one folder. Open `Final_proj_RecipeFinder.py` with VScode, and run the whole profile. 

## Usage

To run the program, use the following command:
`python Final_proj_RecipeFinder.py`

This will scrape recipe data from a website, create `Recipe` objects for each recipe, and save the data to a cache file. When the program is run again, it will load the cache file and convert the saved data back into `Recipe` objects.

## Features

- Search for recipes using the ingredients you have on hand
- Find recipes that match your time preference 
- Browse a collection of delicious and authentic Indian recipes

## Contributing

We welcome contributions to RecipeFinder! If you have an idea for a new feature or improvement, please open an issue or submit a pull request.

