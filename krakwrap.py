#
# This program extends the Krakenex library by veox (github.com/veox/python3-krakenex): 
# and hopefully generalizes it a bit
#   It does some minor error checking:
#     if requests library returns a 5xx http error, it retries a few times (5?)
#
#   It reorganizes the response into a shape that we like for db insertion
#
#
#   

import krakenex



#baseurl = 'https://api.kraken.com/0/'
#urlext = 'public/Assets'
#payload = {'info':'info','aclass':'currency','asset':'ZUSD,XXDG'}#
#
#payload = {'asset':'ZUSD,XXDG'}
#payload = {'aclass':'currency'}
#payload = {'aclass':'currency','asset':'ZUSD,XXDG'}
#r = requests.post(baseurl+urltext, payload)
#r.text

class wrappedAPI() :
  def __init__(self):
    self.api = krakenex.api.API(key='', secret='')
    self.resultRaw = {}
    self.resultFormatted = []
    
  def close(self):
    self.api.close()
  
  def load_key(self, path):
    self.api.load_key(path)
    
  def query_public(self, method, data=None, count=5):
    try:
      self.resultRaw = self.api.query_public(method, data)
    except HTTPError
      pass
    
  def query_private(self, method, data=None):
    self.resultRaw = self.api.query_private(method, data)

if __name__ == "__main__":
  
  print('hellos')
  
  