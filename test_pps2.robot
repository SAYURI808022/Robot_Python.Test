*** Settings ***
Library    Collections
Library    String
Library    Selenium2Library
Library    requestdata.py
Variables  requestdata.py

Suite Setup    Open Browser    https://tw.portal-pokemon.com/cardmap/map?cl=1   chrome
Suite Teardown    Close Browser

*** Variables ***

${article} =       萊爾富大里光正店

*** Keywords *** 

webdata_fromrequests  
    ${result}=  requestdata
    [return]  ${result}

*** Test Cases ***

Click Search Bar
    Wait Until Element Is Visible    //*[@id="map-wrapper"]/div[2]/div/div[1]/div/form/div/input
    Click Element    //*[@id="map-wrapper"]/div[2]/div/div[1]/div/form/div/input


Input Search Store_Name
    [Arguments]    ${article}
    Wait Until Element Is Visible    //*[@id="map-wrapper"]/div[2]/div/div[1]/div/form/div/input
    Input Text       //*[@id="map-wrapper"]/div[2]/div/div[1]/div/form/div/input   ${article}


Click Store_Name Options
    Wait Until Element Is Visible   //*[@id="map-wrapper"]/div[2]/div/div[1]/div/div[1]/ul/li[2]
    Click Element    //*[@id="map-wrapper"]/div[2]/div/div[1]/div/div[1]/ul/li[2]



Click Search Button
    Wait Until Element Is Visible   //*[@id="map-wrapper"]/div[2]/div/div[1]/div/form/div/div[1]
    Click Element    //*[@id="map-wrapper"]/div[2]/div/div[1]/div/form/div/div[1]


Verify Store_Name Is Existing  
    ${value}  webdata_fromrequests
    Log  ${value}
    Wait Until Page Contains Element   //*[@id="map-wrapper"]/div[2]/div/div[2]/div[2]/ul/li[1]/div/div[1]
    ${getarticle} =    Get Text    //*[@id="map-wrapper"]/div[2]/div/div[2]/div[2]/ul/li/div/div[1]
    Should Be Equal As Strings    ${getarticle}   ${value}

