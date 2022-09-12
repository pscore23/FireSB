Param(
    $SaveName,
    $RenameName,
    $DeleteName
)

Stop-Process -Name $DeleteName -Force
Remove-Item -Path $DeleteName
Rename-Item -Path $SaveName -NewName $RenameName
