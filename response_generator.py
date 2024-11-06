from transformers import pipeline

def generate_response(question, transcripts):
    # 使用一個預訓練的模型來生成回答
    # 這裡可以加入提示工程或微調模型的邏輯
    generator = pipeline('text-generation', model='gpt-3.5-turbo')
    context = " ".join([t[0] for t in transcripts])  # 假設transcripts是列表
    prompt = f"根據以下內容回答問題：{context}\n問題：{question}\n回答："
    response = generator(prompt, max_length=150, num_return_sequences=1)
    return response[0]['generated_text'] 