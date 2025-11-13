#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PDF合并工具
功能：合并多个PDF文件到一个PDF中，支持自定义合并顺序和合并方式
"""

import sys
import os
from PyPDF2 import PdfReader, PdfWriter
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
                              QListWidget, QListWidgetItem, QFileDialog, 
                              QMessageBox, QAbstractItemView)
from PySide6.QtCore import QTimer, Qt

# 添加父目录到路径，以便导入common模块
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.ui_base import BaseMainWindow, FileSelectionWidget, OperationWidget


class PdfMergeWindow(BaseMainWindow):
    """PDF合并工具主窗口"""
    
    def __init__(self):
        super().__init__("PDF合并工具", 900, 650)
        
    def setup_content(self):
        """设置内容区域"""
        # 文件选择组件
        self.file_selector = FileSelectionWidget("选择要合并的PDF文件", multi_selection=True)
        self.file_selector.select_files = self.add_files  # 重写选择文件方法
        self.content_layout.addWidget(self.file_selector)
        
        # 文件列表和顺序调整组件
        self.file_list_widget = FileListWidget()
        self.content_layout.addWidget(self.file_list_widget)
        
        # 合并选项组件
        self.merge_options = MergeOptionsWidget()
        self.content_layout.addWidget(self.merge_options)
        
        # 操作区域
        self.operation = OperationWidget("合并操作")
        self.operation.start_operation = self.start_merge
        self.operation.signals.progress.connect(self.update_progress)
        self.operation.signals.finished.connect(self.merge_finished)
        self.content_layout.addWidget(self.operation)
        
    def add_files(self):
        """添加文件到列表"""
        files = QFileDialog.getOpenFileNames(self, "选择PDF文件", "", "PDF文件 (*.pdf)")[0]
        
        if not files:
            return
            
        for file_path in files:
            self.file_list_widget.add_file(file_path)
            
        # 更新文件选择显示
        self.file_selector.file_paths = self.file_list_widget.get_files()
        self.file_selector.update_display()
        
    def start_merge(self):
        """开始合并操作"""
        files = self.file_list_widget.get_files()
        if not files:
            self.show_warning("请先选择要合并的PDF文件")
            return
            
        # 获取合并选项
        options = self.merge_options.get_merge_options()
        
        # 获取保存路径
        save_path = self.get_save_path("保存合并后的PDF文件", "PDF文件 (*.pdf)", "合并文档.pdf")
        if not save_path:
            return
            
        # 开始处理
        self.operation.set_running_state(True)
        self.operation.signals.progress.emit(0, 100, "开始合并PDF文件...")
        
        # 使用定时器异步执行
        QTimer.singleShot(100, lambda: self.process_merge(
            files, options, save_path
        ))
        
    def process_merge(self, files, options, save_path):
        """处理PDF合并"""
        try:
            pdf_writer = PdfWriter()
            total_files = len(files)
            
            for i, file_path in enumerate(files):
                if not self.operation.is_running:
                    break
                    
                self.operation.signals.progress.emit(
                    int(i / total_files * 90), 
                    100, 
                    f"正在合并: {os.path.basename(file_path)}"
                )
                
                try:
                    # 读取PDF文件
                    pdf_reader = PdfReader(file_path)
                    
                    # 根据选项添加页面
                    if options["include_all_pages"]:
                        # 包含所有页面
                        for page_num in range(len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num]
                            
                            # 应用页面处理选项
                            if options["apply_rotation"]:
                                # 旋转页面（如果有旋转值）
                                if hasattr(page, '/Rotate') and page['/Rotate']:
                                    rotation = int(page['/Rotate'])
                                    if rotation not in [0, 360]:
                                        page = page.rotate(rotation % 360)
                            
                            pdf_writer.add_page(page)
                    else:
                        # 只包含指定页面
                        page_ranges = options["page_ranges"]
                        if page_ranges:
                            for page_range in page_ranges:
                                if "-" in page_range:
                                    start, end = page_range.split("-")
                                    start_page = int(start) - 1  # 转换为0索引
                                    end_page = int(end)  # 转换为包含范围
                                    
                                    # 确保范围在有效范围内
                                    start_page = max(0, start_page)
                                    end_page = min(len(pdf_reader.pages), end_page)
                                    
                                    for page_num in range(start_page, end_page):
                                        if page_num < len(pdf_reader.pages):
                                            page = pdf_reader.pages[page_num]
                                            
                                            # 应用页面处理选项
                                            if options["apply_rotation"]:
                                                if hasattr(page, '/Rotate') and page['/Rotate']:
                                                    rotation = int(page['/Rotate'])
                                                    if rotation not in [0, 360]:
                                                        page = page.rotate(rotation % 360)
                                            
                                            pdf_writer.add_page(page)
                                else:
                                    # 单页
                                    page_num = int(page_range) - 1  # 转换为0索引
                                    if 0 <= page_num < len(pdf_reader.pages):
                                        page = pdf_reader.pages[page_num]
                                        
                                        # 应用页面处理选项
                                        if options["apply_rotation"]:
                                            if hasattr(page, '/Rotate') and page['/Rotate']:
                                                rotation = int(page['/Rotate'])
                                                if rotation not in [0, 360]:
                                                    page = page.rotate(rotation % 360)
                                        
                                        pdf_writer.add_page(page)
                        
                except Exception as e:
                    self.operation.signals.finished.emit(False, f"处理文件 {os.path.basename(file_path)} 时出错: {str(e)}")
                    return
            
            # 添加元数据（如果需要）
            if options["add_metadata"]:
                pdf_writer.add_metadata({
                    '/Title': options["title"] or "合并文档",
                    '/Author': options["author"] or "PDF合并工具",
                    '/Subject': options["subject"] or "合并的PDF文档",
                    '/Creator': "PDF合并工具",
                    '/Producer': "PDF合并工具"
                })
            
            # 保存合并后的PDF
            self.operation.signals.progress.emit(90, 100, "正在保存合并后的PDF...")
            
            with open(save_path, "wb") as output_file:
                pdf_writer.write(output_file)
            
            # 完成
            if self.operation.is_running:
                message = f"合并完成，共合并 {total_files} 个PDF文件"
                self.operation.signals.finished.emit(True, message)
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


class FileListWidget(QWidget):
    """文件列表组件，支持拖拽排序"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 标题和按钮
        header_layout = QHBoxLayout()
        header_layout.addWidget(QLabel("文件列表 (可拖拽调整顺序):"))
        
        self.add_file_btn = QPushButton("添加文件")
        self.add_file_btn.clicked.connect(self.add_files)
        header_layout.addWidget(self.add_file_btn)
        
        self.remove_file_btn = QPushButton("删除选中")
        self.remove_file_btn.clicked.connect(self.remove_selected_file)
        header_layout.addWidget(self.remove_file_btn)
        
        self.clear_btn = QPushButton("清空列表")
        self.clear_btn.clicked.connect(self.clear_files)
        header_layout.addWidget(self.clear_btn)
        
        layout.addLayout(header_layout)
        
        # 文件列表
        self.file_list = QListWidget()
        self.file_list.setDragDropMode(QAbstractItemView.InternalMove)
        self.file_list.setSelectionMode(QAbstractItemView.SingleSelection)
        layout.addWidget(self.file_list)
        
    def add_files(self):
        """添加文件"""
        files = QFileDialog.getOpenFileNames(self, "选择PDF文件", "", "PDF文件 (*.pdf)")[0]
        
        if not files:
            return
            
        for file_path in files:
            self.add_file(file_path)
            
    def add_file(self, file_path):
        """添加单个文件"""
        # 检查是否已存在
        for i in range(self.file_list.count()):
            item = self.file_list.item(i)
            if item.data(Qt.UserRole) == file_path:
                return  # 已存在，不添加
                
        # 添加到列表
        item = QListWidgetItem(os.path.basename(file_path))
        item.setData(Qt.UserRole, file_path)
        self.file_list.addItem(item)
        
    def remove_selected_file(self):
        """删除选中的文件"""
        current_row = self.file_list.currentRow()
        if current_row >= 0:
            self.file_list.takeItem(current_row)
            
    def clear_files(self):
        """清空文件列表"""
        self.file_list.clear()
        
    def get_files(self):
        """获取文件路径列表（按列表顺序）"""
        files = []
        for i in range(self.file_list.count()):
            item = self.file_list.item(i)
            files.append(item.data(Qt.UserRole))
        return files


