import requests  
  
def get_url(url, headers, times = 1):  
    try:  
        for i in range(times):  
            requests.get(url, headers = headers)  
            print('Request %s %d times'%(url, i))  
    except:  
        print('error')  
  
if __name__ == '__main__':  
    url = 'http://blog.csdn.net/mmozhang/article/details/48914233'  
    headers = dict()  
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'  
    #headers['Connection'] = 'keep-alive'  
    get_url(url, headers, 5)  

