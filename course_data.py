# course_data.py - Course Database (25+ courses as required)
import pandas as pd

def get_course_catalog():
    courses = [
        # Programming & Development
        {
            'id': 1, 'title': 'Python for Absolute Beginners', 'provider': 'Coursera',
            'duration': '6 weeks', 'level': 'beginner', 'cost': 'Free',
            'prerequisites': [], 
            'skills_covered': ['python', 'programming basics', 'problem solving'],
            'career_path': 'Software Developer', 'link': '#', 'domain': 'Programming'
        },
        {
            'id': 2, 'title': 'Web Development Fundamentals', 'provider': 'freeCodeCamp',
            'duration': '8 weeks', 'level': 'beginner', 'cost': 'Free',
            'prerequisites': [], 
            'skills_covered': ['html', 'css', 'javascript', 'web development'],
            'career_path': 'Frontend Developer', 'link': '#', 'domain': 'Web Development'
        },
        {
            'id': 3, 'title': 'Java Programming Masterclass', 'provider': 'Udemy',
            'duration': '12 weeks', 'level': 'intermediate', 'cost': '$89',
            'prerequisites': ['programming basics'],
            'skills_covered': ['java', 'oop', 'data structures', 'algorithms'],
            'career_path': 'Java Developer', 'link': '#', 'domain': 'Programming'
        },
        
        # Data Science & Analytics
        {
            'id': 4, 'title': 'Data Science Foundations', 'provider': 'edX',
            'duration': '10 weeks', 'level': 'intermediate', 'cost': '$99',
            'prerequisites': ['python', 'statistics'],
            'skills_covered': ['python', 'data analysis', 'statistics', 'machine learning'],
            'career_path': 'Data Scientist', 'link': '#', 'domain': 'Data Science'
        },
        {
            'id': 5, 'title': 'SQL for Data Analysis', 'provider': 'Coursera',
            'duration': '4 weeks', 'level': 'beginner', 'cost': 'Free',
            'prerequisites': [],
            'skills_covered': ['sql', 'database', 'data analysis'],
            'career_path': 'Data Analyst', 'link': '#', 'domain': 'Data Analytics'
        },
        {
            'id': 6, 'title': 'Machine Learning Specialization', 'provider': 'Coursera',
            'duration': '16 weeks', 'level': 'advanced', 'cost': '$199',
            'prerequisites': ['python', 'linear algebra', 'statistics'],
            'skills_covered': ['machine learning', 'python', 'deep learning', 'neural networks'],
            'career_path': 'ML Engineer', 'link': '#', 'domain': 'Data Science'
        },
        
        # Cloud & DevOps
        {
            'id': 7, 'title': 'AWS Cloud Practitioner', 'provider': 'AWS',
            'duration': '4 weeks', 'level': 'beginner', 'cost': 'Free',
            'prerequisites': [],
            'skills_covered': ['aws', 'cloud computing', 'devops'],
            'career_path': 'Cloud Engineer', 'link': '#', 'domain': 'Cloud Computing'
        },
        {
            'id': 8, 'title': 'Docker and Kubernetes', 'provider': 'Udemy',
            'duration': '8 weeks', 'level': 'intermediate', 'cost': '$79',
            'prerequisites': ['linux', 'programming basics'],
            'skills_covered': ['docker', 'kubernetes', 'containers', 'devops'],
            'career_path': 'DevOps Engineer', 'link': '#', 'domain': 'DevOps'
        },
        
        # Business & Marketing
        {
            'id': 9, 'title': 'Digital Marketing Certification', 'provider': 'Google',
            'duration': '5 weeks', 'level': 'beginner', 'cost': 'Free',
            'prerequisites': [],
            'skills_covered': ['seo', 'social media', 'content marketing', 'analytics'],
            'career_path': 'Digital Marketer', 'link': '#', 'domain': 'Marketing'
        },
        {
            'id': 10, 'title': 'Business Analytics', 'provider': 'Coursera',
            'duration': '9 weeks', 'level': 'intermediate', 'cost': '$59',
            'prerequisites': ['excel', 'statistics'],
            'skills_covered': ['excel', 'sql', 'tableau', 'business intelligence'],
            'career_path': 'Business Analyst', 'link': '#', 'domain': 'Business Analytics'
        },
        
        # Design & Creative
        {
            'id': 11, 'title': 'UI/UX Design Principles', 'provider': 'Coursera',
            'duration': '7 weeks', 'level': 'beginner', 'cost': '$79',
            'prerequisites': [],
            'skills_covered': ['figma', 'user research', 'wireframing', 'prototyping'],
            'career_path': 'UI/UX Designer', 'link': '#', 'domain': 'Design'
        },
        {
            'id': 12, 'title': 'Graphic Design Fundamentals', 'provider': 'Skillshare',
            'duration': '6 weeks', 'level': 'beginner', 'cost': 'Free',
            'prerequisites': [],
            'skills_covered': ['photoshop', 'illustrator', 'design principles'],
            'career_path': 'Graphic Designer', 'link': '#', 'domain': 'Design'
        },
        
        # Additional courses to meet 25+ requirement
        {
            'id': 13, 'title': 'React.js Development', 'provider': 'freeCodeCamp',
            'duration': '10 weeks', 'level': 'intermediate', 'cost': 'Free',
            'prerequisites': ['javascript', 'html', 'css'],
            'skills_covered': ['react', 'javascript', 'frontend development'],
            'career_path': 'React Developer', 'link': '#', 'domain': 'Web Development'
        },
        {
            'id': 14, 'title': 'Node.js Backend Development', 'provider': 'Udemy',
            'duration': '11 weeks', 'level': 'intermediate', 'cost': '$89',
            'prerequisites': ['javascript'],
            'skills_covered': ['node.js', 'express', 'mongodb', 'backend development'],
            'career_path': 'Backend Developer', 'link': '#', 'domain': 'Web Development'
        },
        {
            'id': 15, 'title': 'Data Visualization with Python', 'provider': 'edX',
            'duration': '7 weeks', 'level': 'intermediate', 'cost': '$49',
            'prerequisites': ['python'],
            'skills_covered': ['python', 'matplotlib', 'seaborn', 'data visualization'],
            'career_path': 'Data Analyst', 'link': '#', 'domain': 'Data Analytics'
        },
        {
            'id': 16, 'title': 'Cybersecurity Fundamentals', 'provider': 'Coursera',
            'duration': '8 weeks', 'level': 'beginner', 'cost': 'Free',
            'prerequisites': [],
            'skills_covered': ['cybersecurity', 'network security', 'encryption'],
            'career_path': 'Security Analyst', 'link': '#', 'domain': 'Cybersecurity'
        },
        {
            'id': 17, 'title': 'Project Management Professional', 'provider': 'Udemy',
            'duration': '12 weeks', 'level': 'intermediate', 'cost': '$129',
            'prerequisites': [],
            'skills_covered': ['project management', 'leadership', 'agile', 'scrum'],
            'career_path': 'Project Manager', 'link': '#', 'domain': 'Management'
        },
        {
            'id': 18, 'title': 'Advanced Excel for Business', 'provider': 'LinkedIn Learning',
            'duration': '5 weeks', 'level': 'intermediate', 'cost': '$39',
            'prerequisites': ['excel basics'],
            'skills_covered': ['excel', 'pivot tables', 'vlookup', 'data analysis'],
            'career_path': 'Business Analyst', 'link': '#', 'domain': 'Business Analytics'
        },
        {
            'id': 19, 'title': 'Mobile App Development with Flutter', 'provider': 'Udemy',
            'duration': '9 weeks', 'level': 'intermediate', 'cost': '$79',
            'prerequisites': ['programming basics'],
            'skills_covered': ['flutter', 'dart', 'mobile development', 'ui design'],
            'career_path': 'Mobile Developer', 'link': '#', 'domain': 'Mobile Development'
        },
        {
            'id': 20, 'title': 'Content Writing Mastery', 'provider': 'Skillshare',
            'duration': '4 weeks', 'level': 'beginner', 'cost': 'Free',
            'prerequisites': [],
            'skills_covered': ['content writing', 'seo', 'copywriting', 'blogging'],
            'career_path': 'Content Writer', 'link': '#', 'domain': 'Marketing'
        },
        {
            'id': 21, 'title': 'Python for Finance', 'provider': 'edX',
            'duration': '8 weeks', 'level': 'intermediate', 'cost': '$89',
            'prerequisites': ['python'],
            'skills_covered': ['python', 'pandas', 'financial analysis', 'data science'],
            'career_path': 'Financial Analyst', 'link': '#', 'domain': 'Finance'
        },
        {
            'id': 22, 'title': 'Social Media Marketing', 'provider': 'Coursera',
            'duration': '6 weeks', 'level': 'beginner', 'cost': 'Free',
            'prerequisites': [],
            'skills_covered': ['social media', 'marketing', 'analytics', 'content creation'],
            'career_path': 'Social Media Manager', 'link': '#', 'domain': 'Marketing'
        },
        {
            'id': 23, 'title': 'Linux System Administration', 'provider': 'Linux Foundation',
            'duration': '10 weeks', 'level': 'intermediate', 'cost': '$199',
            'prerequisites': [],
            'skills_covered': ['linux', 'system administration', 'bash', 'networking'],
            'career_path': 'System Administrator', 'link': '#', 'domain': 'IT Operations'
        },
        {
            'id': 24, 'title': 'Artificial Intelligence Fundamentals', 'provider': 'edX',
            'duration': '12 weeks', 'level': 'advanced', 'cost': '$149',
            'prerequisites': ['python', 'mathematics'],
            'skills_covered': ['ai', 'machine learning', 'neural networks', 'python'],
            'career_path': 'AI Engineer', 'link': '#', 'domain': 'Artificial Intelligence'
        },
        {
            'id': 25, 'title': 'Product Management Essentials', 'provider': 'Product School',
            'duration': '8 weeks', 'level': 'intermediate', 'cost': '$299',
            'prerequisites': [],
            'skills_covered': ['product management', 'strategy', 'user research', 'roadmapping'],
            'career_path': 'Product Manager', 'link': '#', 'domain': 'Product Management'
        }
    ]
    
    return pd.DataFrame(courses)

if __name__ == "__main__":
    catalog = get_course_catalog()
    print(f"✅ Loaded {len(catalog)} courses")
    print("\n📊 Course Distribution by Domain:")
    print(catalog['domain'].value_counts())