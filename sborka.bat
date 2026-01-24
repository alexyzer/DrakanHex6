cd "../"
md "./Sborka"
xcopy "./DrakanHex6" "./Sborka" /E /I /H /Y
cd "./Sborka"
java -jar packwiz-installer-bootstrap.jar https://raw.githubusercontent.com/alexyzer/DrakanHex6/client/pack.toml -bootstrap-no-update
tar -cf archive.zip "config/*" "datapacks/*" "kubejs/*" "mods/*" "resourcepacks/*" "packwiz-installer.jar" "packwiz-installer-bootstrap.jar" "Updata.bat"
move "./archive.zip" ".././DrakanHex6"
rd /s /q "./Sborka"