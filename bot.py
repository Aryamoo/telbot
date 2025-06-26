from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

# جدول ابجد ساده
abjad_table = {
    'ا':1, 'آ':1, 'ب':2, 'پ':2, 'ت':400, 'ث':500, 'ج':3, 'چ':3,
    'ح':8, 'خ':600, 'د':4, 'ذ':700, 'ر':200, 'ز':7, 'ژ':7,
    'س':60, 'ش':300, 'ص':90, 'ض':800, 'ط':9, 'ظ':900,
    'ع':70, 'غ':1000, 'ف':80, 'ق':100, 'ک':20, 'گ':20,
    'ل':30, 'م':40, 'ن':50, 'و':6, 'ه':5, 'ی':10
}

def calculate_abjad(name):
    return sum(abjad_table.get(char, 0) for char in name)

def reduce_to_single_digit(number):
    while number > 9:
        number = sum(int(d) for d in str(number))
    return number

def taaleh_analysis(digit):
    meanings = {
        1: "آغاز نو، رهبری، قدرت فردی",
        2: "همکاری، تعادل، حساسیت",
        3: "خلاقیت، بیان، شادی",
        4: "ثبات، تلاش، نظم",
        5: "آزادی، تغییر، ماجراجویی",
        6: "مسئولیت، خانواده، عشق",
        7: "معنویت، خرد، پژوهش",
        8: "قدرت مادی، موفقیت، مدیریت",
        9: "نوع‌دوستی، پایان یک دوره، بخشش"
    }
    return meanings.get(digit, "تحلیل نامشخص")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 سلام! برای محاسبه ابجد و طالع، نام و نام مادر را به شکل زیر بفرست:\n\nنام - نام مادر"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    try:
        name, mother = [part.strip() for part in text.split('-')]
        abjad_name = calculate_abjad(name)
        abjad_mother = calculate_abjad(mother)
        total_abjad = abjad_name + abjad_mother
        digit = reduce_to_single_digit(total_abjad)
        analysis = taaleh_analysis(digit)
        result = (
            f"🔹 ابجد نام: {abjad_name}\n"
            f"🔹 ابجد مادر: {abjad_mother}\n"
            f"🔹 جمع ابجد: {total_abjad}\n"
            f"🔹 عدد تک رقمی: {digit}\n"
            f"🔮 تحلیل: {analysis}"
        )
        await update.message.reply_text(result)
    except Exception as e:
        await update.message.reply_text("❗ لطفاً به شکل «نام - نام مادر» بفرست (مثلاً علی - زهرا)")

if __name__ == '__main__':
    # دریافت توکن و URL وب‌هوک از متغیرهای محیطی
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    WEBHOOK_URL = os.getenv("WEBHOOK_URL")
    
    # دریافت پورت از متغیر محیطی Railway (یا پیش‌فرض 8443)
    PORT = int(os.getenv("PORT", 8443))

    if not TOKEN or not WEBHOOK_URL:
        raise ValueError("لطفاً متغیرهای محیطی TELEGRAM_TOKEN و WEBHOOK_URL را تنظیم کنید")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # اجرای ربات با وب‌هوک
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=WEBHOOKантибиотики_URL
    )