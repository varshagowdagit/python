*** Settings ***
Documentation    to valide login page
Library    SeleniumLibrary

*** Keywords ***
*** Variables ***
*** Test Cases ***
Validate Successful login
    open browser    https://www.tutorialspoint.com/tutorialslibrary.htm  chrome
    sleep   5s
    click link  link=Login
    input text  id=user_email   varsha@gmail.com
    input text  id=user_password  Varsha
    click button    id= user_login
    sleep   5s


