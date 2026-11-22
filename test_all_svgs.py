# -*- coding: utf-8 -*-
"""
Test all 13 SVG definitions for Jungle Adventure
"""

SVGS = {
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

    'wolf': '''<svg viewBox="0 0 120 120" class="actor-svg">
      <!-- Snowy Wolf with glowing eyes -->
      <path d="M 35,40 L 25,15 L 45,30 Z" fill="#78909c"/>
      <path d="M 85,40 L 95,15 L 75,30 Z" fill="#78909c"/>
      <circle cx="60" cy="62" r="38" fill="#546e7a" stroke="#37474f" stroke-width="3"/>
      <polygon points="40,55 60,85 80,55" fill="#cfd8dc"/>
      <!-- Glowing yellow/red eyes -->
      <polygon points="44,50 54,54 46,58" fill="#ffd600"/>
      <polygon points="76,50 66,54 74,58" fill="#ffd600"/>
      <circle cx="49" cy="54" r="2" fill="#d50000"/>
      <circle cx="71" cy="54" r="2" fill="#d50000"/>
      <!-- Snout & Fangs -->
      <polygon points="56,72 64,72 60,78" fill="#212121"/>
      <polygon points="52,80 55,87 58,80" fill="#fff"/>
      <polygon points="62,80 65,87 68,80" fill="#fff"/>
    </svg>''',

    'snake': '''<svg viewBox="0 0 120 120" class="actor-svg">
      <!-- Coiled Green Snake -->
      <path d="M 30,95 Q 60,105 90,95 Q 105,80 90,65 Q 50,60 40,45 Q 35,30 55,22 Q 75,18 85,30" fill="none" stroke="#2e7d32" stroke-width="14" stroke-linecap="round"/>
      <path d="M 30,95 Q 60,105 90,95 Q 105,80 90,65 Q 50,60 40,45 Q 35,30 55,22 Q 75,18 85,30" fill="none" stroke="#81c784" stroke-width="6" stroke-linecap="round"/>
      <!-- Snake Head -->
      <ellipse cx="88" cy="30" rx="14" ry="10" fill="#388e3c" stroke="#1b5e20" stroke-width="2"/>
      <circle cx="92" cy="27" r="3" fill="#ffeb3b"/>
      <circle cx="92" cy="27" r="1.5" fill="#000"/>
      <!-- Forked Tongue -->
      <path d="M 102,30 L 114,26 M 102,30 L 114,34" stroke="#d50000" stroke-width="2" stroke-linecap="round"/>
    </svg>''',

    'trunk': '''<svg viewBox="0 0 130 110" class="actor-svg">
      <!-- Massive Fallen Tree Trunk blocking path -->
      <ellipse cx="25" cy="65" rx="16" ry="24" fill="#6d4c41" stroke="#3e2723" stroke-width="3"/>
      <ellipse cx="25" cy="65" rx="10" ry="16" fill="#8d6e63"/>
      <ellipse cx="25" cy="65" rx="5" ry="8" fill="#a1887f"/>
      <path d="M 25,41 L 110,50 Q 120,68 110,86 L 25,89 Z" fill="#4e342e" stroke="#3e2723" stroke-width="3"/>
      <!-- Green moss & small branches -->
      <path d="M 45,45 Q 60,35 75,47" fill="none" stroke="#4caf50" stroke-width="4"/>
      <path d="M 70,40 L 75,26 L 82,24" stroke="#5d4037" stroke-width="3" fill="none"/>
      <circle cx="82" cy="24" r="5" fill="#81c784"/>
    </svg>''',

    'oldman': '''<svg viewBox="0 0 120 120" class="actor-svg">
      <!-- Wise Old Man with glowing lantern -->
      <ellipse cx="60" cy="85" rx="28" ry="30" fill="#455a64"/>
      <!-- Long White Beard -->
      <path d="M 42,55 Q 60,110 78,55 Z" fill="#eceff1" stroke="#b0bec5" stroke-width="2"/>
      <!-- Face -->
      <circle cx="60" cy="45" r="18" fill="#ffcc80"/>
      <!-- White Eyebrows & Eyes -->
      <path d="M 48,40 Q 53,36 57,40" stroke="#fff" stroke-width="3" fill="none"/>
      <path d="M 63,40 Q 67,36 72,40" stroke="#fff" stroke-width="3" fill="none"/>
      <circle cx="53" cy="44" r="2.5" fill="#37474f"/>
      <circle cx="67" cy="44" r="2.5" fill="#37474f"/>
      <!-- Hood -->
      <path d="M 38,45 Q 60,15 82,45 Z" fill="#37474f"/>
      <!-- Glowing Lantern held in hand -->
      <rect x="85" y="60" width="16" height="24" rx="4" fill="#ffd600" stroke="#ff6f00" stroke-width="2"/>
      <line x1="93" y1="52" x2="93" y2="60" stroke="#ff6f00" stroke-width="2"/>
    </svg>''',

    'dragon': '''<svg viewBox="0 0 130 120" class="actor-svg">
      <!-- Fire Dragon -->
      <path d="M 20,80 Q 50,40 85,55 Q 115,45 125,30 Q 110,65 95,85 Q 60,105 20,80 Z" fill="#c62828" stroke="#8e0000" stroke-width="3"/>
      <!-- Horns -->
      <path d="M 85,45 Q 95,20 110,15" stroke="#ffd54f" stroke-width="4" fill="none"/>
      <path d="M 78,48 Q 85,26 96,22" stroke="#ffd54f" stroke-width="3" fill="none"/>
      <!-- Spikes -->
      <polygon points="40,65 48,50 56,65" fill="#ffd54f"/>
      <polygon points="60,65 68,52 76,65" fill="#ffd54f"/>
      <!-- Glowing Eye -->
      <circle cx="102" cy="42" r="5" fill="#ffeb3b"/>
      <circle cx="102" cy="42" r="2" fill="#000"/>
      <!-- Fire smoke from snout -->
      <path d="M 120,40 Q 130,35 125,48 Q 135,45 122,55" fill="#ff9800" opacity="0.85"/>
      <circle cx="128" cy="42" r="4" fill="#ffeb3b"/>
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

    'crocodile': '''<svg viewBox="0 0 130 110" class="actor-svg">
      <ellipse cx="65" cy="90" rx="55" ry="12" fill="#29b6f6" opacity="0.6"/>
      <path d="M 20,70 Q 65,40 110,65 Q 115,80 90,82 Q 50,85 20,70 Z" fill="#388e3c" stroke="#1b5e20" stroke-width="3"/>
      <circle cx="45" cy="46" r="10" fill="#81c784"/>
      <circle cx="45" cy="46" r="4" fill="#000"/>
      <circle cx="68" cy="46" r="10" fill="#81c784"/>
      <circle cx="68" cy="46" r="4" fill="#000"/>
      <polygon points="50,72 55,65 60,72 65,65 70,72" fill="#fff"/>
    </svg>''',

    'monkey': '''<svg viewBox="0 0 120 120" class="actor-svg">
      <circle cx="24" cy="55" r="14" fill="#a1887f"/>
      <circle cx="24" cy="55" r="8" fill="#d7ccc8"/>
      <circle cx="96" cy="55" r="14" fill="#a1887f"/>
      <circle cx="96" cy="55" r="8" fill="#d7ccc8"/>
      <ellipse cx="60" cy="58" rx="34" ry="30" fill="#6d4c41"/>
      <ellipse cx="60" cy="65" rx="26" ry="18" fill="#d7ccc8"/>
      <circle cx="48" cy="50" r="5" fill="#fff"/><circle cx="49" cy="50" r="2.5" fill="#000"/>
      <circle cx="72" cy="50" r="5" fill="#fff"/><circle cx="71" cy="50" r="2.5" fill="#000"/>
      <path d="M 50,70 Q 60,78 70,70" stroke="#3e2723" stroke-width="3" fill="none" stroke-linecap="round"/>
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

    'bear': '''<svg viewBox="0 0 120 120" class="actor-svg">
      <circle cx="32" cy="35" r="14" fill="#5d4037"/>
      <circle cx="88" cy="35" r="14" fill="#5d4037"/>
      <circle cx="60" cy="62" r="36" fill="#795548"/>
      <ellipse cx="60" cy="74" rx="16" ry="12" fill="#d7ccc8"/>
      <ellipse cx="60" cy="69" rx="6" ry="4" fill="#3e2723"/>
      <circle cx="48" cy="56" r="3.5" fill="#212121"/><circle cx="72" cy="56" r="3.5" fill="#212121"/>
      <rect x="76" y="78" width="22" height="24" rx="6" fill="#ffb300" stroke="#e65100" stroke-width="2"/>
    </svg>''',

    'fox': '''<svg viewBox="0 0 100 110" class="actor-svg">
      <!-- Tricky Fox -->
      <polygon points="32,45 25,22 45,35" fill="#ff5722"/>
      <polygon points="72,45 79,22 59,35" fill="#ff5722"/>
      <ellipse cx="52" cy="76" rx="22" ry="24" fill="#ff5722" stroke="#d84315" stroke-width="2.5"/>
      <polygon points="32,45 72,45 52,72" fill="#ff5722"/>
      <polygon points="34,48 48,65 52,70 42,48" fill="#fff"/>
      <polygon points="70,48 56,65 52,70 62,48" fill="#fff"/>
      <!-- Smirking eyes -->
      <path d="M 40,48 Q 45,44 50,49" stroke="#212121" stroke-width="3" fill="none"/>
      <path d="M 64,48 Q 59,44 54,49" stroke="#212121" stroke-width="3" fill="none"/>
      <circle cx="52" cy="70" r="3" fill="#212121"/>
      <!-- Grin -->
      <path d="M 46,65 Q 52,72 58,63" stroke="#d84315" stroke-width="2.5" fill="none"/>
    </svg>''',

    'turtle': '''<svg viewBox="0 0 120 120" class="actor-svg">
      <!-- Slow Turtle -->
      <!-- Shell -->
      <path d="M 25,75 Q 60,30 95,75 Z" fill="#2e7d32" stroke="#1b5e20" stroke-width="3"/>
      <ellipse cx="60" cy="75" rx="36" ry="8" fill="#388e3c"/>
      <!-- Shell patterns -->
      <polygon points="45,65 60,50 75,65 68,75 52,75" fill="#81c784" stroke="#1b5e20" stroke-width="1.5"/>
      <!-- Head with round spectacles -->
      <ellipse cx="102" cy="68" rx="12" ry="9" fill="#81c784" stroke="#1b5e20" stroke-width="2"/>
      <circle cx="104" cy="65" r="4" fill="#fff" stroke="#ff9800" stroke-width="1.5"/>
      <circle cx="104" cy="65" r="2" fill="#212121"/>
      <!-- Feet -->
      <ellipse cx="36" cy="84" rx="8" ry="5" fill="#81c784"/>
      <ellipse cx="84" cy="84" rx="8" ry="5" fill="#81c784"/>
    </svg>''',

    'bat': '''<svg viewBox="0 0 130 110" class="actor-svg">
      <!-- Swarm Bat -->
      <path d="M 65,55 Q 85,25 115,35 Q 105,65 85,75 Q 75,80 65,70" fill="#37474f" stroke="#212121" stroke-width="2"/>
      <path d="M 65,55 Q 45,25 15,35 Q 25,65 45,75 Q 55,80 65,70" fill="#37474f" stroke="#212121" stroke-width="2"/>
      <ellipse cx="65" cy="65" rx="10" ry="14" fill="#263238"/>
      <!-- Ears -->
      <polygon points="58,55 54,42 62,50" fill="#37474f"/>
      <polygon points="72,55 76,42 68,50" fill="#37474f"/>
      <!-- Glowing Red Eyes -->
      <circle cx="61" cy="60" r="2" fill="#ff1744"/>
      <circle cx="69" cy="60" r="2" fill="#ff1744"/>
      <!-- Little fangs -->
      <polygon points="63,68 65,72 67,68" fill="#fff"/>
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

print("All 15 SVGs compiled successfully!")
