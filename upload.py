import requests
import os

path: str = "C:\\Users\\K\\Downloads\\rishit_cv_updated.pdf"
print(path)
job_description = """
Job Title: C# Software Engineer

Company: CodeCraft Solutions

Location: Seattle, WA

Job Description:
CodeCraft Solutions is seeking a skilled and passionate C# Software Engineer to join our dynamic team. As a C# Software Engineer, you will play a key role in designing, developing, and maintaining software solutions using the C# programming language and the .NET framework. You will collaborate with cross-functional teams to deliver high-quality software products that meet our clients' needs and exceed their expectations.

Responsibilities:

    Design, develop, and maintain software applications using C# and the .NET framework.
    Collaborate with product managers, designers, and other stakeholders to understand requirements and translate them into technical specifications.
    Write clean, efficient, and maintainable code following best practices and coding standards.
    Conduct code reviews and provide constructive feedback to team members.
    Troubleshoot and debug issues, and implement solutions to ensure the stability and performance of software applications.
    Work closely with quality assurance engineers to develop and execute test plans and ensure software quality.
    Stay up-to-date with the latest technologies and trends in software development, and continuously improve technical skills.

Qualifications:

    Bachelor's degree in Computer Science, Engineering, or related field; Master's degree preferred.
    3+ years of experience in software development using C# and the .NET framework.
    Proficiency in object-oriented programming concepts and design patterns.
    Strong understanding of software development methodologies, such as Agile or Scrum.
    Experience with database technologies, such as SQL Server or MySQL.
    Familiarity with front-end technologies such as HTML, CSS, and JavaScript is a plus.
    Excellent problem-solving skills and attention to detail.
    Strong communication and interpersonal skills.
"""
# r= requests.get("http://localhost:8000/output")
# print(r)
r = requests.post("http://localhost:8000/upload", files={"resume":open(path, 'rb')}, data={"job_description": job_description})