# Import Libraries
from faker import Faker
import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta, date

# Initialize Faker
fake = Faker()

#######################################
# CLASS DATA
#######################################

# Define the class levels and arms with their corresponding class IDs
class_data = [
    {'class_id': 1, 'class_level': 'JS 1', 'class_arm': 'JS 1A'},
    {'class_id': 2, 'class_level': 'JS 1', 'class_arm': 'JS 1B'},
    {'class_id': 3, 'class_level': 'JS 2', 'class_arm': 'JS 2A'},
    {'class_id': 4, 'class_level': 'JS 2', 'class_arm': 'JS 2B'},
    {'class_id': 5, 'class_level': 'JS 3', 'class_arm': 'JS 3A'},
    {'class_id': 6, 'class_level': 'JS 3', 'class_arm': 'JS 3B'},
    {'class_id': 7, 'class_level': 'SS 1', 'class_arm': 'SS 1A'},
    {'class_id': 8, 'class_level': 'SS 1', 'class_arm': 'SS 1B'},
    {'class_id': 9, 'class_level': 'SS 2', 'class_arm': 'SS 2A'},
    {'class_id': 10, 'class_level': 'SS 2', 'class_arm': 'SS 2B'},
    {'class_id': 11, 'class_level': 'SS 3', 'class_arm': 'SS 3A'},
    {'class_id': 12, 'class_level': 'SS 3', 'class_arm': 'SS 3B'},
]

# Convert class data to DataFrame
df_classes = pd.DataFrame(class_data)

#######################################
# SUBJECT DATA
#######################################

# Define subjects for Junior and Senior levels
subjects = [
    {'subject_name': 'Mathematics', 'department': 'Sciences', 'level': 'Junior'},
    {'subject_name': 'English', 'department': 'Arts', 'level': 'Junior'},
    {'subject_name': 'Basic Sciences', 'department': 'Sciences', 'level': 'Junior'},
    {'subject_name': 'Vocational Studies', 'department': 'Vocational', 'level': 'Junior'},
    {'subject_name': 'Literature', 'department': 'Arts', 'level': 'Junior'},
    {'subject_name': 'History', 'department': 'Arts', 'level': 'Junior'},
    {'subject_name': 'French', 'department': 'Arts', 'level': 'Junior'},
    {'subject_name': 'Physical Education', 'department': 'Vocational', 'level': 'Junior'},
    {'subject_name': 'CRS', 'department': 'Arts', 'level': 'Junior'},
    {'subject_name': 'Agricultural Science', 'department': 'Sciences', 'level': 'Junior'},
    {'subject_name': 'Mathematics', 'department': 'Sciences', 'level': 'Senior'},
    {'subject_name': 'English', 'department': 'Arts', 'level': 'Senior'},
    {'subject_name': 'Literature', 'department': 'Arts', 'level': 'Senior'},
    {'subject_name': 'Agricultural Science', 'department': 'Sciences', 'level': 'Senior'},
    {'subject_name': 'Biology', 'department': 'Sciences', 'level': 'Senior'},
    {'subject_name': 'Physics', 'department': 'Sciences', 'level': 'Senior'},
    {'subject_name': 'Chemistry', 'department': 'Sciences', 'level': 'Senior'},
    {'subject_name': 'Government', 'department': 'Arts', 'level': 'Senior'},
    {'subject_name': 'Economics', 'department': 'Social Studies', 'level': 'Senior'},
    {'subject_name': 'Geography', 'department': 'Sciences', 'level': 'Senior'}
]

# Add subject_id to each entry
for idx, subject in enumerate(subjects, start=1):
    subject['subject_id'] = idx  # Assign incrementing subject_id

# Convert subjects data to DataFrame
df_subjects = pd.DataFrame(subjects)

#######################################
# TEACHER DATA
#######################################

