#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
图片批量处理工具
功能：批量调整图片大小、格式等，支持多种图片处理操作
"""

import sys
import os
from PIL import Image, ImageEnhance, ImageFilter
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                              QPushButton, QTableWidget, QTableWidgetItem, 
                              QHeaderView, QTabWidget, QSlider, QCheckBox,
                              QComboBox, QFileDialog, QMessageBox, QSpinBox)
from PySide6.QtCore import QTimer, Qt

# 添加父目录到路径，以便导入common模块
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.ui_base import BaseMainWindow, FileSelectionWidget, OperationWidget


class ImageProcessWindow(BaseMainWindow):
    """图片批量处理工具主窗口"""
    
    def __init__(self):
        super().__init__("图片批量处理工具", 1000, 700)
        
    def setup_content(self):
        """设置内容区域"""
        # 文件选择组件
        self.file_selector = FileSelectionWidget("选择要处理的图片文件", multi_selection=True)
        self.file_selector.select_files = self.add_files  # 重写选择文件方法
        self.content_layout.addWidget(self.file_selector)
        
        # 使用选项卡组织界面
        self.tab_widget = QTabWidget()
        self.content_layout.addWidget(self.tab_widget)
        
        # 调整大小选项卡
        self.resize_tab = QWidget()
        self.setup_resize_tab()
        self.tab_widget.addTab(self.resize_tab, "调整大小")
        
        # 格式转换选项卡
        self.format_tab = QWidget()
        self.setup_format_tab()
        self.tab_widget.addTab(self.format_tab, "格式转换")
        
        # 图像增强选项卡
        self.enhance_tab = QWidget()
        self.setup_enhance_tab()
        self.tab_widget.addTab(self.enhance_tab, "图像增强")
        
        # 图片旋转选项卡
        self.rotate_tab = QWidget()
        self.setup_rotate_tab()
        self.tab_widget.addTab(self.rotate_tab, "图片旋转")
        
        # 水印添加选项卡
        self.watermark_tab = QWidget()
        self.setup_watermark_tab()
        self.tab_widget.addTab(self.watermark_tab, "水印添加")
        
        # 操作区域
        self.operation = OperationWidget("图片处理操作")
        self.operation.start_operation = self.start_processing
        self.operation.signals.progress.connect(self.update_progress)
        self.operation.signals.finished.connect(self.processing_finished)
        self.content_layout.addWidget(self.operation)
        
    def add_files(self):
        """添加文件到列表"""
        files = QFileDialog.getOpenFileNames(self, "选择图片文件", "", 
                                           "图片文件 (*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.webp)")[0]
        
        if not files:
            return
            
        for file_path in files:
            self.file_selector.file_paths.append(file_path)
            
        self.file_selector.update_display()
        
    def setup_resize_tab(self):
        """设置调整大小选项卡"""
        layout = QVBoxLayout(self.resize_tab)
        
        # 调整模式
        mode_group = QWidget()
        mode_layout = QVBoxLayout(mode_group)
        mode_layout.addWidget(QLabel("调整模式:"))
        
        self.resize_mode_combo = QComboBox()
        self.resize_mode_combo.addItems(["按百分比调整", "按尺寸调整", "按最长边调整"])
        mode_layout.addWidget(self.resize_mode_combo)
        layout.addWidget(mode_group)
        
        # 百分比调整
        percent_group = QWidget()
        percent_layout = QVBoxLayout(percent_group)
        percent_layout.addWidget(QLabel("百分比(%):"))
        
        self.percent_slider = QSlider(Qt.Horizontal)
        self.percent_slider.setMinimum(10)
        self.percent_slider.setMaximum(200)
        self.percent_slider.setValue(100)
        self.percent_slider.setTickPosition(QSlider.TicksBelow)
        self.percent_slider.setTickInterval(20)
        percent_layout.addWidget(self.percent_slider)
        
        self.percent_label = QLabel("100%")
        self.percent_slider.valueChanged.connect(
            lambda value: self.percent_label.setText(f"{value}%")
        )
        percent_layout.addWidget(self.percent_label)
        
        layout.addWidget(percent_group)
        
        # 尺寸调整
        size_group = QWidget()
        size_layout = QVBoxLayout(size_group)
        size_layout.addWidget(QLabel("目标尺寸:"))
        
        size_input_layout = QHBoxLayout()
        size_input_layout.addWidget(QLabel("宽度:"))
        self.width_spin = QSpinBox()
        self.width_spin.setMinimum(10)
        self.width_spin.setMaximum(9999)
        self.width_spin.setValue(800)
        size_input_layout.addWidget(self.width_spin)
        
        size_input_layout.addWidget(QLabel("高度:"))
        self.height_spin = QSpinBox()
        self.height_spin.setMinimum(10)
        self.height_spin.setMaximum(9999)
        self.height_spin.setValue(600)
        size_input_layout.addWidget(self.height_spin)
        
        size_layout.addLayout(size_input_layout)
        
        self.keep_aspect_checkbox = QCheckBox("保持宽高比")
        self.keep_aspect_checkbox.setChecked(True)
        size_layout.addWidget(self.keep_aspect_checkbox)
        
        layout.addWidget(size_group)
        
        # 长边调整
        longest_group = QWidget()
        longest_layout = QVBoxLayout(longest_group)
        longest_layout.addWidget(QLabel("最长边(像素):"))
        
        self.longest_spin = QSpinBox()
        self.longest_spin.setMinimum(100)
        self.longest_spin.setMaximum(9999)
        self.longest_spin.setValue(1024)
        longest_layout.addWidget(self.longest_spin)
        
        layout.addWidget(longest_group)
        
        # 连接信号
        self.resize_mode_combo.currentTextChanged.connect(self.toggle_resize_options)
        self.toggle_resize_options(self.resize_mode_combo.currentText())
        
    def setup_format_tab(self):
        """设置格式转换选项卡"""
        layout = QVBoxLayout(self.format_tab)
        
        # 目标格式
        format_group = QWidget()
        format_layout = QVBoxLayout(format_group)
        format_layout.addWidget(QLabel("目标格式:"))
        
        self.target_format_combo = QComboBox()
        self.target_format_combo.addItems(["JPEG", "PNG", "BMP", "TIFF", "WEBP"])
        format_layout.addWidget(self.target_format_combo)
        layout.addWidget(format_group)
        
        # JPEG质量设置
        jpeg_group = QWidget()
        jpeg_layout = QVBoxLayout(jpeg_group)
        jpeg_layout.addWidget(QLabel("JPEG质量:"))
        
        self.quality_slider = QSlider(Qt.Horizontal)
        self.quality_slider.setMinimum(10)
        self.quality_slider.setMaximum(100)
        self.quality_slider.setValue(85)
        self.quality_slider.setTickPosition(QSlider.TicksBelow)
        self.quality_slider.setTickInterval(10)
        jpeg_layout.addWidget(self.quality_slider)
        
        self.quality_label = QLabel("85")
        self.quality_slider.valueChanged.connect(
            lambda value: self.quality_label.setText(str(value))
        )
        jpeg_layout.addWidget(self.quality_label)
        
        layout.addWidget(jpeg_group)
        
        # 连接信号
        self.target_format_combo.currentTextChanged.connect(self.toggle_quality_options)
        self.toggle_quality_options(self.target_format_combo.currentText())
        
    def setup_enhance_tab(self):
        """设置图像增强选项卡"""
        layout = QVBoxLayout(self.enhance_tab)
        
        # 亮度调整
        brightness_group = QWidget()
        brightness_layout = QVBoxLayout(brightness_group)
        brightness_layout.addWidget(QLabel("亮度:"))
        
        self.brightness_slider = QSlider(Qt.Horizontal)
        self.brightness_slider.setMinimum(50)
        self.brightness_slider.setMaximum(150)
        self.brightness_slider.setValue(100)
        self.brightness_slider.setTickPosition(QSlider.TicksBelow)
        self.brightness_slider.setTickInterval(10)
        brightness_layout.addWidget(self.brightness_slider)
        
        self.brightness_label = QLabel("100%")
        self.brightness_slider.valueChanged.connect(
            lambda value: self.brightness_label.setText(f"{value}%")
        )
        brightness_layout.addWidget(self.brightness_label)
        
        layout.addWidget(brightness_group)
        
        # 对比度调整
        contrast_group = QWidget()
        contrast_layout = QVBoxLayout(contrast_group)
        contrast_layout.addWidget(QLabel("对比度:"))
        
        self.contrast_slider = QSlider(Qt.Horizontal)
        self.contrast_slider.setMinimum(50)
        self.contrast_slider.setMaximum(150)
        self.contrast_slider.setValue(100)
        self.contrast_slider.setTickPosition(QSlider.TicksBelow)
        self.contrast_slider.setTickInterval(10)
        contrast_layout.addWidget(self.contrast_slider)
        
        self.contrast_label = QLabel("100%")
        self.contrast_slider.valueChanged.connect(
            lambda value: self.contrast_label.setText(f"{value}%")
        )
        contrast_layout.addWidget(self.contrast_label)
        
        layout.addWidget(contrast_group)
        
        # 色彩饱和度调整
        saturation_group = QWidget()
        saturation_layout = QVBoxLayout(saturation_group)
        saturation_layout.addWidget(QLabel("饱和度:"))
        
        self.saturation_slider = QSlider(Qt.Horizontal)
        self.saturation_slider.setMinimum(0)
        self.saturation_slider.setMaximum(200)
        self.saturation_slider.setValue(100)
        self.saturation_slider.setTickPosition(QSlider.TicksBelow)
        self.saturation_slider.setTickInterval(20)
        saturation_layout.addWidget(self.saturation_slider)
        
        self.saturation_label = QLabel("100%")
        self.saturation_slider.valueChanged.connect(
            lambda value: self.saturation_label.setText(f"{value}%")
        )
        saturation_layout.addWidget(self.saturation_label)
        
        layout.addWidget(saturation_group)
        
        # 锐度调整
        sharpness_group = QWidget()
        sharpness_layout = QVBoxLayout(sharpness_group)
        sharpness_layout.addWidget(QLabel("锐度:"))
        
        self.sharpness_slider = QSlider(Qt.Horizontal)
        self.sharpness_slider.setMinimum(50)
        self.sharpness_slider.setMaximum(200)
        self.sharpness_slider.setValue(100)
        self.sharpness_slider.setTickPosition(QSlider.TicksBelow)
        self.sharpness_slider.setTickInterval(25)
        sharpness_layout.addWidget(self.sharpness_slider)
        
        self.sharpness_label = QLabel("100%")
        self.sharpness_slider.valueChanged.connect(
            lambda value: self.sharpness_label.setText(f"{value}%")
        )
        sharpness_layout.addWidget(self.sharpness_label)
        
        layout.addWidget(sharpness_group)
        
    def setup_rotate_tab(self):
        """设置图片旋转选项卡"""
        layout = QVBoxLayout(self.rotate_tab)
        
        # 旋转模式
        mode_group = QWidget()
        mode_layout = QVBoxLayout(mode_group)
        mode_layout.addWidget(QLabel("旋转模式:"))
        
        self.rotate_mode_combo = QComboBox()
        self.rotate_mode_combo.addItems(["自定义角度", "90度", "180度", "270度", "水平翻转", "垂直翻转"])
        mode_layout.addWidget(self.rotate_mode_combo)
        layout.addWidget(mode_group)
        
        # 自定义角度
        angle_group = QWidget()
        angle_layout = QVBoxLayout(angle_group)
        angle_layout.addWidget(QLabel("旋转角度(度):"))
        
        self.angle_spin = QSpinBox()
        self.angle_spin.setMinimum(-360)
        self.angle_spin.setMaximum(360)
        self.angle_spin.setValue(90)
        angle_layout.addWidget(self.angle_spin)
        
        layout.addWidget(angle_group)
        
        # 连接信号
        self.rotate_mode_combo.currentTextChanged.connect(self.toggle_angle_input)
        self.toggle_angle_input(self.rotate_mode_combo.currentText())
        
    def setup_watermark_tab(self):
        """设置水印添加选项卡"""
        layout = QVBoxLayout(self.watermark_tab)
        
        # 水印类型
        type_group = QWidget()
        type_layout = QVBoxLayout(type_group)
        type_layout.addWidget(QLabel("水印类型:"))
        
        self.watermark_type_combo = QComboBox()
        self.watermark_type_combo.addItems(["文字水印", "图片水印"])
        self.watermark_type_combo.currentTextChanged.connect(self.toggle_watermark_type)
        type_layout.addWidget(self.watermark_type_combo)
        layout.addWidget(type_group)
        
        # 文字水印选项
        self.text_watermark_widget = QWidget()
        text_layout = QVBoxLayout(self.text_watermark_widget)
        
        text_input_layout = QHBoxLayout()
        text_input_layout.addWidget(QLabel("水印文字:"))
        self.watermark_text_input = QLineEdit("Watermark")
        text_input_layout.addWidget(self.watermark_text_input)
        text_layout.addLayout(text_input_layout)
        
        font_layout = QHBoxLayout()
        font_layout.addWidget(QLabel("字体大小:"))
        self.font_size_spin = QSpinBox()
        self.font_size_spin.setMinimum(10)
        self.font_size_spin.setMaximum(100)
        self.font_size_spin.setValue(30)
        font_layout.addWidget(self.font_size_spin)
        text_layout.addLayout(font_layout)
        
        opacity_layout = QHBoxLayout()
        opacity_layout.addWidget(QLabel("不透明度(%):"))
        self.watermark_opacity_slider = QSlider(Qt.Horizontal)
        self.watermark_opacity_slider.setMinimum(10)
        self.watermark_opacity_slider.setMaximum(100)
        self.watermark_opacity_slider.setValue(50)
        self.watermark_opacity_slider.setTickPosition(QSlider.TicksBelow)
        self.watermark_opacity_slider.setTickInterval(10)
        opacity_layout.addWidget(self.watermark_opacity_slider)
        
        self.watermark_opacity_label = QLabel("50%")
        self.watermark_opacity_slider.valueChanged.connect(
            lambda value: self.watermark_opacity_label.setText(f"{value}%")
        )
        opacity_layout.addWidget(self.watermark_opacity_label)
        text_layout.addLayout(opacity_layout)
        
        position_layout = QHBoxLayout()
        position_layout.addWidget(QLabel("位置:"))
        self.watermark_position_combo = QComboBox()
        self.watermark_position_combo.addItems(["中心", "左上", "右上", "左下", "右下"])
        position_layout.addWidget(self.watermark_position_combo)
        text_layout.addLayout(position_layout)
        
        layout.addWidget(self.text_watermark_widget)
        
        # 图片水印选项
        self.image_watermark_widget = QWidget()
        image_layout = QVBoxLayout(self.image_watermark_widget)
        
        image_path_layout = QHBoxLayout()
        image_path_layout.addWidget(QLabel("水印图片:"))
        self.watermark_image_input = QLineEdit()
        self.watermark_image_input.setReadOnly(True)
        image_path_layout.addWidget(self.watermark_image_input)
        
        self.browse_watermark_btn = QPushButton("浏览")
        self.browse_watermark_btn.clicked.connect(self.browse_watermark_image)
        image_path_layout.addWidget(self.browse_watermark_btn)
        image_layout.addLayout(image_path_layout)
        
        size_layout = QHBoxLayout()
        size_layout.addWidget(QLabel("大小(%):"))
        self.watermark_size_spin = QSpinBox()
        self.watermark_size_spin.setMinimum(5)
        self.watermark_size_spin.setMaximum(50)
        self.watermark_size_spin.setValue(20)
        size_layout.addWidget(self.watermark_size_spin)
        image_layout.addLayout(size_layout)
        
        image_opacity_layout = QHBoxLayout()
        image_opacity_layout.addWidget(QLabel("不透明度(%):"))
        self.watermark_image_opacity_slider = QSlider(Qt.Horizontal)
        self.watermark_image_opacity_slider.setMinimum(10)
        self.watermark_image_opacity_slider.setMaximum(100)
        self.watermark_image_opacity_slider.setValue(50)
        self.watermark_image_opacity_slider.setTickPosition(QSlider.TicksBelow)
        self.watermark_image_opacity_slider.setTickInterval(10)
        image_opacity_layout.addWidget(self.watermark_image_opacity_slider)
        
        self.watermark_image_opacity_label = QLabel("50%")
        self.watermark_image_opacity_slider.valueChanged.connect(
            lambda value: self.watermark_image_opacity_label.setText(f"{value}%")
        )
        image_opacity_layout.addWidget(self.watermark_image_opacity_label)
        image_layout.addLayout(image_opacity_layout)
        
        layout.addWidget(self.image_watermark_widget)
        
        # 初始化控件状态
        self.toggle_watermark_type(self.watermark_type_combo.currentText())
        
    def toggle_resize_options(self, mode):
        """根据调整模式切换选项"""
        is_percent = mode == "按百分比调整"
        is_size = mode == "按尺寸调整"
        is_longest = mode == "按最长边调整"
        
        # 设置各个组件的父元素可见性
        self.percent_slider.parent().setVisible(is_percent)
        self.width_spin.parent().setVisible(is_size)
        self.height_spin.parent().setVisible(is_size)
        self.longest_spin.parent().setVisible(is_longest)
        
    def toggle_quality_options(self, format):
        """根据目标格式切换质量选项"""
        is_jpeg = format == "JPEG"
        self.quality_slider.parent().setVisible(is_jpeg)
        
    def toggle_angle_input(self, mode):
        """根据旋转模式切换角度输入"""
        self.angle_spin.parent().setVisible(mode == "自定义角度")
        
    def toggle_watermark_type(self, type):
        """根据水印类型切换选项"""
        is_text = type == "文字水印"
        self.text_watermark_widget.setVisible(is_text)
        self.image_watermark_widget.setVisible(not is_text)
        
    def browse_watermark_image(self):
        """浏览选择水印图片"""
        file_path = QFileDialog.getOpenFileName(self, "选择水印图片", "", 
                                           "图片文件 (*.png *.jpg *.jpeg *.bmp *.gif)")[0]
        if file_path:
            self.watermark_image_input.setText(file_path)
            
    def start_processing(self):
        """开始图片处理"""
        files = self.file_selector.get_files()
        if not files:
            self.show_warning("请先选择要处理的图片文件")
            return
            
        # 获取保存目录
        save_dir = self.get_directory("选择处理后图片的保存目录")
        if not save_dir:
            return
            
        # 获取当前选项卡的索引
        current_tab_index = self.tab_widget.currentIndex()
        
        # 开始处理
        self.operation.set_running_state(True)
        self.operation.signals.progress.emit(0, 100, "开始处理图片...")
        
        # 使用定时器异步执行
        QTimer.singleShot(100, lambda: self.process_images(
            files, save_dir, current_tab_index
        ))
        
    def process_images(self, files, save_dir, tab_index):
        """处理图片"""
        try:
            total_files = len(files)
            
            for i, file_path in enumerate(files):
                if not self.operation.is_running:
                    break
                    
                self.operation.signals.progress.emit(
                    int(i / total_files * 90), 
                    100, 
                    f"正在处理: {os.path.basename(file_path)}"
                )
                
                try:
                    # 打开图片
                    img = Image.open(file_path)
                    
                    # 根据选项卡进行不同处理
                    if tab_index == 0:  # 调整大小
                        img = self.resize_image(img)
                    elif tab_index == 1:  # 格式转换
                        # 格式转换在保存时处理
                        pass
                    elif tab_index == 2:  # 图像增强
                        img = self.enhance_image(img)
                    elif tab_index == 3:  # 图片旋转
                        img = self.rotate_image(img)
                    elif tab_index == 4:  # 水印添加
                        img = self.add_watermark(img)
                    
                    # 确定保存格式和路径
                    if tab_index == 1:  # 格式转换
                        target_format = self.target_format_combo.currentText()
                        base_name = os.path.splitext(os.path.basename(file_path))[0]
                        ext = target_format.lower()
                        save_path = os.path.join(save_dir, f"{base_name}.{ext}")
                        
                        # 保存图片
                        if target_format == "JPEG":
                            quality = self.quality_slider.value()
                            img.convert("RGB").save(save_path, format="JPEG", quality=quality)
                        elif target_format == "PNG":
                            img.save(save_path, format="PNG")
                        elif target_format == "BMP":
                            img.save(save_path, format="BMP")
                        elif target_format == "TIFF":
                            img.save(save_path, format="TIFF")
                        elif target_format == "WEBP":
                            img.save(save_path, format="WEBP", quality=80)
                    else:
                        # 其他操作保持原格式
                        original_ext = os.path.splitext(file_path)[1]
                        base_name = os.path.splitext(os.path.basename(file_path))[0]
                        save_path = os.path.join(save_dir, f"{base_name}_processed{original_ext}")
                        
                        # 保存图片
                        img.save(save_path)
                        
                except Exception as e:
                    self.operation.signals.finished.emit(False, f"处理文件 {os.path.basename(file_path)} 时出错: {str(e)}")
                    return
            
            # 完成
            if self.operation.is_running:
                message = f"图片处理完成，共处理 {total_files} 个图片"
                self.operation.signals.finished.emit(True, message)
            else:
                self.operation.signals.finished.emit(False, "用户取消操作")
                
        except Exception as e:
            self.operation.signals.finished.emit(False, f"处理过程中发生错误: {str(e)}")
            
    def resize_image(self, img):
        """调整图片大小"""
        mode = self.resize_mode_combo.currentText()
        
        if mode == "按百分比调整":
            percent = self.percent_slider.value() / 100.0
            width, height = img.size
            new_width = int(width * percent)
            new_height = int(height * percent)
            return img.resize((new_width, new_height))
            
        elif mode == "按尺寸调整":
            target_width = self.width_spin.value()
            target_height = self.height_spin.value()
            
            if self.keep_aspect_checkbox.isChecked():
                # 保持宽高比
                img.thumbnail((target_width, target_height))
                return img
            else:
                return img.resize((target_width, target_height))
                
        elif mode == "按最长边调整":
            longest = self.longest_spin.value()
            img.thumbnail((longest, longest))
            return img
            
        return img
        
    def enhance_image(self, img):
        """增强图片"""
        # 亮度
        brightness = self.brightness_slider.value() / 100.0
        if brightness != 1.0:
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(brightness)
        
        # 对比度
        contrast = self.contrast_slider.value() / 100.0
        if contrast != 1.0:
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(contrast)
        
        # 饱和度
        saturation = self.saturation_slider.value() / 100.0
        if saturation != 1.0:
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(saturation)
        
        # 锐度
        sharpness = self.sharpness_slider.value() / 100.0
        if sharpness != 1.0:
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(sharpness)
            
        return img
        
    def rotate_image(self, img):
        """旋转图片"""
        mode = self.rotate_mode_combo.currentText()
        
        if mode == "自定义角度":
            angle = self.angle_spin.value()
            return img.rotate(angle, expand=True)
        elif mode == "90度":
            return img.rotate(90, expand=True)
        elif mode == "180度":
            return img.rotate(180, expand=True)
        elif mode == "270度":
            return img.rotate(270, expand=True)
        elif mode == "水平翻转":
            return img.transpose(Image.FLIP_LEFT_RIGHT)
        elif mode == "垂直翻转":
            return img.transpose(Image.FLIP_TOP_BOTTOM)
            
        return img
        
    def add_watermark(self, img):
        """添加水印"""
        watermark_type = self.watermark_type_combo.currentText()
        
        if watermark_type == "文字水印":
            return self.add_text_watermark(img)
        else:
            return self.add_image_watermark(img)
            
    def add_text_watermark(self, img):
        """添加文字水印"""
        from PIL import ImageDraw, ImageFont
        
        # 创建透明图层
        watermark = Image.new("RGBA", img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(watermark)
        
        # 尝试加载字体
        try:
            font = ImageFont.truetype("arial.ttf", self.font_size_spin.value())
        except:
            font = ImageFont.load_default()
        
        # 获取文字尺寸
        text = self.watermark_text_input.text()
        text_width, text_height = draw.textsize(text, font=font)
        
        # 计算位置
        position = self.watermark_position_combo.currentText()
        width, height = img.size
        
        if position == "中心":
            x, y = (width - text_width) // 2, (height - text_height) // 2
        elif position == "左上":
            x, y = 20, 20
        elif position == "右上":
            x, y = width - text_width - 20, 20
        elif position == "左下":
            x, y = 20, height - text_height - 20
        else:  # 右下
            x, y = width - text_width - 20, height - text_height - 20
        
        # 计算透明度
        opacity = int(self.watermark_opacity_slider.value() * 2.55)  # 0-255
        
        # 绘制文字
        draw.text((x, y), text, fill=(255, 255, 255, opacity), font=font)
        
        # 合成图片
        if img.mode != "RGBA":
            img = img.convert("RGBA")
            
        return Image.alpha_composite(img, watermark)
        
    def add_image_watermark(self, img):
        """添加图片水印"""
        watermark_path = self.watermark_image_input.text()
        
        if not os.path.exists(watermark_path):
            return img
            
        # 打开水印图片
        try:
            watermark = Image.open(watermark_path)
        except:
            return img
        
        # 调整水印大小
        watermark_size = self.watermark_size_spin.value() / 100.0
        img_width, img_height = img.size
        watermark_width = int(img_width * watermark_size)
        watermark_height = int(watermark_size * watermark.size[1] / watermark.size[0] * img_width)
        
        watermark = watermark.resize((watermark_width, watermark_height))
        
        # 确保水印有透明通道
        if watermark.mode != "RGBA":
            watermark = watermark.convert("RGBA")
        
        # 创建透明图层
        overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
        
        # 计算位置
        position = self.watermark_position_combo.currentText()
        
        if position == "中心":
            x, y = (img_width - watermark_width) // 2, (img_height - watermark_height) // 2
        elif position == "左上":
            x, y = 20, 20
        elif position == "右上":
            x, y = img_width - watermark_width - 20, 20
        elif position == "左下":
            x, y = 20, img_height - watermark_height - 20
        else:  # 右下
            x, y = img_width - watermark_width - 20, img_height - watermark_height - 20
        
        # 设置透明度
        opacity = int(self.watermark_image_opacity_slider.value() * 2.55)  # 0-255
        
        # 应用透明度到水印
        alpha = watermark.split()[3]
        alpha = alpha.point(lambda p: int(p * opacity / 255))
        watermark.putalpha(alpha)
        
        # 粘贴水印到图层
        overlay.paste(watermark, (x, y), watermark)
        
        # 合成图片
        if img.mode != "RGBA":
            img = img.convert("RGBA")
            
        return Image.alpha_composite(img, overlay)
        
    def update_progress(self, current, total, status):
        """更新进度"""
        self.operation.progress.update_progress(current, total, status)
        
    def processing_finished(self, success, message):
        """图片处理完成"""
        self.operation.set_running_state(False)
        if success:
            self.show_info(message)
        else:
            self.show_error(message)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = ImageProcessWindow()
    window.show()
    sys.exit(app.exec())