class MergeOptionsWidget(QWidget):
    """合并选项组件"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 页面选择
        page_group = QWidget()
        page_layout = QVBoxLayout(page_group)
        page_layout.addWidget(QLabel("页面选择:"))
        
        self.include_all_radio = QRadioButton("包含所有页面")
        self.include_all_radio.setChecked(True)
        self.include_all_radio.toggled.connect(self.toggle_page_options)
        page_layout.addWidget(self.include_all_radio)
        
        self.include_specific_radio = QRadioButton("只包含指定页面")
        self.include_specific_radio.toggled.connect(self.toggle_page_options)
        page_layout.addWidget(self.include_specific_radio)
        
        # 页面范围输入
        self.page_ranges_input = QLineEdit()
        self.page_ranges_input.setPlaceholderText("例如: 1-5, 7, 9-12")
        self.page_ranges_input.setEnabled(False)
        page_layout.addWidget(self.page_ranges_input)
        
        page_help = QLabel("格式说明: 使用逗号分隔范围，例如 1-5 表示1到5页")
        page_help.setStyleSheet("color: #888; font-size: 12px;")
        page_layout.addWidget(page_help)
        
        layout.addWidget(page_group)
        
        # 页面处理
        process_group = QWidget()
        process_layout = QVBoxLayout(process_group)
        process_layout.addWidget(QLabel("页面处理:"))
        
        self.apply_rotation_checkbox = QCheckBox("应用页面旋转")
        self.apply_rotation_checkbox.setChecked(True)
        process_layout.addWidget(self.apply_rotation_checkbox)
        
        layout.addWidget(process_group)
        
        # 元数据选项
        metadata_group = QWidget()
        metadata_layout = QVBoxLayout(metadata_group)
        metadata_layout.addWidget(QLabel("元数据设置:"))
        
        self.add_metadata_checkbox = QCheckBox("添加元数据")
        self.add_metadata_checkbox.toggled.connect(self.toggle_metadata_options)
        metadata_layout.addWidget(self.add_metadata_checkbox)
        
        # 元数据输入
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("文档标题")
        self.title_input.setEnabled(False)
        metadata_layout.addWidget(self.title_input)
        
        self.author_input = QLineEdit()
        self.author_input.setPlaceholderText("作者")
        self.author_input.setEnabled(False)
        metadata_layout.addWidget(self.author_input)
        
        self.subject_input = QLineEdit()
        self.subject_input.setPlaceholderText("主题")
        self.subject_input.setEnabled(False)
        metadata_layout.addWidget(self.subject_input)
        
        layout.addWidget(metadata_group)
        
    def toggle_page_options(self, all_pages_checked):
        """切换页面选项"""
        self.include_specific_radio.setChecked(not all_pages_checked)
        self.page_ranges_input.setEnabled(not all_pages_checked)
        
    def toggle_metadata_options(self, enabled):
        """切换元数据选项"""
        self.title_input.setEnabled(enabled)
        self.author_input.setEnabled(enabled)
        self.subject_input.setEnabled(enabled)
        
    def get_merge_options(self):
        """获取合并选项"""
        page_ranges = []
        if self.include_specific_radio.isChecked():
            # 解析页面范围
            range_text = self.page_ranges_input.text().strip()
            if range_text:
                ranges = range_text.split(",")
                for r in ranges:
                    r = r.strip()
                    if r:
                        page_ranges.append(r)
        
        return {
            "include_all_pages": self.include_all_radio.isChecked(),
            "page_ranges": page_ranges,
            "apply_rotation": self.apply_rotation_checkbox.isChecked(),
            "add_metadata": self.add_metadata_checkbox.isChecked(),
            "title": self.title_input.text().strip(),
            "author": self.author_input.text().strip(),
            "subject": self.subject_input.text().strip()
        }


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = PdfMergeWindow()
    window.show()
    sys.exit(app.exec())