# cs50p-project
My final project for the CS50P Python course.
Filmmaker Team Selector (Nagpur Edition)
Video URL: https://youtu.be/mpWv8F1DRpY


Description:

The Filmmaker Team Selector is a Python-based application designed to help young filmmakers in Nagpur find a collaborative and qualified team for film projects.

The idea behind this project came from my interest in filmmaking and the difficulty of finding skilled collaborators locally.

This program allows users to enter details such as name, city, filmmaking experience, and role. It then filters candidates based on predefined eligibility criteria and builds a final team of exactly 5 members.

Features:
Accepts user input for name, city, filmmaking experience, and role
Validates that the candidate is from Nagpur
Ensures the candidate has made at least one short film
Restricts roles to a predefined set: actor, director, DOP, writer, producer, and music
Continuously collects valid candidates until a team of 5 members is formed
Displays the final selected team in a structured format

Project Structure:
project.py → Main program logic including input handling, validation functions, and team display
test_project.py → Pytest-based unit tests for validation and member addition logic
README.md → Project documentation

Design Decisions:

The program uses modularity to improve readability and maintainability. Instead of placing all logic in a single function, separate functions handle validation and data processing.

Two key validation functions are implemented:

valid_film_person() → Ensures candidates are from Nagpur and have at least one short film experience
valid_role() → Ensures only predefined filmmaking roles are accepted

A dictionary-based structure is used to store each team member’s details, improving data organization compared to simple lists.

Testing:

The project uses pytest for automated testing. Tests verify:

City and filmmaking experience validation
Role validation (including case-insensitive inputs)
Correct addition of members to the team list

Run tests using:

python -m pytest test_project.py
Future Improvements
Add file storage to save team data permanently
Prevent duplicate roles (e.g., only one director allowed)
Add a graphical user interface (GUI)
Expand eligibility rules for advanced selection logic

Conclusion:

This project demonstrates Python fundamentals such as functions, loops, conditionals, lists, and dictionaries. It also applies modular design and testing principles.

It simulates a real-world filmmaking scenario by helping build structured and qualified teams for creative projects.