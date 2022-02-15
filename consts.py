from telegram import InlineKeyboardButton
from telegram.utils.helpers import escape_markdown as es


def welcome_msg():
     welcome_msg = '''💖Welcome To Instagram Dp Saver Bot💖
 😋Send me anyones instagram username or profile url to get their DP😝
 ex : mahsoom.mjm.18 etc'''

    return welcome_msg


def acc_type(val):
    if(val):
        return "🙊Secret🙈Account🙊"
    else:
        return "😌Public😌"


def create_caption(user):
    caption_msg = f'''💖*Name*💖: {es(user.full_name,version=2)} \n💝*Followers*💝: {es(str(user.followers),version=2)} \n💞*Following*💞: {es(str(user.followees),version=2)}\
        \n😉*Account Type*😉: {acc_type(user.is_private)} \n\n😘😍Thank You For Using Me 😘😍'''

    return caption_msg


def get_username(url):
    try:
        data = url.split("/")[3]
        if "?" in data:
            try:
                data = data.split("?")
                return data[0]
            except Exception:
                return "😢incorrect format😢"
        return data
    except Exception:
        return "😢incorrect format😢"


ratingkey = [[InlineKeyboardButton(
    "🙊OWNER OF BOT🙊", url="https://t.me/Call_me_futurepilot")]]
