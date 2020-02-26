# Http_header
  
  解析超文本傳輸之請求與響應的標頭欄位
  
  
# Code Template, 代碼範例

see

<http://192.168.200.24:10080/tradsysdiv/fb/bondquotefetch/commits/QueenPy2>

usage of request 

<https://realpython.com/python-requests/>

#-----------------------------------------------------------------------------------------
    
# Request, 請求

![req](https://blog.kdchang.cc/2017/07/02/golang101-tutorial-web-basic/http-req.png)

        GET /storage/bond_zone/tradeinfo/internationalbond//2020/202002/FormosaCurve.20200218-C.xls HTTP/1.1
        
        Host: www.tpex.org.tw
        
        Connection: keep-alive
        
        Upgrade-Insecure-Requests: 1
        
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
        Sec-Fetch-User: ?1
        
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
        
        Sec-Fetch-Site: same-origin
        Sec-Fetch-Mode: navigate
        
        Referer: https://www.tpex.org.tw/web/bond/tradeinfo/internationalbond/FormosaDaily.php?l=zh-tw
        
        Accept-Encoding: gzip, deflate, br
        Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
        
        Cookie: _ga=GA1.3.1151499719.1581646624; _gid=GA1.3.567594650.1581921656
        
        If-Modified-Since: Tue, 18 Feb 2020 07:14:03 GMT
        
#-----------------------------------------------------------------------------------------

# Request Field, 請求的欄位

![req](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/1046558725/original/requestpacket.jpg?1477976118)

* Cache-Control: 'no-cache'

   to specify directives that must be obeyed by all caching mechanisms along the request-response chain.

* Accept: 'text/html'

   to sepecify the media type user accepts.
   
* Access-Control-Request-Method: GET

   see Access-Control-Allow-Methods: 'GET, POST' from Server side

   <http://192.168.200.24:10080/QC-109/8888/blob/master/README.md#response-field-%E9%9F%BF%E6%87%89%E7%9A%84%E6%AC%84%E4%BD%8D>        
     
* Forwarded: for=192.0.2.60;proto=http;by=203.0.113.43 

   to disclose original information of a Client connecting to a web Server through an HTTP Proxy.
   
* TE: trailers, deflate

   the TE means the Transfer Encodeing the user agent accepts. 
   
* X-Requested-With: XMLHttpRequest

   	to identify Ajax requests. Most JS frameworks send this field with value of XMLHttpRequest.
   	
* DNT: 1 (Do Not Track Enabled)

    to requests a web app to disable their tracking of a user. 

* X-Forwarded-For: client1, proxy1, proxy2

     A de facto standard for identifying the originating IP address of a client connecting to a web server through an HTTP proxy or load balancer. 
     Superseded by Forwarded header.
     
* X-Csrf-Token: i8XNjC4b8KVok4uw5RftR38Wgp2BFwql

     to be protected from prevent CSRF, cross-site request forgery.
     
![req headers](https://image.winudf.com/v2/image1/YWlyLmh0dHAucmVxdWVzdF9zY3JlZW5fNF8xNTUwMzAwNTc0XzAwOQ/screen-4.jpg?fakeurl=1&type=.jpg)
        
#-----------------------------------------------------------------------------------------

# Remote IP from Request, 使用者網路位置

<https://devco.re/blog/2014/06/19/client-ip-detection/>


* Direct Connection   

        REMOTE_ADDR: User IP
        HTTP_VIA: none
        HTTP_X_FORWARDED_FOR: none

* Transparent Proxy

        REMOTE_ADDR: last proxy server IP
        HTTP_VIA: proxy server IP
        HTTP_X_FORWARDED_FOR: user IP and next hops

* Anonymous Proxy

        REMOTE_ADDR: last hops
        HTTP_VIA: proxy server IP
        HTTP_X_FORWARDED_FOR: user IP and next hops

* High Anonymity Proxy (Elite Proxy)

        REMOTE_ADDR: proxy server IP
        HTTP_VIA: none
        HTTP_X_FORWARDED_FOR: npne
        
#-----------------------------------------------------------------------------------------       

# Start Server in golang, 啟動伺服器所需基本參數

            package main
            
            import (
                "fmt"
                "net/http"
                "log"
            )
            
            func helloHandler(w http.ResponseWriter, r *http.Request) {
                fmt.Fprintf(w, "hello world!")
            }
            
            func main() {
            
    
                http.HandleFunc("/", helloHandler)


                err := http.ListenAndServe(":7777", nil)
                if err != nil {
                    log.Fatal("ListenAndServe", err)
                } else {
            		log.Println("listen 7777")
            	}
            	
             }
 
#-----------------------------------------------------------------------------------------
 
# Response Header, 響應的標頭

![res header](https://1.bp.blogspot.com/-9hutlYT5g2E/Wo0_shCZSRI/AAAAAAAAAwU/37SqJGK82kIGZ842uApaGrBc4HEbwMQLgCLcBGAs/s1600/http%2Bresponse.png)

        HTTP/1.1 200 OK
        
        Date: Thu, 20 Feb 2020 00:26:12 GMT
        
        Server: Apache
        
        Vary: Origin
        
        X-XSS-Protection: 1;mode=block
        
        Last-Modified: Tue, 18 Feb 2020 07:14:03 GMT
        
        Accept-Ranges: bytes
        
        Content-Length: 34304
        
        Content-Security-Policy: frame-ancestors 'self' *.twse.com.tw *.tdcc.com.tw digitalprocesssys-epassbook.cdn.hinet.net http://digitalprocesssyst-epassbook.cdn.hinet.net;
        
        X-Frame-Options: ALLOW-FROM https://www.tpex.org.tw
        
        Content-Type: application/vnd.ms-excel
        
#-----------------------------------------------------------------------------------------

# Response Field, 響應的欄位

see code template in 8888(repo)/Server(flask app project)/ main.py

plz notice that the __ hiden mark will be escaped from markdown...

        from Api import app, d
        from Api import get_file
        
        @app.after_request
        def after_request(response):
        
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
            response.headers.add('Access-Control-Max-Age', '3600')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            response.cache_control.max_age = 1
         
            return response
        
        if __name__ == '__main__':
        
            app.run(host='0.0.0.0', port=8888)
            
head fields plz see wiki <https://en.wikipedia.org/wiki/List_of_HTTP_header_fields>

To specify which web sites can participate in CORS, Cross-Origin Resource Sharing.

        Access-Control-Allow-Origin: '*'
        
        Access-Control-Allow-Credentials: 'true'
        
        Access-Control-Expose-Headers: 
        
        Access-Control-Max-Age '3600' millisec = 3.6 sec
        
        Access-Control-Allow-Methods: 'GET, POST'
        
        Access-Control-Allow-Headers: 'Content-Type, Authorization'
 
 To be protected from click jack attacks, using the fowllowing headers field:
 
 
         X-Frame-Options: deny
        
    
 To ask caching mechanisms from server to client whether they may cache this object uains ms.
 
         
         Cache-Control: max-age=3600
         
         
 To raise a "File Download" dialogue box for a known MIME type with binary format 
 or suggest a filename for dynamic content. 
 
 
         Content-Disposition: attachment; filename="fname.ext"
         
         
 To specify an alternate location for the returned data.
 
  
         Content-Location: /index.htm
         
         
 An identifier for a specific version of a resource, often a message digest.
  
  
         ETag: "737060cd8c284d8af7ad3082f209582d"
         
         
Indicates the authentication scheme that should be used to access the requested entity.


         WWW-Authenticate: Basic
         
 
to specifies origins that are allowed to see val of attr ( retrieved via features of the Resource Timing API), 
which would otherwise be reported as zero due to CoRs, cross-origin restrictions. 


        Timing-Allow-Origin: *
        
 
to prevent from IE from MIME-sniffing a response away from the declared content-type.   


        X-Content-Type-Options: nosniff
        
        
to prevent from XSS, Cross-Sites Scripting Attacks


        X-XSS-Protection: 1; mode=block


#-----------------------------------------------------------------------------------------  

# Cookie in Req & Set-Cookie in Res, 餅乾和設定小餅乾

![ck](https://docs.microsoft.com/zh-tw/aspnet/web-api/overview/advanced/http-cookies/_static/image1.png)


* Cookie in Request


     Cookie: $Version=1; Skin=new; # User response the Value in Cookie fields. (After)


* Set-Cookie in Response


     Set-Cookie: UserID=JohnDoe; Max-Age=3600; Version=1 (Before)

        
#-----------------------------------------------------------------------------------------       
        
# TTFB in Response, 響應優化的要素(至第一字節時間)

Time to first byte (TTFB) is a measurement used as an indication of the responsiveness of a webserver or other network resource.

TTFB measures the duration from the user or client making an HTTP request to the first byte of the page being received by the client's browser.
This time is made up of the socket connection time, the time taken to send the HTTP request, 
and the time taken to get the first byte of the page. 

* Network

Although sometimes misunderstood as a post-DNS calculation, the original calculation of TTFB in networking 
always includes $network latency$ in measuring the time it takes for a resource to begin loading.

* Benchmark

Often, a smaller (faster) TTFB size is seen as a benchmark of a well-configured server application. 
For example, a lower time to first byte could point to fewer dynamic calculations being performed by the webserver, 
although this is often due to caching at either the DNS, server, or application level. 

* Static & Dynamic

More commonly, a very low TTFB is observed with statically served web pages, 
while larger TTFB is often seen with larger, dynamic data requests being pulled from a database.

<https://techmoon.xyz/ttfb/>

#-----------------------------------------------------------------------------------------

# General Header, 請求響應通用的標頭

![general](https://miro.medium.com/max/2448/1*-8Avv9KZTYRc9Pi_hZUROQ.png)

    A general header is an HTTP header that can be used in both request and response messages 
    but doesn't apply to the content itself. 
    Depending on the context they are used in, 
    general headers are either response or request headers. 
    However, they are not entity headers.
    The most common general headers are Date, Cache-Control or Connection.
    
    
        Request URL: https://www.tpex.org.tw/storage/bond_zone/tradeinfo/internationalbond//2020/202002/FormosaCurve.20200218-C.xls
        
        Request Method: GET
        
        Status Code: 304 Not Modified
        
        Remote Address: 210.63.162.130:443
        
        Referrer Policy: no-referrer-when-downgrade
        
![req_res](https://static.packt-cdn.com/products/9781789139433/graphics/3af82a56-a31d-4d63-a7fc-40992a5e0ef3.png)
        
#-----------------------------------------------------------------------------------------    

# Http Secure

![sec](https://www.dgqv.com/media/https_image.png)

discuss later on


