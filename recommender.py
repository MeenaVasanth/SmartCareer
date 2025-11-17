# recommender.py - AI Matching Engine
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class CareerRecommender:
    def __init__(self, courses_df):
        self.courses_df = courses_df
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
        self._train_model()
    
    def _train_model(self):
        """Prepare course features for semantic matching"""
        course_texts = []
        for _, course in self.courses_df.iterrows():
            # Combine all relevant text for semantic matching
            text = f"{course['title']} {' '.join(course['skills_covered'])} {course['career_path']} {course['domain']}"
            course_texts.append(text)
        
        self.course_features = self.vectorizer.fit_transform(course_texts)
        self.feature_names = self.vectorizer.get_feature_names_out()
    
    def calculate_match_score(self, user_profile, course):
        """Calculate comprehensive match score (0-100)"""
        score = 0
        
        # 1. Skill matching (40 points)
        user_skills = [s.lower().strip() for s in user_profile['technical_skills']]
        course_skills = [s.lower().strip() for s in course['skills_covered']]
        
        skill_matches = len(set(user_skills) & set(course_skills))
        total_course_skills = max(len(course_skills), 1)  # Avoid division by zero
        score += (skill_matches / total_course_skills) * 40
        
        # 2. Level appropriateness (25 points)
        user_level = self._get_user_level(user_profile)
        course_level = course['level']
        score += self._calculate_level_score(user_level, course_level)
        
        # 3. Prerequisite satisfaction (20 points)
        missing_prereqs = len([p for p in course['prerequisites'] if p.lower() not in user_skills])
        if missing_prereqs == 0:
            score += 20
        elif missing_prereqs == 1:
            score += 15
        elif missing_prereqs == 2:
            score += 10
        else:
            score += 5
        
        # 4. Career goal alignment (15 points)
        target_domain = user_profile.get('target_domain', '').lower()
        if target_domain and (target_domain in course['domain'].lower() or 
                             target_domain in course['career_path'].lower()):
            score += 15
        
        return min(100, int(score))
    
    def _get_user_level(self, user_profile):
        """Determine user skill level based on experience and skills"""
        skills_count = len(user_profile['technical_skills'])
        experience = user_profile.get('experience_years', 0)
        
        if skills_count <= 3 or experience < 1:
            return 'beginner'
        elif skills_count <= 6 or experience < 3:
            return 'intermediate'
        else:
            return 'advanced'
    
    def _calculate_level_score(self, user_level, course_level):
        """Calculate score based on level matching"""
        level_matrix = {
            ('beginner', 'beginner'): 25,
            ('beginner', 'intermediate'): 15,
            ('beginner', 'advanced'): 5,
            ('intermediate', 'beginner'): 10,
            ('intermediate', 'intermediate'): 25,
            ('intermediate', 'advanced'): 20,
            ('advanced', 'beginner'): 5,
            ('advanced', 'intermediate'): 15,
            ('advanced', 'advanced'): 25
        }
        return level_matrix.get((user_level, course_level), 10)
    
    def generate_recommendations(self, user_profile, top_n=10):
        """Generate ranked course recommendations with justifications"""
        recommendations = []
        
        for _, course in self.courses_df.iterrows():
            match_score = self.calculate_match_score(user_profile, course)
            
            if match_score >= 20:  # Only include courses with reasonable match
                justification = self._generate_justification(user_profile, course, match_score)
                timeline = self._determine_timeline(user_profile, course)
                
                recommendations.append({
                    'course_id': course['id'],
                    'title': course['title'],
                    'provider': course['provider'],
                    'duration': course['duration'],
                    'level': course['level'],
                    'cost': course['cost'],
                    'match_score': match_score,
                    'justification': justification,
                    'timeline': timeline,
                    'career_path': course['career_path'],
                    'domain': course['domain'],
                    'skills_covered': course['skills_covered'],
                    'prerequisites': course['prerequisites'],
                    'link': course['link']
                })
        
        # Sort by match score (highest first) and return top N
        recommendations.sort(key=lambda x: x['match_score'], reverse=True)
        return recommendations[:top_n]
    
    def _generate_justification(self, user_profile, course, score):
        """Generate human-readable justification for recommendation"""
        user_skills = [s.lower() for s in user_profile['technical_skills']]
        course_skills = [s.lower() for s in course['skills_covered']]
        
        matching_skills = set(user_skills) & set(course_skills)
        new_skills = set(course_skills) - set(user_skills)
        missing_prereqs = [p for p in course['prerequisites'] if p.lower() not in user_skills]
        
        if score >= 80:
            return f"🎯 Excellent fit! You have {len(matching_skills)} required skills. This will add {len(new_skills)} new skills to your toolkit."
        elif score >= 60:
            return f"✅ Strong match. Builds on your {len(matching_skills)} existing skills. You'll learn {len(new_skills)} new technologies."
        elif score >= 40:
            if missing_prereqs:
                return f"⚠️ Good potential. Learn {len(new_skills)} new skills. Consider brushing up on: {', '.join(missing_prereqs[:2])}"
            else:
                return f"📈 Solid option. Expands your skillset with {len(new_skills)} new technologies."
        else:
            return f"🎓 Learning opportunity. Challenges you with {len(new_skills)} new skills. Prepare by learning prerequisites first."
    
    def _determine_timeline(self, user_profile, course):
        """Determine if course is short-term, medium-term, or long-term"""
        user_level = self._get_user_level(user_profile)
        course_level = course['level']
        
        if user_level == course_level:
            return 'short-term'  # 1-3 months
        elif (user_level, course_level) in [('beginner', 'intermediate'), ('intermediate', 'advanced')]:
            return 'medium-term'  # 3-6 months
        else:
            return 'long-term'  # 6-12 months

def create_learning_path(recommendations):
    """Create structured learning path from recommendations"""
    short_term = [r for r in recommendations if r['timeline'] == 'short-term']
    medium_term = [r for r in recommendations if r['timeline'] == 'medium-term']
    long_term = [r for r in recommendations if r['timeline'] == 'long-term']
    
    return {
        'short_term_plan': short_term[:3],  # Next 1-3 months
        'medium_term_plan': medium_term[:2],  # Next 3-6 months
        'long_term_plan': long_term[:2]  # Next 6-12 months
    }

def generate_json_output(recommendations, learning_path):
    """Generate JSON output as required by problem statement"""
    output = {
        "user_recommendations": [],
        "learning_timeline": {
            "short_term": [],
            "medium_term": [],
            "long_term": []
        }
    }
    
    for rec in recommendations:
        output["user_recommendations"].append({
            "course_title": rec['title'],
            "provider": rec['provider'],
            "match_score": rec['match_score'],
            "justification": rec['justification'],
            "timeline": rec['timeline'],
            "career_path": rec['career_path']
        })
    
    for timeline in ['short_term', 'medium_term', 'long_term']:
        for course in learning_path[f"{timeline}_plan"]:
            output["learning_timeline"][timeline].append({
                "course_title": course['title'],
                "reason": f"Builds on current skills and leads to {course['career_path']} role"
            })
    
    return output

if __name__ == "__main__":
    from course_data import get_course_catalog
    from sample_profiles import get_sample_profiles
    
    # Test the recommender
    courses = get_course_catalog()
    profiles = get_sample_profiles()
    recommender = CareerRecommender(courses)
    
    test_profile = profiles[0]  # College Student
    recommendations = recommender.generate_recommendations(test_profile)
    
    print(f"✅ Generated {len(recommendations)} recommendations for {test_profile['name']}")
    for i, rec in enumerate(recommendations[:3], 1):
        print(f"{i}. {rec['title']} - {rec['match_score']}%")