# Custom Nigerian names
nigerian_first_names = [
    'Chinaza', 'Ifeanyi', 'Ngozi', 'Ahmed', 'Adebayo', 'Chinedu', 'Bola', 
    'Ibrahim', 'Kemi', 'Obinna', 'Fatima', 'Yusuf', 'Adamu', 'Amara', 
    'Tolu', 'Olu', 'Funke', 'Isioma', 'Ada', 'Gbenga'
]
nigerian_last_names = [
    'Okeke', 'Adeyemi', 'Olawale', 'Bello', 'Nnamdi', 'Danladi', 'Eze', 
    'Abdullahi', 'Abimbola', 'Adenuga', 'Adebayo', 'Aliyu', 'Umar', 'Balogun'
]

# Gender distribution: 63.6% female, 36.4% male
gender_distribution = ['Female'] * 636 + ['Male'] * 364

# Qualification distribution: Bachelors (22%), PGDE (5.5%), NCE (67.5%), Masters (5%)
qualification_distribution = {
    'Bachelors': 22,
    'PGDE': 5.5,
    'NCE': 67.5,
    'Masters': 5
}

# Function to assign salary based on qualification and experience
# Function to assign salary based on qualification and experience, with specific rounded values
def assign_salary(qualification, years_of_experience):
    if years_of_experience <= 2:
        if qualification == 'Bachelors':
            return 50000 if years_of_experience < 2 else 70000  # 50,000 for 0-1 years, 70,000 for 2 years
        elif qualification == 'NCE':
            return 45000 if years_of_experience < 2 else 65000  # 45,000 for 0-1 years, 65,000 for 2 years
    elif 2 < years_of_experience <= 5:
        if qualification == 'Bachelors':
            return random.choice([80000, 90000, 100000, 120000])  # Random selection between 80,000 - 120,000
        elif qualification == 'Masters':
            return random.choice([100000, 120000, 150000])  # Random selection between 100,000 - 150,000
    else:  # Senior (5+ years experience)
        if qualification == 'Masters':
            return random.choice([150000, 180000, 200000])  # Random selection between 150,000 - 200,000
        elif qualification == 'Bachelors':
            return random.choice([120000, 150000, 180000])  # Random selection between 120,000 - 180,000
        elif qualification == 'NCE':
            return random.choice([65000, 70000, 90000])  # Random selection between 65,000 - 90,000
    return random.choice([50000, 200000])  # Default range, should never hit this based on constraints


# Function to determine category based on years of experience
def assign_category(years_of_experience):
    if years_of_experience <= 2:
        return 'Entry-Level'
    elif 2 < years_of_experience <= 5:
        return 'Experienced'
    else:
        return 'Senior'

# Generate teacher data based on constraints
teachers = []
teacher_id = 1
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 1, 1)

for subject in subjects:
    for class_level in ['JS1', 'JS2', 'JS3'] if subject['level'] == 'Junior' else ['SS1', 'SS2', 'SS3']:
        first_name = random.choice(nigerian_first_names)
        last_name = random.choice(nigerian_last_names)
        gender = random.choice(gender_distribution)  # Use gender distribution
        date_of_birth = fake.date_of_birth(minimum_age=23, maximum_age=43)
        years_of_experience = random.randint(0, 10)  # Range from 0 to 10 years of experience
        qualification = random.choices(
            ['Bachelors', 'PGDE', 'NCE', 'Masters'], 
            weights=[qualification_distribution['Bachelors'], 
                    qualification_distribution['PGDE'], 
                    qualification_distribution['NCE'], 
                    qualification_distribution['Masters']], 
            k=1
        )[0]  # Qualification with new distribution
        contact_number = f"0{random.choice([70, 80])}{random.randint(10000000, 99999999)}"
        hire_date = fake.date_between(start_date=start_date, end_date=end_date)

        # Assign salary based on qualification and experience
        salary = assign_salary(qualification, years_of_experience)
        category = assign_category(years_of_experience)

        teachers.append({
            'teacher_id': teacher_id,
            'first_name': first_name,
            'last_name': last_name,
            'gender': gender,
            'date_of_birth': date_of_birth,
            'qualification': qualification,
            'years_of_experience': years_of_experience,
            'subject_expertise': f"{subject['subject_name']}",
            'department': subject['department'],
            'contact_number': contact_number,
            'hire_date': hire_date,
            'salary': salary,
            'category': category  # New category column
        })
        teacher_id += 1

