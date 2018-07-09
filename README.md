pyCCDA
===================


This is a lightweight Python library for parsing raw C-CDA documents without the need to understand the entire specification. If you're using [BlueButton.js](https://github.com/blue-button/bluebutton.js/) this maintains much of the same functionality. This is a largely unstable build so use at your own risk - we have since ported over to C++ for necessary performance improvements and will release a stable version of that shortly. 

Test documents from various vendors available [here](https://github.com/jmandel/sample_ccdas).

----------


Install
-------------

`pip install pyCCDA`


Example Usage
-----

```python

# example
from pyCCDA import CCDA
with open('CCCD_sample.xml') as f:
   ccd = CCDA(f.read())
   # ccd.type   # The document type ('ccda', 'c32', and such)
   # ccd.source # The parsed source data (XML) with added querying methods
   # ccd.data   # The final parsed document data
name = ccd.data.demographics.name
print name.prefix, name.given, name.family
```

 Library Structure
-----
```
.
├── _init_.py
├── core
│   ├── _core.py
│   ├── _init_.py
│   ├── codes.py
│   ├── wrappers.py
│   └── xml.py
├── documents
│   ├── _init_.py
│   └── ccda.py
└── parsers
    ├── _ccda
    │   ├── allergies.py
    │   ├── care_plan.py
    │   ├── demographics.py
    │   ├── documents(_ccda).py
    │   ├── encounters.py
    │   ├── free_text.py
    │   ├── functional_statuses.py
    │   ├── immunizations.py
    │   ├── instructions.py
    │   ├── medications.py
    │   ├── problems.py
    │   ├── procedures.py
    │   ├── results.py
    │   ├── smoking_status.py
    │   └── vitals.py
    └── ccda.py
```



Available Concepts
-----
```
Parser ... 
Generator ... 
Section ... 
Document ... 
Allergies
Care Plan
Chief Complaint 
Demographics 
Encounters 
Functional Statuses
Immunizations 
Instructions 
Results 
Medications 
Problems 
Procedures 
Smoking 
Status 
Vitals
```
