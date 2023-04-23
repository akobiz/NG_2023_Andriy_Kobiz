import requests

links = [
    "https://www.google.com/",
    "https://www.facebook.com/",
    "https://dou.ua/",
    "https://ua.linkedin.com/",
    "https://moodle.kntu.kr.ua/",
    "http://lok.com/"
]

responses = {
    "SUCCESS": {200: "OK",
                202: "Accepted",
                204: "No Content",
                301: "Moved Permamently",
                302: "Found"},
    "FAILED":  {400: "Bad request",
                401: "Unauthorized",
                402: "Payment Required",
                403: "Forbidden",
                404: "Not found",
                500: "Internal Server Error",
                501: "Not Implemented",
                502: "Bad Gateway",
                504: "Gateway Timeout"}
}

def ResponseResult(code):
    for key in responses.keys():
        if code in responses[key]:
            print(f" - {key}. | Status code: {code} {responses[key][code]}")

def statusCodeChecker():
    try:
        for link in links:
            request = requests.get(link)
            print(link, end='')
            ResponseResult(request.status_code)
    except Exception as e:
        print(e)

def main():
    statusCodeChecker()

if __name__ == "__main__":
    main()