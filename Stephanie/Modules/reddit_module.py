from Stephanie.Modules.base_module import BaseModule
import praw
import webbrowser

class RedditModule(BaseModule):

    def __init__(self, *args):

        super(RedditModule,self).__init__(*args)
        self.client_id = self.get_configuration("reddit_client_id")
        self.client_secret = self.get_configuration("reddit_client_secret")
        self.username = self.get_configuration("reddit_username")
        self.password = self.get_configuration("reddit_password")
        self.user_agent = self.get_configuration("reddit_user_agent")
                #When creating a reddit app on the reddit website to gain access to the API ID's and Secret's, it will prompt you for a redirect uri. Make it "http://localhost:8080"

    def ObtainSubreddit(self):

        r = praw.Reddit(self.client_id, self.client_secret, self.password, self.user_agent, self.username)
        self.assistant.say("What subreddit do you want to open and get information on?")
        Users_Subreddit= self.assistant.listen().decipher()
        subreddit = r.subreddit(Users_Subreddit)
        self.assistant.say("Here is some information that I found for you. Here are the subreddit's name, its title, and a description of it.")
        print(subreddit.display_name)
        print(subreddit.title)
        print(subreddit.description)
        self.assistant.say("Would you like to open the website?")
        YesOrNo= self.assistant.listen().decipher()
        if YesOrNo == "yes":
            webbrowser.open('http://www.reddit.com/'+Users_Subreddit)
        else:
            self.assistant.say("No Problem.")

    def Submissions(self):
        r = praw.Reddit(self.client_id, self.client_secret, self.password, self.user_agent, self.username)
        self.assistant.say("What Subreddit's submissions would you like to analyze?")
        Users_Subreddit = self.assistant.listen().decipher()
        subreddit = r.subreddit(Users_Subreddit)
        self.assistant.say("Awesome, I opened up {0}. What kind of submissions would you like to obtain? Say something like 'controversial, gilded, hot, new, rising, top'".format(Users_Subreddit))
        Users_Submission_Type= self.assistant.listen().decipher
        if Users_Submission_Type != "controversial" or "gilded" or "hot" or "new" or "rising" or "top":
            self.assistant.say("Sorry I didn't quite get that. Breaking")
            exit()
        self.assistant.say("Here are the 10 submissions of submission type {0} and general information about them".format(Users_Submission_Type))
        for submission in subreddit.Users_Submission_Type(limit=10):
            print("Here is the submission title: " + submission.title)
            print("This is its score" + submission.score)
            print("The submission id: " + submission.id)
            print("and finally, the submission url: " + submission.url)
