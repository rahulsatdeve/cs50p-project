# cs50p-project
My final project for the CS50P Python course.
#filmmaker team selector (Nagpur edition)
## video url
# description:
The filmmaker team selector is a python based application designed to help young filmmakers in Nagpur like me , find a collaborative and qualified team for film projects. 
The idea behind this came from my interest in filmmaking and the difficulty of finding qualified people in Nagpur.
This program allows users to enter their data such as their name, city, filmmaking experience, their role in filmmaking and then it filters the candidates based on the predefined eligibility creiteria,then builds a final team of exactly 5 members.
## features:
- Accepts user input for name, city, short film experience, and role
- Validates that the candidate is from Nagpur
- Ensures the candidate has made at least one short film
- Restricts roles to a predefined set: actor, director, dop, writer, producer, and music
- Continuously collects valid candidates until a team of 5 members is formed
- Displays the final selected team in a structured format
# project structure:
The project consists of the following files:

- `project.py`: Contains the main program logic, including input handling, validation functions, and team display functionality.
- `test_project.py`: Contains pytest-based unit tests to verify the correctness of validation functions and member addition logic.
- `README.md`: Documentation explaining the project, its functionality, and design decisions.
# design decisions:
The program uses modfularity to improve readability and maintainability. Instead of conjusting all logic into the main function , separate functions were created for validation and data handling.
Two key validation functions were implemented:
- `valid_film_person()` ensures that only candidates from Nagpur with prior short film experience are accepted.
- `valid_role()` ensures that only predefined filmmaking roles are allowed.	
This separation of logic makes the program easy to understand , test , and extend in the future.
A dictionary-based structure was used to store each team member’s details, allowing for better organization of data compared to simple lists.
### Testing

The project includes automated tests written using `pytest`. These tests verify:
- Correct validation of city and filmmaking experience
- Proper role validation including case-insensitive inputs
- Correct addition of members to the team list

Tests can be executed using: python -m pytest test_project.py
### Future Improvements

Possible future enhancements include:
- Adding file storage to save team data permanently
- Preventing duplicate roles (e.g., only one director allowed)
- Adding a graphical interface for easier interaction
- Expanding eligibility criteria for more complex selection logic

### Conclusion

This project demonstrates the use of Python fundamentals such as functions, loops, conditionals, lists, and dictionaries. It also applies basic software engineering principles such as modular design and testing. Overall, it simulates a real-world problem in the filmmaking domain and provides a structured solution for team selection.
