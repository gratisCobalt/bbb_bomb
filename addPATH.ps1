Function Add-PathVariable {
    param (
        [string]$addPath
    )
    if (Test-Path $addPath){
        $regexAddPath = [regex]::Escape($addPath)
        $arrPath = $env:Path -split ';' | Where-Object {$_ -notMatch 
"^$regexAddPath\\?"}
        $env:Path = ($arrPath + $addPath) -join ';'
    } else {
        Throw "'$addPath' is not a valid path."
    }
}
Invoke-WebRequest -OutFile "./VBCABLE_Driver_Pack43.zip" "https://download.vb-audio.com/Download_CABLE/VBCABLE_Driver_Pack43.zip"
Unzip "./VBCABLE_Driver_Pack43.zip" "./VBCABLE_Driver_Pack43"
Remove-Item "./VBCABLE_Driver_Pack43.zip"
Add-PathVariable($PSScriptRoot + "/chromedriver")