# Convert teachers data to DataFrame
df_teachers = pd.DataFrame(teachers)

#######################################
# PARENT DATA
#######################################

occupations = ['Education', 'Healthcare', 'Engineering', 'Technology', 'Business', 'Skilled Trades', 'Service Industry', 'Unemployed', 'Retired']
education_levels = ['Primary', 'Secondary', 'Tertiary']
income_brackets = ['Low', 'Medium', 'High']

# Function to generate phone numbers
def generate_phone_number():
    prefix = random.choice(['080', '070'])
    remaining_digits = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    return prefix + remaining_digits

# Number of unique parents
num_parents = 500
parents = []
low_income_target = int(0.50 * num_parents)
medium_income_target = int(0.35 * num_parents)
high_income_target = num_parents - (low_income_target + medium_income_target)

# Generate parent data
for parent_id in range(101, 101 + num_parents):
    first_name = random.choice(nigerian_first_names)
    last_name = random.choice(nigerian_last_names)
    occupation = random.choice(occupations)
    
    if occupation in ['Education', 'Healthcare', 'Engineering', 'Technology']:
        education_level = 'Tertiary'
    else:
        education_level = random.choices(['Primary', 'Secondary', 'Tertiary'], weights=[0.40, 0.40, 0.20], k=1)[0]
    
    if low_income_target > 0:
        income_bracket = 'Low'
        low_income_target -= 1
    elif medium_income_target > 0:
        income_bracket = 'Medium'
        medium_income_target -= 1
    else:
        income_bracket = 'High'
    
    parent_contact = generate_phone_number()
    
    parents.append({
        'parent_id': parent_id,
        'first_name': first_name,
                'last_name': last_name,
        'occupation': occupation,
        'education_level': education_level,
        'income_bracket': income_bracket,
        'parent_contact': parent_contact
    })

# Convert parent data to DataFrame
df_parents = pd.DataFrame(parents)

#######################################
# STUDENT DATA
#######################################

nigerian_first_names = ['Chinaza', 'Ifeanyi', 'Ngozi', 'Ahmed', 'Adebayo', 'Chinedu', 'Bola', 'Ibrahim', 'Kemi', 'Obinna']
nigerian_last_names = ['Okeke', 'Adeyemi', 'Olawale', 'Bello', 'Nnamdi', 'Danladi', 'Eze', 'Abdullahi', 'Abimbola']

# Fixed number of students per class arm (600 students total)
students_per_class = 50
statuses = ['Active', 'Inactive', 'Repeating']
cities = ['Warri', 'Asaba', 'Ughelli', 'Sapele', 'Agbor', 'Oleh', 'Ozoro', 'Oghara', 'Abraka', 'Koko', 'Burutu', 'Patani', 'Ughelli']

# Generate random street addresses
street_addresses = [fake.street_address() for _ in range(50)]

# Create an empty list to store student data
students = []
parent_ids = list(range(101, 601))  # Assuming 500 unique parents
class_ids = list(range(1, 13))
student_id = 1001
record_id = 1
total_students = 600
repeating_target = int(0.03 * total_students)  # 3% Repeating students
enrollment_start = date(2024, 2, 7)
enrollment_end = date(2024, 2, 21)

# Generate student data
for class_id in class_ids:
    for _ in range(students_per_class):
        dob = fake.date_of_birth(minimum_age=10, maximum_age=16)
        age = datetime.now().year - dob.year
        city = random.choice(cities)
        street_address = random.choice(street_addresses)
        first_name = random.choice(nigerian_first_names)
        last_name = random.choice(nigerian_last_names)
        parent_id = random.choice(parent_ids)

        students.append({
            'record_id': record_id,
            'student_id': student_id,
            'first_name': first_name,
            'last_name': last_name,
            'parent_id': parent_id,
            'class_id': class_id,
            'gender': np.random.choice(['Male', 'Female']),
            'date_of_birth': dob,
            'date_enrolled': fake.date_between(start_date=enrollment_start, end_date=enrollment_end),
            'is_repeating': False,
            'age': age,
            'street_address': street_address,
            'city': city,
            'start_date': datetime.now().strftime('%Y-%m-%d'),
            'end_date': None,
            'is_current': 'Yes'
        })
        record_id += 1
        student_id += 1

