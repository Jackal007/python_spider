from random import randint

def getProxy():
    proxies = (
            '123.134.185.11',
            '115.228.107.142',
            '180.76.135.145',
            '58.218.198.61',
            '110.72.43.148',
        )
    return proxies[randint(0, len(proxies) - 1)]
    
