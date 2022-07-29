*** Settings ***
Documentation     Robot Framework Example
Library           Selenium2Library

Suite Setup    Open Browser    https://pttplay.cc/    chrome
Suite Teardown    Close Browser

*** Variables ***
${articleName1} =       名偵探柯南
${articleName2} =       名偵探柯南：漆黑的追跡者

*** Test Cases ***
My Test
    [Template]    Search Video Template
    ${articleName1}
    ${articleName2}

*** Keywords ***
Click Search Button
    [Documentation]    Click in search button
    Wait Until Element Is Visible    xpath=/html/body/nav/div/div/div[3]/div[1]/form/button  
    Click Element    xpath=/html/body/nav/div/div/div[3]/div[1]/form/button

Click Search Bar
    [Documentation]    Click in search bar area
    Wait Until Element Is Visible   //*[@id="wd"]   
    Click Element    //*[@id="wd"]
     

Input Search Name
    [Documentation]    Input search content name
    [Arguments]    ${article}
    Wait Until Element Is Visible   //*[@id="wd"]  
    Input Text    //*[@id="wd"]   ${article}
    
Click Video Link
    [Documentation]    Click search submit button in search area
    Wait Until Element Is Visible    xpath=//*[@id="content"]/div[1]/div[1]/a
    Click Element    xpath=//*[@id="content"]/div[1]/div[1]/a


Search Video Template
    [Documentation]    Tempalte for search ithelp video need give video variable
    [Arguments]    ${article}
    Click Search Bar
    Input Search Name    ${article}
    Click Search Button
    Click Video Link
    Verify Video Is Existing    ${article}

Verify Video Is Existing
    [Documentation]    Verify search video is existing
    [Arguments]    ${article}
    Wait Until Page Contains Element    //*[@id="zanpian-score"]/h1   10s
    ${getArticle} =    Get Text    //*[@id="zanpian-score"]/h1
    Should Be Equal As Strings    ${getArticle}    ${article}