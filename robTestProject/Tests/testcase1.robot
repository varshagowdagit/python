*** Settings ***


*** Keywords ***

*** Variables ***
${My_var}           This is my variable
@{list}             list1   list2   list3
&{DICTIONARY}		username=varsha		password=123

*** Test Cases ***
TC1
    LOG     ${My_var}
TC2
    log     ${list}[1]
TC3
    log     ${DICTIONARY}[username]
    log     ${DICTIONARY}[password]

