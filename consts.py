from telegram import InlineKeyboardButton
from telegram.utils.helpers import escape_markdown as es


def welcome_msg():
    welcome_msg = '''<b>Hello & Welcome</b>๐๐
 <i>Send me anyones instagram username or profile url to get their DP</i>
 ex : <b>mahsoom.mjm.18</b> , <b>lovedoll</b> etc'''

    return welcome_msg


def acc_type(val):
    if(val):
        return "๐Secret๐Account๐"
    else:
        return "๐Public๐"


def create_caption(user):
    caption_msg = f'''๐*Name*๐: {es(user.full_name,version=2)} \n๐*Followers*๐: {es(str(user.followers),version=2)} \n๐*Following*๐: {es(str(user.followees),version=2)}\
        \n๐*Account Type*๐: {acc_type(user.is_private)} \n\n๐๐Thank You For Using Me ๐๐'''

    return caption_msg


def get_username(url):
    try:
        data = url.split("/")[3]
        if "?" in data:
            try:
                data = data.split("?")
                return data[0]
            except Exception:
                return "๐ขincorrect format๐ข"
        return data
    except Exception:
        return "๐ขincorrect format๐ข"


ratingkey = [[InlineKeyboardButton(
    "๐OWNER OF BOT๐", url="https://t.me/Call_me_futurepilot_bot")]]
