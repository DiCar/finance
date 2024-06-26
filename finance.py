# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:36:38 2024

@author: pauld
"""

import sys
import yfinance as yf
import pandas as pd
from qtpy.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class StockApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Analysis")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.table = QTableWidget()
        layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.load_data()

    def load_data(self):
        stock = yf.Ticker("AAPL")
        hist = stock.history(period="1y")
        hist.reset_index(inplace=True)
        
        self.table.setRowCount(len(hist))
        self.table.setColumnCount(len(hist.columns))
        self.table.setHorizontalHeaderLabels(hist.columns)

        for i, row in hist.iterrows():
            for j, col in enumerate(hist.columns):
                self.table.setItem(i, j, QTableWidgetItem(str(row[col])))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = StockApp()
    mainWin.show()
    sys.exit(app.exec_())
