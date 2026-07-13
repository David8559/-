param(
    [Parameter(Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string]$Name
)

$ErrorActionPreference = 'Stop'
$Vault = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$Invalid = [System.IO.Path]::GetInvalidFileNameChars()
if ($Name.IndexOfAny($Invalid) -ge 0 -or $Name -in '.', '..', 'Project Status') {
    throw 'Invalid project name.'
}

$Project = Join-Path (Join-Path $Vault '06-Projects') $Name
if (Test-Path -LiteralPath $Project) {
    throw "Project already exists: $Project"
}

$null = New-Item -ItemType Directory -Path $Project
$null = New-Item -ItemType Directory -Path (Join-Path $Project 'Code')
$null = New-Item -ItemType Directory -Path (Join-Path $Project 'Data')
$null = New-Item -ItemType Directory -Path (Join-Path $Project 'Paper')
$Date = Get-Date -Format 'yyyy-MM-dd'
$Status = @"
---
type: project-status
project: "$Name"
status: active
updated: "$Date"
tags: [project/status]
---

# $Name — Project Status

## 当前状态

项目已创建，等待定义验收标准。

## 已完成事项

- [x] 创建标准项目目录

## 待办事项

- [ ] 定义问题、数据、模型和交付标准

## 下一步

填写项目目标与验收标准。

## 风险

| 风险 | 可能性 | 影响 | 应对 |
|---|---:|---:|---|

## 决策

| 日期 | 决策 | 理由 | 影响 |
|---|---|---|---|
"@
$ProjectHome = @"
---
type: project-home
status: active
created: "$Date"
tags: [project/active]
---

# $Name

- 状态：[[Project-Status]]
- 代码：`Code/`
- 数据：`Data/`
- 论文：`Paper/`

## 目标与验收标准

## 复现方式
"@
[IO.File]::WriteAllText((Join-Path $Project 'Project-Status.md'), $Status, [Text.UTF8Encoding]::new($false))
[IO.File]::WriteAllText((Join-Path $Project 'Readme.md'), $ProjectHome, [Text.UTF8Encoding]::new($false))
$SectionReadmes = @{
    Code = "# Code`n`n保存可复现的 Python、MATLAB 与运行说明。`n"
    Data = "# Data`n`n保存源数据、处理中间数据及字段说明。`n"
    Paper = "# Paper`n`n保存论文正文、图表、参考文献与提交版本。`n"
}
foreach ($Section in $SectionReadmes.GetEnumerator()) {
    [IO.File]::WriteAllText((Join-Path (Join-Path $Project $Section.Key) 'Readme.md'), $Section.Value, [Text.UTF8Encoding]::new($false))
}
Write-Output "Created project: $Project"
