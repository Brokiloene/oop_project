from bs4 import BeautifulSoup
import random
import requests
import time
import json
import secrets


def get_data():
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0"
    }
    # get page with all recipes

    time.sleep(random.randrange(1, 4))
    req = requests.get("https://kedem.ru/recipe/?ysclid=lamd6hca9r933387071", headers=headers)

    page = BeautifulSoup(req.text, "lxml")
    menus = [el.get("href") for el in page.find_all("a", class_="menupage")]


    step = 1
    total_recipes = 0
    with open("res.txt", "a") as file:
        for el in menus:
            print("Step = {}".format(step))
            print(f"total_recipes = {total_recipes}")
            step += 1
            link = "https://kedem.ru/" + el
            time.sleep(random.randrange(1, 4))
            req = requests.get(link, headers=headers)

            page = BeautifulSoup(req.text, "lxml")
            try:
                total_pages = int(page.find("span", id="totalPages").text)
            except:
                total_pages = 1
            for i in range(1, total_pages + 1):
                #print(f"cur_step = {i}")
                dishes = [(el.get("title"), el.get("href")) for el in page.find_all("a", class_="recipeblocktext")]
                total_recipes += len(dishes)
                for dish in dishes:
                    link = "https://kedem.ru/" + dish[1]
                    time.sleep(random.randrange(1, 4))
                    req = requests.get(link, headers=headers)
                    # with open("text.html", "w") as file:
                    #     file.write(req.text)
                    page_rec = BeautifulSoup(req.text, "lxml")
                    recipe = ""
                    for x in page_rec.find_all("div", itemprop="recipeInstructions"):
                        recipe += "".join(x.text.strip().replace("\n", ''))
                    dish_name = "<s>" + "Название: " + (dish[0]).upper() + " "
                    dish_rec = "Рецепт: " + recipe + "</s>\n"
                    file.write(dish_name + dish_rec)

                try:
                    link = "https://kedem.ru" + page.find("a", id="btnextlink").get("href")
                    time.sleep(random.randrange(1, 4))
                    req = requests.get(link, headers=headers)
                    page = BeautifulSoup(req.text, "lxml")
                except:
                    continue;


def main():
    start_time = time.time()
    get_data()
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()