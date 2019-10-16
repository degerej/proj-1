# Joe Degere
# October 14th 2019
# Project 1

cookies = []
candies = []


def cookies_input():
    for i in range(0,6):
        value = int(input("Type the numbers that will be added to the cookie sales:"))
        cookies.append(value)
    print(cookies)


def cookies_avg():
    sum = 0
    for cookie in cookies:
        sum = sum + cookie
    avg = sum /6
    print(f"The average amount of cookies is {avg}")


def candies_input():
    for i in range (0,6):
        value = int(input("Type the numbers that will be added to candy sales:"))
        candies.append(value)
    print(candies)


def candy_avg():
    sum = 0
    for candy in candies:
        sum = sum + candy
    avg = sum /6
    print(f"The average amount of candies is {avg}")


def max_cookies():
    co_value1 = max(cookies)
    print(f"The max value of cookies: {co_value1}")


def max_candies():
    ca_value1 = max(candies)
    print(f"The max value of candy: {ca_value1}")


def min_cookies():
    co_value2 = min(cookies)
    print(f"The min value for cookies: {co_value2}")


def min_candies():
    ca_value2 = min(candies)
    print(f"The min value of candy: {ca_value2}")


cookies_input()
cookies_avg()
candies_input()
candy_avg()
max_cookies()
min_cookies()
max_candies()
min_candies()
cookies_sum = sum(cookies)
candies_sum = sum(candies)


if cookies_sum > candies_sum:
    print("Cookies at the Hartwick Bakery are the most popular!")
else:
    print("Candy at the Hartwick Bakery is the most popular!")
