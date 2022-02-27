#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScripDir%  ; Ensures a consistent starting directory.


<Alt::LCtrl
SC11D::+F5

^Tab::
Send {Alt down}{Tab}
Keywait Control
Send {Alt up}
return


/*h:: ; KeyHistory 실행 단축키 :

KeyHistory

return
esc::exitapp ; 종료 : esc*/