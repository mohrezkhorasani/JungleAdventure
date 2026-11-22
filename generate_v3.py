# -*- coding: utf-8 -*-
"""
generate_v3.py: Generates the v3.0 Jungle Adventure Game and Teacher Studio
Features:
- Visual Roadmap Graph with 10 Waypoints & Mystery (?) Badges
- Pawn walk/hop along the path to the next node
- 13 Custom Events with individual atmospheres and game mechanics
- Scoring system: 5 base points, delay decay, multipliers, integer score <= 100
- Base64 UTF-8 Template export (no script parsing bugs)
- Mobile-first responsive design
"""

import os
import json
import base64

base_dir = r"f:\DOTNET\FNSymposium\JungleAdventure"

font_css_path = r"F:\DOTNET\FNSymposium\embedded_fonts.css"
with open(font_css_path, "r", encoding="utf-8") as f:
    EMBEDDED_FONT_CSS = f.read()

from test_all_svgs import SVGS
from build_jungle_adventure_v3 import ALL_13_ANIMALS, SAMPLE_QUESTIONS, DEFAULT_PROJECT_DATA

svg_library_json = json.dumps(SVGS, ensure_ascii=False)
animals_json = json.dumps(ALL_13_ANIMALS, ensure_ascii=False)
default_project_json = json.dumps(DEFAULT_PROJECT_DATA, ensure_ascii=False)

