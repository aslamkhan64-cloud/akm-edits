import os
import logging
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

WEBSITE = "https://aslamkhan64-cloud.github.io/akm-edits"

TUTORIALS = [
    ("Tutorial 1 🎬", "https://youtu.be/4iE2sqKAXYE?feature=shared"),
    ("Tutorial 2 🎬", "https://youtu.be/lQEiH6lt0wA?feature=shared"),
]

logging.basicConfig(level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)


def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🌐 Website", url=WEBSITE)],
        [InlineKeyboardButton("🎬 Tutorials", callback_data="tutorials")],
        [InlineKeyboardButton("📢 TikTok", url="https://www.tiktok.com/@aslam_edit3")],
        [InlineKeyboardButton("💬 WhatsApp Channel",
                              url="https://whatsapp.com/channel/0029VbEIlU0BlHpkgOQ7cJ1F")],
        [InlineKeyboardButton("📰 Latest Posts", callback_data="posts")],
        [InlineKeyboardButton("ℹ️ About", callback_data="about")],
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "السلام علیکم ورحمۃ اللہ وبرکاتہ ❤️\n\n"
        "👑 Welcome to AKM EDITS!\n"
        "🎬 Editing • Creativity • Islamic Content\n\n"
        "Apna option select karein:",
        reply_markup=main_menu()
    )


async def website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🌐 AKM EDITS Website:\n{WEBSITE}")


async def tutorials(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(name, url=url)]
        for name, url in TUTORIALS
    ]
    await update.message.reply_text(
        "🎬 AKM EDITS Editing Tutorials:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👑 AKM EDITS | Aslam Khan\n"
        "🎬 Video Editing Tutorials\n"
        "✨ Creative Content\n"
        "🕌 Islamic Content & Updates\n\n"
        f"🌐 {WEBSITE}"
    )


async def latest_posts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📰 Latest posts ke liye AKM EDITS website visit karein:\n"
        f"{WEBSITE}"
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "tutorials":
        keyboard = [
            [InlineKeyboardButton(name, url=url)]
            for name, url in TUTORIALS
        ]
        await query.message.reply_text(
            "🎬 Choose a tutorial:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "posts":
        await query.message.reply_text(
            f"📰 Latest Posts:\n{WEBSITE}"
        )

    elif query.data == "about":
        await query.message.reply_text(
            "👑 AKM EDITS | Aslam Khan\n"
            "🎬 Editing • Creativity • Islamic Content"
        )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start bot\n"
        "/website - Open website\n"
        "/tutorials - Editing tutorials\n"
        "/about - About AKM EDITS\n"
        "/posts - Latest posts\n"
        "/help - Help"
    )


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is missing.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("website", website))
    app.add_handler(CommandHandler("tutorials", tutorials))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("posts", latest_posts))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(
        __import__("telegram.ext", fromlist=["CallbackQueryHandler"])
        .CallbackQueryHandler(buttons)
    )

    app.run_polling()


if __name__ == "__main__":
    main()
