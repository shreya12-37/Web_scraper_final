# Web Scraper - amazon.in
## Scrapes all reviews corresponding to product URL and page numbers given by user
### Link to working scraper - https://review-scraper-app.herokuapp.com/
The URL given by user has to be of the "all reviews page".

The url should look like this - 

https://www.amazon.in/Apple-MacBook-Pro-8th-Generation-Intel-Core-i5/product-reviews/B0883JQQJQ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews

Each page contains 9-10 reviews , number of pages has to be given accordingly.

Two files get downloaded on clicking namely summary.csv and reviews.csv.

Tech stack used :Frontend - React.js

Backend - Python (Framework - Flask) ; Modules used for scraping - BeautifulSoup(4) and Requests.
