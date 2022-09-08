#Description: This is a basic chatbot program. Enjoy!

#import the library
from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['hi %1']],
    ['(hi|hello|yo|hey)', ['hey there', 'hi there', 'hi!']],
    ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],
    ['(.*)(location|city) ?', 'Tokyo, Japan'],
    ['(who created you?|who made you?|who(.*) your creator?)', ['A lovely lady named Athanasia Kalaitzidis created me using NLTK. She also goes by the name of Tania. She\'s so nice.']],
    ['how are you?', ['I\'m doing great, thank you.', 'I\'m fine.', 'I\'m a little sleepy.']],
    ['(.*)help(.*)', ['I can help you.']],
    ['(what|who are you?)', ['I\'m a bot, but I don\'t know that much as I\'m only version 1.0. Please standby for version 2.0 for a more intelligent bot. https://github.com/taniakalaitzidis']],
    ['bye|goodbye|take care|see ya', ['bye!', 'take care.']]
]

chat = Chat(pairs)

chat.converse()