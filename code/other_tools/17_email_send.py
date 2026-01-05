#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
邮件批量发送工具
功能：批量发送个性化邮件，支持附件和HTML格式
"""

import sys
import os
import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                              QPushButton, QTableWidget, QTableWidgetItem, 
                              QHeaderView, QTabWidget, QTextEdit, QComboBox,
                              QFileDialog, QMessageBox, QCheckBox, QSpinBox)
from PySide6.QtCore import QTimer, Qt

# 添加父目录到路径，以便导入common模块
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.ui_base import BaseMainWindow, FileSelectionWidget, OperationWidget


class EmailSendWindow(BaseMainWindow):
    """邮件批量发送工具主窗口"""
    
    def __init__(self):
        super().__init__("邮件批量发送工具", 1000, 700)
        
    def setup_content(self):
        """设置内容区域"""
        # 使用选项卡组织界面
        self.tab_widget = QTabWidget()
        self.content_layout.addWidget(self.tab_widget)
        
        # 邮件设置选项卡
        self.email_settings_tab = QWidget()
        self.setup_email_settings_tab()
        self.tab_widget.addTab(self.email_settings_tab, "邮件设置")
        
        # 收件人列表选项卡
        self.recipients_tab = QWidget()
        self.setup_recipients_tab()
        self.tab_widget.addTab(self.recipients_tab, "收件人列表")
        
        # 邮件内容选项卡
        self.content_tab = QWidget()
        self.setup_content_tab()
        self.tab_widget.addTab(self.content_tab, "邮件内容")
        
        # 操作区域
        self.operation = OperationWidget("发送邮件")
        self.operation.start_operation = self.send_emails
        self.operation.signals.progress.connect(self.update_progress)
        self.operation.signals.finished.connect(self.email_sending_finished)
        self.content_layout.addWidget(self.operation)
        
    def setup_email_settings_tab(self):
        """设置邮件设置选项卡"""
        layout = QVBoxLayout(self.email_settings_tab)
        
        # SMTP服务器设置
        server_group = QWidget()
        server_layout = QVBoxLayout(server_group)
        server_layout.addWidget(QLabel("SMTP服务器设置:"))
        
        # 服务器选择
        preset_layout = QHBoxLayout()
        preset_layout.addWidget(QLabel("预设服务:"))
        self.preset_combo = QComboBox()
        self.preset_combo.addItems(["自定义", "Gmail", "Outlook", "QQ邮箱", "163邮箱"])
        self.preset_combo.currentTextChanged.connect(self.load_preset)
        preset_layout.addWidget(self.preset_combo)
        server_layout.addLayout(preset_layout)
        
        # SMTP服务器
        smtp_layout = QHBoxLayout()
        smtp_layout.addWidget(QLabel("SMTP服务器:"))
        self.smtp_server_input = QLineEdit("smtp.gmail.com")
        smtp_layout.addWidget(self.smtp_server_input)
        
        smtp_layout.addWidget(QLabel("端口:"))
        self.smtp_port_spin = QSpinBox()
        self.smtp_port_spin.setRange(1, 65535)
        self.smtp_port_spin.setValue(587)
        smtp_layout.addWidget(self.smtp_port_spin)
        
        server_layout.addLayout(smtp_layout)
        
        # 加密设置
        self.ssl_checkbox = QCheckBox("使用SSL连接")
        self.tls_checkbox = QCheckBox("使用TLS加密")
        self.tls_checkbox.setChecked(True)
        server_layout.addWidget(self.ssl_checkbox)
        server_layout.addWidget(self.tls_checkbox)
        
        layout.addWidget(server_group)
        
        # 邮箱账户设置
        account_group = QWidget()
        account_layout = QVBoxLayout(account_group)
        account_layout.addWidget(QLabel("邮箱账户设置:"))
        
        # 发件人邮箱
        email_layout = QHBoxLayout()
        email_layout.addWidget(QLabel("发件人邮箱:"))
        self.email_input = QLineEdit("your_email@gmail.com")
        email_layout.addWidget(self.email_input)
        account_layout.addLayout(email_layout)
        
        # 显示名
        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("显示名:"))
        self.display_name_input = QLineEdit("发件人姓名")
        name_layout.addWidget(self.display_name_input)
        account_layout.addLayout(name_layout)
        
        # 密码
        password_layout = QHBoxLayout()
        password_layout.addWidget(QLabel("密码/授权码:"))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        password_layout.addWidget(self.password_input)
        account_layout.addLayout(password_layout)
        
        layout.addWidget(account_group)
        
        # 发送设置
        send_group = QWidget()
        send_layout = QVBoxLayout(send_group)
        send_layout.addWidget(QLabel("发送设置:"))
        
        # 发送间隔
        interval_layout = QHBoxLayout()
        interval_layout.addWidget(QLabel("发送间隔(秒):"))
        self.send_interval_spin = QSpinBox()
        self.send_interval_spin.setMinimum(0)
        self.send_interval_spin.setMaximum(60)
        self.send_interval_spin.setValue(2)
        interval_layout.addWidget(self.send_interval_spin)
        
        self.random_interval_checkbox = QCheckBox("随机间隔")
        interval_layout.addWidget(self.random_interval_checkbox)
        send_layout.addLayout(interval_layout)
        
        # 预览模式
        self.preview_mode_checkbox = QCheckBox("预览模式（不实际发送，只打印邮件内容）")
        send_layout.addWidget(self.preview_mode_checkbox)
        
        layout.addWidget(send_group)
        
    def setup_recipients_tab(self):
        """设置收件人列表选项卡"""
        layout = QVBoxLayout(self.recipients_tab)
        
        # 收件人导入
        import_group = QWidget()
        import_layout = QVBoxLayout(import_group)
        import_layout.addWidget(QLabel("收件人导入:"))
        
        import_btn_layout = QHBoxLayout()
        self.import_csv_btn = QPushButton("从CSV导入")
        self.import_csv_btn.clicked.connect(self.import_from_csv)
        import_btn_layout.addWidget(self.import_csv_btn)
        
        self.add_recipient_btn = QPushButton("手动添加")
        self.add_recipient_btn.clicked.connect(self.add_recipient)
        import_btn_layout.addWidget(self.add_recipient_btn)
        
        import_layout.addLayout(import_btn_layout)
        layout.addWidget(import_group)
        
        # 收件人列表
        layout.addWidget(QLabel("收件人列表:"))
        
        self.recipients_table = QTableWidget(0, 4)
        self.recipients_table.setHorizontalHeaderLabels(["姓名", "邮箱", "变量1", "变量2"])
        self.recipients_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.recipients_table)
        
        # 按钮区域
        btn_layout = QHBoxLayout()
        
        self.remove_recipient_btn = QPushButton("删除选中")
        self.remove_recipient_btn.clicked.connect(self.remove_recipient)
        btn_layout.addWidget(self.remove_recipient_btn)
        
        self.clear_recipients_btn = QPushButton("清空列表")
        self.clear_recipients_btn.clicked.connect(self.clear_recipients)
        btn_layout.addWidget(self.clear_recipients_btn)
        
        layout.addLayout(btn_layout)
        
        # CSV格式说明
        info_label = QLabel("CSV格式说明：第一行为标题行（姓名,邮箱,变量1,变量2...），后续行为数据行")
        info_label.setStyleSheet("color: #888; font-size: 12px;")
        layout.addWidget(info_label)
        
    def setup_content_tab(self):
        """设置邮件内容选项卡"""
        layout = QVBoxLayout(self.content_tab)
        
        # 邮件主题
        subject_layout = QHBoxLayout()
        subject_layout.addWidget(QLabel("邮件主题:"))
        self.subject_input = QLineEdit()
        subject_layout.addWidget(self.subject_input)
        layout.addLayout(subject_layout)
        
        # 邮件格式
        format_layout = QHBoxLayout()
        format_layout.addWidget(QLabel("邮件格式:"))
        self.format_combo = QComboBox()
        self.format_combo.addItems(["纯文本", "HTML"])
        format_layout.addWidget(self.format_combo)
        layout.addLayout(format_layout)
        
        # 邮件内容
        layout.addWidget(QLabel("邮件内容 (可使用变量: {name}, {email}, {var1}, {var2}):"))
        self.content_editor = QTextEdit()
        self.content_editor.setMaximumHeight(300)
        self.content_editor.setPlaceholderText("尊敬的{name}:\n\n这是一封测试邮件。\n\n祝好,\n{sender_name}")
        layout.addWidget(self.content_editor)
        
        # 附件设置
        attachment_group = QWidget()
        attachment_layout = QVBoxLayout(attachment_group)
        attachment_layout.addWidget(QLabel("附件:"))
        
        self.attachment_list = QTextEdit()
        self.attachment_list.setMaximumHeight(100)
        self.attachment_list.setReadOnly(True)
        attachment_layout.addWidget(self.attachment_list)
        
        attachment_btn_layout = QHBoxLayout()
        self.add_attachment_btn = QPushButton("添加附件")
        self.add_attachment_btn.clicked.connect(self.add_attachment)
        attachment_btn_layout.addWidget(self.add_attachment_btn)
        
        self.clear_attachments_btn = QPushButton("清空附件")
        self.clear_attachments_btn.clicked.connect(self.clear_attachments)
        attachment_btn_layout.addWidget(self.clear_attachments_btn)
        
        attachment_layout.addLayout(attachment_btn_layout)
        layout.addWidget(attachment_group)
        
    def load_preset(self, preset_name):
        """加载预设的邮件服务配置"""
        presets = {
            "Gmail": {
                "smtp_server": "smtp.gmail.com",
                "smtp_port": 587,
                "use_ssl": False,
                "use_tls": True
            },
            "Outlook": {
                "smtp_server": "smtp-mail.outlook.com",
                "smtp_port": 587,
                "use_ssl": False,
                "use_tls": True
            },
            "QQ邮箱": {
                "smtp_server": "smtp.qq.com",
                "smtp_port": 465,
                "use_ssl": True,
                "use_tls": False
            },
            "163邮箱": {
                "smtp_server": "smtp.163.com",
                "smtp_port": 465,
                "use_ssl": True,
                "use_tls": False
            }
        }
        
        if preset_name in presets:
            preset = presets[preset_name]
            self.smtp_server_input.setText(preset["smtp_server"])
            self.smtp_port_spin.setValue(preset["smtp_port"])
            self.ssl_checkbox.setChecked(preset["use_ssl"])
            self.tls_checkbox.setChecked(preset["use_tls"])
            
    def import_from_csv(self):
        """从CSV文件导入收件人"""
        file_path = QFileDialog.getOpenFileName(self, "选择CSV文件", "", "CSV文件 (*.csv)")[0]
        if not file_path:
            return
            
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as file:  # 使用utf-8-sig处理BOM
                reader = csv.reader(file)
                headers = next(reader)  # 跳过标题行
                
                # 确保表格有足够的列
                required_cols = max(4, len(headers))
                self.recipients_table.setColumnCount(required_cols)
                
                # 更新表头
                if len(headers) < 4:
                    headers = headers + ["变量1", "变量2", "变量3", "变量4"]
                self.recipients_table.setHorizontalHeaderLabels(headers[:4])
                
                # 清空现有数据
                self.recipients_table.setRowCount(0)
                
                # 添加数据
                for row in reader:
                    row_index = self.recipients_table.rowCount()
                    self.recipients_table.insertRow(row_index)
                    
                    for col_index, cell in enumerate(row):
                        if col_index < 4:  # 只添加前4列
                            item = QTableWidgetItem(cell.strip())
                            self.recipients_table.setItem(row_index, col_index, item)
            
            self.show_info(f"成功导入 {self.recipients_table.rowCount()} 个收件人")
            
        except Exception as e:
            self.show_error(f"导入CSV文件失败: {str(e)}")
            
    def add_recipient(self):
        """手动添加收件人"""
        row_index = self.recipients_table.rowCount()
        self.recipients_table.insertRow(row_index)
        
        for col in range(4):
            self.recipients_table.setItem(row_index, col, QTableWidgetItem(""))
            
        # 自动跳转到新行并选择第一列
        self.recipients_table.setCurrentCell(row_index, 0)
        self.recipients_table.editItem(self.recipients_table.item(row_index, 0))
        
    def remove_recipient(self):
        """删除选中的收件人"""
        current_row = self.recipients_table.currentRow()
        if current_row >= 0:
            self.recipients_table.removeRow(current_row)
            
    def clear_recipients(self):
        """清空收件人列表"""
        self.recipients_table.setRowCount(0)
        
    def add_attachment(self):
        """添加附件"""
        files = QFileDialog.getOpenFileNames(self, "选择附件文件")[0]
        if not files:
            return
            
        for file_path in files:
            if file_path not in self.attachment_list.toPlainText().split("\n"):
                self.attachment_list.append(file_path)
                
    def clear_attachments(self):
        """清空附件列表"""
        self.attachment_list.clear()
        
    def send_emails(self):
        """发送邮件"""
        # 检查收件人列表
        if self.recipients_table.rowCount() == 0:
            self.show_warning("请先添加收件人")
            return
            
        # 检查邮件内容
        if not self.subject_input.text().strip() or not self.content_editor.toPlainText().strip():
            self.show_warning("请填写邮件主题和内容")
            return
            
        # 开始发送
        self.operation.set_running_state(True)
        self.operation.signals.progress.emit(0, 100, "准备发送邮件...")
        
        # 使用定时器异步执行
        QTimer.singleShot(100, self.process_email_sending)
        
    def process_email_sending(self):
        """处理邮件发送"""
        try:
            # 获取SMTP设置
            smtp_server = self.smtp_server_input.text().strip()
            smtp_port = self.smtp_port_spin.value()
            use_ssl = self.ssl_checkbox.isChecked()
            use_tls = self.tls_checkbox.isChecked()
            email = self.email_input.text().strip()
            password = self.password_input.text().strip()
            display_name = self.display_name_input.text().strip()
            
            # 获取发送设置
            send_interval = self.send_interval_spin.value()
            random_interval = self.random_interval_checkbox.isChecked()
            preview_mode = self.preview_mode_checkbox.isChecked()
            
            # 获取邮件内容设置
            subject = self.subject_input.text().strip()
            content = self.content_editor.toPlainText()
            is_html = self.format_combo.currentText() == "HTML"
            
            # 获取附件列表
            attachments = [path.strip() for path in self.attachment_list.toPlainText().split("\n") if path.strip()]
            
            # 获取收件人列表
            recipients = []
            for row in range(self.recipients_table.rowCount()):
                name_item = self.recipients_table.item(row, 0)
                email_item = self.recipients_table.item(row, 1)
                
                if email_item and email_item.text().strip():
                    recipient = {
                        "name": name_item.text().strip() if name_item else "",
                        "email": email_item.text().strip(),
                        "vars": []
                    }
                    
                    # 获取变量
                    for col in range(2, self.recipients_table.columnCount()):
                        var_item = self.recipients_table.item(row, col)
                        if var_item:
                            recipient["vars"].append(var_item.text().strip())
                        else:
                            recipient["vars"].append("")
                    
                    recipients.append(recipient)
            
            total_recipients = len(recipients)
            
            # 如果是预览模式，直接打印邮件内容
            if preview_mode:
                self.operation.signals.progress.emit(50, 100, "预览邮件...")
                
                preview_text = f"=== 邮件预览 ===\n"
                preview_text += f"发件人: {display_name} <{email}>\n"
                preview_text += f"SMTP: {smtp_server}:{smtp_port}\n"
                preview_text += f"收件人数量: {total_recipients}\n\n"
                
                for recipient in recipients:
                    # 替换变量
                    recipient_subject = self.replace_variables(subject, recipient, display_name)
                    recipient_content = self.replace_variables(content, recipient, display_name)
                    
                    preview_text += f"--- 收件人: {recipient['name']} <{recipient['email']}> ---\n"
                    preview_text += f"主题: {recipient_subject}\n"
                    preview_text += f"内容:\n{recipient_content}\n\n"
                    
                    # 添加附件信息
                    if attachments:
                        preview_text += f"附件: {', '.join(os.path.basename(a) for a in attachments)}\n\n"
                
                # 保存预览到文件
                preview_file = os.path.join(os.path.expanduser("~"), "邮件预览.txt")
                with open(preview_file, "w", encoding="utf-8") as f:
                    f.write(preview_text)
                
                self.operation.signals.finished.emit(True, f"预览完成，已保存到: {preview_file}")
                return
            
            # 连接SMTP服务器
            self.operation.signals.progress.emit(10, 100, "连接SMTP服务器...")
            
            if use_ssl:
                server = smtplib.SMTP_SSL(smtp_server, smtp_port)
            else:
                server = smtplib.SMTP(smtp_server, smtp_port)
                
                if use_tls:
                    server.starttls()
            
            # 登录
            server.login(email, password)
            
            # 发送邮件
            for i, recipient in enumerate(recipients):
                if not self.operation.is_running:
                    break
                    
                self.operation.signals.progress.emit(
                    10 + int(i / total_recipients * 80), 
                    100, 
                    f"正在发送邮件 {i+1}/{total_recipients}: {recipient['name']}"
                )
                
                try:
                    # 创建邮件
                    msg = MIMEMultipart()
                    
                    # 替换变量
                    recipient_subject = self.replace_variables(subject, recipient, display_name)
                    recipient_content = self.replace_variables(content, recipient, display_name)
                    
                    # 设置邮件头
                    msg['From'] = Header(f"{display_name} <{email}>", "utf-8")
                    msg['To'] = Header(f"{recipient['name']} <{recipient['email']}>", "utf-8")
                    msg['Subject'] = Header(recipient_subject, "utf-8")
                    
                    # 添加邮件内容
                    if is_html:
                        msg.attach(MIMEText(recipient_content, 'html', 'utf-8'))
                    else:
                        msg.attach(MIMEText(recipient_content, 'plain', 'utf-8'))
                    
                    # 添加附件
                    for attachment in attachments:
                        if os.path.exists(attachment):
                            with open(attachment, "rb") as f:
                                part = MIMEApplication(f.read())
                                part.add_header(
                                    'Content-Disposition', 
                                    'attachment', 
                                    filename=os.path.basename(attachment)
                                )
                                msg.attach(part)
                    
                    # 发送邮件
                    server.send_message(msg)
                    
                    # 发送间隔
                    if send_interval > 0 and i < total_recipients - 1:  # 最后一个不需要等待
                        import time
                        import random
                        actual_interval = send_interval
                        if random_interval:
                            # 随机间隔为设定值的50%-150%
                            actual_interval = send_interval * (0.5 + random.random())
                        time.sleep(actual_interval)
                        
                except Exception as e:
                    self.operation.signals.finished.emit(False, f"发送邮件给 {recipient['name']} ({recipient['email']}) 失败: {str(e)}")
                    server.quit()
                    return
            
            # 关闭连接
            server.quit()
            
            # 完成
            if self.operation.is_running:
                message = f"邮件发送完成，共发送 {total_recipients} 封邮件"
                self.operation.signals.finished.emit(True, message)
            else:
                self.operation.signals.finished.emit(False, "用户取消操作")
                
        except Exception as e:
            self.operation.signals.finished.emit(False, f"发送邮件过程中发生错误: {str(e)}")
            
    def replace_variables(self, text, recipient, sender_name):
        """替换邮件内容中的变量"""
        # 基本变量
        text = text.replace("{name}", recipient["name"])
        text = text.replace("{email}", recipient["email"])
        text = text.replace("{sender_name}", sender_name)
        
        # 自定义变量
        for i, var in enumerate(recipient["vars"]):
            text = text.replace(f"{{var{i+1}}}", var)
        
        return text
        
    def update_progress(self, current, total, status):
        """更新进度"""
        self.operation.progress.update_progress(current, total, status)
        
    def email_sending_finished(self, success, message):
        """邮件发送完成"""
        self.operation.set_running_state(False)
        if success:
            self.show_info(message)
        else:
            self.show_error(message)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = EmailSendWindow()
    window.show()
    sys.exit(app.exec())