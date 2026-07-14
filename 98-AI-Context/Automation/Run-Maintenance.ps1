$ErrorActionPreference = 'Stop'
$Python = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $Python) { $Python = 'D:\python\python.exe' }
& $Python (Join-Path $PSScriptRoot 'research_cleaner.py')
if ($LASTEXITCODE) { throw 'Research Cleaner failed.' }
& $Python (Join-Path $PSScriptRoot 'build_code_catalog.py')
if ($LASTEXITCODE) { throw 'Code catalog build failed.' }
& $Python (Join-Path $PSScriptRoot 'knowledge_graph.py')
if ($LASTEXITCODE) { throw 'Knowledge Graph build failed.' }
& $Python (Join-Path $PSScriptRoot 'integrate_code_into_topic_hubs.py')
if ($LASTEXITCODE) { throw 'Code-to-hub integration failed.' }
& $Python (Join-Path $PSScriptRoot 'validate_integrated_code_hubs.py')
if ($LASTEXITCODE) { throw 'Integrated code hub validation failed.' }
& $Python (Join-Path $PSScriptRoot 'kb_audit.py')
if ($LASTEXITCODE) { throw 'Knowledge Base audit failed.' }
