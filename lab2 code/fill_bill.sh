#!/bin/bash
python3 fill_bill.py
pdftk info.pdf background empty_blank.pdf output filled_blank.pdf
rm -Rf info.pdf
xdg-open filled_blank.pdf
