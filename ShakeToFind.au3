;https://spinalcode.co.uk/2018/11/06/windows-shake-to-find-cursor/
#Region ;**** Directives created by AutoIt3Wrapper_GUI ****
#AutoIt3Wrapper_Compression=5   ;default 3
#AutoIt3Wrapper_UseUpx=n
#EndRegion ;**** Directives created by AutoIt3Wrapper_GUI ****

#include <TrayConstants.au3> ; Required for the $TRAY_ICONSTATE_SHOW constant.
#include <WindowsConstants.au3>
#Include <WinAPI.au3>
#include <GDIPlus.au3>

$gesture1 = "46464"
$gesture2 = "19191"
$gesture3 = "73737"
$gesture4 = "28282"
$gesture5 = "64646"
$gesture6 = "91919"
$gesture7 = "37373"
$gesture8 = "82828"

Global Const $AC_SRC_ALPHA = 1

global $oldMX, $oldMY, $curMx, $curMY, $distX, $distY, $distPix
global $DPI = 144 ; my laptop is 144dpi
global $showing = 0

;HotKeySet("{END}", "_Quit") ; Hit "END" to quit

   $avMousePos = MouseGetPos()
   $win_mate = GUICreate('test', 64, 64, $avMousePos[0], $avMousePos[1], $WS_POPUP, BitOR($WS_EX_LAYERED, $WS_EX_TOOLWINDOW))
   WinSetOnTop($win_mate, '', 1)

   _GDIPlus_Startup()
   $g_hImage = _GDIPlus_BitmapCreateFromMemory(_Torus())

   GUISetState(@SW_SHOW)

_createTray()

; timer for mouse tracking
Global $TIMER = TimerInit()
Global $TIMEOUT = 100; 1 second = 1000

Global $animTIMER = TimerInit()
Global $animTIMEOUT = 10; 1 second = 1000

Global $MouseSizeX = 12
Global $MouseSizeY = 19
Global $direction = 0
Global $oldDirection = 0
Global $dirChangeCount = 0
Global $xAxis
Global $yAxis
Global $xAxisOld
Global $yAxisOld
Global $shakeCount = 0

   $avMousePos = MouseGetPos()
   $curMX = $avMousePos[0]
   $curMY = $avMousePos[1]

Global Const $pi = 3.14159265358979
$current = ""
$direction = ""
Global $pos_old
Global $pos_new
$debug = False


