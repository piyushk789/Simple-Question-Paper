# Simple-Question-Paper

### Quiz-Test
- A Python-based GUI application for conducting `school-college` exams with features like user introduction, question-paper display, and result generation.

### Description:
- **Overview:**
  The provided Python script is a Tkinter-based quiz application designed for conducting exams. It includes features for user registration, question presentation, and result tracking. The application begins with an introduction section, where the user enters their name and course details. After registration, the user proceeds to the main quiz section, answering multiple-choice questions. The application supports navigation between questions and provides a visually appealing interface.

### Key Features:

- **User Registration:**
  - Introduces users to the exam by collecting their name and course details.
  - Validates input to ensure user details meet length requirements.

- **Question Presentation:**
  - Loads questions from a JSON file (`data.json`) for presentation during the quiz.
  - Users navigate through questions using "Next" and "Preview" buttons.

- **Result Calculation:**
  - Stores user responses in a dictionary for each question.
  - Calculates the total number of correct answers upon completing the quiz.

- **GUI and Styling:**
  - Utilizes Tkinter for a visually appealing and interactive graphical user interface (GUI).
  - Incorporates labels, entry fields, buttons, and radiobuttons styled for clarity.

- **Image Display:**
  - Utilizes the Pillow (PIL) library to display the company logo.
  - Enhances the visual representation of the application.

- **Dynamic JSON File Creation:**
  - Generates a JSON file for each exam attempt based on the company name and timestamp.
  - Saves user details, total correct answers, and specific question-response pairs.

- **Executable Version:**
  - Provides the option to run the script as an executable (`.exe`) for users without Python installed.
  - Facilitates ease of use and accessibility.

- **User-Friendly Navigation:**
  - Supports intuitive navigation between questions using buttons.
  - Allows users to review and change their responses before submitting.

- **Input Validation:**
  - Enforces input validation to ensure user-provided details meet specified criteria.
  - Enhances data integrity and user experience.

- **Informative Result Message:**
  - Notifies users about the expected date for receiving their results.
  - Provides clarity on the outcome and next steps.

### Usage:

1. **Introduction Section:**
   - Users start with the introduction section by providing their name and course details.
   - Clicking the "Start Test" button initiates the quiz.

2. **Quiz Section:**
   - Users navigate through questions using the "Next" and "Preview" buttons.
   - Questions are presented with multiple-choice options.
   - Users select their answers using radiobuttons.

3. **Result Display:**
   - After completing the quiz, results are calculated and saved to a JSON file.
   - Users receive a message indicating when they can expect their results.

### Execution:

- The script is executed by running the Python file (`quiz_test.py`) with Python 3.x.
- Ensure the necessary dependencies (`Pillow`) are installed.
- The script supports an executable version (`.exe`), providing a convenient option for users without Python installed.

### Additional Notes:
- The application uses the `Pillow` library for image handling. Install it using `pip install Pillow` before running the script.

### Screenshots:
- Optionally, include screenshots of the application interface or sample outputs. You can add these images to a "screenshots" folder in your repository.

### License:
- The code is licensed under the [MIT License](LICENSE).

### Author:
- Kartikey Baghel
- E-mail : kartikeybaghel@hotmail.com

### Disclaimer:
- Old records are saved.
