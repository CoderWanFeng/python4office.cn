#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Excel数据筛选工具
功能：根据指定条件筛选Excel数据，支持多种筛选条件和自定义输出
"""

import sys
import os
import pandas as pd
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox
from PySide6.QtCore import QTimer, Qt

# 添加父目录到路径，以便导入common模块
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.ui_base import BaseMainWindow, FileSelectionWidget, OperationWidget


class ExcelFilterWindow(BaseMainWindow):
    """Excel数据筛选工具主窗口"""
    
    def __init__(self):
        super().__init__("Excel数据筛选工具", 1000, 700)
        self.df = None  # 存储当前读取的Excel数据
        self.filtered_df = None  # 存储筛选后的数据
        
    def setup_content(self):
        """设置内容区域"""
        # 文件选择组件
        self.file_selector = FileSelectionWidget("选择要筛选的Excel文件", multi_selection=False)
        self.file_selector.select_files = self.load_excel_file  # 重写选择文件方法
        self.content_layout.addWidget(self.file_selector)
        
        # 数据预览区域
        self.data_preview = DataPreviewWidget()
        self.content_layout.addWidget(self.data_preview)
        
        # 筛选条件组件
        self.filter_options = FilterOptionsWidget()
        self.filter_options.filter_clicked.connect(self.apply_filter)
        self.content_layout.addWidget(self.filter_options)
        
        # 操作区域
        self.operation = OperationWidget("筛选操作")
        self.operation.start_operation = self.start_operation
        self.operation.signals.progress.connect(self.update_progress)
        self.operation.signals.finished.connect(self.operation_finished)
        self.content_layout.addWidget(self.operation)
        
    def load_excel_file(self):
        """加载Excel文件并预览数据"""
        files = QFileDialog.getOpenFileNames(self, "选择Excel文件", "", "Excel文件 (*.xlsx *.xls)")[0]
        
        if not files:
            return
            
        file_path = files[0]
        self.file_selector.file_paths = files
        self.file_selector.update_display()
        
        try:
            # 读取Excel文件
            self.df = pd.read_excel(file_path)
            
            # 获取所有工作表名称
            self.sheets = pd.ExcelFile(file_path).sheet_names
            
            # 更新数据预览
            self.data_preview.update_data(self.df)
            
            # 更新筛选选项
            self.filter_options.update_columns(self.df.columns.tolist())
            
            # 更新状态
            self.statusBar().showMessage(f"已加载文件: {os.path.basename(file_path)}, 共 {len(self.df)} 行数据")
            
        except Exception as e:
            self.show_error(f"加载Excel文件失败: {str(e)}")
            
    def apply_filter(self):
        """应用筛选条件"""
        if self.df is None:
            self.show_warning("请先加载Excel文件")
            return
            
        try:
            # 获取筛选条件
            filters = self.filter_options.get_filter_conditions()
            
            # 应用筛选
            self.filtered_df = self.df.copy()
            
            for column, operator, value in filters:
                if operator == "等于":
                    self.filtered_df = self.filtered_df[self.filtered_df[column] == value]
                elif operator == "不等于":
                    self.filtered_df = self.filtered_df[self.filtered_df[column] != value]
                elif operator == "大于":
                    self.filtered_df = self.filtered_df[self.filtered_df[column] > float(value)]
                elif operator == "小于":
                    self.filtered_df = self.filtered_df[self.filtered_df[column] < float(value)]
                elif operator == "大于等于":
                    self.filtered_df = self.filtered_df[self.filtered_df[column] >= float(value)]
                elif operator == "小于等于":
                    self.filtered_df = self.filtered_df[self.filtered_df[column] <= float(value)]
                elif operator == "包含":
                    self.filtered_df = self.filtered_df[self.filtered_df[column].astype(str).str.contains(str(value), na=False)]
                elif operator == "不包含":
                    self.filtered_df = self.filtered_df[~self.filtered_df[column].astype(str).str.contains(str(value), na=False)]
                elif operator == "为空":
                    self.filtered_df = self.filtered_df[self.filtered_df[column].isna()]
                elif operator == "不为空":
                    self.filtered_df = self.filtered_df[~self.filtered_df[column].isna()]
            
            # 更新预览
            self.data_preview.update_data(self.filtered_df, is_filtered=True)
            
            # 更新状态
            self.statusBar().showMessage(f"筛选完成，从 {len(self.df)} 行数据中筛选出 {len(self.filtered_df)} 行")
            
        except Exception as e:
            self.show_error(f"筛选过程中出错: {str(e)}")
            
    def start_operation(self):
        """开始操作（保存筛选结果）"""
        if self.filtered_df is None:
            self.show_warning("请先应用筛选条件")
            return
            
        # 获取保存路径
        save_path = self.get_save_path("保存筛选结果", "Excel文件 (*.xlsx)", "筛选结果.xlsx")
        if not save_path:
            return
            
        # 开始保存
        self.operation.set_running_state(True)
        self.operation.signals.progress.emit(0, 100, "正在保存筛选结果...")
        
        # 使用定时器异步执行
        QTimer.singleShot(100, lambda: self.save_filtered_data(save_path))
        
    def save_filtered_data(self, save_path):
        """保存筛选后的数据"""
        try:
            self.operation.signals.progress.emit(50, 100, "正在写入Excel文件...")
            
            # 保存到Excel
            self.filtered_df.to_excel(save_path, index=False)
            
            # 完成
            if self.operation.is_running:
                self.operation.signals.finished.emit(True, f"筛选结果已保存到: {save_path}")
            else:
                self.operation.signals.finished.emit(False, "用户取消操作")
                
        except Exception as e:
            self.operation.signals.finished.emit(False, f"保存过程中出错: {str(e)}")
            
    def update_progress(self, current, total, status):
        """更新进度"""
        self.operation.progress.update_progress(current, total, status)
        
    def operation_finished(self, success, message):
        """操作完成"""
        self.operation.set_running_state(False)
        if success:
            self.show_info(message)
        else:
            self.show_error(message)


class DataPreviewWidget(QWidget):
    """数据预览组件"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 标题
        title_label = QLabel("数据预览 (最多显示前100行)")
        layout.addWidget(title_label)
        
        # 表格
        self.table = QTableWidget()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)
        
    def update_data(self, df, is_filtered=False):
        """更新表格数据"""
        if df is None or df.empty:
            self.table.setRowCount(0)
            self.table.setColumnCount(0)
            return
            
        # 限制显示行数
        display_df = df.head(100)
        
        # 设置表格
        self.table.setRowCount(display_df.shape[0])
        self.table.setColumnCount(display_df.shape[1])
        self.table.setHorizontalHeaderLabels(display_df.columns)
        
        # 填充数据
        for row in range(display_df.shape[0]):
            for col in range(display_df.shape[1]):
                value = str(display_df.iloc[row, col])
                # 对于NaN值，显示为空
                if value == "nan":
                    value = ""
                self.table.setItem(row, col, QTableWidgetItem(value))
        
        # 设置标题
        title = f"{'筛选结果' if is_filtered else '原始数据'}预览 (共 {len(df)} 行，显示前100行)"
        self.findChild(QLabel).setText(title)


