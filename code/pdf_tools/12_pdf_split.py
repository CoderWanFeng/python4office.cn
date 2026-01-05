#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PDF拆分工具
功能：将PDF文件按指定方式拆分为多个文件，支持多种拆分模式
"""

import sys
import os
from PyPDF2 import PdfReader, PdfWriter
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                              QPushButton, QRadioButton, QButtonGroup,
                              QSpinBox, QCheckBox, QFileDialog, QMessageBox)
from PySide6.QtCore import QTimer, Qt

# 添加父目录到路径，以便导入common模块
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.ui_base import BaseMainWindow, FileSelectionWidget, OperationWidget


class PdfSplitWindow(BaseMainWindow):
    """PDF拆分工具主窗口"""
    
    def __init__(self):
        super().__init__("PDF拆分工具", 900, 650)
        
    def setup_content(self):
        """设置内容区域"""
        # 文件选择组件
        self.file_selector = FileSelectionWidget("选择要拆分的PDF文件", multi_selection=False)
        self.file_selector.select_files = self.load_pdf_file  # 重写选择文件方法
        self.content_layout.addWidget(self.file_selector)
        
        # 拆分选项组件
        self.split_options = SplitOptionsWidget()
        self.content_layout.addWidget(self.split_options)
        
        # 操作区域
        self.operation = OperationWidget("拆分操作")
        self.operation.start_operation = self.start_split
        self.operation.signals.progress.connect(self.update_progress)
        self.operation.signals.finished.connect(self.split_finished)
        self.content_layout.addWidget(self.operation)
        
    def load_pdf_file(self):
        """加载PDF文件"""
        files = QFileDialog.getOpenFileNames(self, "选择PDF文件", "", "PDF文件 (*.pdf)")[0]
        
        if not files:
            return
            
        file_path = files[0]
        self.file_selector.file_paths = files
        self.file_selector.update_display()
        
        try:
            # 读取PDF文件以获取页数
            pdf_reader = PdfReader(file_path)
            page_count = len(pdf_reader.pages)
            
            # 更新拆分选项
            self.split_options.update_page_count(page_count)
            
            # 更新状态
            self.statusBar().showMessage(f"已加载文件: {os.path.basename(file_path)}, 共 {page_count} 页")
            
        except Exception as e:
            self.show_error(f"加载PDF文件失败: {str(e)}")
            
    def start_split(self):
        """开始拆分操作"""
        files = self.file_selector.get_files()
        if not files:
            self.show_warning("请先选择要拆分的PDF文件")
            return
            
        # 获取拆分选项
        options = self.split_options.get_split_options()
        
        # 获取保存目录
        save_dir = self.get_directory("选择拆分文件保存目录")
        if not save_dir:
            return
            
        # 开始处理
        self.operation.set_running_state(True)
        self.operation.signals.progress.emit(0, 100, "开始拆分PDF文件...")
        
        # 使用定时器异步执行
        QTimer.singleShot(100, lambda: self.process_split(
            files[0], options, save_dir
        ))
        
    def process_split(self, file_path, options, save_dir):
        """处理PDF拆分"""
        try:
            # 读取PDF文件
            pdf_reader = PdfReader(file_path)
            page_count = len(pdf_reader.pages)
            
            # 获取文件名（不含扩展名）
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            split_count = 0
            
            if options["split_mode"] == "by_count":
                # 按页数拆分
                pages_per_file = options["pages_per_file"]
                
                for start_page in range(0, page_count, pages_per_file):
                    if not self.operation.is_running:
                        break
                        
                    end_page = min(start_page + pages_per_file, page_count)
                    split_count += 1
                    
                    self.operation.signals.progress.emit(
                        int(split_count / (page_count / pages_per_file) * 90), 
                        100, 
                        f"正在拆分第 {split_count} 个文件: 页面 {start_page+1}-{end_page}"
                    )
                    
                    # 创建新的PDF写入器
                    pdf_writer = PdfWriter()
                    
                    # 添加页面
                    for page_num in range(start_page, end_page):
                        pdf_writer.add_page(pdf_reader.pages[page_num])
                    
                    # 保存文件
                    file_num = (start_page // pages_per_file) + 1
                    output_path = os.path.join(save_dir, f"{base_name}_第{file_num}部分.pdf")
                    
                    with open(output_path, "wb") as output_file:
                        pdf_writer.write(output_file)
            
            elif options["split_mode"] == "by_range":
                # 按页面范围拆分
                page_ranges = options["page_ranges"]
                
                for i, page_range in enumerate(page_ranges):
                    if not self.operation.is_running:
                        break
                        
                    split_count += 1
                    
                    self.operation.signals.progress.emit(
                        int((i+1) / len(page_ranges) * 90), 
                        100, 
                        f"正在拆分第 {split_count} 个文件: 页面范围 {page_range}"
                    )
                    
                    # 解析页面范围
                    if "-" in page_range:
                        start, end = page_range.split("-")
                        start_page = int(start) - 1  # 转换为0索引
                        end_page = int(end)  # 转换为包含范围
                    else:
                        start_page = int(page_range) - 1  # 转换为0索引
                        end_page = int(page_range)
                    
                    # 确保范围在有效范围内
                    start_page = max(0, start_page)
                    end_page = min(page_count, end_page)
                    
                    if start_page >= end_page or start_page >= page_count:
                        continue  # 无效范围，跳过
                    
                    # 创建新的PDF写入器
                    pdf_writer = PdfWriter()
                    
                    # 添加页面
                    for page_num in range(start_page, end_page):
                        if page_num < page_count:
                            pdf_writer.add_page(pdf_reader.pages[page_num])
                    
                    # 保存文件
                    output_path = os.path.join(save_dir, f"{base_name}_范围{page_range.replace('-', '_')}.pdf")
                    
                    with open(output_path, "wb") as output_file:
                        pdf_writer.write(output_file)
            
            elif options["split_mode"] == "every_page":
                # 每页保存为一个文件
                for page_num in range(page_count):
                    if not self.operation.is_running:
                        break
                        
                    split_count += 1
                    
                    self.operation.signals.progress.emit(
                        int((page_num+1) / page_count * 90), 
                        100, 
                        f"正在拆分第 {split_count} 个文件: 页面 {page_num+1}"
                    )
                    
                    # 创建新的PDF写入器
                    pdf_writer = PdfWriter()
                    
                    # 添加页面
                    pdf_writer.add_page(pdf_reader.pages[page_num])
                    
                    # 保存文件
                    output_path = os.path.join(save_dir, f"{base_name}_第{page_num+1}页.pdf")
                    
                    with open(output_path, "wb") as output_file:
                        pdf_writer.write(output_file)
            
            elif options["split_mode"] == "by_bookmark":
                # 按书签拆分（需要实现书签解析）
                self.split_by_bookmarks(pdf_reader, base_name, save_dir)
            
            # 完成
            if self.operation.is_running:
                message = f"拆分完成，共生成 {split_count} 个PDF文件"
                self.operation.signals.finished.emit(True, message)
            else:
                self.operation.signals.finished.emit(False, "用户取消操作")
                
        except Exception as e:
            self.operation.signals.finished.emit(False, f"拆分过程中发生错误: {str(e)}")
            
    def split_by_bookmarks(self, pdf_reader, base_name, save_dir):
        """按书签拆分PDF（简单实现）"""
        try:
            # 这是一个简单的书签拆分实现
            # 实际应用中可能需要更复杂的书签解析
            from PyPDF2.generic import Destination
            
            if not hasattr(pdf_reader, 'outline') or not pdf_reader.outline:
                # 没有书签，改为按页数拆分
                page_count = len(pdf_reader.pages)
                pages_per_file = max(1, page_count // 5)  # 默认分成5部分
                
                for start_page in range(0, page_count, pages_per_file):
                    end_page = min(start_page + pages_per_file, page_count)
                    
                    pdf_writer = PdfWriter()
                    
                    for page_num in range(start_page, end_page):
                        pdf_writer.add_page(pdf_reader.pages[page_num])
                    
                    file_num = (start_page // pages_per_file) + 1
                    output_path = os.path.join(save_dir, f"{base_name}_书签{file_num}.pdf")
                    
                    with open(output_path, "wb") as output_file:
                        pdf_writer.write(output_file)
            
        except Exception as e:
            print(f"按书签拆分失败: {str(e)}")
            # 改为按页数拆分
            page_count = len(pdf_reader.pages)
            pages_per_file = max(1, page_count // 5)
            
            for start_page in range(0, page_count, pages_per_file):
                end_page = min(start_page + pages_per_file, page_count)
                
                pdf_writer = PdfWriter()
                
                for page_num in range(start_page, end_page):
                    pdf_writer.add_page(pdf_reader.pages[page_num])
                
                file_num = (start_page // pages_per_file) + 1
                output_path = os.path.join(save_dir, f"{base_name}_部分{file_num}.pdf")
                
                with open(output_path, "wb") as output_file:
                    pdf_writer.write(output_file)
            
    def update_progress(self, current, total, status):
        """更新进度"""
        self.operation.progress.update_progress(current, total, status)
        
    def split_finished(self, success, message):
        """拆分完成"""
        self.operation.set_running_state(False)
        if success:
            self.show_info(message)
        else:
            self.show_error(message)


class SplitOptionsWidget(QWidget):
    """拆分选项组件"""
    
    def __init__(self):
        super().__init__()
        self.page_count = 0
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 拆分模式选择
        mode_group = QWidget()
        mode_layout = QVBoxLayout(mode_group)
        mode_layout.addWidget(QLabel("拆分模式:"))
        
        self.split_group = QButtonGroup()
        
        self.by_count_radio = QRadioButton("按页数拆分")
        self.by_count_radio.setChecked(True)
        self.split_group.addButton(self.by_count_radio, 0)
        self.by_count_radio.toggled.connect(self.toggle_mode_options)
        mode_layout.addWidget(self.by_count_radio)
        
        self.by_range_radio = QRadioButton("按页面范围拆分")
        self.split_group.addButton(self.by_range_radio, 1)
        self.by_range_radio.toggled.connect(self.toggle_mode_options)
        mode_layout.addWidget(self.by_range_radio)
        
        self.every_page_radio = QRadioButton("每页保存为一个文件")
        self.split_group.addButton(self.every_page_radio, 2)
        self.every_page_radio.toggled.connect(self.toggle_mode_options)
        mode_layout.addWidget(self.every_page_radio)
        
        self.by_bookmark_radio = QRadioButton("按书签拆分")
        self.split_group.addButton(self.by_bookmark_radio, 3)
        self.by_bookmark_radio.toggled.connect(self.toggle_mode_options)
        mode_layout.addWidget(self.by_bookmark_radio)
        
        layout.addWidget(mode_group)
        
        # 拆分参数
        params_group = QWidget()
        self.params_layout = QVBoxLayout(params_group)
        params_layout.addWidget(QLabel("拆分参数:"))
        
        # 按页数拆分参数
        self.count_layout = QHBoxLayout()
        self.count_layout.addWidget(QLabel("每个文件页数:"))
        self.pages_per_file_spin = QSpinBox()
        self.pages_per_file_spin.setMinimum(1)
        self.pages_per_file_spin.setValue(5)
        self.count_layout.addWidget(self.pages_per_file_spin)
        self.params_layout.addLayout(self.count_layout)
        
        # 按页面范围拆分参数
        self.range_layout = QVBoxLayout()
        self.range_layout.addWidget(QLabel("页面范围 (每行一个):"))
        self.page_ranges_input = QLineEdit()
        self.page_ranges_input.setPlaceholderText("例如: 1-5, 7, 9-12")
        self.range_layout.addWidget(self.page_ranges_input)
        self.params_layout.addLayout(self.range_layout)
        
        # 添加范围按钮
        self.add_range_btn = QPushButton("添加常用范围")
        self.add_range_btn.clicked.connect(self.add_common_ranges)
        self.params_layout.addWidget(self.add_range_btn)
        
        layout.addWidget(params_group)
        
        # 其他选项
        other_group = QWidget()
        other_layout = QVBoxLayout(other_group)
        other_layout.addWidget(QLabel("其他选项:"))
        
        self.add_suffix_checkbox = QCheckBox("在文件名后添加页码范围")
        self.add_suffix_checkbox.setChecked(True)
        other_layout.addWidget(self.add_suffix_checkbox)
        
        layout.addWidget(other_group)
        
        # 初始化控件状态
        self.toggle_mode_options(self.by_count_radio.isChecked())
        
    def toggle_mode_options(self, checked):
        """根据拆分模式切换选项可用性"""
        mode_id = self.split_group.checkedId()
        
        # 默认隐藏所有选项
        self.count_layout.parent().setEnabled(False)
        self.range_layout.parent().setEnabled(False)
        self.add_range_btn.setEnabled(False)
        
        if mode_id == 0:  # 按页数拆分
            self.count_layout.parent().setEnabled(True)
        elif mode_id == 1:  # 按页面范围拆分
            self.range_layout.parent().setEnabled(True)
            self.add_range_btn.setEnabled(True)
        # 其他模式不需要额外参数
            
    def update_page_count(self, count):
        """更新页数显示"""
        self.page_count = count
        
        # 可以根据页数自动调整默认值
        if count > 0:
            # 默认每个文件5页，但不超过总页数
            self.pages_per_file_spin.setMaximum(count)
            if count < 5:
                self.pages_per_file_spin.setValue(max(1, count // 2))
            else:
                self.pages_per_file_spin.setValue(5)
                
    def add_common_ranges(self):
        """添加常用页面范围"""
        if self.page_count <= 0:
            return
            
        # 生成平均分割的页面范围
        ranges = []
        pages_per_range = max(1, self.page_count // 4)  # 默认分成4部分
        
        for start in range(1, self.page_count + 1, pages_per_range):
            end = min(start + pages_per_range - 1, self.page_count)
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}-{end}")
        
        self.page_ranges_input.setText(", ".join(ranges))
        
    def get_split_options(self):
        """获取拆分选项"""
        mode_id = self.split_group.checkedId()
        mode_map = {0: "by_count", 1: "by_range", 2: "every_page", 3: "by_bookmark"}
        
        # 解析页面范围
        page_ranges = []
        if mode_id == 1:  # 按页面范围拆分
            range_text = self.page_ranges_input.text().strip()
            if range_text:
                ranges = range_text.split(",")
                for r in ranges:
                    r = r.strip()
                    if r:
                        page_ranges.append(r)
        
        return {
            "split_mode": mode_map.get(mode_id, "by_count"),
            "pages_per_file": self.pages_per_file_spin.value(),
            "page_ranges": page_ranges,
            "add_suffix": self.add_suffix_checkbox.isChecked()
        }


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = PdfSplitWindow()
    window.show()
    sys.exit(app.exec())