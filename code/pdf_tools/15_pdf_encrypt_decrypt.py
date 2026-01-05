#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PDF加密解密工具
功能：为PDF文件添加或移除密码保护，支持不同权限设置
"""

import sys
import os
from PyPDF2 import PdfReader, PdfWriter
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                              QPushButton, QCheckBox, QRadioButton, QButtonGroup,
                              QComboBox, QFileDialog, QMessageBox)
from PySide6.QtCore import QTimer, Qt

# 添加父目录到路径，以便导入common模块
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.ui_base import BaseMainWindow, FileSelectionWidget, OperationWidget


class PdfEncryptDecryptWindow(BaseMainWindow):
    """PDF加密解密工具主窗口"""
    
    def __init__(self):
        super().__init__("PDF加密解密工具", 900, 650)
        
    def setup_content(self):
        """设置内容区域"""
        # 文件选择组件
        self.file_selector = FileSelectionWidget("选择要处理的PDF文件", multi_selection=True)
        self.content_layout.addWidget(self.file_selector)
        
        # 操作选项组件
        self.operation_options = OperationOptionsWidget()
        self.content_layout.addWidget(self.operation_options)
        
        # 操作区域
        self.operation = OperationWidget("加密/解密操作")
        self.operation.start_operation = self.start_operation
        self.operation.signals.progress.connect(self.update_progress)
        self.operation.signals.finished.connect(self.operation_finished)
        self.content_layout.addWidget(self.operation)
        
    def start_operation(self):
        """开始操作"""
        files = self.file_selector.get_files()
        if not files:
            self.show_warning("请先选择要处理的PDF文件")
            return
            
        # 获取操作选项
        options = self.operation_options.get_operation_options()
        
        # 验证选项
        if options["operation"] == "encrypt":
            if not options["user_password"] and not options["owner_password"]:
                self.show_warning("请输入用户密码或所有者密码")
                return
                
        # 获取保存目录
        save_dir = self.get_directory("选择处理后的文件保存目录")
        if not save_dir:
            return
            
        # 开始处理
        self.operation.set_running_state(True)
        self.operation.signals.progress.emit(0, 100, f"开始{'加密' if options['operation'] == 'encrypt' else '解密'}PDF文件...")
        
        # 使用定时器异步执行
        QTimer.singleShot(100, lambda: self.process_operation(
            files, options, save_dir
        ))
        
    def process_operation(self, files, options, save_dir):
        """处理PDF加密/解密"""
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
                    # 读取PDF文件
                    reader = PdfReader(file_path)
                    
                    # 检查PDF是否已加密
                    is_encrypted = reader.is_encrypted
                    
                    # 验证操作是否有效
                    if options["operation"] == "decrypt" and not is_encrypted:
                        self.operation.signals.finished.emit(False, f"文件 {os.path.basename(file_path)} 未加密，无需解密")
                        return
                        
                    if options["operation"] == "encrypt" and is_encrypted:
                        if not options["current_password"]:
                            self.operation.signals.finished.emit(False, f"文件 {os.path.basename(file_path)} 已加密，需要输入当前密码")
                            return
                            
                        # 尝试用提供的密码解密
                        if not reader.decrypt(options["current_password"]):
                            self.operation.signals.finished.emit(False, f"文件 {os.path.basename(file_path)} 密码错误，无法解密")
                            return
                    
                    # 创建PDF写入器
                    writer = PdfWriter()
                    
                    # 复制所有页面
                    for page in reader.pages:
                        writer.add_page(page)
                    
                    # 复制元数据
                    if reader.metadata:
                        writer.add_metadata(reader.metadata)
                    
                    # 执行操作
                    if options["operation"] == "encrypt":
                        # 加密PDF
                        user_password = options["user_password"] if options["user_password"] else None
                        owner_password = options["owner_password"] if options["owner_password"] else None
                        
                        # 设置加密参数
                        if options["use_128bit"]:
                            # 使用128位RC4加密
                            encryption_key_length = 128
                        else:
                            # 使用40位RC4加密
                            encryption_key_length = 40
                        
                        # 设置权限
                        permissions = {
                            "print": options["allow_print"],
                            "modify": options["allow_modify"],
                            "copy": options["allow_copy"],
                            "annotate": options["allow_annotate"],
                            "fill_forms": options["allow_fill_forms"],
                            "extract": options["allow_extract"],
                            "assemble": options["allow_assemble"]
                        }
                        
                        # 添加加密
                        writer.encrypt(
                            user_password=user_password,
                            owner_password=owner_password,
                            use_128bit=encryption_key_length == 128,
                            permissions_flag=self.calculate_permission_flag(permissions)
                        )
                        
                    # 保存文件
                    base_name = os.path.splitext(os.path.basename(file_path))[0]
                    if options["operation"] == "encrypt":
                        new_name = f"{base_name}_加密.pdf"
                    else:
                        new_name = f"{base_name}_解密.pdf"
                    new_path = os.path.join(save_dir, new_name)
                    
                    with open(new_path, "wb") as output_file:
                        writer.write(output_file)
                        
                except Exception as e:
                    self.operation.signals.finished.emit(False, f"处理文件 {os.path.basename(file_path)} 时出错: {str(e)}")
                    return
            
            # 完成
            if self.operation.is_running:
                message = f"操作完成，共处理 {total_files} 个PDF文件"
                self.operation.signals.finished.emit(True, message)
            else:
                self.operation.signals.finished.emit(False, "用户取消操作")
                
        except Exception as e:
            self.operation.signals.finished.emit(False, f"操作过程中发生错误: {str(e)}")
            
    def calculate_permission_flag(self, permissions):
        """计算权限标志"""
        # PyPDF2的权限标志（基于PDF规范）
        flag = 0
        if permissions["print"]:
            flag |= 4  # bit 3 (0-索引) - 打印文档
        if permissions["modify"]:
            flag |= 8  # bit 4 - 修改文档内容
        if permissions["copy"]:
            flag |= 16  # bit 5 - 复制或提取文本和图形
        if permissions["annotate"]:
            flag |= 32  # bit 6 - 添加或修改注释
        if permissions["fill_forms"]:
            flag |= 256  # bit 9 - 填写表单字段
        if permissions["extract"]:
            flag |= 512  # bit 10 - 提取文本和图形以支持残障人士
        if permissions["assemble"]:
            flag |= 1024  # bit 11 - 组装文档
            
        return flag
            
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


class OperationOptionsWidget(QWidget):
    """操作选项组件"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 操作类型选择
        operation_group = QWidget()
        operation_layout = QVBoxLayout(operation_group)
        operation_layout.addWidget(QLabel("操作类型:"))
        
        self.operation_group = QButtonGroup()
        
        self.encrypt_radio = QRadioButton("加密PDF")
        self.encrypt_radio.setChecked(True)
        self.operation_group.addButton(self.encrypt_radio, 0)
        self.encrypt_radio.toggled.connect(self.toggle_operation_options)
        operation_layout.addWidget(self.encrypt_radio)
        
        self.decrypt_radio = QRadioButton("解密PDF")
        self.operation_group.addButton(self.decrypt_radio, 1)
        self.decrypt_radio.toggled.connect(self.toggle_operation_options)
        operation_layout.addWidget(self.decrypt_radio)
        
        layout.addWidget(operation_group)
        
        # 密码设置
        password_group = QWidget()
        self.password_layout = QVBoxLayout(password_group)
        
        # 当前密码（用于解密已加密的文件）
        current_password_layout = QHBoxLayout()
        current_password_layout.addWidget(QLabel("当前密码:"))
        self.current_password_input = QLineEdit()
        self.current_password_input.setEchoMode(QLineEdit.Password)
        current_password_layout.addWidget(self.current_password_input)
        self.password_layout.addLayout(current_password_layout)
        
        # 用户密码
        user_password_layout = QHBoxLayout()
        user_password_layout.addWidget(QLabel("用户密码:"))
        self.user_password_input = QLineEdit()
        self.user_password_input.setEchoMode(QLineEdit.Password)
        user_password_layout.addWidget(self.user_password_input)
        self.password_layout.addLayout(user_password_layout)
        
        # 所有者密码
        owner_password_layout = QHBoxLayout()
        owner_password_layout.addWidget(QLabel("所有者密码:"))
        self.owner_password_input = QLineEdit()
        self.owner_password_input.setEchoMode(QLineEdit.Password)
        owner_password_layout.addWidget(self.owner_password_input)
        self.password_layout.addLayout(owner_password_layout)
        
        layout.addWidget(password_group)
        
        # 加密选项
        self.encrypt_options = QWidget()
        encrypt_layout = QVBoxLayout(self.encrypt_options)
        
        # 加密强度
        encrypt_strength_layout = QHBoxLayout()
        encrypt_strength_layout.addWidget(QLabel("加密强度:"))
        self.encryption_combo = QComboBox()
        self.encryption_combo.addItems(["40位RC4 (兼容性更好)", "128位RC4 (安全性更高)"])
        self.encryption_combo.setCurrentIndex(1)  # 默认使用128位
        encrypt_strength_layout.addWidget(self.encryption_combo)
        encrypt_layout.addLayout(encrypt_strength_layout)
        
        # 权限设置
        encrypt_layout.addWidget(QLabel("权限设置:"))
        
        # 打印权限
        self.allow_print_checkbox = QCheckBox("允许打印")
        self.allow_print_checkbox.setChecked(True)
        encrypt_layout.addWidget(self.allow_print_checkbox)
        
        # 修改权限
        self.allow_modify_checkbox = QCheckBox("允许修改内容")
        self.allow_modify_checkbox.setChecked(True)
        encrypt_layout.addWidget(self.allow_modify_checkbox)
        
        # 复制权限
        self.allow_copy_checkbox = QCheckBox("允许复制文本和图片")
        self.allow_copy_checkbox.setChecked(True)
        encrypt_layout.addWidget(self.allow_copy_checkbox)
        
        # 注释权限
        self.allow_annotate_checkbox = QCheckBox("允许添加注释")
        self.allow_annotate_checkbox.setChecked(True)
        encrypt_layout.addWidget(self.allow_annotate_checkbox)
        
        # 表单权限
        self.allow_fill_forms_checkbox = QCheckBox("允许填写表单")
        self.allow_fill_forms_checkbox.setChecked(True)
        encrypt_layout.addWidget(self.allow_fill_forms_checkbox)
        
        # 提取权限
        self.allow_extract_checkbox = QCheckBox("允许提取页面")
        self.allow_extract_checkbox.setChecked(True)
        encrypt_layout.addWidget(self.allow_extract_checkbox)
        
        # 组装权限
        self.allow_assemble_checkbox = QCheckBox("允许组装文档")
        self.allow_assemble_checkbox.setChecked(True)
        encrypt_layout.addWidget(self.allow_assemble_checkbox)
        
        layout.addWidget(self.encrypt_options)
        
        # 初始化控件状态
        self.toggle_operation_options(self.encrypt_radio.isChecked())
        
    def toggle_operation_options(self, encrypt_checked):
        """根据操作类型切换选项"""
        is_encrypt = encrypt_checked
        
        # 切换密码输入框状态
        self.user_password_input.parent().setEnabled(is_encrypt)
        self.owner_password_input.parent().setEnabled(is_encrypt)
        
        # 切换当前密码输入框状态
        self.current_password_input.parent().setEnabled(False)  # 默认禁用
        
        # 切换加密选项状态
        self.encrypt_options.setVisible(is_encrypt)
        
    def get_operation_options(self):
        """获取操作选项"""
        return {
            "operation": "encrypt" if self.encrypt_radio.isChecked() else "decrypt",
            "current_password": self.current_password_input.text(),
            "user_password": self.user_password_input.text(),
            "owner_password": self.owner_password_input.text(),
            "use_128bit": self.encryption_combo.currentIndex() == 1,
            "allow_print": self.allow_print_checkbox.isChecked(),
            "allow_modify": self.allow_modify_checkbox.isChecked(),
            "allow_copy": self.allow_copy_checkbox.isChecked(),
            "allow_annotate": self.allow_annotate_checkbox.isChecked(),
            "allow_fill_forms": self.allow_fill_forms_checkbox.isChecked(),
            "allow_extract": self.allow_extract_checkbox.isChecked(),
            "allow_assemble": self.allow_assemble_checkbox.isChecked()
        }


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = PdfEncryptDecryptWindow()
    window.show()
    sys.exit(app.exec())