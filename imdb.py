import requests
import  os, sys ,re ,json

class ImdbRating(object):

    def __init__(self, dirpath=os.getcwd()):
        self.dirpath = dirpath
        self.year = None
        self.name = None

    def createurl(self):
        print self.name
        print self.year
        url = "http://www.omdbapi.com/?t="+self.name.replace(" ", "+")+"&y="+str(self.year)+"&plot=short&r=json"
        return url

    def getinfo(self):
        extentions = [".mp4", ".3gp",".mkv"]
        for path, subdir, fileslist in os.walk(self.dirpath):
            for name in fileslist:

                    # print year
                if any(ext in name for ext in extentions):
                    # print  name
                    name = re.sub('[^0-9a-zA-Z]+', " ",name)[:-3]

                    years = ([yr for yr in [int(year) for year in re.findall('\d+', name) if year.isdigit()] if len(str(yr)) == 4 ])

                    if years:
                        name = name.split(str(years[0]))
                        # print name[0]
                        # print years[0]
                        self.name = name[0]
                        self.year = years[0]
                    else:
                        # print name
                        self.name = name
                    self.getrating()

    def getrating(self):
        url = self.createurl()
        print  url

        try:
            responsedata = requests.get(url)

            if responsedata.status_code == 200:
                responsejson = json.loads(responsedata.text)
                print responsejson.get("Title")
                print responsejson.get("imdbRating")
                print ("\n\n")
        except:
            raise Exception("get request error")



def main():
    if len(sys.argv) > 1:
        imdbobj = ImdbRating(sys.argv[1])
        imdbobj.getinfo()
    else:
        imdbobj = ImdbRating()
        imdbobj.getinfo()

if __name__ == '__main__':
    main()