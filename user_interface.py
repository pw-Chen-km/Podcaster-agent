from retrieval import retrieve_relevant_content
from llm_chain import generate_stylized_response

def main():
    print("歡迎來到頻道風格聊天機器人！")
    while True:
        question = input("請輸入您的問題（或輸入 'exit' 退出）：")
        if question.lower() == 'exit':
            break
        
        # 獲取相關集數的內容
        episode_data = retrieve_relevant_content(question)
        
        # 生成回答
        response = generate_stylized_response(question, episode_data)
        print("\n" + response + "\n")

if __name__ == "__main__":
    main() 