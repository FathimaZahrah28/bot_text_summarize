!pip install -U spacy
!python -m spacy download en_core_web_sm
!pip install pytelegrambotapi

import telebot
import logging

api = '5286963937:AAGBxchEzCKM3MUQFr_viGjhrsmcvLaCJzs'
bot = telebot.TeleBot(api)

#menghandle pesan / start
@bot.message_handler(commands=['start'])
def welcome(message):
    #balas pesannya
    bot.reply_to(message, "Halo, Selamat Datang di Bot untuk meringkas Berita. Jika anda ingin meringkas berita klik /Ringkass" )
@bot.message_handler(commands=['help'])
def Bantuan(message):
    #balas pesannya
    bot.reply_to(message, "if you have question please call 0858xxxx" )
    
@bot.message_handler(commands=['ringkass'])
def ringkas(message):
    bot.reply_to(message, 'Untuk Teks Berita menggunakan Bahasa Indonesia ketik format : /ID pada atas teks kemudian teks berita pada bawahnya. apabila inggris ketik format : /EN pada atas teks kemudian teks berita pada bawahnya.')
   
    
@bot.message_handler(commands=['EN'])   
def EN (message):
    text = message.text.replace('EN', "")
    
    import spacy
    from spacy.lang.en.stop_words import STOP_WORDS
    from string import punctuation
    from heapq  import nlargest
    
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    tokens = [token.text for token in doc]
    punctuation = punctuation + '\n'
    word_frequencies = {}
    
    for word in doc :
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                     word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
        
                
    max_frequency = max(word_frequencies.values())
    
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency
    
    sentence_tokens = [sent for sent in doc.sents]
    
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                     sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]
                
    
    select_length = int(len(sentence_tokens)*0.3)
    
    summary = nlargest(select_length, sentence_scores, key= sentence_scores.get)
    
    final_summary = [word.text for word in summary]
    
    summary = ' '.join(final_summary)
    
    bot.send_message(message.chat.id, summary)
    
    
@bot.message_handler(commands=['ID'])   
def ID (message):
    text = message.text.replace('ID', "")
    
    import spacy
    from spacy.lang.id.stop_words import STOP_WORDS
    from string import punctuation
    from heapq  import nlargest
    
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    tokens = [token.text for token in doc]
    punctuation = punctuation + '\n'
    word_frequencies = {}
    
    for word in doc :
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                     word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
        
                
    max_frequency = max(word_frequencies.values())
    
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency
    
    sentence_tokens = [sent for sent in doc.sents]
    
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                     sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]
                
    
    select_length = int(len(sentence_tokens)*0.3)
    
    summary = nlargest(select_length, sentence_scores, key= sentence_scores.get)
    
    final_summary = [word.text for word in summary]
    
    summary = ' '.join(final_summary)
    
    bot.send_message(message.chat.id, summary)

updater.bot.setWebhook(updater.bot.setWebhook('https://ngeringkasyuk.herokuapp.com'+5286963937:AAGBxchEzCKM3MUQFr_viGjhrsmcvLaCJzs))
updater.idle()
bot.polling() #suapay bot selalu dalam keadaan standby dan menerima masage yg masuk





