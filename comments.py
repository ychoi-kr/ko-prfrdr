#!/usr/bin/python3
import sys
import platform
if platform.system() != "Windows":
    sys.exit(platform.system() + "is not supported")

import os
import win32com.client as win32
import pathlib


docxfilename = sys.argv[1]

word = win32.dynamic.Dispatch("Word.Application")
word.Visible = False
filepath = os.path.realpath(docxfilename)

if not os.path.exists(filepath):
    sys.exit(filepath + " is not exists!")

docx = word.Documents.Open(filepath)
docx.Activate()

comments = []
comments.append((
    "파일명",
    "작성자",
    "페이지",
    "행",
    "본문",
    "의견",
    "작성일시",
))

# https://docs.microsoft.com/en-us/office/vba/api/word.wdinformation
wdActiveEndAdjustedPageNumber = 1
wdActiveEndSectionNumber = 2
wdActiveEndPageNumber = 3
wdFirstCharacterLineNumber = 10

for c in word.ActiveDocument.Comments:
    if c.Ancestor:
        pass
    comments.append((
        docxfilename,
        c.Author,
        c.Scope.Information(wdActiveEndPageNumber),
        c.Scope.Information(wdFirstCharacterLineNumber),
        c.Scope.Text,
        c.Range.Text,
        c.Date
    ))

docx.Close()

excel = win32.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Add()
ws = wb.Worksheets("sheet1")
for i, row in enumerate(comments, start=1):
    for j, v in enumerate(row, start=1):
        ws.cells(i, j).Value = v

