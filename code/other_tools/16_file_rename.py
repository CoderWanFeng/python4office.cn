#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件批量重命名工具
功能：根据规则批量重命名文件，支持多种命名模式和预览功能
"""

import sys
import os
import re
from datetime import datetime
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                              QPushButton, QTableWidget, QTableWidgetItem, 
                              QHeaderView, QComboBox, QRadioButton, QButtonGroup,
                              QCheckBox, QFileDialog, QMessageBox)
from PySide6.QtCore import QTimer, Qt

# 添加父目录到路径，以便导入common模块
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.ui_base import BaseMainWindow, FileSelectionWidget, OperationWidget


class FileRenameWindow(BaseMainWindow):
    """文件批量重命名工具主窗口"""
    
    def __init__(self):
        super().__init__("文件批量重命名工具", 1000, 700)
        
    def setup_content(self):
        """设置内容区域"""
        # 文件选择组件
        self.file_selector = FileSelectionWidget("选择要重命名的文件", multi_selection=True)
        self.file_selector.select_files = self.add_files  # 重写选择文件方法
        self.content_layout.addWidget(self.file_selector)
        
        # 重命名规则组件
        self.rename_rules = RenameRulesWidget()
        self.rename_rules.rules_changed.connect(self.update_preview)
        self.content_layout.addWidget(self.rename_rules)
        
        # 文件预览组件
        self.preview_widget = PreviewWidget()
        self.content_layout.addWidget(self.preview_widget)
        
        # 操作区域
        self.operation = OperationWidget("重命名操作")
        self.operation.start_operation = self.start_rename
        self.operation.signals.progress.connect(self.update_progress)
        self.operation.signals.finished.connect(self.rename_finished)
        self.content_layout.addWidget(self.operation)
        
    def add_files(self):
        """添加文件到列表"""
        files = QFileDialog.getOpenFileNames(self, "选择文件")[0]
        
        if not files:
            return
            
        for file_path in files:
            self.preview_widget.add_file(file_path)
            
        # 更新文件选择显示
        self.file_selector.file_paths = self.preview_widget.get_files()
        self.file_selector.update_display()
        
        # 更新预览
        self.update_preview()
        
    def update_preview(self):
        """更新重命名预览"""
        files = self.preview_widget.get_files()
        rules = self.rename_rules.get_rename_rules()
        
        if not files:
            return
            
        # 生成新文件名
        preview_data = []
        for file_path in files:
            old_name = os.path.basename(file_path)
            new_name = self.generate_new_name(file_path, rules)
            preview_data.append([old_name, new_name])
            
        # 更新预览表
        self.preview_widget.update_preview(preview_data)
        
    def generate_new_name(self, file_path, rules):
        """根据规则生成新文件名"""
        if not rules:
            return os.path.basename(file_path)
            
        # 获取文件信息
        dir_path = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)
        name_without_ext, ext = os.path.splitext(file_name)
        
        # 获取文件信息
        try:
            stat = os.stat(file_path)
            mtime = datetime.fromtimestamp(stat.st_mtime)
            ctime = datetime.fromtimestamp(stat.st_ctime)
            size = stat.st_size
        except:
            mtime = datetime.now()
            ctime = datetime.now()
            size = 0
        
        # 根据规则模式生成新名称
        if rules["mode"] == "prefix":
            new_name = f"{rules['prefix']}{name_without_ext}{ext}"
        elif rules["mode"] == "suffix":
            new_name = f"{name_without_ext}{rules['suffix']}{ext}"
        elif rules["mode"] == "replace":
            old_text = rules["old_text"]
            new_text = rules["new_text"]
            if rules["use_regex"]:
                new_name = re.sub(old_text, new_text, file_name)
            else:
                new_name = file_name.replace(old_text, new_text)
        elif rules["mode"] == "template":
            template = rules["template"]
            # 替换模板中的变量
            new_name = template.replace("{name}", name_without_ext)
            new_name = new_name.replace("{ext}", ext[1:])  # 去掉点号
            new_name = new_name.replace("{date}", datetime.now().strftime("%Y%m%d"))
            new_name = new_name.replace("{time}", datetime.now().strftime("%H%M%S"))
            new_name = new_name.replace("{mtime}", mtime.strftime("%Y%m%d"))
            new_name = new_name.replace("{ctime}", ctime.strftime("%Y%m%d"))
            new_name = new_name.replace("{size}", str(size))
            
            # 添加扩展名（如果模板中没有）
            if not new_name.endswith(ext):
                new_name += ext
        elif rules["mode"] == "case":
            if rules["case_type"] == "upper":
                new_name = file_name.upper()
            elif rules["case_type"] == "lower":
                new_name = file_name.lower()
            elif rules["case_type"] == "capitalize":
                new_name = file_name.capitalize()
            elif rules["case_type"] == "title":
                new_name = file_name.title()
            else:
                new_name = file_name
        elif rules["mode"] == "number":
            start_num = rules["start_number"]
            num_digits = rules["num_digits"]
            dir_files = os.listdir(dir_path)
            
            # 计算当前文件在列表中的位置
            all_files = self.preview_widget.get_files()
            index = all_files.index(file_path)
            current_num = start_num + index
            num_str = str(current_num).zfill(num_digits)
            
            new_name = f"{num_str}{name_without_ext}{ext}"
        else:
            new_name = file_name
            
        return new_name
        
    def start_rename(self):
        """开始重命名操作"""
        files = self.preview_widget.get_files()
        if not files:
            self.show_warning("请先选择要重命名的文件")
            return
            
        # 获取重命名规则
        rules = self.rename_rules.get_rename_rules()
        
        # 检查是否有重复的新文件名
        preview_data = self.preview_widget.get_preview_data()
        new_names = [item[1] for item in preview_data]
        if len(new_names) != len(set(new_names)):
            self.show_warning("检测到重复的新文件名，请修改重命名规则")
            return
            
        # 开始处理
        self.operation.set_running_state(True)
        self.operation.signals.progress.emit(0, 100, "开始批量重命名...")
        
        # 使用定时器异步执行
        QTimer.singleShot(100, lambda: self.process_rename(
            files, rules
        ))
        
    def process_rename(self, files, rules):
        """处理文件重命名"""
        try:
            total_files = len(files)
            success_count = 0
            
            for i, file_path in enumerate(files):
                if not self.operation.is_running:
                    break
                    
                old_name = os.path.basename(file_path)
                new_name = self.generate_new_name(file_path, rules)
                
                self.operation.signals.progress.emit(
                    int((i + 1) / total_files * 90), 
                    100, 
                    f"正在重命名: {old_name} → {new_name}"
                )
                
                # 获取目录和新文件路径
                dir_path = os.path.dirname(file_path)
                new_path = os.path.join(dir_path, new_name)
                
                # 检查新文件名是否已存在
                if os.path.exists(new_path) and new_path != file_path:
                    self.operation.signals.finished.emit(False, f"文件 {new_name} 已存在，无法重命名")
                    return
                    
                try:
                    # 重命名文件
                    if new_path != file_path:  # 只有当新名称与旧名称不同时才执行
                        os.rename(file_path, new_path)
                        success_count += 1
                except Exception as e:
                    self.operation.signals.finished.emit(False, f"重命名文件 {old_name} 失败: {str(e)}")
                    return
            
            # 完成
            if self.operation.is_running:
                message = f"重命名完成，成功处理 {success_count}/{total_files} 个文件"
                self.operation.signals.finished.emit(True, message)
            else:
                self.operation.signals.finished.emit(False, "用户取消操作")
                
        except Exception as e:
            self.operation.signals.finished.emit(False, f"重命名过程中发生错误: {str(e)}")
            
    def update_progress(self, current, total, status):
        """更新进度"""
        self.operation.progress.update_progress(current, total, status)
        
    def rename_finished(self, success, message):
        """重命名完成"""
        self.operation.set_running_state(False)
        if success:
            self.show_info(message)
            # 清空预览表
            self.preview_widget.clear_preview()
            self.file_selector.file_paths = []
            self.file_selector.update_display()
        else:
            self.show_error(message)


class RenameRulesWidget(QWidget):
    """重命名规则组件"""
    rules_changed = Signal()
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 重命名模式选择
        mode_group = QWidget()
        mode_layout = QVBoxLayout(mode_group)
        mode_layout.addWidget(QLabel("重命名模式:"))
        
        self.mode_group = QButtonGroup()
        
        self.prefix_radio = QRadioButton("添加前缀")
        self.mode_group.addButton(self.prefix_radio, 0)
        self.prefix_radio.toggled.connect(self.mode_changed)
        mode_layout.addWidget(self.prefix_radio)
        
        self.suffix_radio = QRadioButton("添加后缀")
        self.mode_group.addButton(self.suffix_radio, 1)
        self.suffix_radio.toggled.connect(self.mode_changed)
        mode_layout.addWidget(self.suffix_radio)
        
        self.replace_radio = QRadioButton("替换文本")
        self.mode_group.addButton(self.replace_radio, 2)
        self.replace_radio.setChecked(True)
        self.replace_radio.toggled.connect(self.mode_changed)
        mode_layout.addWidget(self.replace_radio)
        
        self.template_radio = QRadioButton("使用模板")
        self.mode_group.addButton(self.template_radio, 3)
        self.template_radio.toggled.connect(self.mode_changed)
        mode_layout.addWidget(self.template_radio)
        
        self.case_radio = QRadioButton("更改大小写")
        self.mode_group.addButton(self.case_radio, 4)
        self.case_radio.toggled.connect(self.mode_changed)
        mode_layout.addWidget(self.case_radio)
        
        self.number_radio = QRadioButton("添加编号")
        self.mode_group.addButton(self.number_radio, 5)
        self.number_radio.toggled.connect(self.mode_changed)
        mode_layout.addWidget(self.number_radio)
        
        layout.addWidget(mode_group)
        
        # 规则参数区域
        self.params_widget = QWidget()
        self.params_layout = QVBoxLayout(self.params_widget)
        layout.addWidget(self.params_widget)
        
        # 初始化控件状态
        self.mode_changed(self.replace_radio.isChecked())
        
    def mode_changed(self, checked):
        """根据模式切换参数区域"""
        mode_id = self.mode_group.checkedId()
        
        # 清空参数区域
        while self.params_layout.count():
            child = self.params_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        if mode_id == 0:  # 添加前缀
            self.add_prefix_params()
        elif mode_id == 1:  # 添加后缀
            self.add_suffix_params()
        elif mode_id == 2:  # 替换文本
            self.add_replace_params()
        elif mode_id == 3:  # 使用模板
            self.add_template_params()
        elif mode_id == 4:  # 更改大小写
            self.add_case_params()
        elif mode_id == 5:  # 添加编号
            self.add_number_params()
        
        # 发出信号通知预览更新
        self.rules_changed.emit()
        
    def add_prefix_params(self):
        """添加前缀参数"""
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("前缀:"))
        self.prefix_input = QLineEdit()
        self.prefix_input.textChanged.connect(self.rules_changed.emit)
        input_layout.addWidget(self.prefix_input)
        self.params_layout.addLayout(input_layout)
        
    def add_suffix_params(self):
        """添加后缀参数"""
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("后缀:"))
        self.suffix_input = QLineEdit()
        self.suffix_input.textChanged.connect(self.rules_changed.emit)
        input_layout.addWidget(self.suffix_input)
        self.params_layout.addLayout(input_layout)
        
    def add_replace_params(self):
        """添加替换文本参数"""
        old_layout = QHBoxLayout()
        old_layout.addWidget(QLabel("查找文本:"))
        self.old_text_input = QLineEdit()
        self.old_text_input.textChanged.connect(self.rules_changed.emit)
        old_layout.addWidget(self.old_text_input)
        self.params_layout.addLayout(old_layout)
        
        new_layout = QHBoxLayout()
        new_layout.addWidget(QLabel("替换为:"))
        self.new_text_input = QLineEdit()
        self.new_text_input.textChanged.connect(self.rules_changed.emit)
        new_layout.addWidget(self.new_text_input)
        self.params_layout.addLayout(new_layout)
        
        self.use_regex_checkbox = QCheckBox("使用正则表达式")
        self.use_regex_checkbox.stateChanged.connect(self.rules_changed.emit)
        self.params_layout.addWidget(self.use_regex_checkbox)
        
    def add_template_params(self):
        """添加模板参数"""
        template_layout = QVBoxLayout()
        template_layout.addWidget(QLabel("模板 (可用变量: {name}, {ext}, {date}, {time}, {mtime}, {ctime}, {size}):"))
        
        self.template_input = QLineEdit("{name}_{date}_{time}.{ext}")
        self.template_input.textChanged.connect(self.rules_changed.emit)
        template_layout.addWidget(self.template_input)
        
        self.params_layout.addLayout(template_layout)
        
    def add_case_params(self):
        """添加大小写参数"""
        self.case_combo = QComboBox()
        self.case_combo.addItems(["全部大写", "全部小写", "首字母大写", "标题格式"])
        self.case_combo.currentTextChanged.connect(self.rules_changed.emit)
        self.params_layout.addWidget(self.case_combo)
        
    def add_number_params(self):
        """添加编号参数"""
        start_layout = QHBoxLayout()
        start_layout.addWidget(QLabel("起始编号:"))
        self.start_number_spin = QSpinBox()
        self.start_number_spin.setMinimum(1)
        self.start_number_spin.setValue(1)
        self.start_number_spin.valueChanged.connect(self.rules_changed.emit)
        start_layout.addWidget(self.start_number_spin)
        self.params_layout.addLayout(start_layout)
        
        digits_layout = QHBoxLayout()
        digits_layout.addWidget(QLabel("编号位数:"))
        self.num_digits_spin = QSpinBox()
        self.num_digits_spin.setMinimum(1)
        self.num_digits_spin.setMaximum(10)
        self.num_digits_spin.setValue(3)
        self.num_digits_spin.valueChanged.connect(self.rules_changed.emit)
        digits_layout.addWidget(self.num_digits_spin)
        self.params_layout.addLayout(digits_layout)
        
    def get_rename_rules(self):
        """获取重命名规则"""
        mode_id = self.mode_group.checkedId()
        
        # 根据模式获取对应的规则
        if mode_id == 0:  # 添加前缀
            return {
                "mode": "prefix",
                "prefix": self.prefix_input.text()
            }
        elif mode_id == 1:  # 添加后缀
            return {
                "mode": "suffix",
                "suffix": self.suffix_input.text()
            }
        elif mode_id == 2:  # 替换文本
            return {
                "mode": "replace",
                "old_text": self.old_text_input.text(),
                "new_text": self.new_text_input.text(),
                "use_regex": self.use_regex_checkbox.isChecked()
            }
        elif mode_id == 3:  # 使用模板
            return {
                "mode": "template",
                "template": self.template_input.text()
            }
        elif mode_id == 4:  # 更改大小写
            case_type_map = {
                "全部大写": "upper",
                "全部小写": "lower",
                "首字母大写": "capitalize",
                "标题格式": "title"
            }
            return {
                "mode": "case",
                "case_type": case_type_map.get(self.case_combo.currentText(), "lower")
            }
        elif mode_id == 5:  # 添加编号
            return {
                "mode": "number",
                "start_number": self.start_number_spin.value(),
                "num_digits": self.num_digits_spin.value()
            }
        else:
            return {"mode": "none"}


class PreviewWidget(QWidget):
    """预览组件"""
    
    def __init__(self):
        super().__init__()
        self.files = []
        self.preview_data = []
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 标题和按钮
        header_layout = QHBoxLayout()
        header_layout.addWidget(QLabel("重命名预览:"))
        
        self.add_file_btn = QPushButton("添加文件")
        self.add_file_btn.clicked.connect(self.add_files)
        header_layout.addWidget(self.add_file_btn)
        
        self.remove_file_btn = QPushButton("移除选中")
        self.remove_file_btn.clicked.connect(self.remove_selected_file)
        header_layout.addWidget(self.remove_file_btn)
        
        self.clear_btn = QPushButton("清空列表")
        self.clear_btn.clicked.connect(self.clear_files)
        header_layout.addWidget(self.clear_btn)
        
        layout.addLayout(header_layout)
        
        # 预览表格
        self.preview_table = QTableWidget(0, 2)
        self.preview_table.setHorizontalHeaderLabels(["原文件名", "新文件名"])
        self.preview_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.preview_table.setSelectionBehavior(QTableWidget.SelectRows)
        layout.addWidget(self.preview_table)
        
    def add_files(self):
        """添加文件"""
        files = QFileDialog.getOpenFileNames(self, "选择文件")[0]
        
        if not files:
            return
            
        for file_path in files:
            self.add_file(file_path)
            
    def add_file(self, file_path):
        """添加单个文件"""
        # 检查是否已存在
        if file_path in self.files:
            return
            
        self.files.append(file_path)
        
    def remove_selected_file(self):
        """移除选中的文件"""
        current_row = self.preview_table.currentRow()
        if current_row >= 0:
            # 从文件列表中移除
            if 0 <= current_row < len(self.files):
                self.files.pop(current_row)
            
            # 从预览数据中移除
            if 0 <= current_row < len(self.preview_data):
                self.preview_data.pop(current_row)
            
            # 从表格中移除
            self.preview_table.removeRow(current_row)
            
    def clear_files(self):
        """清空文件列表"""
        self.files = []
        self.preview_data = []
        self.preview_table.setRowCount(0)
        
    def get_files(self):
        """获取文件路径列表"""
        return self.files
        
    def update_preview(self, preview_data=None):
        """更新预览表"""
        if preview_data is None:
            return
            
        self.preview_data = preview_data
        
        # 设置表格
        self.preview_table.setRowCount(len(preview_data))
        
        for i, data in enumerate(preview_data):
            self.preview_table.setItem(i, 0, QTableWidgetItem(data[0]))
            self.preview_table.setItem(i, 1, QTableWidgetItem(data[1]))
            
    def get_preview_data(self):
        """获取预览数据"""
        return self.preview_data
        
    def clear_preview(self):
        """清空预览表"""
        self.preview_table.setRowCount(0)
        self.preview_data = []


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = FileRenameWindow()
    window.show()
    sys.exit(app.exec())