While 1

   $avMousePos = MouseGetPos()

   If TimerDiff($animTIMER) >= $animTIMEOUT Then
      $animTIMER = TimerInit()
   If $showing = 0 then
      $hWnd = WinGetHandle($win_mate)
      DllCall("user32.dll" , "int" , "ShowCursor","int",True)

   EndIf

     if $showing = 1 Then
         WinMove($win_mate, "", $avMousePos[0], $avMousePos[1])
         ; hid cursor from pointer image!
         $hWnd = WinGetHandle($win_mate)
         DllCall("user32.dll" , "int" , "ShowCursor","int",False)

       Local $iCursor = MouseGetCursor()

      if $MouseSizeX > 12 then
         $MouseSizeX = $MouseSizeX *.95
         $MouseSizeY = $MouseSizeY *.95

         ;Create New image
         $GC = _GDIPlus_ImageGetGraphicsContext($g_hImage)
         $newBmp = _GDIPlus_BitmapCreateFromGraphics($MouseSizeX, $MouseSizeY,$GC)
         $newGC = _GDIPlus_ImageResize($g_hImage, $MouseSizeX, $MouseSizeY) ;resize image
         ;Draw
         _GDIPlus_GraphicsDrawImageRect($newGC,$g_hImage,0,0,$MouseSizeX, $MouseSizeY)

         SetBitmap($win_mate, $newGC, 255, $MouseSizeX, $MouseSizeY)

         ;Clenaup
         _GDIPlus_GraphicsDispose($GC)
         _GDIPlus_GraphicsDispose($newGC)
         _GDIPlus_BitmapDispose($newBmp)
      else
         SetBitmap($win_mate, $g_hImage, 0, 12, 19)
         $showing = 0
      endif

     endif

   endif

   If TimerDiff($TIMER) >= $TIMEOUT Then


    $TIMER = TimerInit()
    $oldMX = $curMX
    $oldMY = $curMY
    $curMX = $avMousePos[1]
    $curMY = $avMousePos[0]


     $distX = abs($curMX - $oldMX) * abs($curMX - $oldMX)
     $distY = abs($curMY - $oldMY) * abs($curMY - $oldMY)
     local $curDist = int(Sqrt($distX + $distY))
     $distPix = $distPix + $curDist
     TraySetToolTip(round(($distPix / $DPI)/63360, 4) & " miles") ; tray icon tooltip

   if $curDist > 150 then
      $a = GetAnglePO($curMY - $oldMY, $curMX - $oldMX) * 57.2957795130823
      Select
         Case $a >= 337.5 or $a < 22.5
            $direction = "6"
         Case $a >= 22.5 and $a < 67.5
            $direction = "3"
         Case $a >= 67.5 and $a < 112.5
            $direction = "2"
         Case $a >= 112.5 and $a < 157.5
            $direction = "1"
         Case $a >= 157.5 and $a < 202.5
            $direction = "4"
         Case $a >= 202.5 and $a < 247.5
            $direction = "7"
         Case $a >= 247.5 and $a < 292.5
            $direction = "8"
         Case $a >= 292.5 and $a < 337.5
            $direction = "9"
      EndSelect
      If $direction <> StringRight($current, 1) Then $current &= $direction
   endif

   If $debug Then ToolTip("Current:" & @TAB & $current & @CRLF & "Direction:" & @TAB & $direction)

   If StringInStr($current, $gesture1) or StringInStr($current, $gesture2) or StringInStr($current, $gesture3) or StringInStr($current, $gesture4) or StringInStr($current, $gesture5) or StringInStr($current, $gesture6) or StringInStr($current, $gesture7) or StringInStr($current, $gesture8) Then
      $MouseSizeX = 167
      $MouseSizeY = 251
       SetBitmap($win_mate, $g_hImage, 255, $MouseSizeX, $MouseSizeY)
       $showing = 1
      $current = ""
   EndIf



;     if $curDist > 250 Then
;	if ($xShake or $yShake) and $curDist > 250 then
;		$MouseSizeX = 167
;		$MouseSizeY = 251
 ;      SetBitmap($win_mate, $g_hImage, 255, $MouseSizeX, $MouseSizeY)
  ;     $showing = 1
  ;   EndIf

   EndIf


   Switch TrayGetMsg()
     Case $idWebLink ; jump to spinalcode.co.uk
     ShellExecute("www.spinalcode.co.uk")

     Case $idAbout ; Display a message box
       MsgBox($MB_SYSTEMMODAL, "BigMouse", "BigMouse" & @CRLF & "By Spinal Cord" & @CRLF & "Many thinks to 'Dan' at Socoder.net" & @CRLF & "and 'UEZ' at outoitscript.com/forum")

     Case $idExit ; Exit the loop.
       ExitLoop
       _Quit()
   EndSwitch

WEnd


func _createTray ()

   Opt("TrayMenuMode", 3) ; The default tray menu items will not be shown and items are not checked when selected. These are options 1 and 2 for TrayMenuMode.

   global $idWebLink = TrayCreateItem("SpinalCode.co.uk")

   global $idAbout = TrayCreateItem("About")
   TrayCreateItem("") ; Create a separator line.
   global $idExit = TrayCreateItem("Exit")

   TraySetState($TRAY_ICONSTATE_SHOW) ; Show the tray menu.
   TraySetToolTip("BigMouse") ; tray icon tooltip

   Global $hBmp = _GDIPlus_BitmapCreateFromMemory(_AutoIt_Icon()) ;load ico and convert it to a GDI+ bitmap
   ;convert bitmap to HIcon
   Global $hIcon = _GDIPlus_HICONCreateFromBitmap($hBmp)
   _WinAPI_TraySetHIcon($hIcon)

EndFunc

