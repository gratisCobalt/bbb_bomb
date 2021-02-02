Add-Type -AssemblyName System.IO.Compression.FileSystem
function Unzip
{
    param([string]$zipfile, [string]$outpath)

    [System.IO.Compression.ZipFile]::ExtractToDirectory($zipfile, $outpath)
}
$version = (Invoke-WebRequest -Uri https://chromedriver.storage.googleapis.com/LATEST_RELEASE_87).Content
Invoke-WebRequest -OutFile "./chromedriver_win32.zip" "https://chromedriver.storage.googleapis.com/index.html?path=$version/"
Unzip "./chromedriver_win32.zip" "./chromdriver"
Remove-Item "./chromedriver_win32.zip"