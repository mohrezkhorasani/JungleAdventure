# -*- coding: utf-8 -*-
"""
build_jungle_adventure_v3.py: Full Roadmap Graph & 13 Custom Events Generator
"""

import os
import json
import base64

base_dir = r"f:\DOTNET\FNSymposium\JungleAdventure"

font_css_path = r"F:\DOTNET\FNSymposium\embedded_fonts.css"
if not os.path.exists(font_css_path):
    font_css_path = os.path.join(os.path.dirname(__file__), '..', 'embedded_fonts.css')

with open(font_css_path, 'r', encoding='utf-8') as f:
    EMBEDDED_FONT_CSS = f.read()

from test_all_svgs import SVGS

ALL_13_ANIMALS = [
    {
        "id": "wolf",
        "name": "گرگ‌های برفی",
        "role": "محاصره در جنگل برفی",
        "icon": "🐺",
        "selected": True,
        "questionsCount": 2,
        "type": "wolves",
        "greeting": "گله گرگ‌های برفی در کمینند و دندان‌های تیزشان را نشان می‌دهند! هر دو سوال درست، یک گرگ را فراری می‌دهد!",
        "success": "گرگ‌ها با غرش شکست فرار کردند! مسیر برفی باز شد!"
    },
    {
        "id": "snake",
        "name": "مارهای باتلاق",
        "role": "محاصره مارهای خزنده",
        "icon": "🐍",
        "selected": True,
        "questionsCount": 2,
        "type": "snakes",
        "greeting": "مارهای سمی تو را محاصره کرده‌اند! با چوب‌دستی‌ات به هر سوال درست پاسخ بده تا یک مار را نابود کنی!",
        "success": "با شجاعت تمام مارها را کنار زدی و مسیر امن شد!"
    },
    {
        "id": "trunk",
        "name": "تنه درخت غول‌پیکر",
        "role": "مسدودکننده راه باریک",
        "icon": "🪵",
        "selected": True,
        "questionsCount": 2,
        "type": "trunk",
        "greeting": "یک تنه درخت سنگین راه را بسته است! باید به همه سوالات پاسخ بدهی تا بتوانی آن را بلند کنی و رد شوی!",
        "success": "هورا! تنه درخت را بلند کردی و به کناری انداختی! راه باز شد!"
    },
    {
        "id": "oldman",
        "name": "پیرمرد دانا",
        "role": "نگهبان معبد خرد",
        "icon": "🧙‍♂️",
        "selected": True,
        "questionsCount": 1,
        "type": "lantern",
        "greeting": "سلام مسافر کوچک! به سوالات من پاسخ بده تا یک «چراغ راهنمایی» به تو هدیه دهم!",
        "success": "آفرین دانای کوچک! یک چراغ راهنمایی به کوله‌پشتی‌ات اضافه شد!"
    },
    {
        "id": "dragon",
        "name": "اژدهای آتشین",
        "role": "سخت‌ترین چالش آتشین",
        "icon": "🐉",
        "selected": True,
        "questionsCount": 1,
        "type": "dragon",
        "greeting": "خطر! من اژدهای آتشم! برای هر سوال فقط ۳۰ ثانیه وقت داری وگرنه شعله می‌کشم و ۲ جان کم می‌کنم!",
        "success": "باورنکردنی است! خرد تو آتش من را خاموش کرد! عبور کن!"
    },
    {
        "id": "lion",
        "name": "شیر نگهبان",
        "role": "دروازه‌بان شجاع",
        "icon": "🦁",
        "selected": True,
        "questionsCount": 2,
        "type": "extra_life",
        "greeting": "من شیر نگهبانم! اگر معماهایم را حل کنی، راه باز می‌شود و یک جان (❤️) به تو هدیه می‌دهم!",
        "success": "آفرین قهرمان! راه باز شد و یک جان اضافه گرفتی!"
    },
    {
        "id": "crocodile",
        "name": "تمساح رودخانه",
        "role": "نگهبان آب‌های خروشان",
        "icon": "🐊",
        "selected": True,
        "questionsCount": 2,
        "type": "decay_multiplier",
        "greeting": "آب رودخانه عمیق است! امتیازت ضرب‌در ۲ می‌شود، اما عجله کن چون هر ۳ ثانیه از ضریب کم می‌شود!",
        "success": "برگ‌های نیلوفر بالا آمدند و با امتیاز عالی از رودخانه عبور کردی!"
    },
    {
        "id": "monkey",
        "name": "میمون بازیگوش",
        "role": "شاخه‌نورد تند و تیز",
        "icon": "🐵",
        "selected": True,
        "questionsCount": 2,
        "type": "decay_multiplier",
        "greeting": "شاخه‌ها لیزند! با سرعت پاسخ بده تا با ضریب ۲ امتیاز بگیری (هر ۳ ثانیه تأخیر ضریب را کم می‌کند)!",
        "success": "عالی بود! طناب را گرفتی و از شاخه‌ها گذشتی!"
    },
    {
        "id": "owl",
        "name": "جغد دانا",
        "role": "استاد شب‌های جنگل",
        "icon": "🦉",
        "selected": True,
        "questionsCount": 1,
        "type": "lantern",
        "greeting": "درود بر جوینده دانش! پاسخ بده تا یک چراغ راهنمایی (چراغ دانایی) تقدیمت کنم!",
        "success": "درود بر تو! چراغ راهنمایی به جعبه ابزارت اضافه شد!"
    },
    {
        "id": "bear",
        "name": "خرس مهربان",
        "role": "نگهبان درخت عسل",
        "icon": "🐻",
        "selected": True,
        "questionsCount": 1,
        "type": "extra_life",
        "greeting": "من خرس مهربانم! معما را حل کن تا یک جان تازه (❤️) و کمی عسل مقوی به تو بدهم!",
        "success": "نوش جانت! جان اضافه دریافت کردی و مسیر پل چوبی باز شد!"
    },
    {
        "id": "fox",
        "name": "روباه مکار",
        "role": "شعبده‌باز شک و تردید",
        "icon": "🦊",
        "selected": True,
        "questionsCount": 1,
        "type": "trickster",
        "greeting": "به قلمرو شک خوش آمدی! اگر بتوانی در برابر تردیدهای من مقاومت کنی و درست بگویی امتیازت ضرب‌در ۳ می‌شود!",
        "success": "وای! فریبم را نخوردی! امتیاز ۳ برابری مال تو!"
    },
    {
        "id": "turtle",
        "name": "لاک‌پشت کند",
        "role": "کاوشگر آهسته و پیوسته",
        "icon": "🐢",
        "selected": True,
        "questionsCount": 1,
        "type": "step_by_step",
        "greeting": "من خیلی آهسته حرکت می‌کنم! گزینه‌ها را یکی‌یکی با دقت بررسی کن و غلط‌ها را رد کن تا به پاسخ درست برسی!",
        "success": "صبر و حوصله‌ات ستودنی است! لاک‌پشت راه را برایت هموار کرد!"
    },
    {
        "id": "bat",
        "name": "خفاش‌های تاریکی",
        "role": "سایه غار وحشت",
        "icon": "🦇",
        "selected": True,
        "questionsCount": 1,
        "type": "bats_timer",
        "greeting": "تاریکی مطلق! هر ۱۵ ثانیه معطلی یک جان کم می‌کند، اما اگر سریع حل کنی ۴ برابر (×4) امتیاز می‌گیری!",
        "success": "نور دانایی تاریکی را درید! با امتیاز ۴ برابری به سوی خط پایان دویدی!"
    }
]

