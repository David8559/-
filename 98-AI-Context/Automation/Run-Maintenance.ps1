$ErrorActionPreference = 'Stop'
$Python = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $Python) { $Python = 'D:\python\python.exe' }
& $Python (Join-Path $PSScriptRoot 'research_cleaner.py')
if ($LASTEXITCODE) { throw 'Research Cleaner failed.' }
& $Python (Join-Path $PSScriptRoot 'knowledge_graph.py')
if ($LASTEXITCODE) { throw 'Knowledge Graph build failed.' }
& $Python (Join-Path $PSScriptRoot 'kb_audit.py')
if ($LASTEXITCODE) { throw 'Knowledge Base audit failed.' }
