#!/usr/bin/python3
import sys
import platform
if platform.system() != "Windows":
    sys.exit(platform.system() + "is not supported")

import glob
import os
import win32com.client as win32
import pathlib

from natsort import natsorted


# https://docs.microsoft.com/en-us/office/vba/api/word.wdinformation
wdActiveEndAdjustedPageNumber = 1
wdActiveEndSectionNumber = 2
wdActiveEndPageNumber = 3
wdFirstCharacterLineNumber = 10

comments = []
comments.append((
    "파일명",
    "페이지",
    "행",
    "본문",
    "작성자",
    "의견",
    "완료",
    "작성일시",
))

word = win32.dynamic.Dispatch("Word.Application")
word.Visible = False

for docxfilename in natsorted(glob.glob("*.docx")):
    print(docxfilename)
    filepath = os.path.realpath(docxfilename)
    docx = word.Documents.Open(filepath)
    docx.Activate()
    
    for c in word.ActiveDocument.Comments:
        if c.Ancestor:
            pass
        comments.append((
            docxfilename,
            c.Scope.Information(wdActiveEndPageNumber),
            c.Scope.Information(wdFirstCharacterLineNumber),
            c.Scope.Text,
            c.Author,
            c.Range.Text,
            c.Done,
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

