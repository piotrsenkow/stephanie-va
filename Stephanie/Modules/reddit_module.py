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
                #When creating a reddit app to gain access to the API ID's and Secret's, it will prompt you for a redirect uri. Make it "http://localhost:8080"
        if self.client_id and self.client_secret and self.username and self.password and self.user_agent:
            self.reddit_login()
        else:
            return False

    def reddit_login(self):
        reddit = praw.Reddit(self.client_id,self.client_secret,self.password,self.user_agent,self.username)
        return reddit


    def OpenSubreddit(self):

        self.assistant.say("What subreddit do you want to open?")
        user_command = self.assistant.listen().decipher()
        webbrowser.open('http://www.reddit.com/'+user_command)
