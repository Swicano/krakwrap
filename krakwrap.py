#
# This program extends the Krakenex library by veox (github.com/veox/python3-krakenex): 
#   It does some minor error checking:
#
#
#   It reorganizes the response into a shape that we like for db insertion
#
#
#
#
#   


import krakenex


baseurl = 'https://api.kraken.com/0/'
urlext = 'public/Assets'
payload = {'info':'info','aclass':'currency','asset':'ZUSD,XXDG'}

payload = {'asset':'ZUSD,XXDG'}
payload = {'aclass':'currency'}
payload = {'aclass':'currency','asset':'ZUSD,XXDG'}
r = requests.post(baseurl+urltext, payload)
r.text

if __name__ == "__main__":
  print('hellos')
  
  