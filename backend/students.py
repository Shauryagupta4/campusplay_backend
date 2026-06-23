from connection import get_connection, get_engine
import pandas as pd
import psycopg2

def get_all_students():
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("SELECT * FROM students")
    rows=cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_students_df():
    conn=get_connection()
    df=pd.read_sql("SELECT * FROM students", get_engine())
    return df

def add_student(name, email, age, plan_id):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO students (name, email, age, plan_id) VALUES (%s, %s, %s, %s)",
            (name, email, age, plan_id)
        )
        conn.commit()
        return True, "Student added successfully!"
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        return False, "Email already exists!"
    finally:
        cur.close()
        conn.close()

def update_student_plan(student_id, new_plan_id):
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("UPDATE students SET plan_id=%s WHERE id= %s",(new_plan_id,student_id))
    conn.commit()
    cur.close()
    conn.close()
    print("Plan id updated successfully")

def delete_student(student_id):
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("DELETE FROM students WHERE id = %s",(student_id,))
    conn.commit()
    cur.close()
    conn.close()
    print("id deleted successfully")

def get_all_plans():
    df = pd.read_sql("SELECT * FROM plans", get_engine())
    return df

if __name__=="__main__":
    update_student_plan(10, 2)
    delete_student(10)