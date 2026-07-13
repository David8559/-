param([switch]$Promote)
$ErrorActionPreference = 'Stop'
$Python = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $Python) { $Python = 'D:\python\python.exe' }
$Args = @((Join-Path $PSScriptRoot 'research_cleaner.py'))
if ($Promote) { $Args += '--promote' }
& $Python @Args
exit $LASTEXITCODE
