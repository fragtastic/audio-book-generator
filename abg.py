import requests
import os
import shutil

TTSLANGUAGE = 'en'
GoogleTTSURL = 'http://translate.google.com/translate_tts' #gets MP3 files

def get_audio_file(ttsText, fileNum):
    payload = {'tl': TTSLANGUAGE, 'q': ttsText}
    r3 = requests.post(GoogleTTSURL, data=payload)
    with open(str(fileNum) + ".mp3", "wb") as code:
      code.write(r3.content)
    print "Processed: \"" + ttsText + "\""

if __name__ == "__main__":
    inputFile = raw_input('Please enter a file: ')  #[:-1]
    outputFile = raw_input('Please enter output name: ')
    f = open(inputFile, 'r')
    all_words = map(lambda l: l.split(" "), f.readlines())
    fileNum = 0
    ttsText = ""
    for l in all_words:
        for w in l:
            if (len(ttsText) + len(w) + 1 > 100):
                get_audio_file(ttsText, fileNum)
                fileNum += 1
                ttsText = w
            else:
                if (len(ttsText) > 0):
                    ttsText += " "
                ttsText += w
        if (len(ttsText) > 0):
            get_audio_file(ttsText, fileNum)
            fileNum += 1
            ttsText = ""
    #combine all the mp3 files into one at the end. or while we're doing it?
    curFiNum = 0
    destination = open(outputFile + '.mp3', 'wb')
    print "Combining files"
    while (curFiNum < fileNum):
        shutil.copyfileobj(open(str(curFiNum) + ".mp3", 'rb'), destination)
        os.remove(str(curFiNum) + ".mp3")
        curFiNum += 1
    destination.close()