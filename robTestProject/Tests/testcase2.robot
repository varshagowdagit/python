*** Settings ***
Library     BuiltIn

*** Variables ***
&{DICTIONARY}		username=varsha		password=123

*** Keywords ***
log my username
        log  ${DICTIONARY}[username]
log my password
        log  ${DICTIONARY}[password]

log username and password mthd1
	    log  ${DICTIONARY}[username]
	    log  ${DICTIONARY}[password]
log username and password mthd2
    log my username
    log my password

*** Test Cases ***
TC1
    log my username
    log my password

TC2
    log username and password mthd1
TC3
    log username and password mthd2
