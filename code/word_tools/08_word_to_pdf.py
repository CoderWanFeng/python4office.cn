#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Word文档转PDF工具
功能：将Word文档批量转换为PDF格式，支持多种转换选项和批量处理
"""

import sys
import os
import subprocess
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                              QPushButton, QCheckBox, QRadioButton, QButtonGroup,
                              QSpinBox, QMessageBox, QFileDialog)
from PySide6.QtCore import QTimer, QStandardPaths

# 添加父目录到路径，以便导入common模块
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.ui_base import BaseMainWindow, FileSelectionWidget, OperationWidget


class WordToPdfWindow(BaseMainWindow):
    """Word文档转PDF工具主窗口"""
    
    def __init__(self):
        super().__init__("Word文档转PDF工具", 900, 650)
        
    def setup_content(self):
        """设置内容区域"""
        # 文件选择组件
        self.file_selector = FileSelectionWidget("选择要转换的Word文件", multi_selection=True)
        self.content_layout.addWidget(self.file_selector)
        
        # 转换选项组件
        self.convert_options = ConvertOptionsWidget()
        self.content_layout.addWidget(self.convert_options)
        
        # 操作区域
        self.operation = OperationWidget("转换操作")
        self.operation.start_operation = self.start_conversion
        self.operation.signals.progress.connect(self.update_progress)
        self.operation.signals.finished.connect(self.conversion_finished)
        self.content_layout.addWidget(self.operation)
        
    def start_conversion(self):
        """开始转换操作"""
        files = self.file_selector.get_files()
        if not files:
            self.show_warning("请先选择要转换的Word文件")
            return
            
        # 获取转换选项
        options = self.convert_options.get_convert_options()
        
        # 确定输出目录
        if options["output_to_source"]:
            # 输出到源文件所在目录
            output_dir = None
        else:
            # 选择输出目录
            output_dir = self.get_directory("选择PDF输出目录")
            if not output_dir:
                return
                
        # 开始处理
        self.operation.set_running_state(True)
        self.operation.signals.progress.emit(0, 100, "开始转换Word文档...")
        
        # 使用定时器异步执行
        QTimer.singleShot(100, lambda: self.process_files(
            files, options, output_dir
        ))
        
    def process_files(self, files, options, output_dir):
        """处理文件转换"""
        try:
            total_files = len(files)
            converted_files = 0
            
            for i, file_path in enumerate(files):
                if not self.operation.is_running:
                    break
                    
                self.operation.signals.progress.emit(
                    int(i / total_files * 90), 
                    100, 
                    f"正在转换: {os.path.basename(file_path)}"
                )
                
                try:
                    # 确定输出路径
                    if options["output_to_source"]:
                        # 输出到源文件所在目录
                        source_dir = os.path.dirname(file_path)
                        base_name = os.path.splitext(os.path.basename(file_path))[0]
                        output_path = os.path.join(source_dir, f"{base_name}.pdf")
                    else:
                        # 输出到指定目录
                        base_name = os.path.splitext(os.path.basename(file_path))[0]
                        output_path = os.path.join(output_dir, f"{base_name}.pdf")
                    
                    # 转换方法
                    success = self.convert_word_to_pdf(file_path, output_path, options)
                    
                    if success:
                        converted_files += 1
                    else:
                        self.operation.signals.finished.emit(False, f"转换文件 {os.path.basename(file_path)} 失败")
                        return
                        
                except Exception as e:
                    self.operation.signals.finished.emit(False, f"处理文件 {os.path.basename(file_path)} 时出错: {str(e)}")
                    return
            
            # 完成
            if self.operation.is_running:
                message = f"转换完成，共转换 {converted_files}/{total_files} 个Word文档"
                self.operation.signals.finished.emit(True, message)
            else:
                self.operation.signals.finished.emit(False, "用户取消操作")
                
        except Exception as e:
            self.operation.signals.finished.emit(False, f"转换过程中发生错误: {str(e)}")
            
    def convert_word_to_pdf(self, word_path, pdf_path, options):
        """转换Word文档为PDF"""
        try:
            # 方法1: 使用LibreOffice (跨平台)
            if options["convert_method"] == "libreoffice":
                return self.convert_with_libreoffice(word_path, pdf_path, options)
            # 方法2: 使用Win32 COM (仅Windows)
            elif options["convert_method"] == "win32com" and sys.platform == "win32":
                return self.convert_with_win32com(word_path, pdf_path, options)
            # 方法3: 使用docx2pdf (需要额外安装)
            elif options["convert_method"] == "docx2pdf":
                return self.convert_with_docx2pdf(word_path, pdf_path, options)
            # 默认尝试LibreOffice
            else:
                return self.convert_with_libreoffice(word_path, pdf_path, options)
        except Exception as e:
            print(f"转换错误: {str(e)}")
            return False
            
    def convert_with_libreoffice(self, word_path, pdf_path, options):
        """使用LibreOffice转换"""
        try:
            # 获取输出目录
            output_dir = os.path.dirname(pdf_path)
            
            # 构建命令
            if sys.platform == "win32":
                # Windows
                libreoffice_path = self.find_libreoffice_path()
                if not libreoffice_path:
                    self.operation.signals.finished.emit(False, "未找到LibreOffice安装，请安装LibreOffice或使用其他转换方法")
                    return False
                    
                cmd = [
                    libreoffice_path,
                    "--headless",
                    "--convert-to", "pdf",
                    "--outdir", output_dir,
                    word_path
                ]
            else:
                # Linux/Mac
                cmd = [
                    "libreoffice",
                    "--headless",
                    "--convert-to", "pdf",
                    "--outdir", output_dir,
                    word_path
                ]
            
            # 执行命令
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            # 检查结果
            if result.returncode == 0:
                # LibreOffice生成的文件名可能与原始文件名不完全一致
                base_name = os.path.splitext(os.path.basename(word_path))[0]
                expected_pdf = os.path.join(output_dir, f"{base_name}.pdf")
                
                if os.path.exists(expected_pdf):
                    return True
                else:
                    # 查找生成的PDF文件
                    for file in os.listdir(output_dir):
                        if file.endswith(".pdf") and base_name in file:
                            # 如果文件名不完全匹配，重命名
                            generated_path = os.path.join(output_dir, file)
                            os.rename(generated_path, pdf_path)
                            return True
                    return False
            else:
                print(f"LibreOffice转换错误: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print("LibreOffice转换超时")
            return False
        except Exception as e:
            print(f"LibreOffice转换异常: {str(e)}")
            return False
            
    def convert_with_win32com(self, word_path, pdf_path, options):
        """使用Win32 COM转换"""
        try:
            import win32com.client
            
            # 创建Word应用程序对象
            word = win32com.client.Dispatch("Word.Application")
            word.Visible = options["show_word"]
            
            # 打开文档
            doc = word.Documents.Open(os.path.abspath(word_path))
            
            # 设置PDF保存选项
            wdFormatPDF = 17  # Word的PDF格式常量
            
            # 保存为PDF
            doc.SaveAs(os.path.abspath(pdf_path), FileFormat=wdFormatPDF)
            
            # 关闭文档和应用程序
            doc.Close()
            word.Quit()
            
            return True
            
        except Exception as e:
            print(f"Win32 COM转换异常: {str(e)}")
            return False
            
    def convert_with_docx2pdf(self, word_path, pdf_path, options):
        """使用docx2pdf转换"""
        try:
            import docx2pdf
            
            # 直接转换
            docx2pdf.convert(word_path, pdf_path)
            
            return True
            
        except Exception as e:
            print(f"docx2pdf转换异常: {str(e)}")
            return False
            
    def find_libreoffice_path(self):
        """查找LibreOffice安装路径"""
        possible_paths = [
            # Windows常见路径
            r"C:\Program Files\LibreOffice\program\soffice.exe",
            r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
            r"C:\Program Files\LibreOffice\program\soffice.com",
            r"C:\Program Files (x86)\LibreOffice\program\soffice.com",
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                return path
                
        return None
        
    def update_progress(self, current, total, status):
        """更新进度"""
        self.operation.progress.update_progress(current, total, status)
        
    def conversion_finished(self, success, message):
        """转换完成"""
        self.operation.set_running_state(False)
        if success:
            self.show_info(message)
        else:
            self.show_error(message)


class ConvertOptionsWidget(QWidget):
    """转换选项组件"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 转换方法选择
        method_group = QWidget()
        method_layout = QVBoxLayout(method_group)
        method_layout.addWidget(QLabel("转换方法:"))
        
        self.method_group = QButtonGroup()
        
        self.libreoffice_radio = QRadioButton("使用LibreOffice (推荐)")
        self.libreoffice_radio.setChecked(True)
        self.method_group.addButton(self.libreoffice_radio, 0)
        method_layout.addWidget(self.libreoffice_radio)
        
        self.win32com_radio = QRadioButton("使用Word COM接口 (仅Windows)")
        if sys.platform == "win32":
            self.method_group.addButton(self.win32com_radio, 1)
            method_layout.addWidget(self.win32com_radio)
        
        self.docx2pdf_radio = QRadioButton("使用docx2pdf库")
        self.method_group.addButton(self.docx2pdf_radio, 2)
        method_layout.addWidget(self.docx2pdf_radio)
        
        # 添加说明
        info_label = QLabel("注意: docx2pdf方法需要额外安装: pip install docx2pdf")
        info_label.setStyleSheet("color: #888; font-size: 12px;")
        method_layout.addWidget(info_label)
        
        layout.addWidget(method_group)
        
        # 输出选项
        output_group = QWidget()
        output_layout = QVBoxLayout(output_group)
        output_layout.addWidget(QLabel("输出选项:"))
        
        self.output_to_source_radio = QRadioButton("输出到源文件所在目录")
        self.output_to_source_radio.setChecked(True)
        output_layout.addWidget(self.output_to_source_radio)
        
        self.output_to_custom_radio = QRadioButton("输出到指定目录")
        output_layout.addWidget(self.output_to_custom_radio)
        
        layout.addWidget(output_group)
        
        # Word显示选项 (仅Win32 COM)
        self.show_word_checkbox = QCheckBox("转换过程中显示Word界面 (仅Win32 COM)")
        layout.addWidget(self.show_word_checkbox)
        
        # 其他选项
        other_group = QWidget()
        other_layout = QVBoxLayout(other_group)
        other_layout.addWidget(QLabel("其他选项:"))
        
        self.skip_existing_checkbox = QCheckBox("跳过已存在的PDF文件")
        other_layout.addWidget(self.skip_existing_checkbox)
        
        self.open_after_convert_checkbox = QCheckBox("转换完成后打开输出目录")
        other_layout.addWidget(self.open_after_convert_checkbox)
        
        layout.addWidget(other_group)
        
        # 连接信号
        self.output_to_source_radio.toggled.connect(self.toggle_custom_dir_option)
        self.win32com_radio.toggled.connect(self.toggle_word_option)
        
        # 初始化控件状态
        self.toggle_custom_dir_option(True)
        self.toggle_word_option(False)
        
    def toggle_custom_dir_option(self, source_checked):
        """切换自定义目录选项可用性"""
        self.output_to_custom_radio.setChecked(not source_checked)
        
    def toggle_word_option(self, win32_checked):
        """切换Word选项可用性"""
        self.show_word_checkbox.setEnabled(win32_checked)
        
    def get_convert_options(self):
        """获取转换选项"""
        method_index = self.method_group.checkedId()
        method_map = {0: "libreoffice", 1: "win32com", 2: "docx2pdf"}
        
        return {
            "convert_method": method_map.get(method_index, "libreoffice"),
            "output_to_source": self.output_to_source_radio.isChecked(),
            "show_word": self.show_word_checkbox.isChecked(),
            "skip_existing": self.skip_existing_checkbox.isChecked(),
            "open_after_convert": self.open_after_convert_checkbox.isChecked()
        }


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = WordToPdfWindow()
    window.show()
    sys.exit(app.exec())