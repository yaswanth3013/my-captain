import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/best-sellers-books-Amazon/zgbs/books"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

books = soup.find_all("div", class_="a-section a-spacing-none p13n-asin")

for i in range(10):
    book = books[i]
    title = book.find("span", class_="a-size-medium a-color-base a-text-normal").text.strip()
    price = book.find("span", class_="a-offscreen").text.strip()
    print(f"{i+1}. {title} - {price}")
"""
output:
1. Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones - $11.98
2. The Four Winds: A Novel - $19.49
3. The Code Breaker: Jennifer Doudna, Gene Editing, and the Future of the Human Race - $18.00
4. American Marxism - $16.80
5. We Were Never Here: A Novel - $12.29
6. The Midnight Library: A Novel - $13.38
7. The Sanatorium: A Novel - $11.99
8. The Invisible Life of Addie LaRue - $12.99
9. The Body Keeps the Score: Brain, Mind, and Body in the Healing of Trauma - $11.66
10. Greenlights - $14.08
"""
