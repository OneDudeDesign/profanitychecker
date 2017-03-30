import urllib


def read_text():
    quotes = open('/Users/clucier/Desktop/ODD/Udacity/pf-python/profanity/movie_quotes.txt')
    contents_of_file = quotes.read()
    print (contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    # print (output)
    connection.close()
    if "true" in output:
        print ("Profanity has been found in your file!!")
    elif "false" in output:
        print ("Your file is clean and ready to send!!")
    else:
        print ("Your file could not be checked, check for errors!")

read_text()
