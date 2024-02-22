*** Settings ***
Library     AppiumLibrary

*** Variables ***
${check_enter_value_id}	    com.code2lead.kwad:id/EnterValue
${enter_value}              com.code2lead.kwad:id/Et1
${text}                     varsha
${submit}                   com.code2lead.kwad:id/Btn1
${back}                     //android.widget.ImageButton[@content-desc="Navigate up"]
${login}                    com.code2lead.kwad:id/Login
${enter_email}              com.code2lead.kwad:id/Et4
${email_id}                 admin@gmail.com
${enter_password}           com.code2lead.kwad:id/Et5
${password}                 admin123
${click_login}              com.code2lead.kwad:id/Btn3
${enter_admin}              com.code2lead.kwad:id/Edt_admin
${admin}                    varsha
${admin_submit}             com.code2lead.kwad:id/Btn_admin_sub
*** Test Cases ***
testcase1
    open application    http://localhost:4723/wd/hub    platformName=Android    platformVersion=11    deviceName=emulator-5554    appPackage=com.code2lead.kwad   appActivity=com.code2lead.kwad.MainActivity     automationName=Uiautomator2
testcase2

    wait until page contains element    ${check_enter_value_id}
    click element                       ${check_enter_value_id}
    wait until page contains element    ${enter_value}
    input text                          ${enter_value}           ${text}
testcase3
    click element                       ${submit}
testcase4
    click element                       ${back}
testcase5
    wait until page contains element    ${login}
    click element                       ${login}
testcase6
    wait until page contains element    ${enter_email}
    input text                          ${enter_email}            ${email_id}
    input text                          ${enter_password}         ${password}
    click element                       ${click_login}
testcase7
    wait until page contains element    ${enter_admin}
    input text                          ${enter_admin}            ${admin}
    click element                       ${admin_submit}
#    click element                       ${back}
#    click element                       ${back}
