import requests
from bs4 import BeautifulSoup
def reviewScraper(url, page_no):

    my_url = url
    #print(htmlcontent)
    base_url = my_url + "&pageNumber="
    # page = 1
    response = []
    print(page_no,"extraaaaaa")
    for page in range(1, int(page_no) + 1):
        print("Running ",page)
    # while page != page_no:
        star_rating = []
        reviewerName = []
        comments = []
        date = []
        title = []
        url = base_url + str(page)
        r = requests.get(url)
        print(url)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        reviewDiv = soup.find_all("div", {"id": "cm_cr-review_list"})
        for Div in reviewDiv:
            for tag in Div.find_all(class_="review-rating"):
                star_rating.append(tag.get_text(strip=True))
            print(len(star_rating))
            for tag in Div.find_all(class_="review-text-content"):
                comments.append(tag.get_text(strip=True))
            print(len(comments))
            for tag in Div.find_all(class_="a-profile-name"):
                reviewerName.append(tag.get_text(strip=True))
            print(len(reviewerName))
            for tag in Div.find_all(class_="review-date"):
                date.append(tag.get_text(strip=True))
            print(len(date))
            for tag in Div.find_all(class_="review-title"):
                title.append(tag.get_text(strip=True))
            print(len(title))
        print("\n")
        for i in range(0,len(comments)):
            my_dict={"name": reviewerName[i],"stars": star_rating[i],"date": date[i],"title": title[i], "review": comments[i]}
            response.append(my_dict)

        # page = page+1
    print("LENGTH ",len(response))
    return response
