# sample_profiles.py - 5 distinct user profiles as required
def get_sample_profiles():
    """5 distinct user profiles from beginner to advanced"""
    return [
        {
            'name': 'College Student (Beginner)',
            'education': 'Bachelors in Business Administration',
            'technical_skills': ['excel', 'powerpoint', 'word'],
            'soft_skills': ['communication', 'teamwork', 'presentation'],
            'target_domain': 'Business Analytics',
            'experience_years': 0,
            'goals': 'Start career in data-driven business roles'
        },
        {
            'name': 'Career Switcher (Intermediate)',
            'education': 'Bachelors in Mechanical Engineering',
            'technical_skills': ['python', 'matlab', 'excel', 'cad'],
            'soft_skills': ['problem solving', 'project management', 'analytical thinking'],
            'target_domain': 'Data Science',
            'experience_years': 3,
            'goals': 'Transition from engineering to data science role'
        },
        {
            'name': 'IT Professional (Advanced)',
            'education': 'Masters in Computer Science',
            'technical_skills': ['python', 'java', 'sql', 'linux', 'docker', 'aws'],
            'soft_skills': ['leadership', 'mentoring', 'technical architecture'],
            'target_domain': 'DevOps',
            'experience_years': 5,
            'goals': 'Advance to senior DevOps or cloud architecture roles'
        },
        {
            'name': 'Marketing Professional',
            'education': 'Bachelors in Marketing',
            'technical_skills': ['excel', 'social media', 'seo', 'google analytics'],
            'soft_skills': ['creativity', 'communication', 'strategy'],
            'target_domain': 'Digital Marketing',
            'experience_years': 2,
            'goals': 'Become digital marketing manager or specialist'
        },
        {
            'name': 'Recent Bootcamp Grad',
            'education': 'Full Stack Web Development Bootcamp',
            'technical_skills': ['html', 'css', 'javascript', 'react', 'node.js'],
            'soft_skills': ['teamwork', 'adaptability', 'quick learning'],
            'target_domain': 'Web Development',
            'experience_years': 1,
            'goals': 'Land first job as frontend or fullstack developer'
        }
    ]

def get_profile_by_name(profiles, name):
    """Get specific profile by name"""
    for profile in profiles:
        if profile['name'] == name:
            return profile
    return None

if __name__ == "__main__":
    profiles = get_sample_profiles()
    print(f"✅ Loaded {len(profiles)} sample profiles")
    for profile in profiles:
        print(f"\n👤 {profile['name']}")
        print(f"   Skills: {', '.join(profile['technical_skills'])}")
        print(f"   Target: {profile['target_domain']}")