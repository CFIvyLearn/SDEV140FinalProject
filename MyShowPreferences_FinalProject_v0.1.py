#Final GUI Project: Your Show Preferences
#Chanse Franklin

#import from breezy
from breezypythongui import EasyFrame

class ShowPref(EasyFrame):
    #application window
    def __init__(self):
        #initializes window and widgets
        EasyFrame.__init__(self, title = "Your Show Preferences")
        self.addLabel(text = "Enter the show's name or enter !@#$ to quit", row = 0,
                      column = 0)
        self.show = self.addTextField(value = "", row = 0, column = 1)
        self.addButton(text = "Add", row = 1, column = 0,
                       columnspan = 2, command = self.addShow)
        #initializes group of parallel lists to hold data about every show
        showList = []
        scoreList = []
        episodeLength = []
        yearList = []
        genreList = []
        ratingList = []
        studioList = []

        def addShow(self):
            newShow = self.show.get()
            if newShow = "!@#$":
                calculations()
                displayData(self)
            else:
                showList.append(newShow)
                secondScreen(self)
                

        def secondScreen(self):
            self.addLabel(text = "Enter your score from 1 to 10",
                          row = 0, column = 0)
            self.score = self.addIntegerField(value = 0, row = 0, column = 1)
            self.addLabel(text = "Enter the number of episodes",
                          row = 1, column = 0)
            self.episodes = self.addIntegerField(value = 0, row = 1, column = 1)
            self.addLabel(text = "What year did the show release?",
                          row = 2, column = 0)
            self.year = self.addIntegerField(value = 0, row = 2, column = 1)
            self.addLabel(text = "What genre of show is it? ex: drama, action, mystery",
                          row = 3, column = 0)
            self.genre = self.addTextField(value = "", row = 3, column = 1)
            self.addLabel(text = "Enter the age rating of the show",
                          row = 4, column = 0)
            self.rating = self.addTextField(value = "", row = 4, column = 1)
            self.addLabel(text = "Enter the studio who made the show",
                          row = 5, column = 0)
            self.studio = self.addTextField(value = "", row = 5, column = 1)
            self.addButton(text = "Add", row = 6, column = 0, columnspan = 2,
                           command = self.addInfo)

        def addInfo(self):
            newScore = self.score.getNumber()
            scoreList.append(newScore)
            newEpisodes = self.episodes.getNumber()
            episodeLength.append(newEpisodes)
            newYear = self.year.getNumber()
            yearList.append(newYear)
            newGenre = self.genre.get()
            genreList.append(newGenre)
            newRating = self.rating.get()
            ratingList.append(newRating)
            newStudio = self.studio.get()
            studioList.append(newStudio)

            self.addLabel(text = "Enter the show's name or enter !@#$ to quit", row = 0,
                          column = 0)
            self.show = self.addTextField(value = "", row = 0, column = 1)
            self.addButton(text = "Add", row = 1, column = 0,
                           columnspan = 2, command = self.addShow)
            
        def calculations():


        def displayData(self):
            
