import gtts

print("Please Enter a Sentence to create audio (English) = ")
user_sentence = input()

# print(gtts.lang.tts_langs())
audio = gtts.gTTS(user_sentence,lang="en",slow=False)
audio.save("13-GTTS/user.mp3")
print("File Created!")
