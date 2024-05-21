# ⚡Quick Form Fill
Quick Form Fill is an automation developed in Python that reads a database from an Excel file, opens a browser using Selenium, and automatically registers products. This project aims to save time and reduce errors by automating the product registration form filling process.

## 📑 Table of Contents
- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Technologies Used](#-technologies-used)
- [Project Dependencies](#project-dependencies)
  
## 🚀 Key Features
- **Product Data Reading:** The automation is capable of reading product data from an Excel file. 
- **Browser Initialization:** It initiates a web browser (such as Chrome or Firefox) using Selenium. 
- **Automatic Form Filling:** The automation automatically fills in the fields of a product registration form. 
- **Process Automation:** By automating the form filling process, it saves time and reduces errors, making the process more efficient and reliable. 

## 💡 How It Works
1. **Initial Setup:** The automation utilizes Selenium, a web browser automation tool, and pandas, a Python library for data manipulation, to perform tasks.
2. **Browser Initialization:** Firstly, the script initiates a web browser (Chrome, in this case) using Selenium's webdriver.
3. **Accessing the Page:** The browser navigates to the local URL where the product registration form is hosted `http://localhost:3000/`.
4. **Reading Data:** Product data is read from an Excel file named `data.xlsx` using the pandas library and stored in a DataFrame.
5. **Product Iteration:** For each row in the DataFrame, the script fills in the fields of the product registration form with the corresponding data.
6. **Submitting Data:** After filling the fields with the data for each product, the script submits the registration form.
7. **Completion:** After registering all the products, the browser is closed.

## 💻 Technologies Used
- [**Python:**](https://www.python.org/) A versatile and widely-used programming language known for its simplicity and readability. It's used to develop the automation.
- [**Selenium:**](https://www.selenium.dev/) Utilized for browser automation, enabling interaction with web elements and simulating user actions.
- [**Pandas:**](https://pandas.pydata.org/) Employed for efficient data manipulation, enabling the automation to handle product data from an Excel file within the Python environment.
- [**Excel:**](https://support.microsoft.com/en-us/excel) Product data is stored in an Excel file format, widely-used and accessible for tabular data storage.

## 📝 Installation Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/esperanca-leonardo/quick-form-fill.git
```

### 2. Navigate to the Project Directory
```bash
cd quick-form-fill
```

### 3. Create and activate a virtual environment

- #### 3.1. First, install the virtualenv library
    ```bash
    pip install virtualenv
    ```

- #### 3.2. Then, create a virtual environment named `venv`

  - ##### Linux or macOS
      ```bash
      virtualenv venv
      ```
  
  - ##### Windows
      ```bash
      python -m virtualenv venv
      ```

- #### 3.3. Activate the virtual environment
    
    - ##### Linux or macOS
        ```bash
        source venv/bin/activate
        ```
    
    - ##### Windows
        ```bash
        .\venv\Scripts\activate.bat
        ```

### 4. Install dependencies

Make sure you have Python and pip installed on your system. Then, install the project dependencies using pip

```bash
pip install -r requirements.txt
```

## Project Dependencies
This automation depends on two additional projects:
1. [**Quick Form Fill Backend**](https://github.com/esperanca-leonardo/quick-form-fill-backend)
    - This backend project provides the necessary API endpoints and handles the server-side logic required by the automation.
    - Ensure you follow the installation and setup instructions provided in the `README.md` of the backend repository to get it up and running.

2. **Frontend Project**: [Your Frontend Repository](https://github.com/your-username/frontend-repo)
    - This frontend project provides the user interface where the forms are located and filled by the automation.
    - Ensure the frontend project is properly set up and running according to its documentation.

Ensure both the backend and frontend projects are running and accessible before using the Quick Form Fill automation.


https://github.com/esperanca-leonardo/quick-form-fill/assets/110422838/cadec923-7b1e-4e72-9151-306e85ee9f6d

