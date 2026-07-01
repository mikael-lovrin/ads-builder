@echo off
setlocal enabledelayedexpansion

set "SRC=%~dp0skills"
set "DEST=%USERPROFILE%\.claude\skills"

echo Instalando Ads Builder...

if not exist "%SRC%\ads-builder\SKILL.md" (
    echo ERRO: nao encontrei skills\ads-builder\SKILL.md ao lado deste instalador.
    pause
    exit /b 1
)

if not exist "%DEST%" (
    mkdir "%DEST%"
)

for %%S in (ads-builder creative-pattern-analysis knowledge-updater) do (
    if exist "%DEST%\%%S" (
        rmdir /s /q "%DEST%\%%S"
    )
    xcopy "%SRC%\%%S" "%DEST%\%%S" /e /i /y >nul
)

if exist "%DEST%\ads-builder\SKILL.md" (
    echo.
    echo Ads Builder instalado com sucesso!
    echo Skills instaladas: ads-builder, creative-pattern-analysis, knowledge-updater
    echo Crie uma pasta dedicada para cada marca/projeto, abra o Claude Code nela e digite /ads-builder para comecar.
) else (
    echo ERRO: falha ao copiar os arquivos da skill.
)

pause
