# -*- coding: utf-8 -*-
"""
make_app.py: Refactored with 100% Mobile-First CSS, Placeholders instead of pre-filled text, and robust responsive layout.
"""

import os
import json

font_css_path = r"F:\DOTNET\FNSymposium\embedded_fonts.css"
if not os.path.exists(font_css_path):
    font_css_path = os.path.join(os.path.dirname(__file__), '..', 'embedded_fonts.css')

with open(font_css_path, 'r', encoding='utf-8') as f:
    EMBEDDED_FONT_CSS = f.read()

SVG_DEFS = {
    'squirrel': '''<svg viewBox="0 0 100 110" class="actor-svg">
      <path d="M 30,85 C 10,75 -5,40 15,20 C 35,0 55,25 45,45 C 40,55 35,65 30,85" fill="#e65100" stroke="#bf360c" stroke-width="3"/>
      <path d="M 28,75 C 18,65 5,42 20,28 C 32,15 45,30 40,45" fill="#ff9800"/>
      <ellipse cx="50" cy="75" rx="22" ry="26" fill="#f57c00" stroke="#bf360c" stroke-width="2.5"/>
      <ellipse cx="50" cy="78" rx="14" ry="18" fill="#ffe0b2"/>
      <rect x="24" y="65" width="12" height="18" rx="4" fill="#388e3c" stroke="#1b5e20" stroke-width="2"/>
      <ellipse cx="40" cy="100" rx="9" ry="5" fill="#d84315"/>
      <ellipse cx="60" cy="100" rx="9" ry="5" fill="#d84315"/>
      <circle cx="58" cy="45" r="19" fill="#f57c00" stroke="#bf360c" stroke-width="2.5"/>
      <circle cx="58" cy="48" r="13" fill="#ffe0b2"/>
      <path d="M 46,32 L 42,16 L 52,26 Z" fill="#e65100"/>
      <path d="M 64,32 L 68,16 L 58,26 Z" fill="#e65100"/>
      <path d="M 40,34 Q 58,20 76,34 Q 82,35 84,39 L 36,39 Q 34,35 40,34 Z" fill="#0277bd" stroke="#01579b" stroke-width="2"/>
      <circle cx="53" cy="42" r="3.5" fill="#212121"/><circle cx="65" cy="42" r="3.5" fill="#212121"/>
      <circle cx="54" cy="40.5" r="1.2" fill="#fff"/><circle cx="66" cy="40.5" r="1.2" fill="#fff"/>
      <polygon points="57,48 61,48 59,51" fill="#d84315"/>
      <path d="M 56,53 Q 59,56 62,53" fill="none" stroke="#bf360c" stroke-width="1.8" stroke-linecap="round"/>
    </svg>''',

    'rabbit': '''<svg viewBox="0 0 100 110" class="actor-svg">
      <ellipse cx="40" cy="22" rx="7" ry="20" fill="#fff" stroke="#cfd8dc" stroke-width="2"/>
      <ellipse cx="40" cy="22" rx="4" ry="14" fill="#f8bbd0"/>
      <ellipse cx="60" cy="22" rx="7" ry="20" fill="#fff" stroke="#cfd8dc" stroke-width="2"/>
      <ellipse cx="60" cy="22" rx="4" ry="14" fill="#f8bbd0"/>
      <ellipse cx="50" cy="78" rx="24" ry="24" fill="#fff" stroke="#cfd8dc" stroke-width="2"/>
      <ellipse cx="50" cy="80" rx="15" ry="16" fill="#f5f5f5"/>
      <rect x="22" y="68" width="12" height="18" rx="4" fill="#ff7043" stroke="#d84315" stroke-width="2"/>
      <ellipse cx="38" cy="100" rx="10" ry="5" fill="#eceff1"/>
      <ellipse cx="62" cy="100" rx="10" ry="5" fill="#eceff1"/>
      <circle cx="50" cy="48" r="20" fill="#fff" stroke="#cfd8dc" stroke-width="2"/>
      <path d="M 32,36 Q 50,26 68,36 Q 74,38 72,42 L 28,42 Q 26,38 32,36 Z" fill="#ffb300" stroke="#f57c00" stroke-width="2"/>
      <circle cx="43" cy="48" r="3.5" fill="#212121"/><circle cx="57" cy="48" r="3.5" fill="#212121"/>
      <circle cx="44" cy="46.5" r="1.2" fill="#fff"/><circle cx="58" cy="46.5" r="1.2" fill="#fff"/>
      <polygon points="48,54 52,54 50,57" fill="#f06292"/>
      <path d="M 47,59 Q 50,62 53,59" fill="none" stroke="#78909c" stroke-width="2" stroke-linecap="round"/>
    </svg>''',

    'fox': '''<svg viewBox="0 0 100 110" class="actor-svg">
      <path d="M 26,85 C 5,75 -5,45 15,30 C 25,20 40,40 35,60 C 30,75 28,85 26,85" fill="#ff5722" stroke="#d84315" stroke-width="2.5"/>
      <path d="M 12,38 C 18,30 28,35 24,48 C 16,52 10,44 12,38" fill="#fff"/>
      <ellipse cx="52" cy="76" rx="22" ry="24" fill="#ff5722" stroke="#d84315" stroke-width="2.5"/>
      <ellipse cx="52" cy="79" rx="13" ry="16" fill="#fff"/>
      <ellipse cx="40" cy="99" rx="8" ry="5" fill="#3e2723"/>
      <ellipse cx="64" cy="99" rx="8" ry="5" fill="#3e2723"/>
      <polygon points="32,45 72,45 52,70" fill="#ff5722" stroke="#d84315" stroke-width="2.5"/>
      <polygon points="34,48 48,65 52,70 42,48" fill="#fff"/>
      <polygon points="70,48 56,65 52,70 62,48" fill="#fff"/>
      <polygon points="32,45 25,22 45,35" fill="#ff5722"/>
      <polygon points="30,42 27,27 40,36" fill="#3e2723"/>
      <polygon points="72,45 79,22 59,35" fill="#ff5722"/>
      <polygon points="74,42 77,27 64,36" fill="#3e2723"/>
      <circle cx="43" cy="48" r="3" fill="#212121"/><circle cx="61" cy="48" r="3" fill="#212121"/>
      <circle cx="52" cy="68" r="3.5" fill="#212121"/>
    </svg>''',

    'lion': '''<svg viewBox="0 0 120 120" class="actor-svg">
      <circle cx="60" cy="60" r="48" fill="#f57c00" stroke="#e65100" stroke-width="3"/>
      <circle cx="28" cy="30" r="12" fill="#ffb74d" stroke="#f57c00" stroke-width="2"/>
      <circle cx="92" cy="30" r="12" fill="#ffb74d" stroke="#f57c00" stroke-width="2"/>
      <circle cx="60" cy="64" r="32" fill="#ffcc80"/>
      <ellipse cx="48" cy="56" rx="4" ry="6" fill="#3e2723"/>
      <ellipse cx="72" cy="56" rx="4" ry="6" fill="#3e2723"/>
      <circle cx="49" cy="54" r="1.5" fill="#fff"/>
      <circle cx="73" cy="54" r="1.5" fill="#fff"/>
      <ellipse cx="60" cy="74" rx="14" ry="9" fill="#fff8e1"/>
      <polygon points="57,69 63,69 60,73" fill="#d84315"/>
      <path d="M 55,75 Q 60,79 65,75" stroke="#3e2723" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    </svg>''',

    'monkey': '''<svg viewBox="0 0 120 120" class="actor-svg">
      <circle cx="24" cy="55" r="14" fill="#a1887f"/>
      <circle cx="24" cy="55" r="8" fill="#d7ccc8"/>
      <circle cx="96" cy="55" r="14" fill="#a1887f"/>
      <circle cx="96" cy="55" r="8" fill="#d7ccc8"/>
      <ellipse cx="60" cy="58" rx="34" ry="30" fill="#6d4c41"/>
      <ellipse cx="60" cy="65" rx="26" ry="18" fill="#d7ccc8"/>
      <circle cx="48" cy="50" r="5" fill="#fff"/>
      <circle cx="49" cy="50" r="2.5" fill="#000"/>
      <circle cx="72" cy="50" r="5" fill="#fff"/>
      <circle cx="71" cy="50" r="2.5" fill="#000"/>
      <path d="M 50,70 Q 60,78 70,70" stroke="#3e2723" stroke-width="3" fill="none" stroke-linecap="round"/>
    </svg>''',

    'crocodile': '''<svg viewBox="0 0 130 110" class="actor-svg">
      <ellipse cx="65" cy="90" rx="55" ry="12" fill="#29b6f6" opacity="0.6"/>
      <path d="M 20,70 Q 65,40 110,65 Q 115,80 90,82 Q 50,85 20,70 Z" fill="#388e3c" stroke="#1b5e20" stroke-width="3"/>
      <circle cx="45" cy="46" r="10" fill="#81c784"/>
      <circle cx="45" cy="46" r="4" fill="#000"/>
      <circle cx="68" cy="46" r="10" fill="#81c784"/>
      <circle cx="68" cy="46" r="4" fill="#000"/>
      <polygon points="50,72 55,65 60,72 65,65 70,72" fill="#fff"/>
    </svg>''',

    'bear': '''<svg viewBox="0 0 120 120" class="actor-svg">
      <circle cx="32" cy="35" r="14" fill="#5d4037"/>
      <circle cx="88" cy="35" r="14" fill="#5d4037"/>
      <circle cx="60" cy="62" r="36" fill="#795548"/>
      <ellipse cx="60" cy="74" rx="16" ry="12" fill="#d7ccc8"/>
      <ellipse cx="60" cy="69" rx="6" ry="4" fill="#3e2723"/>
      <circle cx="48" cy="56" r="3.5" fill="#212121"/>
      <circle cx="72" cy="56" r="3.5" fill="#212121"/>
      <rect x="76" y="78" width="22" height="24" rx="6" fill="#ffb300" stroke="#e65100" stroke-width="2"/>
    </svg>''',

    'owl': '''<svg viewBox="0 0 120 120" class="actor-svg">
      <rect x="10" y="98" width="100" height="8" rx="4" fill="#4e342e"/>
      <ellipse cx="60" cy="65" rx="30" ry="34" fill="#8d6e63"/>
      <circle cx="46" cy="50" r="14" fill="#fff" stroke="#ffb300" stroke-width="3"/>
      <circle cx="46" cy="50" r="6" fill="#212121"/>
      <circle cx="74" cy="50" r="14" fill="#fff" stroke="#ffb300" stroke-width="3"/>
      <circle cx="74" cy="50" r="6" fill="#212121"/>
      <polygon points="56,60 64,60 60,68" fill="#ff9800"/>
      <circle cx="46" cy="50" r="16" fill="none" stroke="#e65100" stroke-width="2.5"/>
      <circle cx="74" cy="50" r="16" fill="none" stroke="#e65100" stroke-width="2.5"/>
      <line x1="62" y1="50" x2="58" y2="50" stroke="#e65100" stroke-width="3"/>
    </svg>''',

    'custom_generic': '''<svg viewBox="0 0 120 120" class="actor-svg">
      <circle cx="60" cy="60" r="44" fill="#8e24aa" stroke="#4a148c" stroke-width="3"/>
      <circle cx="46" cy="52" r="6" fill="#fff"/><circle cx="46" cy="52" r="3" fill="#212121"/>
      <circle cx="74" cy="52" r="6" fill="#fff"/><circle cx="74" cy="52" r="3" fill="#212121"/>
      <path d="M 48,76 Q 60,86 72,76" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/>
      <polygon points="60,20 68,36 84,36 71,46 76,62 60,52 44,62 49,46 36,36 52,36" fill="#ffd600"/>
    </svg>''',

    'home': '''<svg viewBox="0 0 130 120" class="actor-svg">
      <rect x="85" y="20" width="12" height="25" fill="#5d4037"/>
      <circle cx="91" cy="12" r="5" fill="#cfd8dc" opacity="0.8"/>
      <polygon points="65,18 15,55 115,55" fill="#d32f2f" stroke="#b71c1c" stroke-width="3"/>
      <rect x="25" y="55" width="80" height="50" rx="4" fill="#ffecb3" stroke="#8d6e63" stroke-width="3"/>
      <rect x="52" y="70" width="24" height="35" rx="3" fill="#6d4c41"/>
      <rect x="32" y="65" width="15" height="15" rx="2" fill="#fff59d" stroke="#fbc02d" stroke-width="2"/>
      <rect x="82" y="65" width="15" height="15" rx="2" fill="#fff59d" stroke="#fbc02d" stroke-width="2"/>
    </svg>'''
}

