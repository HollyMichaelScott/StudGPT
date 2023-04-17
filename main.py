#import openai_secret_manager
import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from better_profanity import profanity
#import queue
#import threading
from flask import Flask
from better_profanity import profanity
from telegram import Update
from telegram.ext import CallbackContext


openai.api_key = "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"
model_engine = "text-davinci-003"
openai_prompt = "The following is a conversation with an AI assistant. The assistant can help you with various tasks. To end the conversation, simply type 'bye'."

# Initialize Telegram bot
#secrets = openai_secret_manager.get_secret("telegram")
bot_token = "6119147423:AAG6EfIAbyDxg-q9W6GncOCj1sD1Kofn698"
bot = telegram.Bot(token=bot_token)

# Add bot to Telegram group

bot_username = "studtalksGPT_bot"

async def getbot():
    group_chat_id = -949891880
    bot_chat_id = await bot.get_chat(group_chat_id).id
    bot_member = await bot.get_chat_member(chat_id=group_chat_id, user_id=bot_chat_id)
    if bot_member.status == "left":
        await bot.join_chat(group_chat_id)

    return await True



#response_queue = queue.Queue()

# Define profanity


profane_words = [
    'aad', 'aand', 'bahenchod', 'behenchod', 'bhenchod', 'bhenchodd', 'b.c.', 'bc',
    'bakchod', 'bakchodd', 'bakchodi', 'bevda', 'bewda', 'bevdey', 'bewday',
    'bevakoof', 'bevkoof', 'bevkuf', 'bewakoof', 'bewkoof', 'bewkuf', 'bhadua',
    'bhaduaa', 'bhadva', 'bhadvaa', 'bhadwa', 'bhadwaa', 'bhosada', 'bhosda',
    'bhosdaa', 'bhosdike', 'bhonsdike', 'bhosdiki', 'bhosdiwala', 'bhosdiwale',
    'babbe', 'babbey', 'bube', 'bubey', 'bur', 'burr', 'buurr', 'buur', 'charsi',
    'chooche', 'choochi', 'chuchi', 'chhod', 'chod', 'chodd', 'chudne', 'chudney',
    'chudwa', 'chudwaa', 'chudwane', 'chudwaane', 'chaat', 'choot', 'chut', 'chute',
    'chutia', 'chutiya', 'dalaal', 'dalal', 'dalle', 'dalley', 'fattu', 'gadha',
    'gadhe', 'gadhalund', 'gaand', 'gand', 'gandu', 'gandfat', 'gandfut', 'gandiya',
    'gandiye', 'goo', 'gu', 'gote', 'gotey', 'gotte', 'hag', 'haggu', 'hagne',
    'hagney', 'harami', 'haramjada', 'haraamjaada', 'haramzyada', 'haraamzyaada',
    'haraamjaade', 'haraamzaade', 'haraamkhor', 'haramkhor', 'jhat', 'jhaat',
    'jhaatu', 'jhatu', 'kutta', 'kutte', 'kuttey', 'kutia', 'kutiya', 'kuttiya',
    'kutti', 'landi', 'landy', 'laude', 'laudey', 'laura', 'lora', 'lauda',
    'ling', 'loda', 'lode', 'lund', 'launda', 'lounde', 'laundey', 'laundi',
    'loundi', 'laundiya', 'loundiya', 'lulli', 'maar', 'maro', 'marunga',
    'madarchod', 'madarchodd', 'madarchood', 'madarchoot', 'madarchut', 'm.c.',
    'mc', 'mamme', 'mammey', 'moot', 'mut', 'mootne', 'mutne', 'mooth', 'muth',
    'nunni', 'nunnu', 'paaji', 'paji', 'pesaab', 'pesab', 'peshaab', 'peshab', 'pilla', 'pillay','pille','pilley','pisaab','pisab','pkmkb','porkistan','raand','rand','randi','randy','suar','tatte','tatti','tatty','ullu']
# Define function to warn user
# Define function to warn user

# to search profane words
def gaali_search(arr ,low, high , word):

        
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
        
        # If element is present at the middle itself
        try: 
            if arr[mid] == word:
                
                return mid
            elif arr[mid] > word:
                return gaali_search(arr, low, mid - 1, word)
 
        # Else the element can only be present in right subarray
            else:
                return gaali_search(arr, mid + 1, high, word)

        
        except Exception as E:
            print(E)

    else:
        # Element is not present in the array
        return 0
 
        # If element is smaller than mid, then it can only
        # be present in left subarray

        
