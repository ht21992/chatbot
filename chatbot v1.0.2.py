from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

bot=ChatBot('Training Example')
trainer=ChatterBotCorpusTrainer(bot)
trainer2=ListTrainer(bot)
con=open('conversation.txt','r').readlines()
trainer.train("chatterbot.corpus.french","chatterbot.corpus.english")
trainer2.train(con)
while True:
    request=input("you: ")
    if request =="":
        response=bot.get_response("nothing")
        print("Bot: " + str(response))
    else:
        response=bot.get_response(request)
        print("Bot: "+ str(response))