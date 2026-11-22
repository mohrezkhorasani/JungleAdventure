# -*- coding: utf-8 -*-
"""
Builder script to generate index.html (Teacher Studio) and بازی_ماجراجویی_جنگل.html
Features:
- 100% Mobile Responsive layout (portrait & landscape, dynamic dvh, responsive touch UI)
- Embedded Persian Vazir Font (Base64 WOFF2) for beautiful typography offline
- Complete, functional Admin Panel with Question Assignment, Custom Animals/Events, Bulk Import, Search, etc.
"""

import os
import json

# Read embedded font CSS
with open('embedded_fonts.css', 'r', encoding='utf-8') as f:
    EMBEDDED_FONT_CSS = f.read()

# Common SVG library for characters and animals
SVG_LIBRARY = {
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
      <!-- Ears -->
      <ellipse cx="40" cy="22" rx="7" ry="20" fill="#fff" stroke="#cfd8dc" stroke-width="2"/>
      <ellipse cx="40" cy="22" rx="4" ry="14" fill="#f8bbd0"/>
      <ellipse cx="60" cy="22" rx="7" ry="20" fill="#fff" stroke="#cfd8dc" stroke-width="2"/>
      <ellipse cx="60" cy="22" rx="4" ry="14" fill="#f8bbd0"/>
      <!-- Body -->
      <ellipse cx="50" cy="78" rx="24" ry="24" fill="#fff" stroke="#cfd8dc" stroke-width="2"/>
      <ellipse cx="50" cy="80" rx="15" ry="16" fill="#f5f5f5"/>
      <!-- Backpack -->
      <rect x="22" y="68" width="12" height="18" rx="4" fill="#ff7043" stroke="#d84315" stroke-width="2"/>
      <!-- Feet -->
      <ellipse cx="38" cy="100" rx="10" ry="5" fill="#eceff1"/>
      <ellipse cx="62" cy="100" rx="10" ry="5" fill="#eceff1"/>
      <!-- Head -->
      <circle cx="50" cy="48" r="20" fill="#fff" stroke="#cfd8dc" stroke-width="2"/>
      <!-- Hat -->
      <path d="M 32,36 Q 50,26 68,36 Q 74,38 72,42 L 28,42 Q 26,38 32,36 Z" fill="#ffb300" stroke="#f57c00" stroke-width="2"/>
      <!-- Eyes -->
      <circle cx="43" cy="48" r="3.5" fill="#212121"/><circle cx="57" cy="48" r="3.5" fill="#212121"/>
      <circle cx="44" cy="46.5" r="1.2" fill="#fff"/><circle cx="58" cy="46.5" r="1.2" fill="#fff"/>
      <!-- Nose & mouth -->
      <polygon points="48,54 52,54 50,57" fill="#f06292"/>
      <path d="M 47,59 Q 50,62 53,59" fill="none" stroke="#78909c" stroke-width="2" stroke-linecap="round"/>
    </svg>''',

    'fox': '''<svg viewBox="0 0 100 110" class="actor-svg">
      <!-- Tail -->
      <path d="M 26,85 C 5,75 -5,45 15,30 C 25,20 40,40 35,60 C 30,75 28,85 26,85" fill="#ff5722" stroke="#d84315" stroke-width="2.5"/>
      <path d="M 12,38 C 18,30 28,35 24,48 C 16,52 10,44 12,38" fill="#fff"/>
      <!-- Body -->
      <ellipse cx="52" cy="76" rx="22" ry="24" fill="#ff5722" stroke="#d84315" stroke-width="2.5"/>
      <ellipse cx="52" cy="79" rx="13" ry="16" fill="#fff"/>
      <ellipse cx="40" cy="99" rx="8" ry="5" fill="#3e2723"/>
      <ellipse cx="64" cy="99" rx="8" ry="5" fill="#3e2723"/>
      <!-- Head -->
      <polygon points="32,45 72,45 52,70" fill="#ff5722" stroke="#d84315" stroke-width="2.5"/>
      <!-- Cheeks white -->
      <polygon points="34,48 48,65 52,70 42,48" fill="#fff"/>
      <polygon points="70,48 56,65 52,70 62,48" fill="#fff"/>
      <!-- Ears -->
      <polygon points="32,45 25,22 45,35" fill="#ff5722"/>
      <polygon points="30,42 27,27 40,36" fill="#3e2723"/>
      <polygon points="72,45 79,22 59,35" fill="#ff5722"/>
      <polygon points="74,42 77,27 64,36" fill="#3e2723"/>
      <!-- Eyes -->
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

print("SVG library prepared with", len(SVG_LIBRARY), "items.")