# Shuffle the dataset and set the first 3% as repeating
random.shuffle(students)
for i in range(repeating_target):
    students[i]['is_repeating'] = True

# Convert student data to DataFrame
df_students = pd.DataFrame(students)

#######################################
# CLASS-SUBJECT ALLOCATION DATA
#######################################

class_subject_allocations = []
allocation_id = 1
academic_year = '2024'

# Assign teachers to class-subject combinations
for class_info in class_data:
    class_id = class_info['class_id']
    class_level = class_info['class_level']
    
    if class_level.startswith('JS'):
        relevant_subjects = [subject for subject in subjects if subject['level'] == 'Junior']
    elif class_level.startswith('SS'):
        relevant_subjects = [subject for subject in subjects if subject['level'] == 'Senior']
    
    for subject in relevant_subjects:
        relevant_teachers = [teacher for teacher in teachers if teacher['subject_expertise'] == subject['subject_name']]
        
        if relevant_teachers:
            teacher = random.choice(relevant_teachers)
            periods_per_week = 4
            minutes_per_week = periods_per_week * 40

            class_subject_allocations.append({
                'allocation_id': allocation_id,
                'class_id': class_id,
                'subject_id': subject['subject_id'],
                'teacher_id': teacher['teacher_id'],
                'academic_year': academic_year,
                'periods_per_week': periods_per_week,
                'minutes_per_week': minutes_per_week,
                'created_at': teacher['hire_date']
            })
            allocation_id += 1

# Convert class-subject allocations to DataFrame
df_class_subject_allocation = pd.DataFrame(class_subject_allocations)

#######################################
# EXTRACURRICULAR ACTIVITIES DATA
#######################################

# List of extracurricular activities
activities = ['Drama', 'Music', 'Football', 'Dance', 'Basket Ball', 'Volley Ball']
activities_table = [{'activity_id': idx + 1, 'activity_name': activity} for idx, activity in enumerate(activities)]

# Convert activities to DataFrame
df_activities = pd.DataFrame(activities_table)

# Generate participation data for each student
activity_weights = [0.15, 0.20, 0.23, 0.17, 0.10, 0.5]  # Football is the most popular (40%), others have varied popularity

start_date = datetime(2024, 3, 6)
end_date = start_date + timedelta(days=90)
fridays = [start_date + timedelta(days=i) for i in range((end_date - start_date).days) if (start_date + timedelta(days=i)).weekday() == 4]
hours_distribution = [1, 2, 3]
hours_weights = [0.40, 0.30, 0.30]

participation_data = []
participation_id = 1
student_activities = {student['student_id']: random.randint(1, len(activities)) for student in students}

for student in students:
    student_id = student['student_id']
    activity_id = student_activities[student_id]

    for friday in fridays:
        hours_spent = random.choices(hours_distribution, weights=hours_weights, k=1)[0]
        special_occasion = random.choices([True, False], weights=[0.1, 0.9], k=1)[0]
        if special_occasion:
            hours_spent += random.choice([1, 2])

        participation_data.append({
            'participation_id': participation_id,
            'student_id': student_id,
            'activity_id': activity_id,
            'date': friday,
            'hours_spent': hours_spent,
            'special_occasion': special_occasion
        })
        participation_id += 1

# Convert participation data to DataFrame
df_participation = pd.DataFrame(participation_data)

#######################################
# ATTENDANCE DATA
#######################################

attendance_dates = []
current_date = start_date
while current_date <= end_date:
    if current_date.weekday() < 5:
        attendance_dates.append(current_date)
    current_date += timedelta(days=1)

attendance_data = []
attendance_id = 1
student_ids = df_students['student_id'].tolist()

