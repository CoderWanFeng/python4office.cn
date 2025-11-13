#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PDF水印添加工具
功能：为PDF文件添加文本或图片水印，支持自定义水印样式和位置
"""

import sys
import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color, black, blue, red, green
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import io
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                              QPushButton, QRadioButton, QButtonGroup,
                              QSpinBox, QCheckBox, QComboBox, QColorDialog,
                              QFileDialog, QMessageBox, QSlider)
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QColor

# 添加父目录到路径，以便导入common模块
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.ui_base import BaseMainWindow, FileSelectionWidget, OperationWidget


class PdfWatermarkWindow(BaseMainWindow):
    """PDF水印添加工具主窗口"""
    
    def __init__(self):
        super().__init__("PDF水印添加工具", 900, 650)
        
    def setup_content(self):
        """设置内容区域"""
        # 文件选择组件
        self.file_selector = FileSelectionWidget("选择要添加水印的PDF文件", multi_selection=True)
        self.content_layout.addWidget(self.file_selector)
        
        # 水印选项组件
        self.watermark_options = WatermarkOptionsWidget()
        self.content_layout.addWidget(self.watermark_options)
        
        # 操作区域
        self.operation = OperationWidget("水印添加操作")
        self.operation.start_operation = self.add_watermarks
        self.operation.signals.progress.connect(self.update_progress)
        self.operation.signals.finished.connect(self.watermark_finished)
        self.content_layout.addWidget(self.operation)
        
    def add_watermarks(self):
        """开始添加水印操作"""
        files = self.file_selector.get_files()
        if not files:
            self.show_warning("请先选择要添加水印的PDF文件")
            return
            
        # 获取水印选项
        options = self.watermark_options.get_watermark_options()
        
        # 验证水印选项
        if options["watermark_type"] == "text" and not options["text"]:
            self.show_warning("请输入水印文本")
            return
        elif options["watermark_type"] == "image" and not options["image_path"]:
            self.show_warning("请选择水印图片")
            return
            
        # 获取保存目录
        save_dir = self.get_directory("选择添加水印后文件的保存目录")
        if not save_dir:
            return
            
        # 开始处理
        self.operation.set_running_state(True)
        self.operation.signals.progress.emit(0, 100, "开始添加水印...")
        
        # 使用定时器异步执行
        QTimer.singleShot(100, lambda: self.process_watermarks(
            files, options, save_dir
        ))
        
    def process_watermarks(self, files, options, save_dir):
        """处理水印添加"""
        try:
            total_files = len(files)
            
            # 创建水印PDF
            if options["watermark_type"] == "text":
                watermark_pdf = self.create_text_watermark(options)
            else:
                watermark_pdf = self.create_image_watermark(options)
            
            for i, file_path in enumerate(files):
                if not self.operation.is_running:
                    break
                    
                self.operation.signals.progress.emit(
                    int(i / total_files * 90), 
                    100, 
                    f"正在添加水印: {os.path.basename(file_path)}"
                )
                
                try:
                    # 读取原始PDF
                    reader = PdfReader(file_path)
                    writer = PdfWriter()
                    
                    # 添加水印到每一页
                    for page in reader.pages:
                        # 合并水印页面
                        if options["apply_to_all"] or i == 0:
                            page.merge_page(watermark_pdf.pages[0])
                        
                        writer.add_page(page)
                    
                    # 保存文件
                    base_name = os.path.splitext(os.path.basename(file_path))[0]
                    if options["add_suffix"]:
                        new_name = f"{base_name}_水印.pdf"
                    else:
                        new_name = f"{base_name}.pdf"
                    new_path = os.path.join(save_dir, new_name)
                    
                    with open(new_path, "wb") as output_file:
                        writer.write(output_file)
                        
                except Exception as e:
                    self.operation.signals.finished.emit(False, f"处理文件 {os.path.basename(file_path)} 时出错: {str(e)}")
                    return
            
            # 完成
            if self.operation.is_running:
                message = f"水印添加完成，共处理 {total_files} 个PDF文件"
                self.operation.signals.finished.emit(True, message)
            else:
                self.operation.signals.finished.emit(False, "用户取消操作")
                
        except Exception as e:
            self.operation.signals.finished.emit(False, f"添加水印过程中发生错误: {str(e)}")
            
    def create_text_watermark(self, options):
        """创建文本水印PDF"""
        # 创建一个内存中的PDF文件
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        
        # 设置字体
        try:
            # 尝试加载系统字体
            font_path = self.get_system_font()
            if font_path:
                pdfmetrics.registerFont(TTFont("WatermarkFont", font_path))
                font_name = "WatermarkFont"
            else:
                font_name = "Helvetica"  # 默认字体
        except:
            font_name = "Helvetica"  # 默认字体
        
        # 设置字体大小和颜色
        font_size = options["font_size"]
        opacity = options["opacity"] / 100.0
        
        # 解析颜色
        color_value = options["text_color"]
        color = self.hex_to_color(color_value)
        
        # 获取页面尺寸
        page_width, page_height = letter
        
        # 计算旋转角度
        rotation = options["rotation"]
        
        # 根据位置计算水印位置
        if options["position"] == "center":
            x = page_width / 2
            y = page_height / 2
        elif options["position"] == "top_left":
            x = page_width / 4
            y = 3 * page_height / 4
        elif options["position"] == "top_right":
            x = 3 * page_width / 4
            y = 3 * page_height / 4
        elif options["position"] == "bottom_left":
            x = page_width / 4
            y = page_height / 4
        elif options["position"] == "bottom_right":
            x = 3 * page_width / 4
            y = page_height / 4
        else:  # tiled
            x = page_width / 2
            y = page_height / 2
        
        # 设置透明度和颜色
        can.setFillColorRGB(color.red / 255.0, color.green / 255.0, color.blue / 255.0, alpha=opacity)
        can.setFont(font_name, font_size)
        
        # 保存当前状态
        can.saveState()
        
        # 如果需要旋转，移动到页面中心并旋转
        if rotation != 0:
            can.translate(x, y)
            can.rotate(rotation)
            can.drawCentredText(0, 0, options["text"])
            can.restoreState()
        else:
            # 直接绘制文本
            if options["position"] == "center":
                can.drawCentredText(x, y, options["text"])
            else:
                can.drawString(x, y, options["text"])
        
        # 如果是平铺模式，绘制多个水印
        if options["position"] == "tiled":
            can.restoreState()
            can.setFillColorRGB(color.red / 255.0, color.green / 255.0, color.blue / 255.0, alpha=opacity)
            can.setFont(font_name, font_size)
            
            # 保存当前状态
            can.saveState()
            
            # 计算平铺网格
            tile_width = page_width / options["tile_cols"]
            tile_height = page_height / options["tile_rows"]
            
            # 绘制平铺水印
            for row in range(options["tile_rows"]):
                for col in range(options["tile_cols"]):
                    x = (col + 0.5) * tile_width
                    y = (row + 0.5) * tile_height
                    
                    # 旋转并绘制
                    can.translate(x, y)
                    can.rotate(rotation)
                    can.drawCentredText(0, 0, options["text"])
                    can.translate(-x, -y)
                    can.rotate(-rotation)
        
        # 恢复状态
        can.restoreState()
        
        # 保存PDF
        can.save()
        
        # 移动到文件开头
        packet.seek(0)
        
        # 创建PDF读取器
        watermark = PdfReader(packet)
        return watermark
        
    def create_image_watermark(self, options):
        """创建图片水印PDF"""
        # 创建一个内存中的PDF文件
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        
        # 设置透明度
        opacity = options["opacity"] / 100.0
        
        # 获取页面尺寸
        page_width, page_height = letter
        
        # 计算图片尺寸和位置
        img_width = options["image_width"] * inch
        img_height = options["image_height"] * inch
        
        # 计算旋转角度
        rotation = options["rotation"]
        
        # 根据位置计算水印位置
        if options["position"] == "center":
            x = (page_width - img_width) / 2
            y = (page_height - img_height) / 2
        elif options["position"] == "top_left":
            x = inch
            y = page_height - img_height - inch
        elif options["position"] == "top_right":
            x = page_width - img_width - inch
            y = page_height - img_height - inch
        elif options["position"] == "bottom_left":
            x = inch
            y = inch
        elif options["position"] == "bottom_right":
            x = page_width - img_width - inch
            y = inch
        else:  # tiled
            x = (page_width - img_width) / 2
            y = (page_height - img_height) / 2
        
        # 保存当前状态
        can.saveState()
        
        # 如果需要旋转，移动到中心并旋转
        if rotation != 0:
            can.translate(x + img_width/2, y + img_height/2)
            can.rotate(rotation)
            can.drawImage(options["image_path"], -img_width/2, -img_height/2, 
                         width=img_width, height=img_height, 
                         mask='auto')
            can.restoreState()
        else:
            # 直接绘制图片
            if options["position"] == "center":
                can.drawImage(options["image_path"], x, y, 
                             width=img_width, height=img_height, 
                             mask='auto')
            else:
                can.drawImage(options["image_path"], x, y, 
                             width=img_width, height=img_height, 
                             mask='auto')
        
        # 如果是平铺模式，绘制多个水印
        if options["position"] == "tiled":
            can.restoreState()
            
            # 计算平铺网格
            tile_width = page_width / options["tile_cols"]
            tile_height = page_height / options["tile_rows"]
            
            # 绘制平铺水印
            for row in range(options["tile_rows"]):
                for col in range(options["tile_cols"]):
                    x = (col + 0.5) * tile_width - img_width/2
                    y = (row + 0.5) * tile_height - img_height/2
                    
                    # 旋转并绘制
                    can.saveState()
                    can.translate(x + img_width/2, y + img_height/2)
                    can.rotate(rotation)
                    can.drawImage(options["image_path"], -img_width/2, -img_height/2, 
                                 width=img_width, height=img_height, 
                                 mask='auto')
                    can.restoreState()
        
        # 恢复状态
        can.restoreState()
        
        # 保存PDF
        can.save()
        
        # 移动到文件开头
        packet.seek(0)
        
        # 创建PDF读取器
        watermark = PdfReader(packet)
        return watermark
        
    def get_system_font(self):
        """获取系统字体路径"""
        font_paths = []
        
        if sys.platform == "win32":
            # Windows字体路径
            font_dirs = [
                r"C:\Windows\Fonts",
                r"C:\Users\{}\AppData\Local\Microsoft\Windows\Fonts".format(os.environ.get("USERNAME", "")),
            ]
            font_files = ["msyh.ttc", "msyh.ttf", "simsun.ttc", "simhei.ttf"]
            
            for font_dir in font_dirs:
                if os.path.exists(font_dir):
                    for font_file in font_files:
                        font_path = os.path.join(font_dir, font_file)
                        if os.path.exists(font_path):
                            return font_path
        elif sys.platform == "darwin":
            # macOS字体路径
            font_dirs = [
                "/System/Library/Fonts",
                "/Library/Fonts",
                os.path.expanduser("~/Library/Fonts"),
            ]
            font_files = ["PingFang.ttc", "STHeiti Light.ttc", "STHeiti Medium.ttc"]
            
            for font_dir in font_dirs:
                if os.path.exists(font_dir):
                    for font_file in font_files:
                        font_path = os.path.join(font_dir, font_file)
                        if os.path.exists(font_path):
                            return font_path
        else:
            # Linux字体路径
            font_dirs = [
                "/usr/share/fonts",
                "/usr/local/share/fonts",
                os.path.expanduser("~/.fonts"),
            ]
            font_files = ["wqy-microhei.ttc", "wqy-zenhei.ttc", "arial.ttf"]
            
            for font_dir in font_dirs:
                if os.path.exists(font_dir):
                    for font_file in font_files:
                        font_path = os.path.join(font_dir, font_file)
                        if os.path.exists(font_path):
                            return font_path
        
        return None  # 没有找到合适的字体
        
    def hex_to_color(self, hex_color):
        """将十六进制颜色转换为QColor"""
        return QColor(hex_color)
        
    def update_progress(self, current, total, status):
        """更新进度"""
        self.operation.progress.update_progress(current, total, status)
        
    def watermark_finished(self, success, message):
        """水印添加完成"""
        self.operation.set_running_state(False)
        if success:
            self.show_info(message)
        else:
            self.show_error(message)


class WatermarkOptionsWidget(QWidget):
    """水印选项组件"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 水印类型选择
        type_group = QWidget()
        type_layout = QVBoxLayout(type_group)
        type_layout.addWidget(QLabel("水印类型:"))
        
        self.watermark_group = QButtonGroup()
        
        self.text_radio = QRadioButton("文本水印")
        self.text_radio.setChecked(True)
        self.watermark_group.addButton(self.text_radio, 0)
        self.text_radio.toggled.connect(self.toggle_watermark_type)
        type_layout.addWidget(self.text_radio)
        
        self.image_radio = QRadioButton("图片水印")
        self.watermark_group.addButton(self.image_radio, 1)
        self.image_radio.toggled.connect(self.toggle_watermark_type)
        type_layout.addWidget(self.image_radio)
        
        layout.addWidget(type_group)
        
        # 文本水印选项
        self.text_options = QWidget()
        text_layout = QVBoxLayout(self.text_options)
        
        # 文本输入
        text_input_layout = QHBoxLayout()
        text_input_layout.addWidget(QLabel("水印文本:"))
        self.text_input = QLineEdit("机密文档")
        text_input_layout.addWidget(self.text_input)
        text_layout.addLayout(text_input_layout)
        
        # 字体设置
        font_layout = QHBoxLayout()
        font_layout.addWidget(QLabel("字体大小:"))
        self.font_size_spin = QSpinBox()
        self.font_size_spin.setMinimum(10)
        self.font_size_spin.setMaximum(200)
        self.font_size_spin.setValue(48)
        font_layout.addWidget(self.font_size_spin)
        
        font_layout.addWidget(QLabel("颜色:"))
        self.text_color_btn = QPushButton()
        self.text_color_btn.setStyleSheet("background-color: #000000; border: 1px solid #555; min-width: 50px; min-height: 20px;")
        self.text_color_btn.clicked.connect(self.choose_text_color)
        self.text_color = "#000000"
        font_layout.addWidget(self.text_color_btn)
        
        text_layout.addLayout(font_layout)
        
        layout.addWidget(self.text_options)
        
        # 图片水印选项
        self.image_options = QWidget()
        image_layout = QVBoxLayout(self.image_options)
        
        # 图片选择
        image_input_layout = QHBoxLayout()
        image_input_layout.addWidget(QLabel("水印图片:"))
        self.image_path_input = QLineEdit()
        self.image_path_input.setReadOnly(True)
        image_input_layout.addWidget(self.image_path_input)
        
        self.browse_image_btn = QPushButton("浏览")
        self.browse_image_btn.clicked.connect(self.browse_image)
        image_input_layout.addWidget(self.browse_image_btn)
        
        image_layout.addLayout(image_input_layout)
        
        # 图片尺寸
        size_layout = QHBoxLayout()
        size_layout.addWidget(QLabel("图片尺寸(英寸):"))
        
        size_layout.addWidget(QLabel("宽:"))
        self.image_width_spin = QSpinBox()
        self.image_width_spin.setMinimum(0.5)
        self.image_width_spin.setMaximum(10)
        self.image_width_spin.setSingleStep(0.5)
        self.image_width_spin.setValue(2)
        size_layout.addWidget(self.image_width_spin)
        
        size_layout.addWidget(QLabel("高:"))
        self.image_height_spin = QSpinBox()
        self.image_height_spin.setMinimum(0.5)
        self.image_height_spin.setMaximum(10)
        self.image_height_spin.setSingleStep(0.5)
        self.image_height_spin.setValue(1)
        size_layout.addWidget(self.image_height_spin)
        
        image_layout.addLayout(size_layout)
        
        layout.addWidget(self.image_options)
        
        # 通用水印选项
        common_group = QWidget()
        common_layout = QVBoxLayout(common_group)
        common_layout.addWidget(QLabel("通用选项:"))
        
        # 位置选择
        position_layout = QHBoxLayout()
        position_layout.addWidget(QLabel("水印位置:"))
        self.position_combo = QComboBox()
        self.position_combo.addItems(["中心", "左上", "右上", "左下", "右下", "平铺"])
        self.position_combo.currentTextChanged.connect(self.toggle_tile_options)
        position_layout.addWidget(self.position_combo)
        common_layout.addLayout(position_layout)
        
        # 平铺选项
        self.tile_options = QWidget()
        tile_layout = QHBoxLayout(self.tile_options)
        tile_layout.addWidget(QLabel("平铺网格:"))
        
        tile_layout.addWidget(QLabel("列数:"))
        self.tile_cols_spin = QSpinBox()
        self.tile_cols_spin.setMinimum(2)
        self.tile_cols_spin.setMaximum(10)
        self.tile_cols_spin.setValue(4)
        tile_layout.addWidget(self.tile_cols_spin)
        
        tile_layout.addWidget(QLabel("行数:"))
        self.tile_rows_spin = QSpinBox()
        self.tile_rows_spin.setMinimum(2)
        self.tile_rows_spin.setMaximum(10)
        self.tile_rows_spin.setValue(3)
        tile_layout.addWidget(self.tile_rows_spin)
        
        common_layout.addWidget(self.tile_options)
        
        # 旋转角度
        rotation_layout = QHBoxLayout()
        rotation_layout.addWidget(QLabel("旋转角度(度):"))
        self.rotation_slider = QSlider(Qt.Horizontal)
        self.rotation_slider.setMinimum(-180)
        self.rotation_slider.setMaximum(180)
        self.rotation_slider.setValue(45)
        self.rotation_slider.setTickPosition(QSlider.TicksBelow)
        self.rotation_slider.setTickInterval(30)
        rotation_layout.addWidget(self.rotation_slider)
        
        self.rotation_label = QLabel("45°")
        self.rotation_slider.valueChanged.connect(
            lambda value: self.rotation_label.setText(f"{value}°")
        )
        rotation_layout.addWidget(self.rotation_label)
        
        common_layout.addLayout(rotation_layout)
        
        # 透明度
        opacity_layout = QHBoxLayout()
        opacity_layout.addWidget(QLabel("透明度(%):"))
        self.opacity_slider = QSlider(Qt.Horizontal)
        self.opacity_slider.setMinimum(10)
        self.opacity_slider.setMaximum(100)
        self.opacity_slider.setValue(30)
        self.opacity_slider.setTickPosition(QSlider.TicksBelow)
        self.opacity_slider.setTickInterval(10)
        opacity_layout.addWidget(self.opacity_slider)
        
        self.opacity_label = QLabel("30%")
        self.opacity_slider.valueChanged.connect(
            lambda value: self.opacity_label.setText(f"{value}%")
        )
        opacity_layout.addWidget(self.opacity_label)
        
        common_layout.addLayout(opacity_layout)
        
        layout.addWidget(common_group)
        
        # 其他选项
        other_group = QWidget()
        other_layout = QVBoxLayout(other_group)
        other_layout.addWidget(QLabel("其他选项:"))
        
        self.add_suffix_checkbox = QCheckBox("文件名添加_水印后缀")
        self.add_suffix_checkbox.setChecked(True)
        other_layout.addWidget(self.add_suffix_checkbox)
        
        self.apply_to_all_checkbox = QCheckBox("应用到所有文件（仅在批处理时）")
        self.apply_to_all_checkbox.setChecked(True)
        other_layout.addWidget(self.apply_to_all_checkbox)
        
        layout.addWidget(other_group)
        
        # 初始化控件状态
        self.toggle_watermark_type(self.text_radio.isChecked())
        self.toggle_tile_options(self.position_combo.currentText())
        
    def toggle_watermark_type(self, text_checked):
        """切换水印类型"""
        is_text = text_checked
        self.text_options.setVisible(is_text)
        self.image_options.setVisible(not is_text)
        
    def toggle_tile_options(self, position):
        """切换平铺选项"""
        is_tile = position == "平铺"
        self.tile_options.setVisible(is_tile)
        
    def choose_text_color(self):
        """选择文本颜色"""
        color = QColorDialog.getColor(QColor(self.text_color), self, "选择颜色")
        if color.isValid():
            self.text_color = color.name()
            self.text_color_btn.setStyleSheet(f"background-color: {self.text_color}; border: 1px solid #555; min-width: 50px; min-height: 20px;")
            
    def browse_image(self):
        """浏览选择图片"""
        file_path = QFileDialog.getOpenFileName(self, "选择水印图片", "", "图片文件 (*.png *.jpg *.jpeg *.bmp)")[0]
        if file_path:
            self.image_path_input.setText(file_path)
            
    def get_watermark_options(self):
        """获取水印选项"""
        mode_id = self.watermark_group.checkedId()
        watermark_type = "text" if mode_id == 0 else "image"
        
        return {
            "watermark_type": watermark_type,
            "text": self.text_input.text().strip(),
            "font_size": self.font_size_spin.value(),
            "text_color": self.text_color,
            "image_path": self.image_path_input.text().strip(),
            "image_width": self.image_width_spin.value(),
            "image_height": self.image_height_spin.value(),
            "position": self.position_combo.currentText(),
            "tile_cols": self.tile_cols_spin.value(),
            "tile_rows": self.tile_rows_spin.value(),
            "rotation": self.rotation_slider.value(),
            "opacity": self.opacity_slider.value(),
            "add_suffix": self.add_suffix_checkbox.isChecked(),
            "apply_to_all": self.apply_to_all_checkbox.isChecked()
        }


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = PdfWatermarkWindow()
    window.show()
    sys.exit(app.exec())