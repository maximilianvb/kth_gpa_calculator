# KTH GPA calculator
Automate calculating your KTH GPA.

If you're too lazy to calculate your GPA yourself, just use this Python script and upload a PDF of your grade transcript. Any calculation produced by this program is never to be trusted. Also I have not tested the program with transcripts that are more than 1 page long (It should work though).

Formulas from: https://www.kth.se/en/student/studier/utlandsstudier/utbyte/behorighet-och-urval-for-utbytesstudier-1.1090201
Courses which are only Pass/Failed are ignored because I cannot find how KTH measures those to GPA. 

# How to use:

The PDF can be downloaded in Ladok, this script expects the following parameters for the PDF:
- Official transcript of records:
Define: Courses within selected programme (select your program).
Language: English.
Include: remove all selections.

- Place the pdf and name it 'intyg.pdf' (or change it in the code couldn't be bothered) in the directory of main.py.

- Run main.py and get your GPA

This is an alternative to https://betyg.kottnet.net/kth which requires your password (never give that out). It is also an alternative to just calculating it yourself (takes like 10 min).