for student_id in student_ids:
    for date in attendance_dates:
        attendance_status = random.choices(['Present', 'Absent'], weights=[80, 20], k=1)[0]
        attendance_data.append({
            'attendance_id': attendance_id,
            'student_id': student_id,
            'date': date.strftime('%Y-%m-%d'),
            'status': attendance_status
        })
        attendance_id += 1

# Convert attendance data to DataFrame
df_attendance = pd.DataFrame(attendance_data)

#######################################
# GRADES DATA WITH SUBJECT DIFFICULTY
#######################################

# Function to assign letter grades based on total score
def assign_grade(total_score):
    if 70 <= total_score <= 100:
        return 'A'
    elif 60 <= total_score <= 69:
        return 'B'
    elif 50 <= total_score <= 59:
        return 'C'
    elif 40 <= total_score <= 49:
        return 'D'
    else:
        return 'F'

# Define different difficulty levels for subjects (1-10 scale where 10 is hardest)
subject_difficulty = {
    'Mathematics': 9, 'English': 6, 'Basic Sciences': 8, 'Vocational Studies': 3,
    'Literature': 6, 'History': 5, 'French': 7, 'Physical Education': 2,
    'CRS': 4, 'Agricultural Science': 5, 'Biology': 7, 'Physics': 9,
    'Chemistry': 8, 'Government': 6, 'Economics': 7, 'Geography': 6
}

grades = []
grade_id = 1
fail_rate = 0.40  # Base fail rate
weights = [0.10, 0.15, 0.25, 0.50]  # Weighted score distribution for passing students

# Score ranges reflecting varying levels of performance based on difficulty
score_ranges = [(40, 49), (50, 59), (60, 69), (70, 100)]

# Subjects for Junior and Senior levels
junior_subjects = list(range(1, 11))  # Subject IDs 1-10 are junior subjects
senior_subjects = list(range(11, 21))  # Subject IDs 11-20 are senior subjects

academic_year = '2024'
term = 'First Term'

