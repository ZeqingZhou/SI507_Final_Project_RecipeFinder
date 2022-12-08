# SI507_Final_Project_RecipeFinder

RecipeFinder is a tool for finding delicious recipes. With RecipeFinder, you can easily search for recipes using the ingredients you have on hand, and quickly find recipes that match your preferences. All of the recipes in RecipeFinder are scraped from a popular Indian recipe website https://www.indianhealthyrecipes.com/ , so you can be sure you're getting authentic and delicious recipes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to have the following libraries installed:

- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)
- [Requests](https://pypi.org/project/requests/)

You can install these libraries using `pip`:
pip install beautifulsoup4
pip install requests

### Installing

To download and set up the project on your local machine, follow these steps:

1. Clone the repository to your local machine using `git clone https://github.com/YOUR_USERNAME/recipe-scraper.git`
2. Navigate to the project directory using `cd recipe-scraper`
3. Install the required libraries using `pip install -r requirements.txt`

## Usage

To run the program, use the following command:
python recipe_scraper.py

This will scrape recipe data from a website, create `Recipe` objects for each recipe, and save the data to a cache file. When the program is run again, it will load the cache file and convert the saved data back into `Recipe` objects.

## Features

- Search for recipes using the ingredients you have on hand
- Find recipes that match your time preference 
- Browse a collection of delicious and authentic Indian recipes

## Contributing

We welcome contributions to RecipeFinder! If you have an idea for a new feature or improvement, please open an issue or submit a pull request.

