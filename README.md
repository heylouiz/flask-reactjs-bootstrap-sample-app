## Synopsis

This is a simple app that uses Flask, ReactJS and Bootstrap.


## Motivation

The goal of this project is to have a start point to similar projects.

## Installation

Clone the repository and "cd" to it:
```
git clone https://github.com/heylouiz/flask-reactjs-bootstrap-sample-app.git
cd flask-reactjs-bootstrap-sample-app # Damn, thats a big name
```

Optionally create and source a virtualenv:
```
virtualenv venv
source venv/bin/activate
```

Install the Python requirements:
```
pip install -r requirements.txt
```

Install npm (command for debian based distros):
```
sudo apt-get install npm nodejs nodejs-legacy
```

Intall the Javascript requirements:
```
cd interface
npm install
```

Build the jsx files, the project have a few Makefile targets for this:
```
make build # Run this command at the root directory of the project
```

Run the project:
```
./bin/sample_app 
```

Open (http://localhost:8080) in your browser and you should see a hello world page.


## License

MIT License