SAMPLE_QUESTIONS = [
    {
        "id": 1,
        "text": "حاصل ضرب ۷ × ۸ چند می‌شود؟",
        "type": "4choice",
        "animalId": "wolf",
        "options": ["۵۴", "۵۶", "۶۴", "۴۸"],
        "correct": 1,
        "hint": "به جدول ضرب ۷ یا ۸ فکر کن: ۷ تا ۸ تا می‌شود ۵۶ تا!"
    },
    {
        "id": 2,
        "text": "کدام موجود زیر «پستاندار» است و توانایی پرواز دارد؟",
        "type": "4choice",
        "animalId": "wolf",
        "options": ["عقاب", "خفاش", "کبوتر", "سنجاقک"],
        "correct": 1,
        "hint": "خفاش تنها پستانداری است که بال دارد و تخم‌گذار نیست!"
    },
    {
        "id": 3,
        "text": "اگر یک کیک را به ۴ قسمت مساوی تقسیم کنیم و ۳ قسمت آن را بخوریم، چه کسری باقی مانده است؟",
        "type": "4choice",
        "animalId": "snake",
        "options": ["۱/۴ (یک چهارم)", "۳/۴ (سه چهارم)", "۲/۴ (دو چهارم)", "۴/۴ (کل کیک)"],
        "correct": 0,
        "hint": "از ۴ قسمت مساوی، فقط ۱ قسمت باقی مانده است."
    },
    {
        "id": 4,
        "text": "بزرگ‌ترین سیاره در منظومه شمسی کدام است؟",
        "type": "4choice",
        "animalId": "snake",
        "options": ["مریخ", "زمین", "مشتری (زاوش)", "زهره"],
        "correct": 2,
        "hint": "سیاره غول‌پیکر مشتری بزرگ‌ترین عضو منظومه شمسی است!"
    },
    {
        "id": 5,
        "text": "حاصل عبارت (۲۵ + ۳۵) تقسیم بر ۲ چند می‌شود؟",
        "type": "4choice",
        "animalId": "trunk",
        "options": ["۲۵", "۳۰", "۳۵", "۲۰"],
        "correct": 1,
        "hint": "۲۵ به اضافه ۳۵ می‌شود ۶۰، نصف ۶۰ برابر است با ۳۰."
    },
    {
        "id": 6,
        "text": "گیاهان برای فتوسنتز (غذاسازی) به کدام گاز موجود در هوا نیاز دارند؟",
        "type": "4choice",
        "animalId": "trunk",
        "options": ["اکسیژن", "دی‌اکسید کربن", "نیتروژن", "هلیوم"],
        "correct": 1,
        "hint": "گیاهان دی‌اکسید کربن می‌گیرند و اکسیژن پاکیزه هدیه می‌دهند."
    },
    {
        "id": 7,
        "text": "آیا خورشید یک ستاره است؟",
        "type": "2choice",
        "animalId": "oldman",
        "options": ["صحیح است", "غلط است"],
        "correct": 0,
        "hint": "بله! خورشید نزدیک‌ترین ستاره پرنور به سیاره زمین است."
    },
    {
        "id": 8,
        "text": "محیط یک مربع به ضلع ۶ سانتی‌متر چند است؟",
        "type": "4choice",
        "animalId": "dragon",
        "options": ["۱۲ سانتی‌متر", "۲۴ سانتی‌متر", "۳۶ سانتی‌متر", "۱۸ سانتی‌متر"],
        "correct": 1,
        "hint": "محیط مربع = ۴ × یک ضلع. یعنی ۴ × ۶ = ۲۴."
    },
    {
        "id": 9,
        "text": "کدام عضو بدن خون را به تمام اندام‌ها پمپاژ می‌کند؟",
        "type": "4choice",
        "animalId": "lion",
        "options": ["معده", "قلب", "ریه", "مغز"],
        "correct": 1,
        "hint": "قلب مثل یک تلمبه قدرتمند شبانه‌روز خون را به گردش درمی‌آورد."
    },
    {
        "id": 10,
        "text": "کدام یک از اجسام زیر رسانای جریان برق است؟",
        "type": "4choice",
        "animalId": "crocodile",
        "options": ["قاشق فلزی", "پاک‌کن لاستیکی", "خط‌کش پلاستیکی", "تکه چوب خشک"],
        "correct": 0,
        "hint": "فلزات جریان برق را از خود عبور می‌دهند."
    },
    {
        "id": 11,
        "text": "کدام کلمه جمع مکسر است؟",
        "type": "4choice",
        "animalId": "fox",
        "options": ["کتاب‌ها", "دانش‌آموزان", "کُتُب", "معلمان"],
        "correct": 2,
        "hint": "کلمه کتب جمع بی‌قاعده کتاب است."
    },
    {
        "id": 12,
        "text": "واحد سنجش جرم در زندگی روزمره کدام است؟",
        "type": "4choice",
        "animalId": "turtle",
        "options": ["کیلوگرم", "متر", "لیتر", "ثانیه"],
        "correct": 0,
        "hint": "برای سنجش جرم از کیلوگرم و گرم استفاده می‌کنیم."
    },
    {
        "id": 13,
        "text": "کدام جانور در گروه بی‌مهرگان قرار دارد؟",
        "type": "4choice",
        "animalId": "bat",
        "options": ["کرم خاکی", "ماهی قزل‌آلا", "قورباغه", "گنجشک"],
        "correct": 0,
        "hint": "کرم خاکی ستون مهره ندارد و بی‌مهره است."
    }
]

DEFAULT_PROJECT_DATA = {
    "title": "ماجراجویی در نقشه جنگل شگفت‌انگیز",
    "lesson": "ریاضی و علوم شاد دبستان",
    "teacher": "آموزگار مهربان شما",
    "hero": "squirrel",
    "initialLives": 5,
    "randomize": True,
    "growthMindset": "rescue",
    "animals": ALL_13_ANIMALS,
    "questions": SAMPLE_QUESTIONS
}

print("Base setup ready.")
