import kivy
kivy.require('1.8.0') # replace with your current kivy version !
"""root.x is the reference to x of the root(root app which here is MyChatBot class)
root.top is referencing to the top of the app(here MyChatBot)
self.height is referencig self of the widget"""
from kivy.app import App
from kivy.uix.widget import Widget


from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

bot=ChatBot('Training Example')
trainer=ChatterBotCorpusTrainer(bot)
trainer2=ListTrainer(bot)
trainer.train("chatterbot.corpus.english","chatterbot.corpus.french")
con=open('conversation.txt','r').readlines()
trainer2.train(con)

class MyScreen(Widget):
    def change(self):
        request = self.ids.t_in.text
        if request=="":
            self.ids.lbl.text="don't you wanna say sth!"
        else:
            response = bot.get_response(request)
            response = str(response)
            self.ids.lbl.text = response
            self.ids.t_in.text=''

class MyChatBot(App):

    def build(self):
        return MyScreen()

if __name__ == '__main__':
    MyChatBot().run()