# PearMonie Expense and Budgets Tracking App APIs

This is a Django Rest Framework (DRF) application that allows users to manage expenses and budgets. Users can authenticate and perform CRUD operations on their own expenses and budgets.

## Getting Started

### Prerequisites

- Python (>=3.6)
- Pip (Python package installer)
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Olasq-debug/pear-monie.git

2. Change into the project directory:
   ```bash
   cd pear-monie

3. Create a virtual environment (optional but recommended):
   ```bash
   py -m venv venv

4. Activate the virtual environment:

   - On Windows:
     ```bash
        venv\Scripts\activate
    
   - On MacOS/Linux:
        source venv/bin/activate

5. Install dependencies:

   pip install -r requirements.txt

### Database Setup:

    python manage.py migrate

### Create a Superuser:

    python manage.py createsuperuser

### Running the Server:

1. Start the development server:

    python manage.py runserver 8000

    The application will be accessible at http://localhost:8000/.

2. Access the Django admin panel at http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

### API Authentication

1. Obtain an authentication token by sending a POST request to http://localhost:8000/api/token/ with the superuser credentials.

curl -X POST -d "username=your_superuser&password=your_superuser_password" http://localhost:8000/api/token/

### Using the API

1. Make API requests using the obtained token:

    Access the user's expenses: GET http://localhost:8000/api/expenses/ (replace your_token with the actual token).

    curl -H "Authorization: Token your_token" http://localhost:8000/api/expenses/

    Access the user's budgets: GET http://localhost:8000/api/budgets/ (replace your_token with the actual token).

    curl -H "Authorization: Token your_token" http://localhost:8000/api/budgets/







