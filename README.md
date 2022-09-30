

# TelsaJobAnalyze
* step1：get the telsa job from telsa HR website
* step2：export the job information to the excel files
* step3 : analyze the telsa position trends (not done )

tree -f 

D:.
│  LICENSE
│  README.md
│  requirements.txt
│
├─docs
│      job.json
│
├─logs
│      telsa1664508119.xlsx
│      telsa1664523263.xlsx
│
└─src
        main.py
        parsejobjson.py
        parseurl.py

**start**

`python ./src/main.py`

**output**

  results as below 
* ./logs/telasxxxx.xlsx

* new branch for dev