def warn_user(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    chat_id = update.effective_chat.id
    message_id = update.message.message_id

    # Get user's name or username
    if update.message.from_user.username:
        user_name = f"@{update.message.from_user.username}"
    else:
        user_name = update.message.from_user.name

    # Keep track of the user's warning count
    if user_id in user_warning_count:
        user_warning_count[user_id] += 1
    else:
        user_warning_count[user_id] = 1

    warning_count = user_warning_count[user_id]

    if warning_count == 2:
        context.bot.send_message(chat_id=chat_id,
                                 text=f"{user_name},<b>Stud--talks ke nyay ke anusar</b>.. Order order! Aapka yeh doosra warning hai. Agar phir se warning li toh group se bina laat mare nikal diya jayega!.",parse_mode='HTML')
    elif warning_count == 3:
        context.bot.send_message(chat_id=chat_id,
                                 text=f"{user_name}, <b>Stud--talks ke nyay ke anusar</b>..Bhai tu toh tisri baar warning le raha hai. Agar aur ek warning le li toh group se nikal diya jayega!.",parse_mode='HTML')
    elif warning_count == 4:
        context.bot.send_message(chat_id=chat_id,
                                 text=f"{user_name}, <b>Stud--talks ke nyay ke anusar</b>..Apka chautha aur aakhri warning hai. Ab aap is STUD--Talks group se ban ho gaye hain. Dhanyavaad!.", parse_mode='HTML')
        context.bot.kick_chat_member(chat_id=chat_id, user_id=user_id)
    elif warning_count == 1:
        context.bot.send_message(chat_id=chat_id,
                                 text=f'{user_name} <b>Kripaya aap aisi gandi bhasha ka istemal na karen.</b> Agar dobara aisa kiya toh seedhi tarah bahar nikal diya jayega ya phir STUD--Talks parivar se nikal diya jayega..',
                                 parse_mode='HTML')


# Define function to kick user
def kick_user(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    chat_id = update.effective_chat.id

    context.bot.kick_chat_member(chat_id=chat_id, user_id=user_id)
    context.bot.send_message(chat_id=chat_id,
                             text=f"{update.message.from_user.first_name} has been kicked from the group.")


# Define function to ban user
def ban_user(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    chat_id = update.effective_chat.id

    context.bot.ban_chat_member(chat_id=chat_id, user_id=user_id)
    context.bot.send_message(chat_id=chat_id,
                             text=f"{update.message.from_user.first_name} has been banned from the group.")


# Initialize a dictionary to keep track of each user's warning count


# Define function to handle messages from users
def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text if update.message is not None else None
    bot_username = "@" + bot.username
    message = user_message.lower()
    print(message)
    if profanity.contains_profanity(message):
        print('Contains profanity')
        warn_user(update, context)
    elif 'kick' in message:
        kick_user(update, context)
    elif 'ban' in message:
        ban_user(update, context)
    else:
        message_split=message.split()
        print(message_split)
        for word in message_split:
            print("Word:",word)
            if gaali_search(profane_words,0,len(profane_words)-1,word):
                print('gaali found')
                warn_user(update, context)
                break
    

    try:
        if bot_username in user_message:
            chat_id = update.message.chat_id
            user_id = update.message.from_user.id
            chat_member=bot.getChatMember(chat_id=chat_id, user_id=user_id)

            if profanity.contains_profanity(user_message):
                print(profanity.contains_profanity(user_message))
                text1="Hey, that is inappropriate!! Nyay Baba batao jara inhe \U0001F620"
                print("Hello")
                print(text1)
                update.message.reply_text(text1)
                #update.message.reply_text("/warn {}".format(user_id))
                
            else:
                if user_message.lower() == "bye":
                    update.message.reply_text("Goodbye!")
                    return
                else:
                    # Generate response using OpenAI GPT-3 engine
                    response = openai.Completion.create(
                        engine=model_engine,
                        prompt=f"{openai_prompt}\n\nUser: {user_message}\nAI:",
                        max_tokens=1024,
                        n=1,
                        stop=None,
                        temperature=0.7,
                    )
                    bot_response = response.choices[0].text.strip()
                    update.message.reply_text(bot_response)
    
    except:
        pass


user_warning_count = {}



# Set up Telegram bot handlers
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & Filters.chat_type.groups & ~Filters.command, handle_message))
#dispatcher.add_handler(CommandHandler('ban', ban,Filters.reply))
# Start Telegram bot
updater.start_polling()