DEFAULT_PROJECT_DATA = {
    "title": "ماجراجویی در جنگل شگفت‌انگیز دانایی",
    "lesson": "ریاضی و علوم شاد دبستان",
    "teacher": "آموزگار مهربان شما",
    "hero": "squirrel",
    "initialLives": 5,
    "randomize": True,
    "growthMindset": "rescue",
    "animals": [
        {
            "id": "lion",
            "name": "شیر نگهبان",
            "role": "نگهبان دروازه سنگی",
            "icon": "🦁",
            "selected": True,
            "questionsCount": 2,
            "greeting": "سلام قهرمان کوچک! برای عبور از دروازه سنگی باید به معماهای من پاسخ بدهی!",
            "success": "آفرین قهرمان باهوش! چشم‌های من سنگین شد... می‌توانی رد شوی!"
        },
        {
            "id": "monkey",
            "name": "میمون بازیگوش",
            "role": "نگهبان شاخه‌های باتلاق",
            "icon": "🐵",
            "selected": True,
            "questionsCount": 2,
            "greeting": "هورا! شاخه‌های باتلاق لیز است، به سوالاتم جواب بده تا برایت طناب پرتاب کنم!",
            "success": "عالی بود! طناب را بگیر و با خیال راحت از باتلاق رد شو!"
        },
        {
            "id": "crocodile",
            "name": "تمساح رودخانه",
            "role": "نگهبان آب‌های خروشان",
            "icon": "🐊",
            "selected": True,
            "questionsCount": 2,
            "greeting": "آب رودخانه عمیق است! با پاسخ درست، برگ‌های نیلوفر برای عبور بالا می‌آیند!",
            "success": "وای چقدر زرنگی! برگ‌های نیلوفر بالا آمدند، بپر آن طرف آب!"
        },
        {
            "id": "bear",
            "name": "خرس مهربان",
            "role": "نگهبان درخت عسل",
            "icon": "🐻",
            "selected": True,
            "questionsCount": 1,
            "greeting": "من عاشق معمای شیرینم! پاسخ درست بده تا راه پل چوبی را باز کنم!",
            "success": "به به چه جوابی! بفرما یک قاشق عسل خوشمزه هم نوش جانت!"
        },
        {
            "id": "owl",
            "name": "جغد دانا",
            "role": "نگهبان صندوقچه اسرار",
            "icon": "🦉",
            "selected": True,
            "questionsCount": 1,
            "greeting": "من نگهبان کلید خانه‌ام! معمای نهایی را حل کن تا به کلبه امن برسی!",
            "success": "تبریک می‌گویم دانشمند کوچک! کلید طلایی خانه در دستان توست!"
        }
    ],
    "questions": [
        {
            "id": 1,
            "text": "حاصل ضرب ۷ × ۸ چند می‌شود؟",
            "type": "4choice",
            "animalId": "lion",
            "options": ["۵۴", "۵۶", "۶۴", "۴۸"],
            "correct": 1,
            "hint": "به جدول ضرب ۷ یا ۸ فکر کن: ۷ تا ۸ تا می‌شود ۵۶ تا!"
        },
        {
            "id": 2,
            "text": "کدام موجود زیر «پستاندار» است و توانایی پرواز دارد؟",
            "type": "4choice",
            "animalId": "lion",
            "options": ["عقاب", "خفاش", "کبوتر", "سنجاقک"],
            "correct": 1,
            "hint": "خفاش تنها پستانداری است که بال دارد و تخم‌گذار نیست!"
        },
        {
            "id": 3,
            "text": "اگر یک کیک را به ۴ قسمت مساوی تقسیم کنیم و ۳ قسمت آن را بخوریم، چه کسری باقی مانده است؟",
            "type": "4choice",
            "animalId": "monkey",
            "options": ["۱/۴ (یک چهارم)", "۳/۴ (سه چهارم)", "۲/۴ (دو چهارم)", "۴/۴ (کل کیک)"],
            "correct": 0,
            "hint": "از ۴ قسمت مساوی، فقط ۱ قسمت باقی مانده است."
        },
        {
            "id": 4,
            "text": "بزرگ‌ترین سیاره در منظومه شمسی کدام است؟",
            "type": "4choice",
            "animalId": "monkey",
            "options": ["مریخ", "زمین", "مشتری (زاوش)", "زهره"],
            "correct": 2,
            "hint": "سیاره غول‌پیکر مشتری بزرگ‌ترین عضو منظومه شمسی است!"
        },
        {
            "id": 5,
            "text": "آیا خورشید یک ستاره است؟",
            "type": "2choice",
            "animalId": "crocodile",
            "options": ["صحیح است", "غلط است"],
            "correct": 0,
            "hint": "بله! خورشید نزدیک‌ترین ستاره پرنور به زمین است."
        },
        {
            "id": 6,
            "text": "گیاهان برای فتوسنتز (غذاسازی) به گاز دی‌اکسید کربن نیاز دارند.",
            "type": "2choice",
            "animalId": "crocodile",
            "options": ["صحیح است", "غلط است"],
            "correct": 0,
            "hint": "گیاهان دی‌اکسید کربن می‌گیرند و اکسیژن پاک می‌دهند."
        },
        {
            "id": 7,
            "text": "محیط یک مربع به ضلع ۶ سانتی‌متر چقدر است؟",
            "type": "4choice",
            "animalId": "bear",
            "options": ["۱۲ سانتی‌متر", "۲۴ سانتی‌متر", "۳۶ سانتی‌متر", "۱۸ سانتی‌متر"],
            "correct": 1,
            "hint": "محیط مربع = ۴ × اندازه یک ضلع. پس ۴ × ۶ = ۲۴."
        },
        {
            "id": 8,
            "text": "کدام عضو بدن خون را به تمام قسمت‌ها پمپاژ می‌کند؟",
            "type": "4choice",
            "animalId": "owl",
            "options": ["معده", "قلب", "ریه", "مغز"],
            "correct": 1,
            "hint": "قلب مثل یک تلمبه قدرتمند شبانه‌روز خون را به حرکت درمی‌آورد."
        }
    ]
}

