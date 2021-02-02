Add-Type -AssemblyName System.IO.Compression.FileSystem
function Unzip
{
    param([string]$zipfile, [string]$outpath)

    [System.IO.Compression.ZipFile]::ExtractToDirectory($zipfile, $outpath)
}
Invoke-WebRequest -OutFile "./VBCABLE_Driver_Pack43.zip" "https://download.vb-audio.com/Download_CABLE/VBCABLE_Driver_Pack43.zip"
Unzip "./VBCABLE_Driver_Pack43.zip" "./VBCABLE_Driver_Pack43"
Remove-Item "./VBCABLE_Driver_Pack43.zip"