Func _Quit()
   _GDIPlus_ShutDown()
   Exit
EndFunc   ;==>_Quit

; ===============================================================================================================================
; SetBitMap
; ===============================================================================================================================
Func SetBitmap($hGUI, $hImage, $iOpacity, $mx, $my)
   Local $hScrDC, $hMemDC, $hBitmap, $hOld, $pSize, $tSize, $pSource, $tSource, $pBlend, $tBlend

   $hScrDC = _WinAPI_GetDC(0)
   $hMemDC = _WinAPI_CreateCompatibleDC($hScrDC)

   $hBitmap = _GDIPlus_BitmapCreateHBITMAPFromBitmap($hImage)



   $hOld = _WinAPI_SelectObject($hMemDC, $hBitmap)

   $tSize = DllStructCreate($tagSIZE)
   $pSize = DllStructGetPtr($tSize)
   DllStructSetData($tSize, "X", $mx);_GDIPlus_ImageGetWidth($hImage))
   DllStructSetData($tSize, "Y", $my);_GDIPlus_ImageGetHeight($hImage))

   $tSource = DllStructCreate($tagPOINT)
   $pSource = DllStructGetPtr($tSource)
   $tBlend = DllStructCreate($tagBLENDFUNCTION)
   $pBlend = DllStructGetPtr($tBlend)
   DllStructSetData($tBlend, "Alpha", $iOpacity)
   DllStructSetData($tBlend, "Format", $AC_SRC_ALPHA)

   _WinAPI_UpdateLayeredWindow($hGUI, $hScrDC, 0, $pSize, $hMemDC, $pSource, 0, $pBlend, $ULW_ALPHA)

   _WinAPI_ReleaseDC(0, $hScrDC)
   _WinAPI_SelectObject($hMemDC, $hOld)
   _WinAPI_DeleteObject($hBitmap)
   _WinAPI_DeleteDC($hMemDC)
EndFunc   ;==>SetBitmap


; https://www.autoitscript.com/forum/topic/134350-file-to-base64-string-code-generator-v120-build-2015-01-20-embed-your-files-easily/

Func _WinAPI_TraySetHIcon($hIcon) ;function by Mat
    Local Const $tagNOTIFYICONDATA = _
                    "dword Size;" & _
                    "hwnd Wnd;" & _
                    "uint ID;" & _
                    "uint Flags;" & _
                    "uint CallbackMessage;" & _
                    "ptr Icon;" & _
                    "wchar Tip[128];" & _
                    "dword State;" & _
                    "dword StateMask;" & _
                    "wchar Info[256];" & _
                    "uint Timeout;" & _
                    "wchar InfoTitle[64];" & _
                    "dword InfoFlags;" & _
                    "dword Data1;word Data2;word Data3;byte Data4[8];" & _
                    "ptr BalloonIcon"
    Local Const $TRAY_ICON_GUI = WinGetHandle(AutoItWinGetTitle()), $NIM_ADD = 0, $NIM_MODIFY = 1, $NIF_MESSAGE = 1, $NIF_ICON = 2, $AUT_WM_NOTIFYICON = $WM_USER + 1, $AUT_NOTIFY_ICON_ID = 1
    Local $tNOTIFY = DllStructCreate($tagNOTIFYICONDATA)
    DllStructSetData($tNOTIFY, "Size", DllStructGetSize($tNOTIFY))
    DllStructSetData($tNOTIFY, "Wnd", $TRAY_ICON_GUI)
    DllStructSetData($tNOTIFY, "ID", $AUT_NOTIFY_ICON_ID)
    DllStructSetData($tNOTIFY, "Icon", $hIcon)
    DllStructSetData($tNOTIFY, "Flags", BitOR($NIF_ICON, $NIF_MESSAGE))
    DllStructSetData($tNOTIFY, "CallbackMessage", $AUT_WM_NOTIFYICON)
    Local $aRet = DllCall("shell32.dll", "int", "Shell_NotifyIconW", "dword", $NIM_MODIFY, "ptr", DllStructGetPtr($tNOTIFY))
    If (@error) Then Return SetError(1, 0, 0)
    Return $aRet[0] <> 0
