import sys
import yfinance as yf
import pandas as pd

def analyze_stock(ticker):
    print(f"🔍 正在分析標的: {ticker}")
    print("-" * 40)
    
    # 抓取過去半年的歷史資料
    stock = yf.Ticker(ticker)
    df = stock.history(period="6mo")
    
    if df.empty:
        print(f"❌ 找不到 {ticker} 的歷史資料，請確認代號是否正確 (上市請加 .TW，上櫃請加 .TWO)")
        return
        
    # 計算均線 (趨勢判斷 - Lesson 3 & 散戶防護網 - Lesson 2)
    df['SMA20'] = df['Close'].rolling(window=20).mean() # 月線
    df['SMA60'] = df['Close'].rolling(window=60).mean() # 季線
    
    # 計算成交量均線 (量價配合驗證 - Lesson 4)
    df['VOL20'] = df['Volume'].rolling(window=20).mean()
    
    # 取得最新一天的資料
    latest = df.iloc[-1]
    prev = df.iloc[-2]
    
    current_price = latest['Close']
    monthly_line = latest['SMA20']
    
    print(f"📊 最新收盤價: {current_price:.2f}")
    if pd.isna(monthly_line):
        print("⚠️ 資料不足以計算月線")
        return
        
    print(f"📈 月線 (SMA20): {monthly_line:.2f}")
    
    print("\n🚨 [Lesson 3] 趨勢與紀律檢查:")
    if current_price > monthly_line:
        print("  ✅ 股價站上月線，屬於偏多格局。")
    else:
        print("  ❌ 股價跌破月線，屬於空頭弱勢，不建議盲目抄底！")
        
    print("\n🚨 [Lesson 4] K線底部反轉掃描:")
    # 判斷是否出量 (大於月均量)
    is_high_volume = latest['Volume'] > latest['VOL20']
    volume_status = "有爆量配合" if is_high_volume else "量能不足"
    
    # 長下影線 (打樁K線)
    body = abs(latest['Close'] - latest['Open'])
    lower_shadow = latest['Open'] - latest['Low'] if latest['Close'] > latest['Open'] else latest['Close'] - latest['Low']
    is_hammer = lower_shadow > (body * 2) and lower_shadow > 0
    
    # 陽包陰 (吞噬)
    is_engulfing = (prev['Close'] < prev['Open']) and (latest['Close'] > latest['Open']) and (latest['Open'] <= prev['Close']) and (latest['Close'] >= prev['Open'])
    
    if is_hammer:
        print(f"  🔥 發現【長下影線/槌子線】，且{volume_status}。")
        print(f"  🛡️ 防守價 (停損點): 建議設在該K線低點 {latest['Low']:.2f}")
    elif is_engulfing:
        print(f"  🔥 發現【陽包陰 (吞噬型態)】，且{volume_status}。多頭強勢反撲！")
        print(f"  🛡️ 防守價 (停損點): 建議設在紅K低點或開盤價 {latest['Open']:.2f}")
    else:
        print("  ➖ 目前未出現明顯的底部反轉K線 (如長下影線、陽包陰)。")

    print("\n🚨 [Lesson 2] 散戶防護網 (過熱警告):")
    if is_high_volume and latest['Close'] < latest['Open'] and latest['Close'] < prev['Close']:
        print("  ⚠️ 警告: 爆量且收長黑K，可能有主力出貨、散戶接盤風險，請避免追高！")
    else:
        print("  ✅ 目前無明顯的爆量收黑過熱危險。")
        
    print("\n💡 總結操作建議:")
    if current_price > monthly_line and (is_hammer or is_engulfing) and is_high_volume:
        print("  👉 趨勢偏多且出現帶量反轉訊號，符合【大膽試單】條件！請嚴格設定防守價。")
    elif current_price < monthly_line:
        print("  👉 趨勢偏弱，空手觀望，或等待站回月線再說。")
    else:
        print("  👉 趨勢雖為多頭，但未見明確反轉或攻擊訊號，建議觀察或分批佈局。")
    
    print("-" * 40)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python analyze.py <股票代號>")
        sys.exit(1)
        
    ticker = sys.argv[1]
    analyze_stock(ticker)
