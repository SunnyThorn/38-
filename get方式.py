import urllib
import urllib2
 
values={}
values['username'] = "1437594580@qq.com"
values['password']="q493230."
data = urllib.urlencode(values) 
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
