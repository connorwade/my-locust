import random

"""
Updated on Aug 9th 2023 by Connor Wade
Using this site as source: https://www.useragents.me/
We can probably just download the JSON in the future, but it comes with a lot of info we don't need and I don't want to deal with it right now
"""
user_agents = {
    "chrome-windows-lts": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "edge-windows-lts": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188",
    "chrome-mac-lts": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "safari-mac-lts": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
    "ff-windows-lts": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",     
    "chrome-android-lts": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.3",
    "safari-ios-lts": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.2 Mobile/15E148 Safari/604.",
    "chrome-ios-lts": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.5672.69 Mobile/15E148 Safari/604.",
}

# As fraction of market share (does not add to 1 - ommitted values)
# Order is important! We can fix with sorting, but be sure to do that globally on initialization rather than everytime the function is called
market_share = {
    "chrome-ios-lts": .0100,     
    "ff-windows-lts": .0311,
    "safari-mac-lts": .0392,
    "chrome-mac-lts": .0673,
    "safari-ios-lts": .1030,
    "edge-windows-lts": .1381,
    "chrome-windows-lts": .2144,
    "chrome-android-lts": .5228,
}

def get_random_agent():
    rand = random.uniform(0,1)
    # reduce as you go
    run = 0
    for user_key in market_share:
        run += market_share[user_key]
        if rand <= run:
            return user_agents[user_key]

    # Fallback
    return user_agents["chrome-android-lts"]    