def generate_game_engine_code(data):
    """Mobile-first game engine with robust layout and empty value placeholder inputs."""
    serialized = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c").replace(">", "\\u003e")
    svg_defs_json = json.dumps(SVG_DEFS, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>{data.get('title', 'ماجراجویی جنگل دانایی')}</title>
  <style>
    {EMBEDDED_FONT_CSS}

    /* ==================================================
       MOBILE-FIRST BASE STYLES
       ================================================== */
    :root {{
      --primary: #2e7d32;
      --primary-dark: #1b5e20;
      --wood: #5d4037;
      --wood-light: #8d6e63;
      --gold: #ffb300;
      --danger: #e53935;
      --sky: #81d4fa;
      --font-main: 'VazirFont', system-ui, -apple-system, sans-serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: var(--font-main);
      -webkit-tap-highlight-color: transparent;
      user-select: none;
      -webkit-user-select: none;
    }}

    body {{
      background: #1b5e20;
      color: #333;
      width: 100vw;
      height: 100vh;
      height: 100dvh;
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: hidden;
      padding: 0;
      margin: 0;
    }}

    /* GAME CONTAINER: Fullscreen on mobile, framed on desktop */
    #game-container {{
      width: 100vw;
      height: 100dvh;
      max-width: 100%;
      max-height: 100%;
      background: #81d4fa;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}

    @media (min-width: 768px) and (min-height: 560px) {{
      #game-container {{
        width: 94vw;
        height: 92dvh;
        max-width: 960px;
        max-height: 640px;
        border: 6px solid var(--wood);
        border-radius: 24px;
        box-shadow: 0 16px 40px rgba(0,0,0,0.45);
      }}
    }}

    /* STATUS BAR (Mobile-first compact) */
    .status-bar {{
      height: 48px;
      flex-shrink: 0;
      background: rgba(62, 39, 35, 0.95);
      backdrop-filter: blur(8px);
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 12px;
      color: white;
      z-index: 50;
      border-bottom: 2.5px solid var(--gold);
    }}

    .lives-box {{
      display: flex;
      gap: 2px;
      align-items: center;
    }}

    .heart {{
      font-size: 18px;
      filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
      transition: all 0.2s;
    }}

    .heart.lost {{
      opacity: 0.25;
      filter: grayscale(1);
      transform: scale(0.85);
    }}

    .player-tag {{
      font-size: 13px;
      font-weight: 800;
      background: rgba(255, 255, 255, 0.18);
      padding: 3px 10px;
      border-radius: 14px;
      border: 1px solid rgba(255, 255, 255, 0.3);
      max-width: 130px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .score-badge {{
      display: flex;
      align-items: center;
      gap: 4px;
      font-size: 14px;
      font-weight: 800;
      color: #ffeb3b;
    }}

    .btn-sound {{
      background: none;
      border: none;
      font-size: 18px;
      cursor: pointer;
      color: white;
      padding: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    /* SCREENS */
    .screen {{
      flex: 1;
      width: 100%;
      height: calc(100% - 48px);
      display: none;
      flex-direction: column;
      position: relative;
      overflow: hidden;
    }}

    .screen.active {{
      display: flex;
    }}

    /* 1. START SCREEN (Mobile-first centered column) */
    #start-screen {{
      background: linear-gradient(180deg, #4fc3f7 0%, #81c784 60%, #2e7d32 100%);
      padding: 16px;
      text-align: center;
      justify-content: center;
      align-items: center;
      overflow-y: auto;
    }}

    .game-title-banner {{
      background: var(--wood);
      color: white;
      border: 3px solid var(--gold);
      padding: 12px 16px;
      border-radius: 16px;
      box-shadow: 0 6px 18px rgba(0,0,0,0.25);
      margin-bottom: 16px;
      width: 100%;
      max-width: 380px;
    }}

    .game-title-banner h1 {{
      font-size: 19px;
      color: #fff9c4;
      line-height: 1.4;
      text-shadow: 1px 1px 0px #3e2723;
    }}

    .game-title-banner p {{
      font-size: 12px;
      margin-top: 4px;
      color: #e0f2f1;
    }}

    .player-input-card {{
      background: white;
      padding: 18px 20px;
      border-radius: 20px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.18);
      display: flex;
      flex-direction: column;
      gap: 12px;
      width: 100%;
      max-width: 340px;
    }}

    .player-input-card input {{
      padding: 12px;
      font-size: 16px !important;
      text-align: center;
      border: 2px solid #a5d6a7;
      border-radius: 12px;
      outline: none;
      font-weight: bold;
      width: 100%;
      background: #fafafa;
    }}

    .player-input-card input:focus {{
      border-color: #2e7d32;
      background: white;
    }}

    .btn-start {{
      background: linear-gradient(135deg, #ff9800 0%, #f57c00 100%);
      color: white;
      font-size: 16px;
      font-weight: 800;
      padding: 12px 20px;
      border: none;
      border-radius: 14px;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(245, 124, 0, 0.4);
      min-height: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      width: 100%;
    }}

    .btn-start:active {{
      transform: scale(0.98);
    }}

    /* 2. STAGE SCREEN (Mobile-first flex column) */
    #stage-screen {{
      background: linear-gradient(180deg, #81d4fa 0%, #c8e6c9 55%, #4caf50 100%);
      display: none;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
    }}

    #stage-screen.active {{
      display: flex;
    }}

    /* SPEECH BUBBLE (Mobile-first top area) */
    .dialog-area {{
      padding: 10px 12px 4px 12px;
      display: flex;
      justify-content: center;
      z-index: 20;
    }}

    .dialog-bubble {{
      background: white;
      border: 2.5px solid var(--wood);
      border-radius: 16px;
      padding: 8px 14px;
      width: 100%;
      max-width: 480px;
      text-align: center;
      font-weight: 700;
      font-size: 13px;
      line-height: 1.5;
      color: #1b5e20;
      box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    }}

    /* ARENA (CHARACTERS FACING EACH OTHER) */
    .arena-area {{
      flex: 1;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      padding: 0 16px 8px 16px;
      position: relative;
      min-height: 130px;
    }}

    .stage-actor {{
      display: flex;
      flex-direction: column;
      align-items: center;
      transition: all 0.4s ease;
      z-index: 10;
    }}

    .actor-svg {{
      width: clamp(72px, 26vw, 115px);
      height: auto;
      filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));
    }}

    /* PATH AT BOTTOM */
    .adventure-path {{
      height: 58px;
      margin: 0 10px 10px 10px;
      background: #8d6e63;
      border-radius: 30px;
      border: 3px dashed #ffecb3;
      display: flex;
      justify-content: space-around;
      align-items: center;
      padding: 0 6px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.2);
      z-index: 5;
      flex-shrink: 0;
    }}

    .station-node {{
      width: 36px;
      height: 36px;
      background: #fff;
      border: 3px solid #795548;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 14px;
      color: #5d4037;
      transition: all 0.3s;
    }}

    .station-node.completed {{
      background: #4caf50;
      border-color: #1b5e20;
      color: white;
    }}

    .station-node.current {{
      background: #ffb300;
      border-color: #e65100;
      color: white;
      transform: scale(1.18);
      box-shadow: 0 0 12px rgba(255, 179, 0, 0.9);
      animation: pulseNode 1.5s infinite;
    }}

    @keyframes pulseNode {{
      0% {{ box-shadow: 0 0 0 0 rgba(255, 179, 0, 0.7); }}
      70% {{ box-shadow: 0 0 0 8px rgba(255, 179, 0, 0); }}
      100% {{ box-shadow: 0 0 0 0 rgba(255, 179, 0, 0); }}
    }}

    /* CHALLENGE OVERLAY (BOTTOM SHEET / MODAL) */
    .challenge-panel {{
      position: absolute;
      inset: 0;
      background: rgba(255, 255, 255, 0.98);
      backdrop-filter: blur(4px);
      z-index: 60;
      display: none;
      flex-direction: column;
      padding: 14px;
      overflow-y: auto;
      -webkit-overflow-scrolling: touch;
      animation: slideUp 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}

    .challenge-panel.open {{
      display: flex;
    }}

    @keyframes slideUp {{
      from {{ transform: translateY(30px); opacity: 0; }}
      to {{ transform: translateY(0); opacity: 1; }}
    }}

    .challenge-header {{
      display: flex;
      align-items: center;
      gap: 10px;
      border-bottom: 2px dashed #c8e6c9;
      padding-bottom: 8px;
      margin-bottom: 10px;
      flex-shrink: 0;
    }}

    .challenge-header h3 {{
      font-size: 15px;
      color: var(--wood);
    }}

    .question-prompt {{
      font-size: 15.5px;
      font-weight: 800;
      color: #1b5e20;
      margin-bottom: 12px;
      text-align: center;
      background: #e8f5e9;
      padding: 12px;
      border-radius: 12px;
      border: 2px solid #a5d6a7;
      line-height: 1.6;
      flex-shrink: 0;
    }}

    .choices-container {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      flex: 1;
    }}

    @media (min-width: 600px) {{
      .choices-container {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
      }}
    }}

    .choice-btn {{
      background: #fff;
      border: 2px solid #b0bec5;
      border-radius: 12px;
      padding: 10px 12px;
      font-size: 15px;
      font-weight: 800;
      color: #37474f;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: all 0.15s ease;
      min-height: 48px;
      text-align: right;
    }}

    .choice-btn:active {{
      background: #e8f5e9;
      border-color: #81c784;
    }}

    .choice-btn.correct-glow {{
      background: #4caf50 !important;
      color: white !important;
      border-color: #1b5e20 !important;
      animation: bounceWin 0.35s ease;
    }}

    .choice-btn.wrong-glow {{
      background: #e53935 !important;
      color: white !important;
      border-color: #b71c1c !important;
      animation: shakeWrong 0.35s ease;
    }}

    @keyframes bounceWin {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.04); }}
    }}

    @keyframes shakeWrong {{
      0%, 100% {{ transform: translateX(0); }}
      20%, 60% {{ transform: translateX(-6px); }}
      40%, 80% {{ transform: translateX(6px); }}
    }}

    .feedback-hint {{
      margin-top: 10px;
      padding: 8px 12px;
      background: #fff3e0;
      color: #e65100;
      border-radius: 10px;
      font-size: 12.5px;
      font-weight: 700;
      display: none;
      align-items: center;
      gap: 6px;
      flex-shrink: 0;
    }}

    /* 3. VICTORY SCREEN */
    #victory-screen {{
      background: linear-gradient(180deg, #fff8e1 0%, #ffe082 100%);
      padding: 16px;
      text-align: center;
      overflow-y: auto;
      justify-content: center;
      align-items: center;
    }}

    .diploma-card {{
      background: white;
      border: 4px double #ff8f00;
      border-radius: 18px;
      padding: 16px;
      width: 100%;
      max-width: 440px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.18);
    }}

    .diploma-seal {{
      width: 52px;
      height: 52px;
      background: #ffb300;
      border-radius: 50%;
      border: 3px dashed white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 28px;
      margin: 0 auto 8px;
    }}

    .diploma-card h2 {{
      font-size: 18px;
      color: #e65100;
      margin-bottom: 4px;
    }}

    .diploma-text {{
      font-size: 13.5px;
      line-height: 1.7;
      color: #4e342e;
      margin: 10px 0;
    }}

    .diploma-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 12px;
      padding-top: 10px;
      border-top: 2px dashed #ffcc80;
      font-size: 12.5px;
      font-weight: bold;
      flex-wrap: wrap;
      gap: 6px;
    }}

    #confetti-canvas {{
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 100;
    }}
  </style>