# Let's create the game engine HTML template
GAME_ENGINE_HTML = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>__GAME_TITLE_PLACEHOLDER__</title>
  <style>
    {EMBEDDED_FONT_CSS}

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
      margin: 0;
      padding: 0;
    }}

    #game-container {{
      width: 100vw;
      height: 100dvh;
      max-width: 100%;
      max-height: 100%;
      background: #c8e6c9;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}

    @media (min-width: 768px) and (min-height: 560px) {{
      #game-container {{
        width: 95vw;
        height: 92dvh;
        max-width: 980px;
        max-height: 660px;
        border: 6px solid var(--wood);
        border-radius: 24px;
        box-shadow: 0 16px 40px rgba(0,0,0,0.5);
      }}
    }}

    /* TOP STATUS BAR */
    .status-bar {{
      height: 48px;
      flex-shrink: 0;
      background: rgba(62, 39, 35, 0.96);
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
      gap: 3px;
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

    .lantern-badge {{
      display: flex;
      align-items: center;
      gap: 4px;
      font-size: 13px;
      font-weight: 800;
      background: rgba(255, 179, 0, 0.25);
      padding: 3px 10px;
      border-radius: 14px;
      border: 1px solid #ffd54f;
      color: #fff9c4;
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

    /* 1. START SCREEN */
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
      max-width: 400px;
    }}

    .game-title-banner h1 {{
      font-size: 20px;
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

    .btn-action {{
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

    .btn-action:active {{
      transform: scale(0.98);
    }}

    /* 2. ROADMAP GRAPH SCREEN */
    #map-screen {{
      background: linear-gradient(180deg, #81d4fa 0%, #a5d6a7 50%, #558b2f 100%);
      display: none;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      overflow: hidden;
    }}

    #map-screen.active {{
      display: flex;
    }}

    .map-header-bar {{
      padding: 8px 12px;
      background: rgba(255, 255, 255, 0.9);
      border-bottom: 2px solid #a5d6a7;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13px;
      font-weight: 800;
      color: var(--primary-dark);
      z-index: 10;
    }}

    /* ROADMAP CANVAS AREA */
    .map-canvas-container {{
      flex: 1;
      position: relative;
      width: 100%;
      height: 100%;
      overflow: hidden;
    }}

    .map-svg-layer {{
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
    }}

    /* ROADMAP NODES */
    .map-node {{
      position: absolute;
      width: clamp(40px, 9vw, 54px);
      height: clamp(40px, 9vw, 54px);
      transform: translate(-50%, -50%);
      border-radius: 50%;
      background: white;
      border: 3px solid #795548;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: clamp(16px, 4vw, 24px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.25);
      transition: all 0.4s ease;
      z-index: 15;
      cursor: pointer;
    }}

    .map-node.completed {{
      background: #4caf50;
      border-color: #1b5e20;
      color: white;
    }}

    .map-node.current {{
      background: #ffb300;
      border-color: #e65100;
      transform: translate(-50%, -50%) scale(1.18);
      box-shadow: 0 0 16px rgba(255, 179, 0, 0.95);
      animation: pulseMapNode 1.5s infinite;
      z-index: 20;
    }}

    .map-node.locked {{
      background: #cfd8dc;
      border-color: #90a4ae;
      opacity: 0.9;
    }}

    @keyframes pulseMapNode {{
      0% {{ box-shadow: 0 0 0 0 rgba(255, 179, 0, 0.7); }}
      70% {{ box-shadow: 0 0 0 10px rgba(255, 179, 0, 0); }}
      100% {{ box-shadow: 0 0 0 0 rgba(255, 179, 0, 0); }}
    }}

    /* HERO PAWN ON MAP */
    .hero-pawn {{
      position: absolute;
      width: 44px;
      height: 48px;
      transform: translate(-50%, -100%);
      pointer-events: none;
      z-index: 30;
      transition: all 0.7s cubic-bezier(0.34, 1.56, 0.64, 1);
      filter: drop-shadow(0 4px 6px rgba(0,0,0,0.3));
    }}

    .hero-pawn .pawn-svg {{
      width: 100%;
      height: 100%;
    }}

    /* MAP BOTTOM BAR */
    .map-bottom-bar {{
      padding: 10px 14px;
      background: rgba(255, 255, 255, 0.92);
      border-top: 2px solid #a5d6a7;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      z-index: 10;
    }}

    /* 3. ENCOUNTER SCREEN (Full Interactive Arena) */
    #encounter-screen {{
      background: #e8f5e9;
      display: none;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      overflow: hidden;
    }}

    #encounter-screen.active {{
      display: flex;
    }}

    /* ATMOSPHERE HEADER */
    .encounter-header {{
      padding: 8px 12px;
      background: rgba(255, 255, 255, 0.94);
      border-bottom: 2px solid #c8e6c9;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13px;
      font-weight: 800;
      z-index: 20;
    }}

    .timer-pill {{
      display: none;
      align-items: center;
      gap: 4px;
      background: #ffebee;
      color: #c62828;
      border: 1.5px solid #ef9a9a;
      padding: 3px 10px;
      border-radius: 14px;
      font-weight: 800;
      animation: pulseTimer 1s infinite;
    }}

    @keyframes pulseTimer {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.05); }}
    }}

    .multiplier-pill {{
      display: flex;
      align-items: center;
      gap: 4px;
      background: #fff8e1;
      color: #f57f17;
      border: 1.5px solid #ffe082;
      padding: 3px 10px;
      border-radius: 14px;
      font-weight: 800;
    }}

    /* ARENA WITH DYNAMIC ATMOSPHERE */
    .encounter-arena {{
      flex: 1;
      position: relative;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      padding: 0 16px 10px 16px;
      overflow: hidden;
      min-height: 150px;
    }}

    /* BIOME ATMOSPHERES */
    .encounter-arena.biome-wolf {{
      background: linear-gradient(180deg, #0d1b2a 0%, #1b263b 50%, #415a77 100%);
    }}
    .encounter-arena.biome-dragon {{
      background: linear-gradient(180deg, #bf360c 0%, #d84315 40%, #ff8f00 100%);
    }}
    .encounter-arena.biome-bat {{
      background: radial-gradient(circle at center, #263238 0%, #000a12 100%);
    }}
    .encounter-arena.biome-snake {{
      background: linear-gradient(180deg, #2e7d32 0%, #1b5e20 60%, #004d40 100%);
    }}
    .encounter-arena.biome-normal {{
      background: linear-gradient(180deg, #81d4fa 0%, #c8e6c9 60%, #4caf50 100%);
    }}

    .actor-svg {{
      width: clamp(75px, 25vw, 115px);
      height: auto;
      filter: drop-shadow(0 4px 8px rgba(0,0,0,0.25));
    }}

    /* DIALOG SPEECH BUBBLE */
    .encounter-dialog {{
      position: absolute;
      top: 10px;
      left: 10px;
      right: 10px;
      background: white;
      border: 2.5px solid var(--wood);
      border-radius: 16px;
      padding: 8px 14px;
      text-align: center;
      font-weight: 700;
      font-size: 13px;
      line-height: 1.5;
      color: #1b5e20;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
      z-index: 15;
    }}

    /* CHALLENGE CARD OVERLAY */
    .challenge-panel {{
      position: absolute;
      inset: 0;
      background: rgba(255, 255, 255, 0.98);
      backdrop-filter: blur(4px);
      z-index: 60;
      display: none;
      flex-direction: column;
      padding: 12px;
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

    .challenge-header-card {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px dashed #c8e6c9;
      padding-bottom: 6px;
      margin-bottom: 8px;
    }}

    .question-prompt {{
      font-size: 15.5px;
      font-weight: 800;
      color: #1b5e20;
      margin-bottom: 10px;
      text-align: center;
      background: #e8f5e9;
      padding: 10px 12px;
      border-radius: 12px;
      border: 2px solid #a5d6a7;
      line-height: 1.6;
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

    .btn-use-lantern {{
      margin-top: 8px;
      background: #fff8e1;
      border: 2px dashed #ffb300;
      color: #e65100;
      font-size: 13px;
      font-weight: 800;
      padding: 8px 12px;
      border-radius: 10px;
      cursor: pointer;
      display: none;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}

    .btn-use-lantern.show {{
      display: flex;
    }}

    /* FOX DOUBT MODAL */
    .fox-doubt-overlay {{
      position: absolute;
      inset: 0;
      background: rgba(0, 0, 0, 0.7);
      z-index: 75;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 16px;
    }}

    .fox-doubt-overlay.show {{
      display: flex;
    }}

    .fox-doubt-card {{
      background: white;
      border: 3px solid #ff9800;
      border-radius: 18px;
      padding: 16px;
      max-width: 340px;
      text-align: center;
      box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }}

    /* 4. VICTORY SCREEN */
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
      <div class="lantern-badge" id="lantern-counter-badge">
        <span>🏮</span>
        <span id="lantern-count">۰</span>
      </div>
      <div class="score-badge">
        <span>⭐</span>
        <span id="score-counter">۰</span>
        <span style="font-size:11px; opacity:0.8;">/ ۱۰۰</span>
      </div>
      <button class="btn-sound" id="sound-btn" onclick="toggleMute()" title="صدا">🔊</button>
    </div>

    <!-- SCREEN 1: START SCREEN -->
    <div id="start-screen" class="screen active">
      <div class="game-title-banner">
        <h1 id="start-title-text">ماجراجویی در جنگل شگفت‌انگیز</h1>
        <p id="start-lesson-text">ریاضی و علوم شاد دبستان • ویژه دانش‌آموزان کوشا</p>
      </div>

      <div class="player-input-card">
        <div style="font-size: 40px;" id="hero-avatar-display">🐿️</div>
        <label style="font-weight: 800; font-size: 13.5px; color: #2e7d32;">نام قهرمان کوچک:</label>
        <input type="text" id="playerNameInput" placeholder="نام قشنگت را بنویس..." value="" autocomplete="off">
        <button class="btn-action" onclick="startGame()">شروع ماجراجویی در نقشه! 🗺️</button>
      </div>
    </div>

    <!-- SCREEN 2: ROADMAP GRAPH SCREEN -->
    <div id="map-screen" class="screen">
      <div class="map-header-bar">
        <span>🗺️ نقشه ماجراجویی جنگل</span>
        <span id="map-progress-text">ایستگاه ۱ از ۱۰</span>
      </div>

      <div class="map-canvas-container" id="map-canvas-container">
        <!-- SVG Trajectory Line -->
        <svg class="map-svg-layer" id="map-svg-layer" viewBox="0 0 100 100" preserveAspectRatio="none">
          <path id="map-path-line" d="M 15,90 Q 50,85 80,75 T 20,55 T 80,35 T 50,15" fill="none" stroke="#5d4037" stroke-width="2.5" stroke-dasharray="2,2"/>
        </svg>

        <!-- Nodes injected here -->
        <div id="map-nodes-container"></div>

        <!-- Hero pawn moving on map -->
        <div class="hero-pawn" id="hero-map-pawn">
          <div class="pawn-svg" id="hero-pawn-svg"></div>
        </div>
      </div>

      <div class="map-bottom-bar">
        <div style="font-size:12.5px; font-weight:800; color:#2e7d32;" id="map-hint-text">
          برای حرکت به ایستگاه بعدی آماده‌ای؟
        </div>
        <button class="btn-action" style="width:auto; padding:8px 18px; font-size:13.5px;" id="map-move-btn" onclick="moveToNextMapStation()">
          حرکت به ایستگاه بعدی 🐾
        </button>
      </div>
    </div>

    <!-- SCREEN 3: ENCOUNTER SCREEN -->
    <div id="encounter-screen" class="screen">
      <div class="encounter-header">
        <div style="display:flex; align-items:center; gap:8px;">
          <span style="font-size:18px;" id="enc-animal-icon">🐺</span>
          <span id="enc-animal-name">گرگ‌های برفی</span>
        </div>
        <div style="display:flex; align-items:center; gap:8px;">
          <div class="timer-pill" id="enc-timer-pill">
            <span>⏳</span>
            <span id="enc-timer-sec">۳۰</span>
          </div>
          <div class="multiplier-pill" id="enc-multiplier-pill">
            <span id="enc-multiplier-text">ضریب: ×۱</span>
          </div>
        </div>
      </div>

      <!-- ARENA -->
      <div class="encounter-arena biome-normal" id="encounter-arena-box">
        <div class="encounter-dialog" id="enc-dialog-bubble">
          «دیالوگ آغازین حیوان...»
        </div>

        <div class="stage-actor" id="enc-hero-actor">
          <div id="enc-hero-svg"></div>
        </div>
        <div class="stage-actor" id="enc-enemy-actor">
          <div id="enc-enemy-svg"></div>
        </div>
      </div>

      <!-- CHALLENGE POPUP -->
      <div class="challenge-panel" id="enc-challenge-panel">
        <div class="challenge-header-card">
          <span style="font-size:12px; font-weight:800; color:#2e7d32;" id="enc-q-badge">معمای ۱ از ۲</span>
          <span style="font-size:11.5px; color:#546e7a;" id="enc-special-rule-badge">قاعده رویداد</span>
        </div>

        <div class="question-prompt" id="enc-question-text">متن سوال...</div>

        <!-- Choices for 4-choice or 2-choice -->
        <div class="choices-container" id="enc-choices-box"></div>

        <!-- Slow Turtle Step-by-Step UI -->
        <div id="turtle-step-container" style="display:none; flex-direction:column; gap:10px; margin-top:8px;">
          <div style="background:#fff3e0; padding:10px; border-radius:10px; font-weight:800; font-size:14px; text-align:center;" id="turtle-current-opt-text">
            گزینه...
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
            <button class="choice-btn" style="justify-content:center; background:#e8f5e9; border-color:#4caf50;" onclick="submitTurtleAnswer(true)">✅ درست است</button>
            <button class="choice-btn" style="justify-content:center; background:#ffebee; border-color:#e53935;" onclick="submitTurtleAnswer(false)">❌ غلط است</button>
          </div>
        </div>

        <!-- Lantern Powerup Button -->
        <button class="btn-use-lantern" id="btn-use-lantern" onclick="useLanternPowerup()">
          🏮 استفاده از چراغ راهنمایی (حذف یک گزینه غلط)
        </button>
      </div>

      <!-- FOX DOUBT MODAL -->
      <div class="fox-doubt-overlay" id="fox-doubt-overlay">
        <div class="fox-doubt-card">
          <div style="font-size:36px; margin-bottom:4px;">🦊</div>
          <h4 style="color:#e65100; margin-bottom:6px;">روباه مکار به شک افتاده!</h4>
          <p style="font-size:13px; line-height:1.6; color:#37474f; margin-bottom:12px;" id="fox-doubt-text">
            «صبر کن! مطمئنی این جوابه؟ من فکر می‌کنم گزینه دیگه‌ای درسته... نظرت رو عوض می‌کنی؟»
          </p>
          <div style="display:flex; gap:8px;">
            <button class="btn-action" style="padding:6px 12px; font-size:13px; background:#4caf50;" onclick="confirmFoxChoice(true)">نه! کاملاً مطمئنم</button>
            <button class="btn-action" style="padding:6px 12px; font-size:13px; background:#78909c;" onclick="confirmFoxChoice(false)">تغییر می‌دهم</button>
          </div>
        </div>
      </div>
    </div>

    <!-- SCREEN 4: VICTORY SCREEN -->
    <div id="victory-screen" class="screen">
      <div class="diploma-card">
        <div class="diploma-seal">🏆</div>
        <h2>لوح افتخار قهرمان جنگل دانایی</h2>
        <p style="font-size: 12px; color: #795548; font-weight: bold;">به نام خداوند دانایی و خرد</p>
        
        <div class="diploma-text">
          این لوح به قهرمان کوشا و دانا، 
          <strong style="color: #2e7d32; font-size: 16px;" id="cert-player-name">نام دانش‌آموز</strong> 
          اهدا می‌گردد که با موفقیت نقشه جنگل را درنوردید، ۱۰ ایستگاه چالش را پشت سر گذاشت و به کلبه امن رسید.
          <br>
          مبحث: <strong>__GAME_LESSON_PLACEHOLDER__</strong>
          <br>
          امتیاز نهایی کسب‌شده: <span id="cert-score" style="color: #e65100; font-weight: 800; font-size: 18px;">۱۰۰</span> از ۱۰۰ ستاره درخشان ⭐
        </div>

        <div class="diploma-footer">
          <div>آموزگار گرامی: <strong>__GAME_TEACHER_PLACEHOLDER__</strong></div>
          <button class="btn-action" style="padding: 6px 12px; font-size: 12.5px; width: auto;" onclick="window.print()">🖨️ چاپ لوح</button>
        </div>
      </div>
      
      <button class="btn-action" style="margin-top: 12px; background: #2e7d32; width: auto; padding: 8px 24px;" onclick="location.reload()">🔄 ماجراجویی دوباره</button>
    </div>

  </div>

  <script>
    // --- EMBEDDED CONFIG ---
    const GAME_CONFIG = __GAME_CONFIG_PLACEHOLDER__;
    const SVG_LIB = {svg_library_json};

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

    // --- GAME ENGINE STATE ---
    let currentLives = GAME_CONFIG.initialLives || 5;
    let lanternCount = 0;
    let rawScoreAccumulator = 0;
    let maxPossibleRawScore = 0;
    let playerName = 'قهرمان دانا';

    // 10 Map Waypoint Stations
    let mapStations = [];
    let currentStationIndex = 0;

    // Node coordinates along S-curve trail
    const NODE_COORDINATES = [
      {{ x: 15, y: 88, isStart: true }},
      {{ x: 45, y: 83 }},
      {{ x: 78, y: 76 }},
      {{ x: 82, y: 62 }},
      {{ x: 50, y: 55 }},
      {{ x: 20, y: 48 }},
      {{ x: 22, y: 34 }},
      {{ x: 52, y: 28 }},
      {{ x: 80, y: 22 }},
      {{ x: 85, y: 8, isHome: true }}
    ];

    // Current encounter runtime
    let activeEncounter = null;
    let encounterQIndex = 0;
    let encounterStartTime = 0;
    let questionStartTime = 0;
    let encounterTimerInterval = null;
    let encounterMultiplier = 1.0;
    let pendingChoiceIdx = null;

    // Turtle step-by-step state
    let turtleOptIndex = 0;

    // --- START GAME ---
    function startGame() {{
      const input = document.getElementById('playerNameInput');
      playerName = input.value.trim() || input.placeholder || 'قهرمان دانا';
      document.getElementById('cert-player-name').innerText = playerName;

      buildRoadmapStations();
      updateLivesDisplay();
      updateLanternDisplay();
      updateScoreDisplay();

      // Render Hero SVGs
      const heroKey = GAME_CONFIG.hero || 'squirrel';
      document.getElementById('hero-pawn-svg').innerHTML = SVG_LIB[heroKey] || SVG_LIB.squirrel;
      document.getElementById('enc-hero-svg').innerHTML = SVG_LIB[heroKey] || SVG_LIB.squirrel;

      // Switch to Roadmap screen
      document.getElementById('start-screen').classList.remove('active');
      document.getElementById('map-screen').classList.add('active');

      renderMapNodes();
      positionPawnAtNode(0);
      sfxJump();
    }}

    // Build 10 Map Stations from Active Animals
    function buildRoadmapStations() {{
      let activeAnimals = (GAME_CONFIG.animals || []).filter(a => a.selected);
      if (activeAnimals.length === 0) activeAnimals = [{animals_json}[0]];

      let poolAnimals = [...activeAnimals];
      if (GAME_CONFIG.randomize) poolAnimals.sort(() => Math.random() - 0.5);

      let poolQuestions = [...(GAME_CONFIG.questions || [])];
      if (GAME_CONFIG.randomize) poolQuestions.sort(() => Math.random() - 0.5);

      mapStations = [];
      maxPossibleRawScore = 0;

      for (let i = 0; i < 10; i++) {{
        const coords = NODE_COORDINATES[i];
        if (coords.isStart) {{
          mapStations.push({{
            index: i,
            x: coords.x,
            y: coords.y,
            isStart: true,
            completed: true
          }});
        }} else if (coords.isHome) {{
          mapStations.push({{
            index: i,
            x: coords.x,
            y: coords.y,
            isHome: true,
            completed: false
          }});
        }} else {{
          // Pick animal for this station
          const animal = poolAnimals[(i - 1) % poolAnimals.length];
          // Assign questions (specific or from pool)
          let specificQ = poolQuestions.filter(q => q.animalId === animal.id);
          let assignedQ = [];
          let reqCount = animal.questionsCount || 1;

          for (let q of specificQ) {{
            if (assignedQ.length < reqCount) assignedQ.push(q);
          }}
          while (assignedQ.length < reqCount && poolQuestions.length > 0) {{
            assignedQ.push(poolQuestions[assignedQ.length % poolQuestions.length]);
          }}
          if (assignedQ.length === 0) {{
            assignedQ.push({{ id: 99, text: 'سوال نمونه', options: ['الف', 'ب', 'ج', 'د'], correct: 0, hint: '' }});
          }}

          // Calculate max possible raw score for normalization
          let mult = (animal.type === 'decay_multiplier') ? 2.0 : ((animal.type === 'trickster') ? 3.0 : ((animal.type === 'bats_timer') ? 4.0 : 1.0));
          maxPossibleRawScore += (assignedQ.length * 5.0 * mult);

          mapStations.push({{
            index: i,
            x: coords.x,
            y: coords.y,
            animal: animal,
            questions: assignedQ,
            revealed: false,
            completed: false
          }});
        }}
      }}

      if (maxPossibleRawScore <= 0) maxPossibleRawScore = 50;
    }}

    // Render nodes on roadmap
    function renderMapNodes() {{
      const container = document.getElementById('map-nodes-container');
      container.innerHTML = mapStations.map((st, i) => {{
        let content = '';
        let nodeClass = 'map-node';

        if (st.isStart) {{
          content = '🏕️';
          nodeClass += ' completed';
        }} else if (st.isHome) {{
          content = '🏡';
          nodeClass += ' locked';
        }} else if (st.completed) {{
          content = '✓';
          nodeClass += ' completed';
        }} else if (i === currentStationIndex + 1) {{
          content = st.revealed ? (st.animal ? st.animal.icon : '🐾') : '❓';
          nodeClass += ' current';
        }} else {{
          content = '❓';
          nodeClass += ' locked';
        }}

        return `<div class="${{nodeClass}}" id="map-node-${{i}}" style="left:${{st.x}}%; top:${{st.y}}%;" onclick="onMapNodeClick(${{i}})">
          ${{content}}
        </div>`;
      }}).join('');
    }}

    function positionPawnAtNode(index) {{
      const st = mapStations[index];
      const pawn = document.getElementById('hero-map-pawn');
      if (st && pawn) {{
        pawn.style.left = `${{st.x}}%`;
        pawn.style.top = `${{st.y}}%`;
      }}
    }}

    function onMapNodeClick(idx) {{
      if (idx === currentStationIndex + 1) {{
        moveToNextMapStation();
      }}
    }}

    function moveToNextMapStation() {{
      const nextIdx = currentStationIndex + 1;
      if (nextIdx >= mapStations.length) return;

      const st = mapStations[nextIdx];
      sfxJump();

      // Animate pawn to node
      positionPawnAtNode(nextIdx);

      setTimeout(() => {{
        if (st.isHome) {{
          triggerVictory();
          return;
        }}

        // Reveal mystery icon
        st.revealed = true;
        renderMapNodes();
        playSoundTone(580, 'sine', 0.2);

        document.getElementById('map-progress-text').innerText = `ایستگاه ${{toPersianDigits(nextIdx)}} از ۱۰`;
        document.getElementById('map-hint-text').innerText = `به قلمرو ${{st.animal.name}} رسیدی!`;

        setTimeout(() => {{
          openEncounterScreen(st);
        }}, 800);
      }}, 700);
    }}

    // --- ENCOUNTER SCREEN & 13 EVENTS ---
    function openEncounterScreen(station) {{
      activeEncounter = station;
      encounterQIndex = 0;
      encounterStartTime = Date.now();

      document.getElementById('map-screen').classList.remove('active');
      document.getElementById('encounter-screen').classList.add('active');

      const animal = station.animal;
      document.getElementById('enc-animal-icon').innerText = animal.icon;
      document.getElementById('enc-animal-name').innerText = animal.name;
      document.getElementById('enc-special-rule-badge').innerText = animal.role || '';
      document.getElementById('enc-dialog-bubble').innerText = animal.greeting.replace('قهرمان', playerName);

      // Render enemy SVG
      const enemyBox = document.getElementById('enc-enemy-svg');
      enemyBox.innerHTML = SVG_LIB[animal.id] || SVG_LIB.custom_generic || SVG_LIB.lion;

      // Set Arena Biome Atmosphere
      const arenaBox = document.getElementById('encounter-arena-box');
      arenaBox.className = 'encounter-arena';
      if (animal.id === 'wolf') arenaBox.classList.add('biome-wolf');
      else if (animal.id === 'dragon') arenaBox.classList.add('biome-dragon');
      else if (animal.id === 'bat') arenaBox.classList.add('biome-bat');
      else if (animal.id === 'snake') arenaBox.classList.add('biome-snake');
      else arenaBox.classList.add('biome-normal');

      // Setup Event Mechanics & Multipliers
      setupEventMechanic(animal);

      setTimeout(() => {{
        showCurrentEncounterQuestion();
      }}, 900);
    }}

    function setupEventMechanic(animal) {{
      clearInterval(encounterTimerInterval);
      const timerPill = document.getElementById('enc-timer-pill');
      const multPill = document.getElementById('enc-multiplier-pill');

      timerPill.style.display = 'none';
      multPill.style.display = 'flex';
      encounterMultiplier = 1.0;

      if (animal.type === 'decay_multiplier') {{
        // Crocodile or Monkey: starts at 2.0, decays by 0.1 every 3s
        encounterMultiplier = 2.0;
        updateMultiplierText();
        encounterTimerInterval = setInterval(() => {{
          if (encounterMultiplier > 1.0) {{
            encounterMultiplier = Math.max(1.0, Math.round((encounterMultiplier - 0.1) * 10) / 10);
            updateMultiplierText();
          }}
        }}, 3000);

      }} else if (animal.type === 'trickster') {{
        // Fox: x3 multiplier
        encounterMultiplier = 3.0;
        updateMultiplierText();

      }} else if (animal.type === 'bats_timer') {{
        // Bats: x4 multiplier, 15s survival clock costs 1 life
        encounterMultiplier = 4.0;
        updateMultiplierText();
        timerPill.style.display = 'flex';
        let batSec = 15;
        document.getElementById('enc-timer-sec').innerText = toPersianDigits(batSec);

        encounterTimerInterval = setInterval(() => {{
          batSec--;
          document.getElementById('enc-timer-sec').innerText = toPersianDigits(batSec);
          if (batSec <= 0) {{
            batSec = 15;
            currentLives--;
            updateLivesDisplay();
            sfxWrong();
            alert('🦇 خفاش‌های غار تاریک هجوم آوردند! یک جان کم شد! سریع‌تر پاسخ بده!');
            if (currentLives <= 0) handleRescue();
          }}
        }}, 1000);

      }} else if (animal.type === 'dragon') {{
        // Dragon: 30s timer, fires flames dealing 2 lives
        timerPill.style.display = 'flex';
        let dragSec = 30;
        document.getElementById('enc-timer-sec').innerText = toPersianDigits(dragSec);

        encounterTimerInterval = setInterval(() => {{
          dragSec--;
          document.getElementById('enc-timer-sec').innerText = toPersianDigits(dragSec);
          if (dragSec <= 0) {{
            dragSec = 30;
            currentLives = Math.max(0, currentLives - 2);
            updateLivesDisplay();
            sfxWrong();
            alert('🔥 اژدها آتش پرتاب کرد و ۲ جان کم کرد! زمان دوباره ۳۰ ثانیه تنظیم شد!');
            if (currentLives <= 0) handleRescue();
          }}
        }}, 1000);

      }} else {{
        encounterMultiplier = 1.0;
        updateMultiplierText();
      }}
    }}

    function updateMultiplierText() {{
      document.getElementById('enc-multiplier-text').innerText = `ضریب: ×${{toPersianDigits(encounterMultiplier)}}`;
    }}

    function showCurrentEncounterQuestion() {{
      const q = activeEncounter.questions[encounterQIndex];
      if (!q) {{
        onEncounterCleared();
        return;
      }}

      questionStartTime = Date.now();
      document.getElementById('enc-q-badge').innerText = `معمای ${{toPersianDigits(encounterQIndex + 1)}} از ${{toPersianDigits(activeEncounter.questions.length)}}`;
      document.getElementById('enc-question-text').innerText = q.text;

      const choicesBox = document.getElementById('enc-choices-box');
      const turtleBox = document.getElementById('turtle-step-container');

      // Check if Turtle Slow Sequential Evaluation
      if (activeEncounter.animal.id === 'turtle') {{
        choicesBox.style.display = 'none';
        turtleBox.style.display = 'flex';
        turtleOptIndex = 0;
        showTurtleOption();
      }} else {{
        choicesBox.style.display = 'flex';
        turtleBox.style.display = 'none';

        const labels = ['الف', 'ب', 'ج', 'د'];
        choicesBox.innerHTML = q.options.map((opt, idx) => `
          <button class="choice-btn" id="enc-opt-${{idx}}" onclick="onChoiceSelected(${{idx}})">
            <span style="background:#cfd8dc; color:#37474f; border-radius:8px; padding:2px 8px; font-size:12px; font-weight:bold;">${{labels[idx] || (idx+1)}}</span>
            <span style="flex:1;">${{opt}}</span>
          </button>
        `).join('');
      }}

      // Lantern button
      const lanternBtn = document.getElementById('btn-use-lantern');
      if (lanternCount > 0 && q.options && q.options.length > 2) {{
        lanternBtn.classList.add('show');
      }} else {{
        lanternBtn.classList.remove('show');
      }}

      document.getElementById('enc-challenge-panel').classList.add('open');
    }}

    // Turtle Sequential Step-by-Step
    function showTurtleOption() {{
      const q = activeEncounter.questions[encounterQIndex];
      const opt = q.options[turtleOptIndex];
      const label = ['الف', 'ب', 'ج', 'د'][turtleOptIndex] || (turtleOptIndex + 1);
      document.getElementById('turtle-current-opt-text').innerText = `گزینه ${{label}}: «${{opt}}»`;
    }}

    function submitTurtleAnswer(userSaidTrue) {{
      const q = activeEncounter.questions[encounterQIndex];
      const isActuallyTrue = (turtleOptIndex === q.correct);

      if (userSaidTrue === isActuallyTrue) {{
        // User was right!
        if (isActuallyTrue) {{
          // Reached the true option!
          sfxCorrect();
          recordQuestionScore();
          document.getElementById('enc-dialog-bubble').innerText = `«آفرین ${{playerName}}! گزینه درست رو پیدا کردی! 🐢»`;
          setTimeout(() => {{
            document.getElementById('enc-challenge-panel').classList.remove('open');
            encounterQIndex++;
            showCurrentEncounterQuestion();
          }}, 700);
        }} else {{
          // Correctly said false, advance to next option
          playSoundTone(440, 'sine', 0.15);
          turtleOptIndex++;
          if (turtleOptIndex < q.options.length) {{
            showTurtleOption();
          }}
        }}
      }} else {{
        // User was wrong
        sfxWrong();
        currentLives--;
        updateLivesDisplay();
        alert('❌ اشتباه بود! یک جان کم شد. دوباره دقت کن!');
        if (currentLives <= 0) handleRescue();
      }}
    }}

    // Choice Selected (Normal, Fox, etc.)
    function onChoiceSelected(chosenIdx) {{
      pendingChoiceIdx = chosenIdx;

      // Fox Event: 50% chance of psychological trick
      if (activeEncounter.animal.id === 'fox' && Math.random() < 0.5) {{
        document.getElementById('fox-doubt-overlay').classList.add('show');
        return;
      }}

      finalizeAnswer(chosenIdx);
    }}

    function confirmFoxChoice(confirmed) {{
      document.getElementById('fox-doubt-overlay').classList.remove('show');
      if (confirmed) {{
        finalizeAnswer(pendingChoiceIdx);
      }} else {{
        // Student wants to change mind
        showToast('می‌توانی گزینه دیگری را انتخاب کنی!');
      }}
    }}

    function finalizeAnswer(chosenIdx) {{
      const q = activeEncounter.questions[encounterQIndex];
      const btn = document.getElementById(`enc-opt-${{chosenIdx}}`);

      if (chosenIdx === q.correct) {{
        // CORRECT
        sfxCorrect();
        if (btn) btn.classList.add('correct-glow');
        recordQuestionScore();

        // Wolf mechanic: defeat wolf
        if (activeEncounter.animal.id === 'wolf') {{
          document.getElementById('enc-dialog-bubble').innerText = `«آفرین ${{playerName}}! یک گرگ عقب‌نشینی کرد! 🐺»`;
        }} else if (activeEncounter.animal.id === 'snake') {{
          document.getElementById('enc-dialog-bubble').innerText = `«با چوب‌دستی یک مار رو دفع کردی! 🐍»`;
        }} else {{
          document.getElementById('enc-dialog-bubble').innerText = `«آفرین ${{playerName}}! کاملاً درست بود! 👏»`;
        }}

        setTimeout(() => {{
          document.getElementById('enc-challenge-panel').classList.remove('open');
          encounterQIndex++;
          if (encounterQIndex < activeEncounter.questions.length) {{
            setTimeout(showCurrentEncounterQuestion, 500);
          }} else {{
            onEncounterCleared();
          }}
        }}, 700);

      }} else {{
        // WRONG
        sfxWrong();
        if (btn) btn.classList.add('wrong-glow');
        currentLives--;
        updateLivesDisplay();

        if (activeEncounter.animal.id === 'fox') {{
          alert('🦊 روباه خندید: «ها ها ها! دیدی بهت گفتم؟ گول خوردی!»');
        }} else {{
          if (q.hint) alert(`💡 راهنمایی: ${{q.hint}}`);
        }}

        if (currentLives <= 0) handleRescue();
      }}
    }}

    function recordQuestionScore() {{
      const elapsedSec = Math.max(0, (Date.now() - questionStartTime) / 1000 - 2.0);
      const basePoints = Math.max(1.5, 5.0 - (elapsedSec * 0.1));
      const earned = basePoints * encounterMultiplier;
      rawScoreAccumulator += earned;
      updateScoreDisplay();
    }}

    function updateScoreDisplay() {{
      // Map rawScoreAccumulator to an integer <= 100
      let normalized = Math.min(100, Math.round((rawScoreAccumulator / maxPossibleRawScore) * 100));
      document.getElementById('score-counter').innerText = toPersianDigits(normalized);
    }}

    function useLanternPowerup() {{
      if (lanternCount <= 0) return;
      const q = activeEncounter.questions[encounterQIndex];
      // Find a wrong option and disable it
      for (let i = 0; i < q.options.length; i++) {{
        if (i !== q.correct) {{
          const btn = document.getElementById(`enc-opt-${{i}}`);
          if (btn && !btn.disabled) {{
            btn.disabled = true;
            btn.style.opacity = '0.3';
            btn.style.pointerEvents = 'none';
            lanternCount--;
            updateLanternDisplay();
            document.getElementById('btn-use-lantern').classList.remove('show');
            sfxJump();
            showToast('🏮 چراغ راهنمایی یک گزینه نادرست را حذف کرد!');
            break;
          }}
        }}
      }}
    }}

    function onEncounterCleared() {{
      clearInterval(encounterTimerInterval);
      sfxWin();

      const animal = activeEncounter.animal;
      let rewardText = '';

      // Rewards:
      if (animal.type === 'extra_life') {{
        currentLives = Math.min(5, currentLives + 1);
        updateLivesDisplay();
        rewardText = ' (❤️ ۱ جان اضافه شدی!)';
      }} else if (animal.type === 'lantern') {{
        lanternCount++;
        updateLanternDisplay();
        rewardText = ' (🏮 ۱ چراغ راهنمایی دریافت کردی!)';
      }}

      alert(`🌟 ${{animal.success}}${{rewardText}}`);

      // Mark station completed
      activeEncounter.completed = true;
      currentStationIndex++;

      // Transition back to Map
      document.getElementById('encounter-screen').classList.remove('active');
      document.getElementById('map-screen').classList.add('active');

      renderMapNodes();
      positionPawnAtNode(currentStationIndex);

      if (currentStationIndex < mapStations.length - 1) {{
        document.getElementById('map-hint-text').innerText = 'ایستگاه بعدی در انتظار توست!';
      }} else {{
        document.getElementById('map-hint-text').innerText = 'به کلبه امن رسیدی!';
      }}
    }}

    function handleRescue() {{
      sfxCorrect();
      alert('🦉 جغد دانا از راه رسید: «هیچ قهرمانی در جنگل تسلیم نمی‌شود! ۳ جان تازه به تو هدیه می‌دهم!»');
      currentLives = 3;
      updateLivesDisplay();
    }}

    function updateLivesDisplay() {{
      const box = document.getElementById('lives-display');
      let html = '';
      for (let i = 0; i < 5; i++) {{
        html += `<span class="heart ${{i < currentLives ? '' : 'lost'}}">❤️</span>`;
      }}
      box.innerHTML = html;
    }}

    function updateLanternDisplay() {{
      document.getElementById('lantern-count').innerText = toPersianDigits(lanternCount);
    }}

    function triggerVictory() {{
      document.getElementById('map-screen').classList.remove('active');
      document.getElementById('encounter-screen').classList.remove('active');
      document.getElementById('victory-screen').classList.add('active');

      let finalNormalized = Math.min(100, Math.round((rawScoreAccumulator / maxPossibleRawScore) * 100));
      if (finalNormalized < 60) finalNormalized = 60 + Math.floor(Math.random() * 20); // Friendly floor
      document.getElementById('cert-score').innerText = toPersianDigits(finalNormalized);

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

      for (let i = 0; i < 80; i++) {{
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

# Generate standalone pre-built game
sample_game_html = GAME_ENGINE_HTML.replace("__GAME_TITLE_PLACEHOLDER__", DEFAULT_PROJECT_DATA["title"])
sample_game_html = sample_game_html.replace("__GAME_LESSON_PLACEHOLDER__", DEFAULT_PROJECT_DATA["lesson"])
sample_game_html = sample_game_html.replace("__GAME_TEACHER_PLACEHOLDER__", DEFAULT_PROJECT_DATA["teacher"])
sample_game_html = sample_game_html.replace("__GAME_CONFIG_PLACEHOLDER__", default_project_json)

sample_game_file = os.path.join(base_dir, "بازی_ماجراجویی_جنگل.html")
with open(sample_game_file, "w", encoding="utf-8") as f:
    f.write(sample_game_html)
print(f"Generated {sample_game_file} (size: {os.path.getsize(sample_game_file)} bytes)")

# Base64 encode the template for embedding inside index.html
template_for_builder = GAME_ENGINE_HTML.replace("__GAME_CONFIG_PLACEHOLDER__", "__CLIENT_CONFIG_JSON__")
template_b64 = base64.b64encode(template_for_builder.encode("utf-8")).decode("ascii")

# Now update index_template.html to incorporate all 13 events, Roadmap preview, and base64 template
with open(os.path.join(base_dir, "index_template.html"), "r", encoding="utf-8") as f:
    builder_template = f.read()

final_builder_html = builder_template.replace("__EMBEDDED_FONT_CSS__", EMBEDDED_FONT_CSS)
final_builder_html = final_builder_html.replace("__DEFAULT_PROJECT_DATA_JSON__", default_project_json)
final_builder_html = final_builder_html.replace("__BASE_GAME_TEMPLATE_B64__", template_b64)

# In JS of index.html, replace the config placeholder
final_builder_html = final_builder_html.replace(
    "return baseCode.replace('__GAME_CONFIG_PLACEHOLDER__', serialized);",
    """return baseCode.replace('__CLIENT_CONFIG_JSON__', serialized)
              .replace('__GAME_TITLE_PLACEHOLDER__', data.title || 'ماجراجویی در جنگل')
              .replace('__GAME_LESSON_PLACEHOLDER__', data.lesson || 'ریاضی و علوم شاد')
              .replace('__GAME_TEACHER_PLACEHOLDER__', data.teacher || 'آموزگار مهربان');"""
)

index_file = os.path.join(base_dir, "index.html")
with open(index_file, "w", encoding="utf-8") as f:
    f.write(final_builder_html)
print(f"Generated {index_file} (size: {os.path.getsize(index_file)} bytes)")
