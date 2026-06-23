from connection import get_connection, get_engine
import pandas as pd
import psycopg2

def add_rating(student_id, video_id, rating, review):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO ratings (student_id, video_id, rating, review) VALUES (%s, %s, %s, %s)",
            (student_id, video_id, rating, review)
        )
        conn.commit()
        return True, "Rating added successfully!"
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        return False, "You have already rated this video!"
    finally:
        conn.close()

def get_video_ratings(video_id):
    conn= get_connection()
    df=pd.read_sql("SELECT r.rating, s.name AS Student_name, v.title AS Video_title FROM ratings r JOIN students s ON r.student_id=s.id JOIN videos v ON r.video_id=v.id WHERE r.video_id = %s", get_engine() , params=(video_id,))
    return df

def get_average_rating(video_id):
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("SELECT ROUND(AVG(rating), 2) FROM ratings WHERE video_id = %s", (video_id,))
    result= cur.fetchone()
    cur.close()
    conn.close()
    return result[0]

def get_all_rating():
    df = pd.read_sql("""
    SELECT s.name AS student_name, v.title AS video_title, 
           r.rating, r.review, r.rated_at
    FROM ratings r
    JOIN students s ON r.student_id = s.id
    JOIN videos v ON r.video_id = v.id
    ORDER BY r.rated_at DESC
    """, get_engine())
    return df

if __name__=="__main__":
    add_rating(1, 2, 5, "Great lecture!")
    print(get_video_ratings(2))
    print("Avg rating:", get_average_rating(2))