# Loop through students and generate grades with subject variability
for _, student in df_students.iterrows():
    student_id = student['student_id']
    class_id = student['class_id']
    
    # Assign subjects based on class level (Junior or Senior)
    if class_id in range(1, 7):  # JS1 to JS3 classes
        subjects_for_student = junior_subjects
    else:  # SS1 to SS3 classes
        subjects_for_student = senior_subjects

    # Generate grades for each subject the student is taking
    for subject_id in subjects_for_student:
        subject_name = df_subjects[df_subjects['subject_id'] == subject_id]['subject_name'].values[0]
        difficulty = subject_difficulty.get(subject_name, 5)  # Default difficulty is 5
        
        # Increase fail rate for difficult subjects
        adjusted_fail_rate = fail_rate + (difficulty * 0.05)  # Higher difficulty = higher fail rate
        
        if random.random() <= adjusted_fail_rate:
            # If the student is failing, assign lower test/exam scores
            first_test = random.randint(0, 5)
            second_test = random.randint(0, 5)
            exam = random.randint(0, 40)
        else:
            # If the student is passing, assign scores based on weighted score distribution
            score_range = random.choices(score_ranges, weights=weights, k=1)[0]
            total_score = random.randint(*score_range)

            # Break the total score into test and exam components
            first_test = random.randint(10, 15)
            second_test = random.randint(10, 15)
            exam = total_score - (first_test + second_test)

        # Calculate total score and assign a letter grade
        total_score = first_test + second_test + exam
        grade = assign_grade(total_score)
        
        # Add to the grades list
        grades.append({
            'grade_id': grade_id,
            'student_id': student_id,
            'subject_id': subject_id,
            'first_test': first_test,
            'second_test': second_test,
            'exam': exam,
            'total_score': total_score,
            'grade': grade,
            'academic_year': academic_year,
            'term': term,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        grade_id += 1

# Convert grades data to DataFrame
df_grades = pd.DataFrame(grades)


# Convert grades data to DataFrame
df_grades = pd.DataFrame(grades)

#######################################
# SURVEY DATA
#######################################

# Number of survey responses (assuming all 600 students participated)
num_responses = 600

# Survey data points
survey_data = []

for _ in range(num_responses):
    # Study hours per week: mostly below 6 hours (0 to 12 hours)
    study_hours = random.choices(range(0, 13), weights=[30]*6 + [10]*7, k=1)[0]
    
    # Resource access: 40% No, 60% Yes
    resource_access = random.choices(['Yes', 'No'], weights=[60, 40], k=1)[0]
    
    # Computer access: 35.5% Yes, 64.5% No
    computer_access = random.choices(['Yes', 'No'], weights=[35.5, 64.5], k=1)[0]
    
    # Computer literacy: 50% Low, 30% Medium, 20% High
    computer_literacy = random.choices(['Low', 'Medium', 'High'], weights=[70, 20, 10], k=1)[0]
    
    # Stress level: 50% High, 30% Medium, 20% Low
    stress_level = random.choices(['High', 'Medium', 'Low'], weights=[50, 30, 20], k=1)[0]
    
    # Exam anxiety: 75% High, 10% Medium, 5% Low
    exam_anxiety = random.choices(['High', 'Medium', 'Low'], weights=[75, 10, 5], k=1)[0]
    
    # Internet access: 15% No, 75% Yes
    internet_access = random.choices(['Yes', 'No'], weights=[75, 15], k=1)[0]
    
    # Parental support: 65% Poor, 25% Average, 10% Good
    home_study_environment = random.choices(['Poor', 'Average', 'Good'], weights=[65, 25 , 10], k=1)[0]
    
    # Parental support: 65% Low, 25% Medium, 10% High
    parental_support = random.choices(['Low', 'Medium', 'High'], weights=[65, 25 , 10], k=1)[0]
    
    # Extracurricular balance: 50% Struggling, 30% Average, 20% Good
    extracurricular_balance = random.choices(['Struggling', 'Average', 'Good'], weights=[50, 30, 20], k=1)[0]
    
    # Teacher engagement: 50% Low, 30% Medium, 20% High
    teacher_engagement = random.choices(['Low', 'Medium', 'High'], weights=[50, 30, 20], k=1)[0]
    
    # Motivation level: 50% Low, 30% Medium, 20% High
    motivation_level = random.choices(['Low', 'Medium', 'High'], weights=[50, 30, 20], k=1)[0]
    
    # Peer influence: 40% Negative, 40% Neutral, 20% Positive
    peer_influence = random.choices(['Negative', 'Neutral', 'Positive'], weights=[40, 20, 20], k=1)[0]
    
    # Study group participation: 60% No, 40% Yes
    study_group_participation = random.choices(['Yes', 'No'], weights=[40, 60], k=1)[0]

    # Append the survey data
    survey_data.append({
        'study_hours_per_week': study_hours,
        'resource_access': resource_access,
        'computer_access': computer_access,
        'computer_literacy': computer_literacy,
        'stress_level': stress_level,
        'exam_anxiety': exam_anxiety,
        'internet_access': internet_access,
        'home_study_environment' : 'home_study_environment',
        'parental_support': parental_support,
        'extracurricular_balance': extracurricular_balance,
        'teacher_engagement': teacher_engagement,
        'motivation_level': motivation_level,
        'peer_influence': peer_influence,
        'study_group_participation': study_group_participation
    })

# Convert survey data to DataFrame
df_survey = pd.DataFrame(survey_data)

#######################################
# SAVING DATA TO CSV FILES
#######################################

# Save all generated data to CSV files
df_classes.to_csv("../data/classes.csv", index=False)
df_subjects.to_csv("../data/subjects.csv", index=False)
df_teachers.to_csv("../data/teachers.csv", index=False)
df_parents.to_csv("../data/parents.csv", index=False)
df_students.to_csv("../data/students.csv", index=False)
df_class_subject_allocation.to_csv("../data/class_subject_allocation.csv", index=False)
df_activities.to_csv("../data/extracurricular_activities.csv", index=False)
df_participation.to_csv("../data/student_activity_participation.csv", index=False)
df_attendance.to_csv("../data/attendance.csv", index=False)
df_grades.to_csv('../data/grades.csv', index=False)
df_survey.to_csv('../data/student_survey.csv', index=False)


