# Observe+

![GitHub](https://img.shields.io/github/license/vijay9908/Observe_Plus)
![GitHub last commit](https://img.shields.io/github/last-commit/vijay9908/Observe_Plus)

#### A video positioning tool with for varied applications.

The following are the documentation prepared with all the development steps followed in each phase. 

[Project abstract](https://docs.google.com/document/d/19zJ_vhUqpcnr4rFXrMF0_B0vo8KWHMm8xhgTVgO4eAE/edit?usp=sharing)

[Mock WireFrame](https://app.uizard.io/p/6f611e4c)


#### 🛠 How to Run Locally & Develop ?
1. Install [Python](https://www.python.org/downloads/) and [Pipenv](https://pypi.org/project/pipenv/).
   If you had installed python and Pipenv previously, No need to re-install again.
2. Clone this repository and rename the folder as per your requirement.

  Your directory structure should appear as follows;
  ```structure
  Observe+
      ├── pipfile
      ├── app.py
      ├── source
      └── requirements.txt
  ```
3. Installing **Requirements** is important. **(in root)**
   for Mac Users,
  ```requirements1
    python -m pip install -r requirements.txt 
  ```
  for Linux Users,
  ```requirements1
    pip install -r requirements.txt 
  ```
4. Navigate to **system/settings.py**, Change the Secret-key to your own project key and set Debug = True;
5. To run the server, Inside root use the command;
  ```
    flask run
  ```
  For help with commands, Use the following;
  ```
    flask --help
  ```
6. Access the client at localhost **(http://127.0.0.1:5000/)**
 Use the follow to run the application in Debug mode.
 ```
   FLASK_DEBUG=1 flask run
 ```

Check the #app.py for accessable urls

