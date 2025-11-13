#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
数据清洗工具
功能：清洗和标准化数据，支持多种数据源和清洗规则
"""

import sys
import os
import pandas as pd
import numpy as np
import re
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                              QPushButton, QTableWidget, QTableWidgetItem, 
                              QHeaderView, QTabWidget, QComboBox, QCheckBox,
                              QFileDialog, QMessageBox, QTextEdit, QSpinBox)
from PySide6.QtCore import QTimer, Qt

# 添加父目录到路径，以便导入common模块
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.ui_base import BaseMainWindow, FileSelectionWidget, OperationWidget


class DataCleanWindow(BaseMainWindow):
    """数据清洗工具主窗口"""
    
    def __init__(self):
        super().__init__("数据清洗工具", 1000, 700)
        self.df = None  # 存储当前读取的数据
        
    def setup_content(self):
        """设置内容区域"""
        # 文件选择组件
        self.file_selector = FileSelectionWidget("选择要清洗的数据文件", multi_selection=False)
        self.file_selector.select_files = self.load_data_file  # 重写选择文件方法
        self.content_layout.addWidget(self.file_selector)
        
        # 数据预览组件
        self.preview_widget = DataPreviewWidget()
        self.content_layout.addWidget(self.preview_widget)
        
        # 使用选项卡组织界面
        self.tab_widget = QTabWidget()
        self.content_layout.addWidget(self.tab_widget)
        
        # 缺失值处理选项卡
        self.missing_tab = QWidget()
        self.setup_missing_tab()
        self.tab_widget.addTab(self.missing_tab, "缺失值处理")
        
        # 重复值处理选项卡
        self.duplicate_tab = QWidget()
        self.setup_duplicate_tab()
        self.tab_widget.addTab(self.duplicate_tab, "重复值处理")
        
        # 数据格式选项卡
        self.format_tab = QWidget()
        self.setup_format_tab()
        self.tab_widget.addTab(self.format_tab, "数据格式")
        
        # 异常值处理选项卡
        self.outlier_tab = QWidget()
        self.setup_outlier_tab()
        self.tab_widget.addTab(self.outlier_tab, "异常值处理")
        
        # 自定义规则选项卡
        self.custom_tab = QWidget()
        self.setup_custom_tab()
        self.tab_widget.addTab(self.custom_tab, "自定义规则")
        
        # 操作区域
        self.operation = OperationWidget("数据清洗操作")
        self.operation.start_operation = self.start_cleaning
        self.operation.signals.progress.connect(self.update_progress)
        self.operation.signals.finished.connect(self.cleaning_finished)
        self.content_layout.addWidget(self.operation)
        
    def load_data_file(self):
        """加载数据文件"""
        files = QFileDialog.getOpenFileNames(self, "选择数据文件", "", 
                                           "数据文件 (*.csv *.xlsx *.xls *.json *.txt)")[0]
        
        if not files:
            return
            
        file_path = files[0]
        self.file_selector.file_paths = files
        self.file_selector.update_display()
        
        try:
            # 根据文件扩展名读取数据
            ext = os.path.splitext(file_path)[1].lower()
            
            if ext == ".csv":
                self.df = pd.read_csv(file_path)
            elif ext in [".xlsx", ".xls"]:
                self.df = pd.read_excel(file_path)
            elif ext == ".json":
                self.df = pd.read_json(file_path)
            elif ext == ".txt":
                self.df = pd.read_csv(file_path, sep="\t")
            else:
                self.show_error("不支持的文件格式")
                return
            
            # 更新预览
            self.preview_widget.update_data(self.df)
            
            # 更新状态
            self.statusBar().showMessage(f"已加载文件: {os.path.basename(file_path)}, 共 {len(self.df)} 行, {len(self.df.columns)} 列")
            
        except Exception as e:
            self.show_error(f"加载数据文件失败: {str(e)}")
            
    def setup_missing_tab(self):
        """设置缺失值处理选项卡"""
        layout = QVBoxLayout(self.missing_tab)
        
        # 缺失值处理方式
        method_group = QWidget()
        method_layout = QVBoxLayout(method_group)
        method_layout.addWidget(QLabel("处理方式:"))
        
        self.missing_method_combo = QComboBox()
        self.missing_method_combo.addItems(["删除行", "删除列", "填充值", "插值"])
        self.missing_method_combo.currentTextChanged.connect(self.toggle_missing_options)
        method_layout.addWidget(self.missing_method_combo)
        layout.addWidget(method_group)
        
        # 填充值选项
        fill_group = QWidget()
        fill_layout = QVBoxLayout(fill_group)
        fill_layout.addWidget(QLabel("填充值设置:"))
        
        self.fill_value_combo = QComboBox()
        self.fill_value_combo.addItems(["0", "均值", "中位数", "众数", "前值", "后值", "自定义"])
        self.fill_value_combo.currentTextChanged.connect(self.toggle_custom_fill)
        fill_layout.addWidget(self.fill_value_combo)
        
        self.custom_fill_input = QLineEdit()
        fill_layout.addWidget(self.custom_fill_input)
        
        layout.addWidget(fill_group)
        
        # 插值选项
        interp_group = QWidget()
        interp_layout = QVBoxLayout(interp_group)
        interp_layout.addWidget(QLabel("插值方法:"))
        
        self.interp_method_combo = QComboBox()
        self.interp_method_combo.addItems(["线性", "多项式", "样条", "时间序列"])
        interp_layout.addWidget(self.interp_method_combo)
        
        # 多项式阶数
        order_layout = QHBoxLayout()
        order_layout.addWidget(QLabel("多项式阶数:"))
        self.poly_order_spin = QSpinBox()
        self.poly_order_spin.setMinimum(1)
        self.poly_order_spin.setMaximum(10)
        self.poly_order_spin.setValue(2)
        order_layout.addWidget(self.poly_order_spin)
        interp_layout.addLayout(order_layout)
        
        layout.addWidget(interp_group)
        
        # 初始化控件状态
        self.toggle_missing_options(self.missing_method_combo.currentText())
        
    def setup_duplicate_tab(self):
        """设置重复值处理选项卡"""
        layout = QVBoxLayout(self.duplicate_tab)
        
        # 重复值处理方式
        method_group = QWidget()
        method_layout = QVBoxLayout(method_group)
        method_layout.addWidget(QLabel("处理方式:"))
        
        self.duplicate_method_combo = QComboBox()
        self.duplicate_method_combo.addItems(["删除重复行", "标记重复行", "保留重复统计"])
        method_layout.addWidget(self.duplicate_method_combo)
        layout.addWidget(method_group)
        
        # 重复判断依据
        subset_group = QWidget()
        subset_layout = QVBoxLayout(subset_group)
        subset_layout.addWidget(QLabel("判断依据:"))
        
        self.all_columns_radio = QRadioButton("所有列")
        self.all_columns_radio.setChecked(True)
        subset_layout.addWidget(self.all_columns_radio)
        
        self.selected_columns_radio = QRadioButton("指定列")
        self.selected_columns_radio.toggled.connect(self.toggle_column_selector)
        subset_layout.addWidget(self.selected_columns_radio)
        
        self.duplicate_columns_input = QLineEdit()
        self.duplicate_columns_input.setPlaceholderText("输入列名，用逗号分隔")
        self.duplicate_columns_input.setEnabled(False)
        subset_layout.addWidget(self.duplicate_columns_input)
        
        layout.addWidget(subset_group)
        
        # 保留策略
        keep_group = QWidget()
        keep_layout = QVBoxLayout(keep_group)
        keep_layout.addWidget(QLabel("保留策略:"))
        
        self.keep_combo = QComboBox()
        self.keep_combo.addItems(["第一条", "最后一条"])
        keep_layout.addWidget(self.keep_combo)
        
        layout.addWidget(keep_group)
        
    def setup_format_tab(self):
        """设置数据格式选项卡"""
        layout = QVBoxLayout(self.format_tab)
        
        # 数据类型转换
        type_group = QWidget()
        type_layout = QVBoxLayout(type_group)
        type_layout.addWidget(QLabel("数据类型转换:"))
        
        # 列选择
        column_layout = QHBoxLayout()
        column_layout.addWidget(QLabel("列名:"))
        self.type_column_combo = QComboBox()
        column_layout.addWidget(self.type_column_combo)
        type_layout.addLayout(column_layout)
        
        # 目标类型
        target_layout = QHBoxLayout()
        target_layout.addWidget(QLabel("目标类型:"))
        self.target_type_combo = QComboBox()
        self.target_type_combo.addItems(["数值", "文本", "日期", "布尔值"])
        target_layout.addWidget(self.target_type_combo)
        type_layout.addLayout(target_layout)
        
        self.apply_type_btn = QPushButton("应用转换")
        self.apply_type_btn.clicked.connect(self.apply_type_conversion)
        type_layout.addWidget(self.apply_type_btn)
        
        layout.addWidget(type_group)
        
        # 文本处理
        text_group = QWidget()
        text_layout = QVBoxLayout(text_group)
        text_layout.addWidget(QLabel("文本处理:"))
        
        self.trim_checkbox = QCheckBox("去除首尾空格")
        text_layout.addWidget(self.trim_checkbox)
        
        self.lowercase_checkbox = QCheckBox("转换为小写")
        text_layout.addWidget(self.lowercase_checkbox)
        
        self.remove_punct_checkbox = QCheckBox("去除标点符号")
        text_layout.addWidget(self.remove_punct_checkbox)
        
        layout.addWidget(text_group)
        
        # 日期格式标准化
        date_group = QWidget()
        date_layout = QVBoxLayout(date_group)
        date_layout.addWidget(QLabel("日期格式标准化:"))
        
        date_input_layout = QHBoxLayout()
        date_input_layout.addWidget(QLabel("日期列:"))
        self.date_column_combo = QComboBox()
        date_input_layout.addWidget(self.date_column_combo)
        date_layout.addLayout(date_input_layout)
        
        format_layout = QHBoxLayout()
        format_layout.addWidget(QLabel("目标格式:"))
        self.date_format_input = QLineEdit("%Y-%m-%d")
        format_layout.addWidget(self.date_format_input)
        date_layout.addLayout(format_layout)
        
        self.apply_date_btn = QPushButton("应用格式")
        self.apply_date_btn.clicked.connect(self.apply_date_format)
        date_layout.addWidget(self.apply_date_btn)
        
        layout.addWidget(date_group)
        
    def setup_outlier_tab(self):
        """设置异常值处理选项卡"""
        layout = QVBoxLayout(self.outlier_tab)
        
        # 检测方法
        method_group = QWidget()
        method_layout = QVBoxLayout(method_group)
        method_layout.addWidget(QLabel("检测方法:"))
        
        self.outlier_method_combo = QComboBox()
        self.outlier_method_combo.addItems(["标准差法", "四分位距法", "Z-Score法"])
        self.outlier_method_combo.currentTextChanged.connect(self.toggle_outlier_options)
        method_layout.addWidget(self.outlier_method_combo)
        layout.addWidget(method_group)
        
        # 参数设置
        param_group = QWidget()
        param_layout = QVBoxLayout(param_group)
        param_layout.addWidget(QLabel("参数设置:"))
        
        # 标准差倍数
        std_layout = QHBoxLayout()
        std_layout.addWidget(QLabel("标准差倍数:"))
        self.std_spin = QSpinBox()
        self.std_spin.setMinimum(1)
        self.std_spin.setMaximum(5)
        self.std_spin.setValue(3)
        std_layout.addWidget(self.std_spin)
        param_layout.addLayout(std_layout)
        
        # IQR倍数
        iqr_layout = QHBoxLayout()
        iqr_layout.addWidget(QLabel("IQR倍数:"))
        self.iqr_spin = QSpinBox()
        self.iqr_spin.setMinimum(1)
        self.iqr_spin.setMaximum(5)
        self.iqr_spin.setValue(1.5)
        iqr_layout.addWidget(self.iqr_spin)
        param_layout.addLayout(iqr_layout)
        
        # Z-Score阈值
        zscore_layout = QHBoxLayout()
        zscore_layout.addWidget(QLabel("Z-Score阈值:"))
        self.zscore_spin = QSpinBox()
        self.zscore_spin.setMinimum(1)
        self.zscore_spin.setMaximum(5)
        self.zscore_spin.setValue(3)
        zscore_layout.addWidget(self.zscore_spin)
        param_layout.addLayout(zscore_layout)
        
        layout.addWidget(param_group)
        
        # 处理方式
        treat_group = QWidget()
        treat_layout = QVBoxLayout(treat_group)
        treat_layout.addWidget(QLabel("处理方式:"))
        
        self.outlier_treat_combo = QComboBox()
        self.outlier_treat_combo.addItems(["删除异常值", "替换为边界值", "替换为中位数"])
        treat_layout.addWidget(self.outlier_treat_combo)
        
        layout.addWidget(treat_group)
        
        # 初始化控件状态
        self.toggle_outlier_options(self.outlier_method_combo.currentText())
        
    def setup_custom_tab(self):
        """设置自定义规则选项卡"""
        layout = QVBoxLayout(self.custom_tab)
        
        # 规则编辑
        rules_layout = QVBoxLayout()
        rules_layout.addWidget(QLabel("自定义规则:"))
        
        # 规则列表
        self.custom_rules_table = QTableWidget(0, 4)
        self.custom_rules_table.setHorizontalHeaderLabels(["列名", "操作", "条件", "替换值"])
        self.custom_rules_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        rules_layout.addWidget(self.custom_rules_table)
        
        # 规则操作按钮
        btn_layout = QHBoxLayout()
        
        self.add_rule_btn = QPushButton("添加规则")
        self.add_rule_btn.clicked.connect(self.add_custom_rule)
        btn_layout.addWidget(self.add_rule_btn)
        
        self.remove_rule_btn = QPushButton("删除规则")
        self.remove_rule_btn.clicked.connect(self.remove_custom_rule)
        btn_layout.addWidget(self.remove_rule_btn)
        
        rules_layout.addLayout(btn_layout)
        layout.addLayout(rules_layout)
        
        # 规则示例
        example_layout = QVBoxLayout()
        example_layout.addWidget(QLabel("规则示例:"))
        
        example_text = QTextEdit()
        example_text.setMaximumHeight(100)
        example_text.setPlainText(
            "1. 替换值: 列名='年龄', 操作='替换', 条件='18', 替换值='青年'\n"
            "2. 条件过滤: 列名='收入', 操作='过滤', 条件='>0', 替换值=''\n"
            "3. 文本替换: 列名='姓名', 操作='替换', 条则='张三', 替换值='李四'\n"
        )
        example_text.setReadOnly(True)
        example_layout.addWidget(example_text)
        
        layout.addLayout(example_layout)
        
        # 添加一个默认规则
        self.add_custom_rule()
        
    def toggle_missing_options(self, method):
        """根据缺失值处理方式切换选项"""
        is_fill = method == "填充值"
        is_interp = method == "插值"
        
        # 设置各组件的可见性
        self.fill_value_combo.parent().setVisible(is_fill)
        self.custom_fill_input.setVisible(is_fill and self.fill_value_combo.currentText() == "自定义")
        
        self.interp_method_combo.parent().setVisible(is_interp)
        self.poly_order_spin.parent().setVisible(
            is_interp and self.interp_method_combo.currentText() == "多项式"
        )
        
    def toggle_custom_fill(self, value):
        """切换自定义填充值输入框"""
        is_custom = value == "自定义"
        self.custom_fill_input.setVisible(is_custom)
        
    def toggle_column_selector(self, checked):
        """切换列选择器状态"""
        self.duplicate_columns_input.setEnabled(checked)
        self.all_columns_radio.setChecked(not checked)
        
    def toggle_outlier_options(self, method):
        """根据异常值检测方法切换选项"""
        is_std = method == "标准差法"
        is_iqr = method == "四分位距法"
        is_zscore = method == "Z-Score法"
        
        # 设置各组件的可见性
        self.std_spin.parent().setVisible(is_std)
        self.iqr_spin.parent().setVisible(is_iqr)
        self.zscore_spin.parent().setVisible(is_zscore)
        
    def add_custom_rule(self):
        """添加自定义规则"""
        row = self.custom_rules_table.rowCount()
        self.custom_rules_table.insertRow(row)
        
        # 添加下拉框
        column_combo = QComboBox()
        if self.df is not None:
            column_combo.addItems(self.df.columns.tolist())
        self.custom_rules_table.setCellWidget(row, 0, column_combo)
        
        operation_combo = QComboBox()
        operation_combo.addItems(["替换", "过滤", "删除", "转换"])
        self.custom_rules_table.setCellWidget(row, 1, operation_combo)
        
        self.custom_rules_table.setItem(row, 2, QTableWidgetItem(""))
        self.custom_rules_table.setItem(row, 3, QTableWidgetItem(""))
        
    def remove_custom_rule(self):
        """删除自定义规则"""
        current_row = self.custom_rules_table.currentRow()
        if current_row >= 0:
            self.custom_rules_table.removeRow(current_row)
            
    def apply_type_conversion(self):
        """应用数据类型转换"""
        if self.df is None:
            self.show_warning("请先加载数据")
            return
            
        column = self.type_column_combo.currentText()
        if not column:
            self.show_warning("请选择要转换的列")
            return
            
        target_type = self.target_type_combo.currentText()
        
        try:
            if target_type == "数值":
                self.df[column] = pd.to_numeric(self.df[column], errors='coerce')
            elif target_type == "文本":
                self.df[column] = self.df[column].astype(str)
            elif target_type == "日期":
                self.df[column] = pd.to_datetime(self.df[column], errors='coerce')
            elif target_type == "布尔值":
                self.df[column] = self.df[column].astype(bool)
                
            # 更新预览
            self.preview_widget.update_data(self.df)
            self.show_info(f"列 '{column}' 已转换为 {target_type}")
            
        except Exception as e:
            self.show_error(f"类型转换失败: {str(e)}")
            
    def apply_date_format(self):
        """应用日期格式"""
        if self.df is None:
            self.show_warning("请先加载数据")
            return
            
        column = self.date_column_combo.currentText()
        if not column:
            self.show_warning("请选择日期列")
            return
            
        format_str = self.date_format_input.text()
        if not format_str:
            self.show_warning("请输入目标日期格式")
            return
            
        try:
            # 转换为日期
            self.df[column] = pd.to_datetime(self.df[column], errors='coerce')
            
            # 应用格式
            self.df[column] = self.df[column].dt.strftime(format_str)
            
            # 更新预览
            self.preview_widget.update_data(self.df)
            self.show_info(f"列 '{column}' 日期格式已应用")
            
        except Exception as e:
            self.show_error(f"日期格式应用失败: {str(e)}")
            
    def start_cleaning(self):
        """开始数据清洗"""
        if self.df is None:
            self.show_warning("请先加载数据")
            return
            
        # 获取保存路径
        save_path = self.get_save_path("保存清洗后的数据", "数据文件 (*.csv *.xlsx)", "cleaned_data.csv")
        if not save_path:
            return
            
        # 获取当前选项卡的索引
        current_tab_index = self.tab_widget.currentIndex()
        
        # 开始处理
        self.operation.set_running_state(True)
        self.operation.signals.progress.emit(0, 100, "开始数据清洗...")
        
        # 使用定时器异步执行
        QTimer.singleShot(100, lambda: self.process_cleaning(
            save_path, current_tab_index
        ))
        
    def process_cleaning(self, save_path, tab_index):
        """处理数据清洗"""
        try:
            # 创建数据副本以避免修改原始数据
            cleaned_df = self.df.copy()
            
            # 根据选项卡进行不同处理
            if tab_index == 0:  # 缺失值处理
                cleaned_df = self.clean_missing_values(cleaned_df)
            elif tab_index == 1:  # 重复值处理
                cleaned_df = self.clean_duplicates(cleaned_df)
            elif tab_index == 2:  # 数据格式
                cleaned_df = self.clean_format(cleaned_df)
            elif tab_index == 3:  # 异常值处理
                cleaned_df = self.clean_outliers(cleaned_df)
            elif tab_index == 4:  # 自定义规则
                cleaned_df = self.apply_custom_rules(cleaned_df)
            
            # 保存清洗后的数据
            self.operation.signals.progress.emit(80, 100, "正在保存清洗后的数据...")
            
            ext = os.path.splitext(save_path)[1].lower()
            if ext == ".csv":
                cleaned_df.to_csv(save_path, index=False)
            elif ext in [".xlsx", ".xls"]:
                cleaned_df.to_excel(save_path, index=False)
            
            # 更新数据并刷新预览
            self.df = cleaned_df
            self.preview_widget.update_data(self.df)
            
            # 完成
            if self.operation.is_running:
                message = f"数据清洗完成，共 {len(cleaned_df)} 行数据"
                self.operation.signals.finished.emit(True, message)
            else:
                self.operation.signals.finished.emit(False, "用户取消操作")
                
        except Exception as e:
            self.operation.signals.finished.emit(False, f"数据清洗过程中发生错误: {str(e)}")
            
    def clean_missing_values(self, df):
        """处理缺失值"""
        method = self.missing_method_combo.currentText()
        
        if method == "删除行":
            return df.dropna()
        elif method == "删除列":
            return df.dropna(axis=1)
        elif method == "填充值":
            fill_value = self.fill_value_combo.currentText()
            
            if fill_value == "自定义":
                fill_value = self.custom_fill_input.text()
            elif fill_value == "均值":
                return df.fillna(df.mean())
            elif fill_value == "中位数":
                return df.fillna(df.median())
            elif fill_value == "众数":
                return df.fillna(df.mode().iloc[0])
            elif fill_value == "前值":
                return df.fillna(method='ffill')
            elif fill_value == "后值":
                return df.fillna(method='bfill')
            else:  # 数值
                try:
                    return df.fillna(float(fill_value))
                except:
                    return df.fillna(fill_value)
                    
        elif method == "插值":
            interp_method = self.interp_method_combo.currentText()
            
            if interp_method == "线性":
                return df.interpolate(method='linear')
            elif interp_method == "多项式":
                order = self.poly_order_spin.value()
                return df.interpolate(method='polynomial', order=order)
            elif interp_method == "样条":
                return df.interpolate(method='spline', order=3)
            elif interp_method == "时间序列":
                return df.interpolate(method='time')
                
        return df
        
    def clean_duplicates(self, df):
        """处理重复值"""
        method = self.duplicate_method_combo.currentText()
        
        if self.selected_columns_radio.isChecked():
            subset = self.duplicate_columns_input.text().split(',')
            subset = [col.strip() for col in subset if col.strip()]
        else:
            subset = None
            
        keep = 'first' if self.keep_combo.currentText() == "第一条" else 'last'
        
        if method == "删除重复行":
            return df.drop_duplicates(subset=subset, keep=keep)
        elif method == "标记重复行":
            # 添加重复标记列
            df['is_duplicate'] = df.duplicated(subset=subset, keep=keep)
            return df
        elif method == "保留重复统计":
            # 添加重复计数列
            df['duplicate_count'] = df.groupby(subset).transform('size')
            return df
            
        return df
        
    def clean_format(self, df):
        """处理数据格式"""
        # 文本处理
        if self.trim_checkbox.isChecked():
            for col in df.select_dtypes(include=['object']):
                df[col] = df[col].str.strip()
                
        if self.lowercase_checkbox.isChecked():
            for col in df.select_dtypes(include=['object']):
                df[col] = df[col].str.lower()
                
        if self.remove_punct_checkbox.isChecked():
            for col in df.select_dtypes(include=['object']):
                df[col] = df[col].str.replace(r'[^\w\s]', '', regex=True)
                
        return df
        
    def clean_outliers(self, df):
        """处理异常值"""
        method = self.outlier_method_combo.currentText()
        treat = self.outlier_treat_combo.currentText()
        
        # 只处理数值列
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        
        for col in numeric_cols:
            if method == "标准差法":
                std = self.std_spin.value()
                mean = df[col].mean()
                std_dev = df[col].std()
                lower_bound = mean - std * std_dev
                upper_bound = mean + std * std_dev
                
            elif method == "四分位距法":
                iqr_factor = self.iqr_spin.value()
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - iqr_factor * IQR
                upper_bound = Q3 + iqr_factor * IQR
                
            elif method == "Z-Score法":
                threshold = self.zscore_spin.value()
                z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
                lower_bound = -threshold
                upper_bound = threshold
                # 使用Z-Score直接标记
                outliers = z_scores > threshold
            else:
                continue
                
            if method == "Z-Score法":
                if treat == "删除异常值":
                    df = df[~outliers]
                elif treat == "替换为边界值":
                    df[col] = np.where(outliers, df[col].mean(), df[col])
                elif treat == "替换为中位数":
                    df[col] = np.where(outliers, df[col].median(), df[col])
            else:
                # 标准差法和四分位距法使用边界值
                outliers = (df[col] < lower_bound) | (df[col] > upper_bound)
                
                if treat == "删除异常值":
                    df = df[~outliers]
                elif treat == "替换为边界值":
                    df[col] = np.where(df[col] < lower_bound, lower_bound, df[col])
                    df[col] = np.where(df[col] > upper_bound, upper_bound, df[col])
                elif treat == "替换为中位数":
                    df[col] = np.where(outliers, df[col].median(), df[col])
                    
        return df
        
    def apply_custom_rules(self, df):
        """应用自定义规则"""
        rules = []
        
        # 收集规则
        for row in range(self.custom_rules_table.rowCount()):
            column_combo = self.custom_rules_table.cellWidget(row, 0)
            operation_combo = self.custom_rules_table.cellWidget(row, 1)
            condition_item = self.custom_rules_table.item(row, 2)
            replace_item = self.custom_rules_table.item(row, 3)
            
            if column_combo and operation_combo and condition_item and replace_item:
                column = column_combo.currentText()
                operation = operation_combo.currentText()
                condition = condition_item.text()
                replace_value = replace_item.text()
                
                if column and operation and condition:
                    rules.append({
                        'column': column,
                        'operation': operation,
                        'condition': condition,
                        'replace_value': replace_value
                    })
        
        # 应用规则
        for rule in rules:
            column = rule['column']
            operation = rule['operation']
            condition = rule['condition']
            replace_value = rule['replace_value']
            
            if column not in df.columns:
                continue
                
            if operation == "替换":
                df[column] = df[column].replace(condition, replace_value)
            elif operation == "过滤":
                try:
                    if ">" in condition:
                        val = float(condition.replace(">", "").strip())
                        df = df[df[column] > val]
                    elif "<" in condition:
                        val = float(condition.replace("<", "").strip())
                        df = df[df[column] < val]
                    elif "=" in condition:
                        val = condition.replace("=", "").strip()
                        df = df[df[column] == val]
                    elif "!=" in condition:
                        val = condition.replace("!=", "").strip()
                        df = df[df[column] != val]
                except:
                    continue
            elif operation == "删除":
                df = df[df[column] != condition]
            elif operation == "转换":
                # 简单转换示例：转大写
                df[column] = df[column].astype(str).str.upper()
                
        return df
        
    def update_progress(self, current, total, status):
        """更新进度"""
        self.operation.progress.update_progress(current, total, status)
        
    def cleaning_finished(self, success, message):
        """数据清洗完成"""
        self.operation.set_running_state(False)
        if success:
            self.show_info(message)
        else:
            self.show_error(message)
            
        # 更新列选择框
        if self.df is not None:
            columns = self.df.columns.tolist()
            self.type_column_combo.clear()
            self.type_column_combo.addItems(columns)
            self.date_column_combo.clear()
            self.date_column_combo.addItems(columns)
            
            # 更新自定义规则的列选择框
            for row in range(self.custom_rules_table.rowCount()):
                column_combo = self.custom_rules_table.cellWidget(row, 0)
                if column_combo:
                    column_combo.clear()
                    column_combo.addItems(columns)


class DataPreviewWidget(QWidget):
    """数据预览组件"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 标题
        title_label = QLabel("数据预览")
        layout.addWidget(title_label)
        
        # 表格
        self.table = QTableWidget()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)
        
    def update_data(self, df):
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
        
        # 更新标题
        self.findChild(QLabel).setText(f"数据预览 (共 {len(df)} 行，显示前100行)")


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = DataCleanWindow()
    window.show()
    sys.exit(app.exec())