# Working with Virtual Environments in This Repository  

## 1. Creating a Virtual Environment  
Each project in this repository should use its own virtual environment to manage dependencies.  
Navigate to the project's root folder and run:  
```sh
python -m venv venv
```

## 2. Activating the Virtual Environment  
- **Windows (CMD/PowerShell)**:  
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux**:  
  ```sh
  source venv/bin/activate
  ```

## 3. Installing Dependencies  
Once the virtual environment is activated, install the required dependencies:  
```sh
pip install -r requirements.txt
```

## 4. Deactivating the Virtual Environment  
When finished, deactivate the environment with:  
```sh
deactivate
```

## 5. Keeping Dependencies Updated  
If you install new packages, update `requirements.txt` before pushing changes:  
```sh
pip freeze > requirements.txt
```

> **Note:** Virtual environments should not be committed to the repository. The `.gitignore` file is already configured to exclude them.  
