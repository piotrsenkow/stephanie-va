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

    def obtain_subreddit(self):

        r = praw.Reddit(client_id = self.client_id, client_secret = self.client_secret,password= self.password, user_agent=  self.user_agent,username = self.username)
        self.assistant.say("What subreddit do you want to open and get information on?")
        Users_Subreddit= self.assistant.listen().decipher()
        subreddit = r.subreddit(Users_Subreddit)
        self.assistant.say("Here is some information that I found for you. Here are the subreddit's name, its title, and a description of it")
        print(subreddit.display_name)
        print(subreddit.title)
        print(subreddit.description)
        self.assistant.say("Would you like to open the website?")
        YesOrNo= self.assistant.listen().decipher()
        if YesOrNo == "yes":
            webbrowser.open('http://www.reddit.com/r/'+Users_Subreddit)
        else:
            self.assistant.say("No Problem.")
        return 0

    def search_subreddit(self):
        self.assistant.say("What subreddit would you like to look up?")
        SearchTerm = self.assistant.listen().decipher()
        self.assistant.say("Okay. Let me look that up for you.")
        webbrowser.open('https://www.reddit.com/subreddits/search?q='+SearchTerm)
        return 0
