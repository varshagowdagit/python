*** Settings ***
Library     BuiltIn
Library     BuiltIn
*** Variables ***
&{DICTIONARY1}		username=user1	    password=123
&{DICTIONARY2}		username=user2		password=456

*** Keywords ***
log my specific username
        [Arguments]     ${USERNAME}
        log             ${USERNAME}

log my specific username and password
        [Arguments]     ${USERNAME}     ${PASSWORD}
        log             ${USERNAME}
        log             ${PASSWORD}
*** Test Cases ***
TC1
    log my specific username                ${DICTIONARY2}[username]
    log my specific username and password   ${DICTIONARY1}[username]        ${DICTIONARY1}[password]

