# Anki Interview Q&A

This project creates an Anki deck with tailored interview questions and answers to help you prepare for job interviews. The questions and answers are specific to your experiences and the roles you are targeting, such as political analysts and lobbyists.

## Features

- Generates an Anki deck with common interview questions and tailored answers
- Includes questions specific to political analysts and lobbyists
- Uses the `genanki` library to create and export the Anki deck

## Requirements

- Python 3.6 or higher
- `genanki` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/anki-interview-qa.git
    cd anki-interview-qa
    ```

2. Create a virtual environment:

    ```sh
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    - On macOS/Linux:

      ```sh
      source venv/bin/activate
      ```

    - On Windows:

      ```sh
      venv\Scripts\activate
      ```

4. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script to generate the Anki deck:

    ```sh
    python app.py
    ```

2. The script will create an Anki deck file named `interview_questions_deck.apkg` in the project directory.

3. Import the `interview_questions_deck.apkg` file into Anki to start your interview preparation.

## Example Interview Questions

- Tell me about yourself.
- What are your strengths and weaknesses?
- Why do you want to work here?
- What are your career goals?
- Can you describe a challenging situation and how you handled it?
- How do you stay informed about current political events and trends?
- Describe your experience with policy analysis.
- How do you build and maintain relationships with key stakeholders?

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please contact [Jackson Miller](mailto:jackson@civitas.ltd).
