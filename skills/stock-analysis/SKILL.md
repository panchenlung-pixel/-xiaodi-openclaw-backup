---
name: stock-analysis
description: Analyze Taiwan stock market tickers using K-line patterns, volume-price relationship, trend following, and risk management. Use when the user asks to analyze a stock, check trading signals, or evaluate a ticker based on the "股票學堂" (stock learning) rules (late trading volume, retail trap avoidance, moving average trends, reversal K-line patterns).
---

# Stock Analysis

A skill to analyze stocks based on a strict set of trading disciplines and technical signals learned from the "股票學堂" lessons.

## Core Logic (Lessons 1-4)
1. **Lesson 1 (Late Trading/尾盤)**: Identify strong closes and volume surges in the late session.
2. **Lesson 2 (Retail Traps/散戶防護)**: Avoid stocks with overbought black K-lines or heavy retail margin, enforce stop losses (e.g., breaking monthly lines).
3. **Lesson 3 (Trend Following/順勢而為)**: Only buy in an upward trend (MAs pointing up). Calculate Risk/Reward ratio and a strict stop-loss.
4. **Lesson 4 (Reversal Patterns/底部反轉)**: Scan for Hammer (長下影線), Bullish Engulfing (陽包陰), or Morning Star patterns at the bottom, validated by high volume.

## Usage

Run the analysis script on a specific ticker (Taiwan stocks append `.TW` for listed, `.TWO` for OTC).

```bash
python /Users/panchenlung/.openclaw/workspace/skills/stock-analysis/scripts/analyze.py 2330.TW
```

## Setup

Ensure dependencies are installed:
```bash
pip install yfinance pandas pandas-ta
```
