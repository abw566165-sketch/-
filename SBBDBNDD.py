import requests
from telebot import *
import os
import webbrowser
import logging
from datetime import datetime
import json

# فتح قناة المطور
webbrowser.open('https://t.me/fndbdbb')

# إعدادات التسجيل (Logging)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)

#_______________________________

def load_config():
    """تحميل الإعدادات من ملف"""
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except:
        return {}

def save_config(config):
    """حفظ الإعدادات في ملف"""
    with open('config.json', 'w') as f:
        json.dump(config, f)

# تحميل التوكن من الإعدادات أو من المستخدم
config = load_config()
token = config.get('token8406956439:AAHNCeM23zMF-Gq5BAgdxkwm_Rfm7iGg4hQ') or input('ENTER YOUR TOKEN => ')

if not config.get('token'):
    config['token'] ="8406956439:AAHNCeM23zMF-Gq5BAgdxkwm_Rfm7iGg4hQ" token
    save_config(config)

os.system('clear')

bot = telebot.TeleBot(token)

# قائمة بالمطورين
developers = [8678817970]  # اضف هنا أي دي المطورين

# كيبورد عائم
keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn1 = types.KeyboardButton('مساعدة')
btn2 = types.KeyboardButton('حول البوت')
btn3 = types.KeyboardButton('المطور')
btn4 = types.KeyboardButton('إرسال رسالة للمطور')
keyboard.add(btn1, btn2, btn3, btn4)

@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = """
    🚀 **أهلاً بك في بوت البرمجة الذكي!**
    
    يمكنني مساعدتك في:
    • كتابة الأكواد البرمجية
    • شرح المفاهيم البرمجية
    • حل المشاكل التقنية
    
    فقط اكتب طلبك وسأجيبك!
    """
    bot.send_message(message.chat.id, text=welcome_text, reply_markup=keyboard, parse_mode='Markdown')

@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = """
    📖 **أوامر البوت:**
    
    /start - بدء استخدام البوت
    /help - عرض هذه المساعدة
    /about - معلومات عن البوت
    /contact - الاتصال بالمطور
    
    **يمكنك أيضًا استخدام الأزرار:**
    • مساعدة - عرض هذه الرسالة
    • حول البوت - معلومات عن البوت
    • المطور - معلومات عن المطور
    • إرسال رسالة للمطور - لإرسال ملاحظاتك
    """
    bot.send_message(message.chat.id, help_text, parse_mode='Markdown')

@bot.message_handler(commands=['about'])
def about(message):
    about_text = """
    🤖 **معلومات البوت:**
    
    **الإصدار:** 2.0
    **الوصف:** بوت متخصص في المساعدة البرمجية
    **المطور:** @SBBDBNDD
    **اللغة:** Python
    """
    bot.send_message(message.chat.id, about_text)

@bot.message_handler(commands=['contact'])
def contact(message):
    bot.send_message(message.chat.id, "📧 للتواصل مع المطور: @SBBDBNDD")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text.strip()
    
    if text == 'مساعدة':
        help_command(message)
    elif text == 'حول البوت':
        about(message)
    elif text == 'المطور':
        bot.send_message(message.chat.id, "👨‍💻 المطور: @SBBDBNDD")
    elif text == 'إرسال رسالة للمطور':
        msg = bot.send_message(message.chat.id, "📝 الرجاء كتابة رسالتك للمطور:")
        bot.register_next_step_handler(msg, forward_to_developer)
    else:
        # إظهار رسالة انتظار
        wait_msg = bot.send_message(message.chat.id, "⏳ جاري معالجة طلبك...")
        
        try:
            # طلب البيانات من API
            re = requests.get(f'https://sii3.top/api/code.php?text={text}', timeout=10)
            re.raise_for_status()
            res = re.json()['response']
            
            # حذف رسالة الانتظار
            bot.delete_message(message.chat.id, wait_msg.message_id)
            
            # إرسال النتيجة
            if len(res) > 4000:
                # إذا كانت الرسالة طويلة، نقسمها
                for x in range(0, len(res), 4000):
                    bot.send_message(message.chat.id, res[x:x+4000])
            else:
                bot.send_message(message.chat.id, res)
                
        except requests.exceptions.Timeout:
            bot.edit_message_text("⏰ انتهى وقت الانتظار، حاول مرة أخرى.", message.chat.id, wait_msg.message_id)
        except Exception as e:
            bot.edit_message_text("❌ حدث خطأ أثناء المعالجة.", message.chat.id, wait_msg.message_id)
            logging.error(f"Error: {str(e)}")

def forward_to_developer(message):
    """إعادة توجيه الرسالة إلى المطور"""
    try:
        for dev_id in developers:
            bot.send_message(dev_id, f"📩 رسالة جديدة من {message.from_user.first_name}:\n\n{message.text}")
        bot.send_message(message.chat.id, "✅ تم إرسال رسالتك للمطور!")
    except Exception as e:
        bot.send_message(message.chat.id, "❌ فشل في إرسال الرسالة.")
        logging.error(f"Forward error: {str(e)}")

# معالج للأخطاء
@bot.message_handler(func=lambda message: True, content_types=['audio', 'video', 'document', 'photo'])
def handle_media(message):
    bot.send_message(message.chat.id, "⚠️ أستطيع معالجة النصوص فقط حالياً.")

if __name__ == "__main__":
    print('🤖 تم تشغيل البوت بنجاح')
    logging.info("Bot started successfully")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logging.error(f"Bot stopped: {str(e)}")
        print('❌ حدث خطأ في البوت')