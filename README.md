# Uber Trips Data Analysis 🚗📊

## Project Overview
This project is part of my **internship at Uneeq** and focuses on performing **Exploratory Data Analysis (EDA)** on an Uber trips dataset to uncover meaningful **business and behavioral insights**.

The analysis aims to understand trip purposes, mileage patterns across different times of day, and differences between business and personal trips.

---

## Dataset Description
The dataset contains Uber trip records with the following key columns:

- **START_DATE**: Trip start date and time  
- **END_DATE**: Trip end date and time  
- **CATEGORY**: Trip category (Business / Personal)  
- **START**: Starting location  
- **STOP**: Ending location  
- **MILES**: Trip distance in miles  
- **PURPOSE**: Purpose of the trip  

---

## Key Questions Answered

### Q1: What are the most common purposes for Uber trips?
**Finding:**
- The most frequent trip purpose is **Meeting**, indicating heavy Uber usage for business-related activities.

---

### Q2: What is the average trip mileage by purpose and time of day?
Trips were analyzed across four time periods:
- Morning
- Afternoon
- Evening
- Night

**Key Insights:**
- **Customer Visit** trips are longer in the afternoon.
- **Meeting** trips show higher average mileage at night.
- **Commute** and **Temporary Site** trips can reach very long distances.
- **Errand/Supplies** trips are short and consistent across all times.

---

### Q3: How do trip lengths differ between Business and Personal categories?

| Category  | Avg Miles | Variability | Max Distance |
|---------|----------|------------|--------------|
| Business | Higher    | High       | Very Long    |
| Personal | Lower     | Moderate   | Long         |

**Insight:**
- Business trips are generally longer and more variable.
- Personal trips tend to be shorter and more consistent.

---

## Conclusion
This analysis highlights Uber’s strong role in **business transportation**, especially for:
- Meetings
- Customer visits
- Office-to-office travel

Understanding trip purposes and time-of-day patterns can support:
- Better pricing strategies
- Improved driver allocation
- Smarter operational planning

---

## Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib / Seaborn
- Jupyter Notebook

---

## Skills Gained
- Exploratory Data Analysis (EDA)
- Data cleaning and preprocessing
- Grouping and aggregation
- Business insight generation
- Data storytelling

---

## Author
**Ahmed Galal**  
Data Analyst Intern @ Uneeq  

---

## Acknowledgment
Special thanks to **Uneeq** for the mentorship and hands-on learning opportunity.
