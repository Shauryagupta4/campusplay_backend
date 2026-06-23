import streamlit as st
import pandas as pd
import sys
sys.path.append("backend") 
import plotly.express as px
from analytics import get_most_watched_videos, get_category_stats, get_top_rated_videos,get_most_active_students
from videos import get_all_videos,get_all_categories, add_video
from students import get_students_df, get_all_plans, add_student
from ratings import get_all_rating, add_rating


st.title("CampusPlay")
st.sidebar.title("MENU")
st.sidebar.markdown("---")
page=st.sidebar.selectbox("CHOOSE: ", ["Analytics Dashboard", "Video Library", "Students", "Ratings"])


if page=="Analytics Dashboard":
    st.header("Analytic Dashboard")
    col1,col2=st.columns(2)
    with col1:
        most_watched_df= get_most_watched_videos()
        fig = px.bar(most_watched_df, x="title", y="watch_count", title="Most Watched Videos")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        category_stat_df = get_category_stats()
        fig = px.pie(category_stat_df, names="name", values="total_watches", title="Watches by Category")
        st.plotly_chart(fig, use_container_width=True)
    
    col3, col4= st.columns(2)
    with col3:
        st.subheader("Top Rated Videos")
        st.dataframe(get_top_rated_videos(), use_container_width=True)

    with col4:
        st.subheader("Most Active Students")
        st.dataframe(get_most_active_students(), use_container_width=True)


elif page=="Video Library":
    st.header("Video Library")
    video_df=get_all_videos()
    st.dataframe(video_df)
    st.subheader("Fill below to add new video: ")

    title=st.text_input("Video Title")
    
    description=st.text_input("Video Description")
    
    duration=st.number_input("Duration(mins)", min_value=1)
    
    category_df=get_all_categories()
    options=category_df["name"].tolist()
    category=st.selectbox("Select", options)
    categ=category_df[category_df["name"]==category]
    category_id=int(categ["id"].iloc[0])

    uploaded_by=st.text_input("Uploaded by")

    if st.button("ADD VIDEO"):
        if title and uploaded_by:
            success, message = add_video(title, description, duration, category_id, uploaded_by)
            if success:
                st.success(message)
            else:
                st.error(message)
        else:
            st.error("Title and Uploaded By are required!")


elif page=="Students":
    st.header("Students")
    student_df=get_students_df()
    st.dataframe(student_df)
    st.subheader("Fill below to add a student: ")

    name=st.text_input("Name")
    
    email=st.text_input("E-Mail")
    
    age=st.number_input("Age", min_value=15)
    
    plan_df=get_all_plans()
    options=plan_df["name"].tolist()
    choice=st.selectbox("Plans", options)
    plan=plan_df[plan_df["name"]==choice]
    plan_id=int(plan["id"].iloc[0])

    if st.button("SUBMIT"):
        if name and email and age:
            success, message = add_student(name, email, age, plan_id)
            if success:
                st.success(message)
            else:
                st.error(message)
        else:
            st.error("Name, Email and Age are required!")


elif page=="Ratings":
    st.header("Rating")
    rating_df=get_all_rating()
    st.dataframe(rating_df)
    st.subheader("Fill below to add new rating: ")

    student_df=get_students_df()
    student_option=student_df["name"].tolist()
    student=st.selectbox("Students", student_option)

    video_df=get_all_videos()
    video_option=video_df["title"].tolist()
    video=st.selectbox("Video", video_option)

    rating=st.slider("Rating", min_value=1, max_value=5, value=2)
    
    review=st.text_input("Review(optional)")

    if st.button("SUBMIT"):
        student_id = int(student_df[student_df["name"] == student]["id"].iloc[0])
        video_id = int(video_df[video_df["title"] == video]["id"].iloc[0])
        success, message = add_rating(student_id, video_id, rating, review)
        if success:
            st.success(message)
        else:
            st.error(message)