EndFunc   ;==>_Tray_SetHIcon

Func _AutoIt_Icon($bSaveBinary = False, $sSavePath = @ScriptDir)
    Local $AutoIt_Icon
   $AutoIt_Icon &= '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'
   Local $bString = Binary(_WinAPI_Base64Decode($AutoIt_Icon))
    If $bSaveBinary Then
        Local $hFile = FileOpen($sSavePath & "\AutoIt.ico", 18)
        FileWrite($hFile, $bString)
        FileClose($hFile)
    EndIf
    Return  $bString
 EndFunc   ;==>_AutoIt_Icon


Func _WinAPI_DisplayTransparentBitmapInGUI($hHBitmap, $hGUI, $iOpacity = 0xFF)
    If Not BitAND(GUIGetStyle($hGUI)[1], $WS_EX_LAYERED) = $WS_EX_LAYERED Then Return SetError(1, 0, 0)
    Local Const $hScrDC = _WinAPI_GetDC(0), $hMemDC = _WinAPI_CreateCompatibleDC($hScrDC), $hOld = _WinAPI_SelectObject($hMemDC, $hHBitmap)
    Local $tSize = DllStructCreate($tagSIZE)
    $tSize.X = $iW
    $tSize.Y = $iH
    Local $tSource = DllStructCreate($tagPOINT)
    Local $tBlend = DllStructCreate($tagBLENDFUNCTION)
    $tBlend.Alpha = $iOpacity
    $tBlend.Format = 1
    _WinAPI_UpdateLayeredWindow($hGUI, $hScrDC, 0, DllStructGetPtr($tSize), $hMemDC, DllStructGetPtr($tSource), 0, DllStructGetPtr($tBlend), $ULW_ALPHA)
    _WinAPI_ReleaseDC(0, $hScrDC)
    _WinAPI_SelectObject($hMemDC, $hOld)
    _WinAPI_DeleteObject($hHBitmap)
    _WinAPI_DeleteDC($hMemDC)
    Return True
EndFunc

;Code below was generated by: 'File to Base64 String' Code Generator v1.19 Build 2014-11-14

Func _Torus($bSaveBinary = False, $sSavePath = @ScriptDir)
   local $Pointer
   $Pointer &= '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'


    Local $bString = Binary(_WinAPI_Base64Decode($Pointer))
    If $bSaveBinary Then
        Local $hFile = FileOpen($sSavePath & "\Pointer.png", 18)
        FileWrite($hFile, $bString)
        FileClose($hFile)
    EndIf
    Return  $bString
EndFunc   ;==>_Torus

Func _WinAPI_Base64Decode($sB64String)
    Local $aCrypt = DllCall("Crypt32.dll", "bool", "CryptStringToBinaryA", "str", $sB64String, "dword", 0, "dword", 1, "ptr", 0, "dword*", 0, "ptr", 0, "ptr", 0)
    If @error Or Not $aCrypt[0] Then Return SetError(1, 0, "")
    Local $bBuffer = DllStructCreate("byte[" & $aCrypt[5] & "]")
    $aCrypt = DllCall("Crypt32.dll", "bool", "CryptStringToBinaryA", "str", $sB64String, "dword", 0, "dword", 1, "struct*", $bBuffer, "dword*", $aCrypt[5], "ptr", 0, "ptr", 0)
    If @error Or Not $aCrypt[0] Then Return SetError(2, 0, "")
    Return DllStructGetData($bBuffer, 1)
EndFunc   ;==>_WinAPI_Base64Decode

Func GetAnglePO( $x, $y )   ;by blindwig
   Select
      Case $x > 0
         If $y >= 0 Then
            Return ATan($y / $x)
         Else
            Return ATan($y / $x) + 2 * $pi
         EndIf
      Case $x = 0
         If $y = 0 Then
            Return 0
         ElseIf $y > 0 Then
            Return $pi / 2
         Else
            Return 3 * $pi / 2
         EndIf
      Case $x < 0
         Return ATan($y / $x) + $pi
   EndSelect
EndFunc