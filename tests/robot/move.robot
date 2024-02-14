***Settings***
Documentation   I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template   Move character
Library         MoveLibrary.py

*** Test Cases ****     StartingX   StartingY   Direction   EndingX     EndingY   
Test Case1              9           0           N           9           1
Test Case2              9           0           S           9           0
Test Case3              9           0           E           9           0
Test Case4              9           0           W           8           0
Test Case5              0           0           N           0           1
Test Case6              0           0           S           0           0
Test Case7              0           0           E           1           0
Test Case8              0           0           W           0           0
Test Case9              0           9           N           0           9
Test Case10             0           9           S           0           8
Test Case11             0           9           E           1           0
Test Case12             0           9           W           0           9
Test Case13             9           9           N           9           9
Test Case14             9           9           S           9           8
Test Case15             9           9           E           9           9
Test Case16             9           9           W           8           9
Test Case17             5           5           N           5           6
Test Case18             5           5           S           5           4
Test Case19             5           5           E           6           5
Test Case20             5           5           W           4           5



*** Keywords ***
Move character
    [Arguments] ${startingX}    ${startingY}    ${direction}    ${endingX}  ${endingY}
    Initialize character xposition with ${startingX}
    Initialize character yposition with ${startingY}
    Move in direction                   ${direction}
    Character xposition should be       ${endingX}
    Character yposition should be       ${endingY}

