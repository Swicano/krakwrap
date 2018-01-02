#
# This program extends the Krakenex library by veox (github.com/veox/python3-krakenex): 
# and hopefully generalizes it a bit
#   It takes it from a class to an object (kinda useless but it kinda helps keep track if we have
#   multiple instances running
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
#'{"error":["EGeneral:Invalid arguments"]}'

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
    except requests.exceptions.HTTPError:
      # kraken has a 520 error problem right now, try it 5 times then give up
      if count > 0:
        time.sleep(1)
        self.query_public(method, data, count-1 )
      else:
        raise
    
  def query_private(self, method, data=None):
    try:
      self.resultRaw = self.api.query_private(method, data)
    except requests.exceptions.HTTPError:
      # kraken has a 520 error problem right now, try it 5 times then give up
      if count > 0:
        time.sleep(1)
        self.query_public(method, data, count-1 )
      else:
        raise
    except Exception as e:
      #the krakenex library is a little weird on this error, not sure if i want to deal with it at all
      if e.args[0] == "Either key or secret is not set! (Use `load_key()`.":
        print("Key/Secret Error, make sure you load the correct file or use query_public")
        # kick the can to get this caught in the error checking routine
        return {'error': ["EGeneral:Invalid arguments"], 'result': {}}
      else:
        raise


if __name__ == "__main__":
  
  print('hellos')
  
  