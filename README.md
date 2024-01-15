# fastapi postgresql todo api

This is a simple Todo application built with FastAPI, SQLAlchemy, and Streamlit. It also includes a console client written in Python and Node.js.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- Node.js 14+
- pip
- npm

### Installing

- Create a virtual python environment (optional)

```console
python -m venv myenv
```

1. Clone the repository:

```console
git clone https://github.com/Umar-Waseem/fastapi-postgres-todo-api
```

2. Install Python dependencies:

```console
pip install -r requirements.txt
```

3. Install Node.js dependencies:

```console
npm install
```

4. Create a `.env` file in the root directory of the project and add the following environment variables:

```env
POSTGRES_URL=
```

5. Run the application:

```console
uvicorn app.main:app --reload
```

6. Open the application in your browser:

```console
streamlit run streamlit_client.py     
```

7. Running Tests

```console
pytest test_api.py
```
