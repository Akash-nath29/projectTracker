# Project Manager using Flask - README 🚀

![GitHub forks](https://img.shields.io/github/forks/Akash-nath29/projectTracker?style=social)
![GitHub stars](https://img.shields.io/github/stars/Akash-nath29/projectTracker?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/Akash-nath29/projectTracker?style=social)
![GitHub repo size](https://img.shields.io/github/repo-size/Akash-nath29/projectTracker)
![GitHub issues](https://img.shields.io/github/issues/Akash-nath29/projectTracker)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Akash-nath29/projectTracker)
![GitHub license](https://img.shields.io/github/license/Akash-nath29/projectTracker)

Welcome to the Project Manager application developed using Flask! This application provides a user-friendly interface for managing projects. You can easily add projects along with their names, descriptions, and participant names, which will be stored in a database for efficient tracking.

## Table of Contents 📑

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation 🛠️

Get started with the Project Manager application locally by following these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Akash-nath29/projectTracker.git
   cd projectTracker
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   or, for cmd
   ```bash
   venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. Run the application:
   ```bash
   flask run
   ```

Access the application through your web browser at `http://127.0.0.1:80`.

## Usage 🚀

Interact with the application through a user-friendly web interface:

- **Add a Project:** Click the "Add Project" button and provide the project name, description, and participant names. Click "Submit" to store the project in the database.

- **View Projects:** The main page lists all projects. You can view project details and participant names.

- **Edit Project:** Update project details by clicking the "Edit" button next to a project.

- **Delete Project:** Remove a project by clicking the "Delete" button next to it.

## Contributing 👥

Contributions are welcome! To contribute:

1. Fork the repository and create a new branch for your feature/fix.

2. Make changes, commit them, and push to your forked repository.

3. Create a pull request to the main project repository.

4. Your contribution will be reviewed and merged upon approval.

## License 📜

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute the code as per the terms of the license.

---

Thanks for using the Project Manager application! If you have questions or encounter issues, please open an issue on the [GitHub repository](https://github.com/Akash-nath29/projectTracker/issues). Happy managing! 🌟