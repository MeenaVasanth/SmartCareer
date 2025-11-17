# app.py - SIMPLIFIED CORRECT VERSION
import streamlit as st
import pandas as pd
import plotly.express as px
import json
from course_data import get_course_catalog
from recommender import CareerRecommender, create_learning_path, generate_json_output

# Configure the page
st.set_page_config(
    page_title="SmartCareer - AI Learning Path Recommender",
    page_icon="🎯",
    layout="wide"
)

def main():
    # Header
    st.title("🎯 SmartCareer AI")
    st.markdown("### Personalized Learning Path Recommender")
    st.markdown("Get course recommendations based on your education, skills, and career goals")
    
    # Initialize data
    courses_df = get_course_catalog()
    recommender = CareerRecommender(courses_df)
    
    # ONLY ONE INPUT METHOD - User Profile Form
    show_user_input(recommender)

def show_user_input(recommender):
    """Show ONLY the required user profile input form"""
    st.header("📝 Enter Your Profile")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # REQUIRED: Education level
        education = st.selectbox("Education Level", 
            ["High School", "Associate Degree", "Bachelors Degree", "Masters Degree", "PhD", "Other"])
        
        # REQUIRED: Major/degree  
        major = st.text_input("Major/Field of Study", "Computer Science")
        
        # REQUIRED: Technical skills
        st.write("**Technical Skills**")
        technical_skills = st.text_area(
            "List your technical skills (comma-separated)",
            "python, excel, sql",
            help="Example: python, java, sql, excel, javascript"
        )
    
    with col2:
        # REQUIRED: Soft skills
        st.write("**Soft Skills**")
        soft_skills = st.text_area(
            "List your soft skills (comma-separated)", 
            "communication, problem solving",
            help="Example: leadership, communication, teamwork, creativity"
        )
        
        # OPTIONAL: Target domain
        target_domain = st.selectbox("Target Career Domain (Optional)", 
            ["", "Data Science", "Web Development", "Cloud Computing", "Digital Marketing", 
             "Business Analytics", "DevOps", "UI/UX Design", "Cybersecurity", "Other"])
        
        # OPTIONAL: Preferred study duration
        study_duration = st.selectbox("Preferred Study Duration (Optional)", 
            ["", "1-3 months", "3-6 months", "6-12 months", "12+ months"])
    
    # Process skills
    technical_skills_list = [skill.strip().lower() for skill in technical_skills.split(',') if skill.strip()]
    soft_skills_list = [skill.strip().lower() for skill in soft_skills.split(',') if skill.strip()]
    
    if st.button("🚀 Get Recommendations", type="primary", use_container_width=True):
        if not technical_skills_list:
            st.error("Please enter at least one technical skill")
            return
            
        # Create user profile
        user_profile = {
            'education': education,
            'technical_skills': technical_skills_list,
            'soft_skills': soft_skills_list,
            'target_domain': target_domain if target_domain else None,
            'study_duration': study_duration if study_duration else None
        }
        
        with st.spinner("🤖 Analyzing your profile and generating recommendations..."):
            recommendations = recommender.generate_recommendations(user_profile, top_n=10)
            learning_path = create_learning_path(recommendations)
            
            display_recommendations(recommendations, learning_path, user_profile)

def display_recommendations(recommendations, learning_path, user_profile):
    """Display the required outputs"""
    st.header("🎯 Your Personalized Learning Path")
    
    # 1. Ranked list of recommendations
    st.subheader("📋 Recommended Courses & Certifications")
    
    for i, rec in enumerate(recommendations, 1):
        with st.expander(f"{i}. {rec['title']} - {rec['match_score']}% Match"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Provider:** {rec['provider']}")
                st.write(f"**Duration:** {rec['duration']}")
                st.write(f"**Level:** {rec['level'].title()}")
                st.write(f"**Cost:** {rec['cost']}")
            with col2:
                st.write(f"**Career Path:** {rec['career_path']}")
                st.write(f"**Skills Covered:** {', '.join(rec['skills_covered'][:5])}")
            
            # 2. Short rationale for each recommendation (REQUIRED)
            st.write(f"**🤔 Why this course?** {rec['justification']}")
    
    # 3. Suggested learning timeline (REQUIRED)
    st.subheader("🗓️ Suggested Learning Timeline")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**🟢 Short-Term (1-3 months)**")
        for course in learning_path['short_term_plan']:
            st.write(f"• {course['title'][:30]}...")
    
    with col2:
        st.markdown("**🟡 Medium-Term (3-6 months)**")
        for course in learning_path['medium_term_plan']:
            st.write(f"• {course['title'][:30]}...")
    
    with col3:
        st.markdown("**🔴 Long-Term (6-12 months)**")
        for course in learning_path['long_term_plan']:
            st.write(f"• {course['title'][:30]}...")
    
    # 4. JSON output (REQUIRED)
    st.subheader("📄 JSON Output")
    json_output = generate_json_output(recommendations, learning_path)
    st.code(json.dumps(json_output, indent=2), language='json')

if __name__ == "__main__":
    main()