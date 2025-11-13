#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PDF转图片工具
功能：将PDF页面转换为图片格式，支持多种图片格式和分辨率设置
"""

import sys
import os
import tempfile
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                              QPushButton, QComboBox, QSpinBox, QCheckBox,
                              QFileDialog, QMessageBox, QGroupBox)
from PySide6.QtCore import QTimer, Qt

# 添加父目录到路径，以便导入common模块
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.ui_base import BaseMainWindow, FileSelectionWidget, OperationWidget

# 尝试导入PDF转图片的库
try:
    from pdf2image import convert_from_path
    PDF2IMAGE_AVAILABLE = True
except ImportError:
    PDF2IMAGE_AVAILABLE = False

try:
    import fitz  # PyMuPDF
    PYMUPDF_AVAILABLE = True
except ImportError:
    PYMUPDF_AVAILABLE = False


class PdfToImageWindow(BaseMainWindow):
    """PDF转图片工具主窗口"""
    
    def __init__(self):
        super().__init__("PDF转图片工具", 900, 650)
        
    def setup_content(self):
        """设置内容区域"""
        # 文件选择组件
        self.file_selector = FileSelectionWidget("选择要转换的PDF文件", multi_selection=True)
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
        
        # 检查库的可用性并显示警告
        self.check_library_availability()
        
    def check_library_availability(self):
        """检查并显示库的可用性"""
        if not PDF2IMAGE_AVAILABLE and not PYMUPDF_AVAILABLE:
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setWindowTitle("警告")
            warning.setText("未检测到PDF转图片库")
            warning.setInformativeText("请安装以下库之一:\n"
                                     "1. pdf2image: pip install pdf2image\n"
                                     "2. PyMuPDF: pip install PyMuPDF")
            warning.exec()
            
    def start_conversion(self):
        """开始转换操作"""
        files = self.file_selector.get_files()
        if not files:
            self.show_warning("请先选择要转换的PDF文件")
            return
            
        # 检查库的可用性
        if not PDF2IMAGE_AVAILABLE and not PYMUPDF_AVAILABLE:
            self.show_error("未检测到PDF转图片库，请安装pdf2image或PyMuPDF")
            return
            
        # 获取转换选项
        options = self.convert_options.get_convert_options()
        
        # 获取保存目录
        save_dir = self.get_directory("选择图片保存目录")
        if not save_dir:
            return
            
        # 开始处理
        self.operation.set_running_state(True)
        self.operation.signals.progress.emit(0, 100, "开始转换PDF文件...")
        
        # 使用定时器异步执行
        QTimer.singleShot(100, lambda: self.process_conversion(
            files, options, save_dir
        ))
        
    def process_conversion(self, files, options, save_dir):
        """处理PDF转换"""
        try:
            total_files = len(files)
            
            for i, file_path in enumerate(files):
                if not self.operation.is_running:
                    break
                    
                base_name = os.path.splitext(os.path.basename(file_path))[0]
                
                # 选择转换方法
                if options["conversion_method"] == "PyMuPDF" and PYMUPDF_AVAILABLE:
                    success = self.convert_with_pymupdf(file_path, options, save_dir, base_name)
                elif options["conversion_method"] == "pdf2image" and PDF2IMAGE_AVAILABLE:
                    success = self.convert_with_pdf2image(file_path, options, save_dir, base_name)
                else:
                    # 自动选择可用方法
                    if PYMUPDF_AVAILABLE:
                        success = self.convert_with_pymupdf(file_path, options, save_dir, base_name)
                    elif PDF2IMAGE_AVAILABLE:
                        success = self.convert_with_pdf2image(file_path, options, save_dir, base_name)
                    else:
                        self.operation.signals.finished.emit(False, "没有可用的PDF转换库，请安装PyMuPDF或pdf2image")
                        return
                
                if not success:
                    return
                    
                self.operation.signals.progress.emit(
                    int((i + 1) / total_files * 90), 
                    100, 
                    f"已转换: {os.path.basename(file_path)}"
                )
            
            # 完成
            if self.operation.is_running:
                message = f"转换完成，共处理 {total_files} 个PDF文件"
                self.operation.signals.finished.emit(True, message)
            else:
                self.operation.signals.finished.emit(False, "用户取消操作")
                
        except Exception as e:
            self.operation.signals.finished.emit(False, f"转换过程中发生错误: {str(e)}")
            
    def convert_with_pymupdf(self, file_path, options, save_dir, base_name):
        """使用PyMuPDF转换PDF为图片"""
        try:
            import fitz
            
            # 打开PDF文件
            pdf_document = fitz.open(file_path)
            total_pages = len(pdf_document)
            
            # 确定要转换的页面
            page_ranges = self.parse_page_ranges(options["page_ranges"], total_pages)
            if not page_ranges:
                page_ranges = list(range(1, total_pages + 1))  # 默认所有页面
            
            # 获取DPI
            dpi = options["dpi"]
            zoom = dpi / 72.0  # PDF的标准DPI是72
            
            # 转换每一页
            for page_num in page_ranges:
                if not self.operation.is_running:
                    break
                    
                # 获取页面（注意：PyMuPDF使用0索引）
                page = pdf_document[page_num - 1]
                
                # 创建变换矩阵
                mat = fitz.Matrix(zoom, zoom)
                
                # 渲染页面
                pix = page.get_pixmap(matrix=mat)
                
                # 根据输出格式选择保存方式
                if options["output_format"] == "PNG":
                    img_path = os.path.join(save_dir, f"{base_name}_page{page_num:04d}.png")
                    pix.save(img_path, "png")
                elif options["output_format"] == "JPEG":
                    img_path = os.path.join(save_dir, f"{base_name}_page{page_num:04d}.jpg")
                    pix.save(img_path, "jpeg", jpeg_quality=options["jpeg_quality"])
                else:  # 其他格式，默认使用PNG
                    img_path = os.path.join(save_dir, f"{base_name}_page{page_num:04d}.png")
                    pix.save(img_path, "png")
            
            # 关闭PDF文档
            pdf_document.close()
            return True
            
        except Exception as e:
            self.operation.signals.finished.emit(False, f"使用PyMuPDF转换文件 {os.path.basename(file_path)} 时出错: {str(e)}")
            return False
            
    def convert_with_pdf2image(self, file_path, options, save_dir, base_name):
        """使用pdf2image转换PDF为图片"""
        try:
            # 确定要转换的页面
            # 注意：pdf2image的页码从1开始
            page_ranges = options["page_ranges"]
            
            # 获取DPI
            dpi = options["dpi"]
            
            # 转换参数
            kwargs = {
                'dpi': dpi,
                'output_folder': save_dir,
                'fmt': options["output_format"].lower(),
                'thread_count': 4,
                'use_pdftocairo': True,  # 使用pdftocairo可能质量更高
                'paths_only': True  # 只返回路径，不加载到内存
            }
            
            # 如果有JPEG质量设置
            if options["output_format"] == "JPEG":
                kwargs['jpeg_quality'] = options['jpeg_quality']
            
            # 转换PDF
            if page_ranges:
                # 指定页面范围
                images = convert_from_path(file_path, **kwargs, first_page=min(page_ranges), last_page=max(page_ranges))
                # 过滤不需要的页面
                filtered_images = []
                for i, image in enumerate(images):
                    page_num = min(page_ranges) + i
                    if page_num in page_ranges:
                        filtered_images.append(image)
                images = filtered_images
            else:
                # 转换所有页面
                images = convert_from_path(file_path, **kwargs)
            
            # 重命名图片
            for i, image_path in enumerate(images):
                page_num = page_ranges[i] if page_ranges else i + 1
                ext = os.path.splitext(image_path)[1]
                new_path = os.path.join(save_dir, f"{base_name}_page{page_num:04d}{ext}")
                os.rename(image_path, new_path)
            
            return True
            
        except Exception as e:
            self.operation.signals.finished.emit(False, f"使用pdf2image转换文件 {os.path.basename(file_path)} 时出错: {str(e)}")
            return False
            
    def parse_page_ranges(self, range_text, total_pages):
        """解析页面范围文本，返回页码列表"""
        if not range_text:
            return []
            
        pages = []
        ranges = range_text.split(",")
        
        for r in ranges:
            r = r.strip()
            if "-" in r:
                start, end = r.split("-")
                start_page = max(1, int(start))
                end_page = min(total_pages, int(end))
                pages.extend(range(start_page, end_page + 1))
            else:
                page_num = int(r)
                if 1 <= page_num <= total_pages:
                    pages.append(page_num)
                    
        return sorted(set(pages))  # 去重并排序
            
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
        
        # 输出格式选择
        format_group = QGroupBox("输出格式")
        format_layout = QVBoxLayout(format_group)
        
        self.format_combo = QComboBox()
        self.format_combo.addItems(["PNG", "JPEG", "BMP", "TIFF"])
        format_layout.addWidget(self.format_combo)
        
        layout.addWidget(format_group)
        
        # 转换方法选择
        method_group = QGroupBox("转换方法")
        method_layout = QVBoxLayout(method_group)
        
        self.method_combo = QComboBox()
        if PYMUPDF_AVAILABLE and PDF2IMAGE_AVAILABLE:
            self.method_combo.addItems(["PyMuPDF (推荐)", "pdf2image"])
        elif PYMUPDF_AVAILABLE:
            self.method_combo.addItems(["PyMuPDF (推荐)"])
        elif PDF2IMAGE_AVAILABLE:
            self.method_combo.addItems(["pdf2image"])
        else:
            self.method_combo.addItems(["(无可用库)"])
        
        method_layout.addWidget(self.method_combo)
        
        layout.addWidget(method_group)
        
        # 分辨率设置
        dpi_group = QGroupBox("分辨率(DPI)")
        dpi_layout = QVBoxLayout(dpi_group)
        
        self.dpi_spin = QSpinBox()
        self.dpi_spin.setMinimum(72)
        self.dpi_spin.setMaximum(600)
        self.dpi_spin.setValue(150)
        self.dpi_spin.setSingleStep(10)
        dpi_layout.addWidget(self.dpi_spin)
        
        layout.addWidget(dpi_group)
        
        # 页面选择
        page_group = QGroupBox("页面选择")
        page_layout = QVBoxLayout(page_group)
        
        self.all_pages_radio = QRadioButton("所有页面")
        self.all_pages_radio.setChecked(True)
        page_layout.addWidget(self.all_pages_radio)
        
        self.specified_pages_radio = QRadioButton("指定页面")
        self.specified_pages_radio.toggled.connect(self.toggle_page_input)
        page_layout.addWidget(self.specified_pages_radio)
        
        self.page_input = QLineEdit()
        self.page_input.setPlaceholderText("例如: 1-5, 7, 9-12")
        self.page_input.setEnabled(False)
        page_layout.addWidget(self.page_input)
        
        layout.addWidget(page_group)
        
        # JPEG质量设置（仅在输出格式为JPEG时显示）
        self.jpeg_group = QGroupBox("JPEG质量")
        jpeg_layout = QVBoxLayout(self.jpeg_group)
        
        self.quality_spin = QSpinBox()
        self.quality_spin.setMinimum(1)
        self.quality_spin.setMaximum(100)
        self.quality_spin.setValue(85)
        jpeg_layout.addWidget(self.quality_spin)
        
        self.format_combo.currentTextChanged.connect(self.toggle_jpeg_options)
        
        # 默认隐藏JPEG选项
        self.jpeg_group.setVisible(False)
        layout.addWidget(self.jpeg_group)
        
        # 其他选项
        other_group = QGroupBox("其他选项")
        other_layout = QVBoxLayout(other_group)
        
        self.create_folder_checkbox = QCheckBox("为每个PDF创建单独文件夹")
        self.create_folder_checkbox.setChecked(True)
        other_layout.addWidget(self.create_folder_checkbox)
        
        layout.addWidget(other_group)
        
    def toggle_page_input(self, specified_checked):
        """切换页面输入框状态"""
        self.page_input.setEnabled(specified_checked)
        self.all_pages_radio.setChecked(not specified_checked)
        
    def toggle_jpeg_options(self, format_text):
        """切换JPEG选项显示状态"""
        self.jpeg_group.setVisible(format_text == "JPEG")
        
    def get_convert_options(self):
        """获取转换选项"""
        # 获取页面范围
        page_ranges = []
        if self.specified_pages_radio.isChecked():
            range_text = self.page_input.text().strip()
            if range_text:
                ranges = range_text.split(",")
                for r in ranges:
                    r = r.strip()
                    if r:
                        page_ranges.append(r)
        
        # 获取方法名
        method_text = self.method_combo.currentText()
        if "PyMuPDF" in method_text:
            method = "PyMuPDF"
        elif "pdf2image" in method_text:
            method = "pdf2image"
        else:
            method = "PyMuPDF"  # 默认使用PyMuPDF
        
        return {
            "output_format": self.format_combo.currentText(),
            "conversion_method": method,
            "dpi": self.dpi_spin.value(),
            "all_pages": self.all_pages_radio.isChecked(),
            "page_ranges": page_ranges,
            "jpeg_quality": self.quality_spin.value(),
            "create_folder": self.create_folder_checkbox.isChecked()
        }


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = PdfToImageWindow()
    window.show()
    sys.exit(app.exec())