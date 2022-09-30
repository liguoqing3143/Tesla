

# TelsaJobAnalyze
* step1：get the telsa job from telsa HR website
* step2：export the job information to the excel files
* step3 : analyze the telsa position trends (not done )

tree -f 

D:.
│  LICENSE
│  README.md
│  requirements.txt
│  t.txt
│  
├─docs
│      guide.md
│      job.json
│      
├─logs
│      telsa1664508119.xlsx
│      telsa1664523263.xlsx
│      
└─src
    │  main.py
    │  parsejobjson.py
    │  parseurl.py
    │  
    ├─test
    │      test.py
    │      titleregualar.py
    │      
    └─__pycache__
            parsejobjson.cpython-310.pyc
            parseurl.cpython-310.pyc

**start**

`python ./src/main.py`

**output**

  results as below 
* ./logs/telasxxxx.xlsx