class FilterOptionsWidget(QWidget):
    """筛选条件设置组件"""
    filter_clicked = Signal()
    
    def __init__(self):
        super().__init__()
        self.filter_conditions = []
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 条件设置区域
        self.conditions_widget = QWidget()
        self.conditions_layout = QVBoxLayout(self.conditions_widget)
        layout.addWidget(self.conditions_widget)
        
        # 添加一个默认条件
        self.add_filter_condition()
        
        # 添加条件按钮
        add_condition_btn = QPushButton("添加筛选条件")
        add_condition_btn.clicked.connect(self.add_filter_condition)
        layout.addWidget(add_condition_btn)
        
        # 应用筛选按钮
        apply_btn = QPushButton("应用筛选")
        apply_btn.clicked.connect(self.filter_clicked.emit)
        layout.addWidget(apply_btn)
        
    def add_filter_condition(self):
        """添加一个筛选条件"""
        condition = FilterConditionWidget(len(self.filter_conditions))
        condition.remove_requested.connect(self.remove_filter_condition)
        self.filter_conditions.append(condition)
        self.conditions_layout.addWidget(condition)
        
    def remove_filter_condition(self, index):
        """移除筛选条件"""
        if 0 <= index < len(self.filter_conditions):
            condition = self.filter_conditions[index]
            self.conditions_layout.removeWidget(condition)
            condition.deleteLater()
            
            # 移除并更新索引
            self.filter_conditions.pop(index)
            for i, cond in enumerate(self.filter_conditions):
                cond.update_index(i)
                
    def update_columns(self, columns):
        """更新可用列名"""
        for condition in self.filter_conditions:
            condition.update_columns(columns)
            
    def get_filter_conditions(self):
        """获取所有筛选条件"""
        conditions = []
        for condition in self.filter_conditions:
            cond = condition.get_condition()
            if cond:  # 只添加有效条件
                conditions.append(cond)
        return conditions


class FilterConditionWidget(QWidget):
    """单个筛选条件组件"""
    remove_requested = Signal(int)
    
    def __init__(self, index):
        super().__init__()
        self.index = index
        self.setup_ui()
        
    def setup_ui(self):
        layout = QHBoxLayout(self)
        
        # 列名选择
        layout.addWidget(QLabel("列名:"))
        self.column_combo = QComboBox()
        layout.addWidget(self.column_combo)
        
        # 操作符选择
        layout.addWidget(QLabel("操作:"))
        self.operator_combo = QComboBox()
        self.operator_combo.addItems([
            "等于", "不等于", "大于", "小于", "大于等于", "小于等于", 
            "包含", "不包含", "为空", "不为空"
        ])
        self.operator_combo.currentTextChanged.connect(self.toggle_value_input)
        layout.addWidget(self.operator_combo)
        
        # 值输入
        layout.addWidget(QLabel("值:"))
        self.value_input = QLineEdit()
        layout.addWidget(self.value_input)
        
        # 删除按钮
        self.remove_btn = QPushButton("删除")
        self.remove_btn.clicked.connect(lambda: self.remove_requested.emit(self.index))
        layout.addWidget(self.remove_btn)
        
    def update_index(self, new_index):
        """更新索引"""
        self.index = new_index
        
    def update_columns(self, columns):
        """更新列名列表"""
        self.column_combo.clear()
        self.column_combo.addItems(columns)
        
    def toggle_value_input(self, text):
        """根据操作符切换值输入框状态"""
        # 对于"为空"和"不为空"操作，值输入框不可用
        self.value_input.setEnabled(text not in ["为空", "不为空"])
        
    def get_condition(self):
        """获取筛选条件"""
        column = self.column_combo.currentText()
        operator = self.operator_combo.currentText()
        value = self.value_input.text()
        
        # 如果没有选择列，返回空
        if not column:
            return None
            
        return (column, operator, value)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = ExcelFilterWindow()
    window.show()
    sys.exit(app.exec())