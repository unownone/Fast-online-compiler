# Fast-Compiler
[![Build and publish](https://github.com/unownone/Fast-online-compiler/actions/workflows/docker-image.yml/badge.svg)](https://github.com/unownone/Fast-online-compiler/actions/workflows/docker-image.yml)
[![Test](https://github.com/unownone/Fast-online-compiler/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/unownone/Fast-online-compiler/actions/workflows/test.yml)
# Demo:
### [Hosted at DigitalOcean](http://139.59.52.61/)
<a href="https://youtu.be/eZSkH8Ox26k" title="Fast Compiler">
  <p align="center">
    <img width="100%" src="https://i.ytimg.com/vi/eZSkH8Ox26k/mqdefault.jpg" alt="Fast compiler Demo"/>
  </p>
</a>


## Compile code fast on the cloud! 

## Language Support Currently: 
- Python
- C++
- C
- Java
- More coming soon!

## Feature RoadMap
- Add Languages:
  - Go
  - Javascript
  - C#
  - Swift
- Add Login/Signup:
  - Based on API keys
  - generate API keys to use on multi platforms
  - Store Code.
- Multi Platform Integration:
  - Add GDrive Integration to store code in GDrive
  - Add OneDrive Integration to store code in OneDrive
  - Add telegram integration to compile code from telegram
- More!!

## API End Points:
- ```
    /api/getLangs
    ```
    - Type : ```GET```
    - Args : ```None```
    - Returns : ```list[strings]```

- ```
    /api/compile
    ```
    - Type : ```POST```
    - body :
        - lang : ```string``` 
        - code : ```string```
        - args : ```string``` [optional]
    - Returns : ```{ response: String }```

or

## [Use Front End](http://139.59.52.61/) : 
    at index : \
![compile](./demos/demo.gif)

# Setup on Local:

## Using Docker :
``` 
    docker-compose up -d --build 
```
    Server will be running at localhost:80    
## Using VirtualEnv :
```
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python wsgi.py
```
    Server will be running at localhost:5000
    
    - Set up languages for proper compilation/running
