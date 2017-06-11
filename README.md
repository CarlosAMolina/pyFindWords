# pyFindWords
This script allows you to find several words with only one search.

The script retrieves the number of searches for each word, the word does not need to match exactly.

How it works:
- wordsToFind.txt: write here words you want to search
- fileWhereFindWords.txt: text where find desired words
- web.html: you can analyze an URL instead of the .txt file. Web html code is saved in web.html

Available options
- f=file. Checks if words in wordsToFind.txt are in fileWhereFindWords.txt
- r=repeated. Search in fileWhereFindWords.txt the number of times each word appears
- w=web. Checks if words in wordsToFind.txt are in the specified web page. Web html code is saved in web.html

Example
- words2find.txt:

   git people

   car

- fileWhereFindWords.txt:

   GitHub

   How people build software

- result:

   git: 1 (0 extact, 1 partial)

   people: 1 (1 extact, 0 partial)

   car: 0 (0 extact, 0 partial)
   
Execution example
- python findWords.py w https://github.com/ Built for developers
