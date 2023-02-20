*** Settings ***
Library  ./Cal.py
Library  ./add.py

*** Variables ***
${MESSAGE}  Hello, world!

*** Variables ***
${arg1}    ${100}

*** Keywords ***
ADD TWO
    [Arguments]    ${input}
    ${v}=  add.add_one_to_integer  ${input}
    ${v}=  Evaluate    ${v} + 1
    Log    cal result: ${v}
    [Return]   ${v}

*** Test Cases ***
Calling function from python
    # 使用 <file_name><dot><function name> 调用方法
    ${value}=  add.add_one_to_integer  ${1}
    Should Be Equal    ${value}   ${2}

Calling function from python module
    [Documentation]  test cal.py inc method
    [Tags]  method
    ${result}=  Cal.add_value  ${arg1}
    Should Be Equal    ${result}  ${101}

Calling from keywords
    ${v}=  ADD TWO    ${100}
    Should Be Equal    ${v}   ${102}

Test Variable
    [Documentation]    test variable
    [Tags]    variable
    Should Be Equal    ${MESSAGE}   Hello, world!
