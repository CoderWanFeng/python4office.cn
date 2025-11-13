#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Excel表格合并工具
功能：合并多个Excel文件到一个工作簿中，支持将不同文件的合并到同一个工作表或不同工作表
"""

import sys
import os
import pandas as pd
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QCheckBox, QRadioButton, QButtonGroup
from PySide6.QtCore import QTimer

# 添加父目录到路径，以便导入common模块
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.ui_base import BaseMainWindow, FileSelectionWidget, OperationWidget


class ExcelMergeWindow(BaseMainWindow):
    """Excel表格合并工具主窗口"""
    
    def __init__(self):
        super().__init__("Excel表格合并工具", 900, 650)
        
    def setup_content(self):
        """设置内容区域"""
        # 文件选择组件
        self.file_selector = FileSelectionWidget("选择要合并的Excel文件", multi_selection=True)
        self.content_layout.addWidget(self.file_selector)
        
        # 合并选项组件
        self.merge_options = MergeOptionsWidget()
        self.content_layout.addWidget(self.merge_options)
        
        # 操作区域
        self.operation = OperationWidget("合并操作")
        self.operation.start_operation = self.start_merge
        self.operation.signals.progress.connect(self.update_progress)
        self.operation.signals.finished.connect(self.merge_finished)
        self.content_layout.addWidget(self.operation)
        
    def start_merge(self):
        """开始合并操作"""
        files = self.file_selector.get_files()
        if not files:
            self.show_warning("请先选择要合并的Excel文件")
            return
            
        # 获取保存路径
        save_path = self.get_save_path("保存合并后的Excel文件", "Excel文件 (*.xlsx)", "合并结果.xlsx")
        if not save_path:
            return
            
        # 获取合并选项
        merge_mode = self.merge_options.get_merge_mode()
        sheet_name = self.merge_options.get_sheet_name()
        add_source = self.merge_options.add_source_info()
        
        # 开始处理
        self.operation.set_running_state(True)
        self.operation.signals.progress.emit(0, 100, "开始合并Excel文件...")
        
        # 使用定时器异步执行，避免界面冻结
        QTimer.singleShot(100, lambda: self.process_files(
            files, save_path, merge_mode, sheet_name, add_source
        ))
        
    def process_files(self, files, save_path, merge_mode, sheet_name, add_source):
        """处理文件合并"""
        try:
            total_files = len(files)
            all_data = []
            
            # 读取所有文件
            for i, file_path in enumerate(files):
                if not self.operation.is_running:
                    break
                    
                self.operation.signals.progress.emit(
                    int((i + 1) / total_files * 50), 
                    100, 
                    f"正在读取文件: {os.path.basename(file_path)}"
                )
                
                try:
                    # 读取Excel文件
                    if merge_mode == "single_sheet":
                        # 读取第一个工作表
                        df = pd.read_excel(file_path)
                        if add_source:
                            df["来源文件"] = os.path.basename(file_path)
                        all_data.append(df)
                    else:
                        # 读取所有工作表（在后续步骤中处理）
                        pass
                except Exception as e:
                    self.operation.signals.finished.emit(False, f"读取文件 {os.path.basename(file_path)} 失败: {str(e)}")
                    return
            
            if not self.operation.is_running:
                self.operation.signals.finished.emit(False, "用户取消操作")
                return
                
            # 执行合并
            self.operation.signals.progress.emit(50, 100, "正在合并数据...")
            
            if merge_mode == "single_sheet":
                # 合并到单个工作表
                if all_data:
                    merged_df = pd.concat(all_data, ignore_index=True)
                    merged_df.to_excel(save_path, index=False, sheet_name=sheet_name)
            else:
                # 合并到不同工作表
                with pd.ExcelWriter(save_path) as writer:
                    for i, file_path in enumerate(files):
                        try:
                            # 读取文件的所有工作表
                            xl_file = pd.ExcelFile(file_path)
                            for sheet in xl_file.sheet_names:
                                df = pd.read_excel(file_path, sheet_name=sheet)
                                # 为避免工作表名称冲突，添加文件前缀
                                sheet_prefixed = f"{os.path.basename(file_path).split('.')[0]}_{sheet}"[:31]
                                df.to_excel(writer, sheet_name=sheet_prefixed, index=False)
                        except Exception as e:
                            self.operation.signals.finished.emit(False, f"处理文件 {os.path.basename(file_path)} 的工作表时出错: {str(e)}")
                            return
            
            # 完成
            if self.operation.is_running:
                self.operation.signals.finished.emit(True, f"成功合并 {total_files} 个Excel文件到: {save_path}")
            else:
                self.operation.signals.finished.emit(False, "用户取消操作")
                
        except Exception as e:
            self.operation.signals.finished.emit(False, f"合并过程中发生错误: {str(e)}")
            
    def update_progress(self, current, total, status):
        """更新进度"""
        self.operation.progress.update_progress(current, total, status)
        
    def merge_finished(self, success, message):
        """合并完成"""
        self.operation.set_running_state(False)
        if success:
            self.show_info(message)
        else:
            self.show_error(message)


class MergeOptionsWidget(OperationWidget):
    """合并选项组件"""
    
    def __init__(self):
        super().__init__("合并选项")
        # 不使用父类的进度条等组件，只保留参数设置部分
        self.setup_params()
        
    def setup_params(self):
        """设置参数控件"""
        # 清空默认布局
        for i in reversed(range(self.param_layout.count())): 
            self.param_layout.itemAt(i).widget().setParent(None)
        
        # 合并模式选择
        mode_label = QLabel("合并模式:")
        self.param_layout.addWidget(mode_label)
        
        self.mode_group = QButtonGroup()
        self.single_sheet_radio = QRadioButton("合并到单个工作表")
        self.single_sheet_radio.setChecked(True)
        self.multi_sheet_radio = QRadioButton("合并到不同工作表")
        
        self.mode_group.addButton(self.single_sheet_radio, 0)
        self.mode_group.addButton(self.multi_sheet_radio, 1)
        
        self.param_layout.addWidget(self.single_sheet_radio)
        self.param_layout.addWidget(self.multi_sheet_radio)
        
        # 工作表名称（仅对单个工作表模式）
        self.sheet_name_layout = QHBoxLayout()
        self.sheet_name_layout.addWidget(QLabel("工作表名称:"))
        self.sheet_name_input = QLineEdit("合并数据")
        self.sheet_name_input.setPlaceholderText("输入工作表名称")
        self.sheet_name_layout.addWidget(self.sheet_name_input)
        self.param_layout.addLayout(self.sheet_name_layout)
        
        # 添加来源信息选项（仅对单个工作表模式）
        self.add_source_checkbox = QCheckBox("添加来源文件信息列")
        self.add_source_checkbox.setChecked(True)
        self.param_layout.addWidget(self.add_source_checkbox)
        
        # 连接信号
        self.single_sheet_radio.toggled.connect(self.toggle_options)
        
        # 隐藏进度条和按钮，因为这些在父类OperationWidget中已经处理
        self.progress.hide()
        self.start_btn.hide()
        self.cancel_btn.hide()
        
    def toggle_options(self, checked):
        """根据模式切换可用选项"""
        self.sheet_name_input.setEnabled(checked)
        self.add_source_checkbox.setEnabled(checked)
        
    def get_merge_mode(self):
        """获取合并模式"""
        return "single_sheet" if self.single_sheet_radio.isChecked() else "multi_sheet"
        
    def get_sheet_name(self):
        """获取工作表名称"""
        return self.sheet_name_input.text() or "合并数据"
        
    def add_source_info(self):
        """是否添加来源信息"""
        return self.add_source_checkbox.isChecked()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExcelMergeWindow()
    window.show()
    sys.exit(app.exec())