from connection import get_connection, get_engine
import pandas as pd

def get_all_videos():
    df=pd.read_sql("SELECT v.id, v.title , c.name AS Category_name FROM videos v JOIN categories c ON v.category_id=c.id", get_engine())
    return df

def add_video(title, description, duration_mins, category_id, uploaded_by):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO videos (title, description, duration_mins, category_id, uploaded_by) VALUES (%s, %s, %s, %s, %s)",
            (title, description, duration_mins, category_id, uploaded_by)
        )
        conn.commit()
        return True, "Video added successfully!"
    except Exception as e:
        conn.rollback()
        return False, str(e)
    finally:
        conn.close()

def get_videos_by_category(category_id):
    df=pd.read_sql("SELECT * FROM videos WHERE category_id = %s", get_engine() , params=(category_id,))
    return df

def get_all_categories():
    df = pd.read_sql("SELECT * FROM categories", get_engine())
    return df
    
if __name__=="__main__":
    print(get_all_videos())
    add_video("ML Lecture 1", "Intro to ML", 60, 1, "Prof. AI")
    print(get_videos_by_category(1))