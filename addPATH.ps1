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
$release = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_87"
Invoke-WebRequest -OutFile "./chromedriver_win32.zip" "https://chromedriver.storage.googleapis.com/index.html?path=$release/"
Unzip "./chromedriver_win32.zip" "./chromdriver"
Remove-Item "./chromedriver_win32.zip"
