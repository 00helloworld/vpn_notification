import http.client, urllib
from confs import push_token, push_user

def pushover(message):
    # Need to pay
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", 
                 "/1/messages.json",
                urllib.parse.urlencode({
                    "token": push_token,
                    "user": push_user,
                    "message": message,
                }), 
                { "Content-type": "application/x-www-form-urlencoded" })
    return conn.getresponse().status

if __name__ == '__main__':
    print(pushover('hello') == 200)