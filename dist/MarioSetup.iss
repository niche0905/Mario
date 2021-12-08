; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{CF669AEB-4930-4BC0-AC6F-F98EFB1E75BB}
AppName=Mario
AppVersion=1.0
;AppVerName=Mario 1.0
AppPublisher=It's Me!
AppPublisherURL=https://www.kpu.ac.kr
AppSupportURL=https://www.kpu.ac.kr
AppUpdatesURL=https://www.kpu.ac.kr
DefaultDirName={autopf}\Mario
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputBaseFilename=MarioCopySetup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\User\Documents\GitHub\Mario\dist\mygame.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\GitHub\Mario\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\Mario"; Filename: "{app}\mygame.exe"
Name: "{autodesktop}\Mario"; Filename: "{app}\mygame.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\mygame.exe"; Description: "{cm:LaunchProgram,Mario}"; Flags: nowait postinstall skipifsilent

