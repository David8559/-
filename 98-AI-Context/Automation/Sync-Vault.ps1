param([string]$Message = "vault backup: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')")
$ErrorActionPreference = 'Stop'
$Vault = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$Git = (Get-Command git -ErrorAction SilentlyContinue).Source
if (-not $Git) { $Git = 'D:\Git\cmd\git.exe' }
& $Git -C $Vault pull --rebase --autostash origin main
if ($LASTEXITCODE) { throw 'Git pull failed; push aborted.' }
& $Git -C $Vault add --all
$Changes = & $Git -C $Vault status --porcelain
if ($Changes) {
    & $Git -C $Vault commit -m $Message
    if ($LASTEXITCODE) { throw 'Git commit failed.' }
}
& $Git -C $Vault push origin main
if ($LASTEXITCODE) { throw 'Git push failed.' }
Write-Output 'Vault sync complete.'