</head>
<body>

  <div id="game-container">
    <canvas id="confetti-canvas"></canvas>

    <!-- STATUS BAR -->
    <div class="status-bar">
      <div class="lives-box" id="lives-display"></div>
      <div class="player-tag" id="top-player-name">قهرمان دانا</div>
      <div style="display: flex; align-items: center; gap: 8px;">
        <div class="score-badge">
          <span>⭐</span>
          <span id="score-counter">۰</span>
        </div>
        <button class="btn-sound" id="sound-btn" onclick="toggleMute()" title="صدا">🔊</button>
      </div>
    </div>

    <!-- 1. START SCREEN -->
    <div id="start-screen" class="screen active">
      <div class="game-title-banner">
        <h1>{data.get('title', 'ماجراجویی در جنگل')}</h1>
        <p>{data.get('lesson', '')} • ویژه دانش‌آموزان کوشا</p>
      </div>

      <div class="player-input-card">
        <div style="font-size: 40px;">{ '🐿️' if data.get('hero') == 'squirrel' else ('🐰' if data.get('hero') == 'rabbit' else '🦊') }</div>
        <label style="font-weight: 800; font-size: 13.5px; color: #2e7d32;">نام قهرمان کوچک:</label>
        <input type="text" id="playerNameInput" placeholder="نام قشنگت را بنویس..." value="" autocomplete="off">
        <button class="btn-start" onclick="startGame()">شروع ماجراجویی در جنگل! 🚀</button>
      </div>
    </div>

    <!-- 2. STAGE SCREEN -->
    <div id="stage-screen" class="screen">
      <!-- TOP SPEECH DIALOG -->
      <div class="dialog-area">
        <div class="dialog-bubble" id="actor-dialog">
          «سلام قهرمان! به جنگل دانایی خوش آمدی!»
        </div>
      </div>

      <!-- ARENA: CHARACTERS FACING EACH OTHER -->
      <div class="arena-area">
        <div class="stage-actor" id="hero-actor">
          <div id="hero-svg-box"></div>
        </div>
        <div class="stage-actor" id="enemy-actor">
          <div id="enemy-svg-box"></div>
        </div>
      </div>

      <!-- PATH AT BOTTOM -->
      <div class="adventure-path" id="progress-path"></div>

      <!-- CHALLENGE POPUP OVERLAY -->
      <div class="challenge-panel" id="challenge-panel">
        <div class="challenge-header">
          <div style="font-size: 22px;" id="panel-animal-icon">🦁</div>
          <div>
            <h3 id="panel-animal-name">ایستگاه نگهبان</h3>
            <span style="font-size: 11px; color: #558b2f;" id="panel-station-info">سوال ۱ از ۲</span>
          </div>
        </div>

        <div class="question-prompt" id="question-text">متن سوال...</div>
        <div class="choices-container" id="choices-box"></div>

        <div class="feedback-hint" id="feedback-hint">
          <span>💡 راهنمایی:</span>
          <span id="hint-text">...</span>
        </div>
      </div>
    </div>

    <!-- 3. VICTORY SCREEN -->
    <div id="victory-screen" class="screen">
      <div class="diploma-card">
        <div class="diploma-seal">🏆</div>
        <h2>لوح افتخار قهرمان جنگل دانایی</h2>
        <p style="font-size: 12px; color: #795548; font-weight: bold;">به نام خداوند دانایی و خرد</p>
        
        <div class="diploma-text">
          این لوح به قهرمان کوشا و دانا، 
          <strong style="color: #2e7d32; font-size: 16px;" id="cert-player-name">نام دانش‌آموز</strong> 
          اهدا می‌گردد که با موفقیت از تمام موانع جنگل گذشت و به کلبه امن رسید.
          <br>
          مبحث: <strong>{data.get('lesson', '')}</strong>
          <br>
          امتیاز کسب‌شده: <span id="cert-score" style="color: #e65100; font-weight: 800;">۱۰۰</span> ستاره درخشان ⭐
        </div>

        <div class="diploma-footer">
          <div>آموزگار گرامی: <strong>{data.get('teacher', 'معلم مهربان شما')}</strong></div>
          <button class="btn-start" style="padding: 6px 12px; font-size: 12.5px; width: auto;" onclick="window.print()">🖨️ چاپ لوح</button>
        </div>
      </div>
      
      <button class="btn-start" style="margin-top: 12px; background: #2e7d32; width: auto; padding: 8px 24px;" onclick="location.reload()">🔄 بازی دوباره</button>
    </div>

  </div>

  <script>
    const GAME_CONFIG = {serialized};
    const SVG_LIB = {svg_defs_json};

    let audioCtx = null;
    let isMuted = false;

    function toPersianDigits(n) {{
      const p = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
      return String(n).replace(/[0-9]/g, d => p[+d]);
    }}

    function getAudioCtx() {{
      if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      if (audioCtx.state === 'suspended') audioCtx.resume();
      return audioCtx;
    }}

    function toggleMute() {{
      isMuted = !isMuted;
      document.getElementById('sound-btn').innerText = isMuted ? '🔇' : '🔊';
    }}

    function playSoundTone(freq, type, duration, delay = 0) {{
      if (isMuted) return;
      try {{
        const ctx = getAudioCtx();
        setTimeout(() => {{
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = type;
          osc.frequency.setValueAtTime(freq, ctx.currentTime);
          gain.gain.setValueAtTime(0.2, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start();
          osc.stop(ctx.currentTime + duration);
        }}, delay * 1000);
      }} catch (e) {{}}
    }}

    function sfxCorrect() {{
      playSoundTone(523.25, 'triangle', 0.15, 0);
      playSoundTone(659.25, 'triangle', 0.15, 0.08);
      playSoundTone(783.99, 'triangle', 0.15, 0.16);
      playSoundTone(1046.50, 'sine', 0.35, 0.24);
    }}

    function sfxWrong() {{
      playSoundTone(220, 'sawtooth', 0.18, 0);
      playSoundTone(180, 'sawtooth', 0.25, 0.12);
    }}

    function sfxJump() {{
      playSoundTone(350, 'sine', 0.18, 0);
    }}

    function sfxWin() {{
      const notes = [523, 659, 784, 1046, 880, 1046];
      notes.forEach((n, i) => playSoundTone(n, 'triangle', 0.25, i * 0.12));
    }}

    let currentStationIndex = 0;
    let stations = [];
    let currentLives = GAME_CONFIG.initialLives || 5;
    let currentScore = 0;
    let playerName = "قهرمان کوچک";

    function startGame() {{
      const nameInput = document.getElementById('playerNameInput');
      playerName = nameInput.value.trim() || 'قهرمان دانا';
      document.getElementById('top-player-name').innerText = playerName;
      document.getElementById('cert-player-name').innerText = playerName;

      const heroKey = GAME_CONFIG.hero || 'squirrel';
      document.getElementById('hero-svg-box').innerHTML = SVG_LIB[heroKey] || SVG_LIB.squirrel;

      buildJourney();
      updateLivesDisplay();
      updateScore(0);

      document.getElementById('start-screen').classList.remove('active');
      document.getElementById('stage-screen').classList.add('active');

      sfxJump();
      goToStation(0);
    }}

    function buildJourney() {{
      let activeAnimals = (GAME_CONFIG.animals || []).filter(a => a.selected);
      if (activeAnimals.length === 0) {{
        activeAnimals = [{{ id: 'lion', name: 'شیر نگهبان', icon: '🦁', questionsCount: 2, greeting: 'سلام!', success: 'آفرین!' }}];
      }}

      let chosenOrder = [...activeAnimals];
      if (GAME_CONFIG.randomize) {{
        chosenOrder.sort(() => Math.random() - 0.5);
      }}

      let generalPool = (GAME_CONFIG.questions || []).filter(q => !q.animalId || q.animalId === 'all');
      if (GAME_CONFIG.randomize) generalPool.sort(() => Math.random() - 0.5);

      stations = [];
      let generalIdx = 0;

      chosenOrder.forEach((animal, i) => {{
        let specificQuestions = (GAME_CONFIG.questions || []).filter(q => q.animalId === animal.id);
        if (GAME_CONFIG.randomize) specificQuestions.sort(() => Math.random() - 0.5);

        let qCount = animal.questionsCount || 1;
        let stationQuestions = [];

        for (let q of specificQuestions) {{
          if (stationQuestions.length < qCount) stationQuestions.push(q);
        }}

        while (stationQuestions.length < qCount && generalPool.length > 0) {{
          stationQuestions.push(generalPool[generalIdx % generalPool.length]);
          generalIdx++;
        }}

        if (stationQuestions.length === 0 && GAME_CONFIG.questions.length > 0) {{
          stationQuestions.push(GAME_CONFIG.questions[0]);
        }}

        stations.push({{
          index: i,
          animal: animal,
          questions: stationQuestions,
          currentQ: 0
        }});
      }});

      stations.push({{
        index: stations.length,
        isHome: true,
        animal: {{ id: 'home', name: 'کلبه امن جنگلی', icon: '🏡' }}
      }});

      renderPathNodes();
    }}

    function renderPathNodes() {{
      const pathEl = document.getElementById('progress-path');
      pathEl.innerHTML = stations.map((st, i) => {{
        let label = st.isHome ? '🏡' : (st.animal ? st.animal.icon : toPersianDigits(i + 1));
        return `<div class="station-node" id="node-${{i}}">${{label}}</div>`;
      }}).join('');
    }}

    function goToStation(index) {{
      currentStationIndex = index;

      stations.forEach((st, i) => {{
        const node = document.getElementById(`node-${{i}}`);
        if (!node) return;
        node.classList.remove('current', 'completed');
        if (i < index) node.classList.add('completed');
        else if (i === index) node.classList.add('current');
      }});

      const currentStation = stations[index];

      if (currentStation.isHome) {{
        triggerVictory();
        return;
      }}

      const enemySvgBox = document.getElementById('enemy-svg-box');
      const animKey = currentStation.animal.id;
      enemySvgBox.innerHTML = SVG_LIB[animKey] || SVG_LIB.custom_generic || SVG_LIB.lion;

      const dialogBubble = document.getElementById('actor-dialog');
      const greetingMsg = currentStation.animal.greeting || `«سلام ${{playerName}}! من ${{currentStation.animal.name}} هستم. معماهای من را حل کن!»`;
      dialogBubble.innerText = greetingMsg.replace('قهرمان', playerName);

      setTimeout(() => {{
        showQuestionForCurrentStation();
      }}, 800);
    }}

    function showQuestionForCurrentStation() {{
      const station = stations[currentStationIndex];
      const q = station.questions[station.currentQ];

      if (!q) {{
        onStationCleared();
        return;
      }}

      document.getElementById('panel-animal-icon').innerText = station.animal.icon;
      document.getElementById('panel-animal-name').innerText = station.animal.name;
      document.getElementById('panel-station-info').innerText = `معمای ${{toPersianDigits(station.currentQ + 1)}} از ${{toPersianDigits(station.questions.length)}}`;
      document.getElementById('question-text').innerText = q.text;

      const choicesBox = document.getElementById('choices-box');
      const labels = ['الف', 'ب', 'ج', 'د'];
      choicesBox.innerHTML = q.options.map((opt, idx) => `
        <button class="choice-btn" onclick="submitAnswer(${{idx}})">
          <span style="background:#cfd8dc; color:#37474f; border-radius:8px; padding:2px 8px; font-size:12px; font-weight:bold;">${{labels[idx] || (idx+1)}}</span>
          <span style="flex:1;">${{opt}}</span>
        </button>
      `).join('');

      document.getElementById('feedback-hint').style.display = 'none';
      document.getElementById('challenge-panel').classList.add('open');
    }}

    function submitAnswer(chosenIdx) {{
      const station = stations[currentStationIndex];
      const q = station.questions[station.currentQ];
      const buttons = document.querySelectorAll('.choice-btn');

      if (chosenIdx === q.correct) {{
        sfxCorrect();
        if (buttons[chosenIdx]) buttons[chosenIdx].classList.add('correct-glow');
        updateScore(currentScore + 20);

        document.getElementById('actor-dialog').innerText = `«آفرین ${{playerName}}! کاملاً درست بود! 👏»`;

        setTimeout(() => {{
          document.getElementById('challenge-panel').classList.remove('open');
          station.currentQ++;
          if (station.currentQ < station.questions.length) {{
            setTimeout(showQuestionForCurrentStation, 500);
          }} else {{
            onStationCleared();
          }}
        }}, 700);

      }} else {{
        sfxWrong();
        if (buttons[chosenIdx]) buttons[chosenIdx].classList.add('wrong-glow');
        currentLives--;
        updateLivesDisplay();

        if (q.hint) {{
          document.getElementById('hint-text').innerText = q.hint;
          document.getElementById('feedback-hint').style.display = 'flex';
        }}

        document.getElementById('actor-dialog').innerText = `«اشکالی نداره قهرمان! یه بار دیگه دقت کن!»`;

        if (currentLives <= 0) {{
          setTimeout(handleRescueOrRetry, 800);
        }}
      }}
    }}

    function onStationCleared() {{
      sfxJump();
      const station = stations[currentStationIndex];
      const successMsg = station.animal.success || `«تبریک می‌گم ${{playerName}}! راه باز شد، موفق باشی! 🌟»`;
      document.getElementById('actor-dialog').innerText = successMsg.replace('قهرمان', playerName);
      
      const hero = document.getElementById('hero-actor');
      hero.style.transform = 'translateY(-14px) scale(1.1)';
      setTimeout(() => {{
        hero.style.transform = 'translateY(0) scale(1)';
        goToStation(currentStationIndex + 1);
      }}, 900);
    }}

    function handleRescueOrRetry() {{
      document.getElementById('challenge-panel').classList.remove('open');
      sfxCorrect();
      alert("🦉 جغد دانا از راه رسید: «هیچ قهرمانی در جنگل تسلیم نمی‌شود! من ۳ جان تازه به تو هدیه می‌دهم!»");
      currentLives = 3;
      updateLivesDisplay();
      showQuestionForCurrentStation();
    }}

    function updateLivesDisplay() {{
      const box = document.getElementById('lives-display');
      let html = '';
      for (let i = 0; i < (GAME_CONFIG.initialLives || 5); i++) {{
        html += `<span class="heart ${{i < currentLives ? '' : 'lost'}}">❤️</span>`;
      }}
      box.innerHTML = html;
    }}

    function updateScore(val) {{
      currentScore = val;
      document.getElementById('score-counter').innerText = toPersianDigits(currentScore);
    }}

    function triggerVictory() {{
      document.getElementById('stage-screen').classList.remove('active');
      document.getElementById('victory-screen').classList.add('active');
      document.getElementById('cert-score').innerText = toPersianDigits(currentScore);
      sfxWin();
      startConfetti();
    }}

    function startConfetti() {{
      const canvas = document.getElementById('confetti-canvas');
      const ctx = canvas.getContext('2d');
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;

      const pieces = [];
      const colors = ['#f44336', '#e91e63', '#9c27b0', '#3f51b5', '#03a9f4', '#4caf50', '#ffeb3b', '#ff9800'];

      for (let i = 0; i < 70; i++) {{
        pieces.push({{
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height - canvas.height,
          size: Math.random() * 7 + 4,
          color: colors[Math.floor(Math.random() * colors.length)],
          speedY: Math.random() * 3 + 2,
          speedX: Math.random() * 2 - 1,
          rot: Math.random() * 360
        }});
      }}

      function update() {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        pieces.forEach(p => {{
          p.y += p.speedY;
          p.x += p.speedX;
          p.rot += 2;
          if (p.y > canvas.height) p.y = -10;
          ctx.save();
          ctx.translate(p.x, p.y);
          ctx.rotate((p.rot * Math.PI) / 180);
          ctx.fillStyle = p.color;
          ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
          ctx.restore();
        }});
        requestAnimationFrame(update);
      }}
      update();
    }}
  </script>
</body>
</html>"""
