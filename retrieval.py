import sqlite3
import numpy as np
from langchain_openai import OpenAIEmbeddings
import faiss

def setup_database_chain():
    conn = sqlite3.connect('channel_content.db')
    cursor = conn.cursor()
    return conn, cursor

def load_summaries_from_database():
    conn, cursor = setup_database_chain()
    cursor.execute("SELECT id, summary, transcript FROM episodes")
    episodes = cursor.fetchall()
    conn.close()
    return episodes

def build_faiss_index(embeddings):
    dimension = 1536
    index = faiss.IndexFlatL2(dimension)
    
    episodes = load_summaries_from_database()
    ids = []
    vectors = []
    episode_data = {}  # 儲存每集的完整資訊

    for episode in episodes:
        episode_id, summary, transcript = episode
        embedding_vector = embeddings.embed_query(summary)
        ids.append(episode_id)
        vectors.append(embedding_vector)
        episode_data[episode_id] = {
            'summary': summary,
            'transcript': transcript,
            'episode_number': episode_id
        }

    vectors_array = np.array(vectors).astype('float32')
    index.add(vectors_array)
    return index, ids, episode_data

def retrieve_relevant_content(question):
    embeddings = OpenAIEmbeddings()
    index, ids, episode_data = build_faiss_index(embeddings)
    
    question_vector = embeddings.embed_query(question)
    _, indices = index.search(np.array([question_vector]).astype('float32'), k=1)
    
    # 獲取最相關的一集內容
    relevant_id = ids[indices[0][0]]
    relevant_episode = episode_data[relevant_id]
    
    return {
        'episode_number': relevant_episode['episode_number'],
        'summary': relevant_episode['summary'],
        'transcript': relevant_episode['transcript']
    }