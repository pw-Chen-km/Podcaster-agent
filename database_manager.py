import sqlite3

def create_database():
    conn = sqlite3.connect('channel_content.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS episodes (
                    id INTEGER PRIMARY KEY,
                    summary TEXT,
                    transcript TEXT)''')
    conn.commit()
    conn.close()

def insert_episode(summary, transcript):
    conn = sqlite3.connect('channel_content.db')
    c = conn.cursor()
    c.execute('INSERT INTO episodes (summary, transcript) VALUES (?, ?)', (summary, transcript))
    conn.commit()
    conn.close()

def retrieve_episodes():
    conn = sqlite3.connect('channel_content.db')
    c = conn.cursor()
    c.execute('SELECT summary, transcript FROM episodes')
    results = c.fetchall()
    conn.close()
    return results 

create_database()

# 隨機生成內容並插入資料庫
sample_summaries = [
    "這集討論了時間管理的重要性及其在日常生活中的應用。",
    "這一集帶我們探討如何面對失敗與成長的機會。",
    "討論如何建立健康的飲食習慣，並介紹一些實用的技巧。",
    "這集探索了自我激勵的方法以及如何達成長期目標。",
    "本集介紹了簡單有效的正念冥想方法。"
]

sample_transcripts = [
    {
        "title": "時間管理技巧方法論",
        "steps": [
            "步驟一：制定待辦事項清單 - 每天或每週列出要完成的任務，並將任務分為高優先級和低優先級，確保重要事項優先完成。",
            "步驟二：使用時間區塊法 - 將一天分成不同的時間區塊，並為每個區塊指定具體的任務，避免多任務處理，提升專注度和效率。"
        ]
    },
    {
        "title": "從失敗中學習方法論",
        "steps": [
            "步驟一：回顧失敗經驗 - 將失敗的過程和原因詳細記錄，深入分析失敗的根本原因。",
            "步驟二：建立學習框架 - 將失敗轉化為具體的學習機會，設定改進的目標和行動計劃，並逐步實施。",
            "步驟三：定期反思和調整方向 - 定期回顧進步情況和調整策略，以持續優化方向，從經驗中學習成長。"
        ]
    },
    {
        "title": "健康飲食習慣方法論",
        "steps": [
            "步驟一：了解健康飲食的基本原則 - 掌握營養均衡的基礎知識，例如多攝取蔬果、減少糖分和避免加工食品。",
            "步驟二：制定飲食計劃 - 每週安排健康的食物選擇，避免臨時決定和不健康外食，確保飲食多樣性。",
            "步驟三：建立防範不健康飲食的策略 - 制定具體方法，如限制垃圾食品的攝入，或選擇健康替代品，達成每日飲食目標。"
        ]
    },
    {
        "title": "長期目標自我激勵方法論",
        "steps": [
            "步驟一：設定清晰的長期目標 - 將長期目標分解為可達成的短期目標，每個階段都具體化並清晰定義。",
            "步驟二：定期檢查目標進度 - 每週或每月檢視進展，確保方向正確，並根據進度適時調整策略。",
            "步驟三：設立激勵機制 - 每達成一個小目標，給自己一個小獎勵，保持動力，增加挑戰的樂趣。"
        ]
    },
    {
        "title": "正念冥想方法論",
        "steps": [
            "步驟一：選擇固定時間進行冥想 - 每天選擇一個固定時間段進行冥想，養成習慣（如早晨或睡前）。",
            "步驟二：專注於呼吸或一個對象 - 在冥想中專注於呼吸，或集中於特定的對象（如聲音或詞語），提升注意力。",
            "步驟三：逐步提升冥想時間 - 從5-10分鐘開始，逐漸增加至15-20分鐘，幫助培養專注力和內心平靜。"
        ]
    }
]


# 插入範例數據
for i in range(5):
    summary = sample_summaries[i]
    transcript = sample_transcripts[i]
    insert_episode(summary, transcript)