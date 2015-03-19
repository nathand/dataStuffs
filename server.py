from flask import Flask
from flask import render_template
import ConfigParser
import twitter
app = Flask(__name__)


WORLD_WOE_ID = 1
US_WOE_ID = 23424977
## twitter credentials
t = {}
allTrends = {}
def getTwitterApi():
    Config = ConfigParser.ConfigParser()
    Config.read('config.ini')
    section = "Twitter"
    conf = Config.options(section)
    for option in conf:
        t[option] = Config.get(section, option)
    auth = twitter.oauth.OAuth(t['oauthtoken'], t['oauthtokensecret'], t['consumerkey'], t['consumersecret'])
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

def trends():
    trends = {}
    trends['world'] = twitter_api.trends.place(_id=WORLD_WOE_ID)
    trends['us'] = twitter_api.trends.place(_id=US_WOE_ID)
    print(trends)
    #print json.dumps(trends, indent=1)
    return trends

@app.route("/")
def hello():
    return render_template('index.html')

twitter_api = getTwitterApi()
allTrends = trends()
if __name__ == "__main__":
    app.run()
