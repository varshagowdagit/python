*** Settings ***
*** Variables ***
*** Test Cases ***
testcase1
    [Documentation]         This is some info abt test
    [tags]                  101
    open browser            https://www.youtube.com/results?search_query=robot+framework+with+python        firefox
    Set selenium speed      .2s
    Set selenium timeout    10s
    log                     sample testcase
    sleep                   5s
    close browser
*** Keywords ***
