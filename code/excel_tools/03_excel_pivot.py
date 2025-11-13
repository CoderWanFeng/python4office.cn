#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Excel数据透视表生成工具
功能：根据Excel数据自动生成数据透视表，支持自定义行、列、值和筛选器
"""

import sys
import os
import pandas as pd
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QListWidget, QListWidgetItem
from PySide6.QtCore import QTimer, Qt

# 添加父目录到路径，以便导入common模块
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.ui_base import BaseMainWindow, FileSelectionWidget, OperationWidget


class ExcelPivotWindow(BaseMainWindow):
    """Excel数据透视表生成工具主窗口"""
    
    def __init__(self):
        super().__init__("Excel数据透视表生成工具", 1000, 700)
        self.df = None  # 存储当前读取的Excel数据
        self.pivot_df = None  # 存储生成的透视表
        
    def setup_content(self):
        """设置内容区域"""
        # 文件选择组件
        self.file_selector = FileSelectionWidget("选择要生成透视表的Excel文件", multi_selection=False)
        self.file_selector.select_files = self.load_excel_file  # 重写选择文件方法
        self.content_layout.addWidget(self.file_selector)
        
        # 数据预览区域
        self.data_preview = DataPreviewWidget()
        self.content_layout.addWidget(self.data_preview)
        
        # 透视表设置组件
        self.pivot_options = PivotOptionsWidget()
        self.pivot_options.generate_clicked.connect(self.generate_pivot_table)
        self.content_layout.addWidget(self.pivot_options)
        
        # 操作区域
        self.operation = OperationWidget("透视表操作")
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
            
            # 更新数据预览
            self.data_preview.update_data(self.df)
            
            # 更新透视表选项
            self.pivot_options.update_columns(self.df.columns.tolist())
            
            # 更新状态
            self.statusBar().showMessage(f"已加载文件: {os.path.basename(file_path)}, 共 {len(self.df)} 行数据")
            
        except Exception as e:
            self.show_error(f"加载Excel文件失败: {str(e)}")
            
    def generate_pivot_table(self):
        """生成数据透视表"""
        if self.df is None:
            self.show_warning("请先加载Excel文件")
            return
            
        try:
            # 获取透视表配置
            config = self.pivot_options.get_pivot_config()
            
            # 提取配置参数
            index = config["index"]
            columns = config["columns"]
            values = config["values"]
            aggfunc = config["aggfunc"]
            filters = config["filters"]
            
            # 验证必要参数
            if not index and not columns:
                self.show_warning("请至少选择一个行或列字段")
                return
                
            if not values:
                self.show_warning("请至少选择一个值字段")
                return
            
            # 应用筛选器
            filtered_df = self.df.copy()
            if filters:
                for column, value in filters:
                    filtered_df = filtered_df[filtered_df[column] == value]
            
            # 生成透视表
            self.pivot_df = pd.pivot_table(
                filtered_df,
                index=index if index else None,
                columns=columns if columns else None,
                values=values,
                aggfunc=aggfunc,
                fill_value=0
            )
            
            # 如果只有一列值，将其扁平化
            if len(values) == 1 and (columns or index):
                self.pivot_df = self.pivot_df[values[0]]
            
            # 更新预览
            self.data_preview.update_pivot_data(self.pivot_df)
            
            # 更新状态
            self.statusBar().showMessage(f"透视表生成完成，共 {len(self.pivot_df)} 行数据")
            
        except Exception as e:
            self.show_error(f"生成透视表过程中出错: {str(e)}")
            
    def start_operation(self):
        """开始操作（保存透视表）"""
        if self.pivot_df is None:
            self.show_warning("请先生成透视表")
            return
            
        # 获取保存路径
        save_path = self.get_save_path("保存透视表", "Excel文件 (*.xlsx)", "透视表结果.xlsx")
        if not save_path:
            return
            
        # 开始保存
        self.operation.set_running_state(True)
        self.operation.signals.progress.emit(0, 100, "正在保存透视表...")
        
        # 使用定时器异步执行
        QTimer.singleShot(100, lambda: self.save_pivot_table(save_path))
        
    def save_pivot_table(self, save_path):
        """保存透视表"""
        try:
            self.operation.signals.progress.emit(50, 100, "正在写入Excel文件...")
            
            # 保存到Excel
            if isinstance(self.pivot_df, pd.DataFrame):
                self.pivot_df.to_excel(save_path)
            else:
                # 如果是Series，转换为DataFrame
                df = self.pivot_df.reset_index()
                df.to_excel(save_path, index=False)
            
            # 完成
            if self.operation.is_running:
                self.operation.signals.finished.emit(True, f"透视表已保存到: {save_path}")
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
        self.title_label = QLabel("数据预览")
        layout.addWidget(self.title_label)
        
        # 表格
        self.table = QTableWidget()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)
        
    def update_data(self, df):
        """更新原始数据预览"""
        if df is None or df.empty:
            self.table.setRowCount(0)
            self.table.setColumnCount(0)
            self.title_label.setText("数据预览")
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
        self.title_label.setText(f"原始数据预览 (共 {len(df)} 行，显示前100行)")
        
    def update_pivot_data(self, pivot_df):
        """更新透视表预览"""
        if pivot_df is None:
            self.table.setRowCount(0)
            self.table.setColumnCount(0)
            self.title_label.setText("数据预览")
            return
            
        # 如果是Series，转换为DataFrame
        if isinstance(pivot_df, pd.Series):
            pivot_df = pivot_df.reset_index()
        
        # 设置表格
        self.table.setRowCount(pivot_df.shape[0])
        self.table.setColumnCount(pivot_df.shape[1])
        
        # 设置列名
        if isinstance(pivot_df.columns, pd.MultiIndex):
            # 对于多级列索引，转换为字符串
            columns = ["_".join(map(str, col)).strip() if isinstance(col, tuple) else str(col) for col in pivot_df.columns]
            self.table.setHorizontalHeaderLabels(columns)
        else:
            self.table.setHorizontalHeaderLabels([str(col) for col in pivot_df.columns])
        
        # 填充数据
        for row in range(pivot_df.shape[0]):
            for col in range(pivot_df.shape[1]):
                value = str(pivot_df.iloc[row, col])
                # 对于NaN值，显示为空
                if value == "nan":
                    value = ""
                self.table.setItem(row, col, QTableWidgetItem(value))
        
        # 设置标题
        self.title_label.setText(f"透视表预览 (共 {len(pivot_df)} 行)")


class PivotOptionsWidget(QWidget):
    """透视表设置组件"""
    generate_clicked = Signal()
    
    def __init__(self):
        super().__init__()
        self.columns = []  # 存储可用的列名
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 四个区域：行、列、值、筛选器
        areas_layout = QHBoxLayout()
        
        # 行区域
        index_group = QWidget()
        index_layout = QVBoxLayout(index_group)
        index_layout.addWidget(QLabel("行:"))
        self.index_list = DragDropListWidget("行字段")
        index_layout.addWidget(self.index_list)
        areas_layout.addWidget(index_group)
        
        # 列区域
        columns_group = QWidget()
        columns_layout = QVBoxLayout(columns_group)
        columns_layout.addWidget(QLabel("列:"))
        self.columns_list = DragDropListWidget("列字段")
        columns_layout.addWidget(self.columns_list)
        areas_layout.addWidget(columns_group)
        
        # 值区域
        values_group = QWidget()
        values_layout = QVBoxLayout(values_group)
        values_layout.addWidget(QLabel("值:"))
        self.values_list = DragDropListWidget("值字段")
        values_layout.addWidget(self.values_list)
        areas_layout.addWidget(values_group)
        
        # 筛选器区域
        filters_group = QWidget()
        filters_layout = QVBoxLayout(filters_group)
        filters_layout.addWidget(QLabel("筛选器:"))
        self.filters_list = DragDropListWidget("筛选器字段")
        filters_layout.addWidget(self.filters_list)
        areas_layout.addWidget(filters_group)
        
        layout.addLayout(areas_layout)
        
        # 可用字段区域
        layout.addWidget(QLabel("可用字段:"))
        self.available_list = DragDropListWidget("可用字段")
        self.available_list.itemDoubleClicked.connect(self.add_to_default)
        layout.addWidget(self.available_list)
        
        # 聚合函数选择
        func_layout = QHBoxLayout()
        func_layout.addWidget(QLabel("值聚合方式:"))
        self.aggfunc_combo = QComboBox()
        self.aggfunc_combo.addItems(["求和", "计数", "平均值", "最大值", "最小值"])
        func_layout.addWidget(self.aggfunc_combo)
        func_layout.addStretch()
        layout.addLayout(func_layout)
        
        # 生成按钮
        generate_btn = QPushButton("生成透视表")
        generate_btn.clicked.connect(self.generate_clicked.emit)
        layout.addWidget(generate_btn)
        
    def update_columns(self, columns):
        """更新可用列名"""
        self.columns = columns
        self.available_list.clear()
        self.available_list.addItems(columns)
        
    def add_to_default(self, item):
        """将字段添加到默认区域（行）"""
        text = item.text()
        self.available_list.takeItem(self.available_list.row(item))
        self.index_list.addItem(text)
        
    def get_pivot_config(self):
        """获取透视表配置"""
        # 获取行、列、值和筛选器字段
        index = self.get_list_items(self.index_list)
        columns = self.get_list_items(self.columns_list)
        values = self.get_list_items(self.values_list)
        filters = []
        
        # 处理筛选器字段
        for i in range(self.filters_list.count()):
            item = self.filters_list.item(i)
            widget = self.filters_list.itemWidget(item)
            if widget:
                column = widget.get_column()
                value = widget.get_value()
                if column and value:
                    filters.append((column, value))
        
        # 获取聚合函数
        aggfunc_text = self.aggfunc_combo.currentText()
        aggfunc_map = {
            "求和": "sum",
            "计数": "count",
            "平均值": "mean",
            "最大值": "max",
            "最小值": "min"
        }
        aggfunc = aggfunc_map.get(aggfunc_text, "sum")
        
        return {
            "index": index,
            "columns": columns,
            "values": values,
            "aggfunc": aggfunc,
            "filters": filters
        }
        
    def get_list_items(self, list_widget):
        """获取列表中的所有文本项"""
        items = []
        for i in range(list_widget.count()):
            item = list_widget.item(i)
            # 检查是否有自定义小部件
            widget = list_widget.itemWidget(item)
            if widget:
                items.append(widget.get_column())
            else:
                items.append(item.text())
        return items


class DragDropListWidget(QListWidget):
    """支持拖拽的列表小部件"""
    
    def __init__(self, name=""):
        super().__init__()
        self.name = name
        self.setAcceptDrops(True)
        self.setDragDropMode(QListWidget.DragDrop)
        self.setDefaultDropAction(Qt.MoveAction)
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()
            
    def dropEvent(self, event):
        text = event.mimeData().text()
        
        # 如果是筛选器区域，需要创建特殊的小部件
        if self.name == "筛选器字段":
            from PySide6.QtWidgets import QLineEdit, QHBoxLayout, QWidget
            
            # 创建自定义小部件
            widget = QWidget()
            layout = QHBoxLayout(widget)
            layout.setContentsMargins(5, 5, 5, 5)
            
            # 列名标签
            label = QLabel(text + ":")
            layout.addWidget(label)
            
            # 值输入框
            value_edit = QLineEdit()
            value_edit.setPlaceholderText("输入筛选值")
            layout.addWidget(value_edit)
            
            # 设置方法以获取列名和值
            widget.get_column = lambda: text
            widget.get_value = lambda: value_edit.text()
            
            # 创建列表项
            item = QListWidgetItem()
            item.setSizeHint(widget.sizeHint())
            self.addItem(item)
            self.setItemWidget(item, widget)
        else:
            # 普通列表项
            self.addItem(text)
        
        event.acceptProposedAction()


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication, QFileDialog
    app = QApplication(sys.argv)
    window = ExcelPivotWindow()
    window.show()
    sys.exit(app.exec())