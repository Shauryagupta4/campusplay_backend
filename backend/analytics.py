from connection import get_connection, get_engine
import pandas as pd

def get_most_watched_videos():
    conn=get_connection()
    df=pd.read_sql("SELECT v.title, COUNT(wh.id) AS watch_count FROM videos v JOIN watch_history wh ON v.id=wh.video_id GROUP BY v.title ORDER BY watch_count DESC", get_engine())
    return df 

def get_top_rated_videos():
    conn=get_connection()
    df=pd.read_sql("SELECT v.title, ROUND(AVG(r.rating),2) AS avg_rating FROM videos v JOIN ratings r ON v.id=r.video_id GROUP BY v.title ORDER BY avg_rating DESC", get_engine())
    return df

def get_most_active_students():
    conn=get_connection()
    df=pd.read_sql("SELECT s.name, COUNT(wh.id) AS watch_count FROM students s JOIN watch_history wh ON s.id=wh.student_id GROUP BY s.name ORDER BY watch_count DESC",get_engine())
    return df 

def get_category_stats():
    conn=get_connection()
    df=pd.read_sql("SELECT c.name, COUNT(wh.id) AS total_watches FROM categories c JOIN videos v ON c.id=v.category_id JOIN watch_history wh ON v.id=wh.video_id GROUP BY c.name", get_engine())
    return df

if __name__=="__main__":
    print(get_most_watched_videos())
    print(get_top_rated_videos())
    print(get_most_active_students())
    print(get_category_stats())

