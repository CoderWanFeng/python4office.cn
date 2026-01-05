#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
定时任务自动化工具
功能：创建定时执行的任务，支持多种触发条件和操作类型
"""

import sys
import os
import json
import subprocess
import platform
from datetime import datetime, timedelta
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                              QPushButton, QTableWidget, QTableWidgetItem, 
                              QHeaderView, QTabWidget, QComboBox, QCheckBox,
                              QFileDialog, QMessageBox, QDateTimeEdit, QSpinBox)
from PySide6.QtCore import QTimer, Qt, QDateTime

# 添加父目录到路径，以便导入common模块
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.ui_base import BaseMainWindow, FileSelectionWidget, OperationWidget


class AutoTaskWindow(BaseMainWindow):
    """定时任务自动化工具主窗口"""
    
    def __init__(self):
        super().__init__("定时任务自动化工具", 1000, 700)
        self.tasks = []  # 存储任务列表
        
    def setup_content(self):
        """设置内容区域"""
        # 使用选项卡组织界面
        self.tab_widget = QTabWidget()
        self.content_layout.addWidget(self.tab_widget)
        
        # 任务列表选项卡
        self.tasks_tab = QWidget()
        self.setup_tasks_tab()
        self.tab_widget.addTab(self.tasks_tab, "任务列表")
        
        # 任务创建选项卡
        self.create_tab = QWidget()
        self.setup_create_tab()
        self.tab_widget.addTab(self.create_tab, "创建任务")
        
        # 定时器用于检查任务
        self.check_timer = QTimer()
        self.check_timer.timeout.connect(self.check_scheduled_tasks)
        self.check_timer.start(60000)  # 每分钟检查一次
        
    def setup_tasks_tab(self):
        """设置任务列表选项卡"""
        layout = QVBoxLayout(self.tasks_tab)
        
        # 任务列表
        self.tasks_table = QTableWidget(0, 5)
        self.tasks_table.setHorizontalHeaderLabels(["任务名称", "触发条件", "下次执行", "执行状态", "操作"])
        self.tasks_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tasks_table.setSelectionBehavior(QTableWidget.SelectRows)
        layout.addWidget(self.tasks_table)
        
        # 按钮区域
        btn_layout = QHBoxLayout()
        
        self.refresh_btn = QPushButton("刷新任务")
        self.refresh_btn.clicked.connect(self.refresh_tasks)
        btn_layout.addWidget(self.refresh_btn)
        
        self.edit_task_btn = QPushButton("编辑任务")
        self.edit_task_btn.clicked.connect(self.edit_task)
        btn_layout.addWidget(self.edit_task_btn)
        
        self.delete_task_btn = QPushButton("删除任务")
        self.delete_task_btn.clicked.connect(self.delete_task)
        btn_layout.addWidget(self.delete_task_btn)
        
        self.run_now_btn = QPushButton("立即执行")
        self.run_now_btn.clicked.connect(self.run_task_now)
        btn_layout.addWidget(self.run_now_btn)
        
        layout.addLayout(btn_layout)
        
        # 状态栏
        status_layout = QHBoxLayout()
        status_layout.addWidget(QLabel("任务状态:"))
        
        self.status_label = QLabel("就绪")
        status_layout.addWidget(self.status_label)
        
        layout.addLayout(status_layout)
        
        # 加载任务
        self.load_tasks()
        
    def setup_create_tab(self):
        """设置任务创建选项卡"""
        layout = QVBoxLayout(self.create_tab)
        
        # 基本信息
        basic_group = QWidget()
        basic_layout = QVBoxLayout(basic_group)
        basic_layout.addWidget(QLabel("基本信息:"))
        
        # 任务名称
        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("任务名称:"))
        self.task_name_input = QLineEdit()
        name_layout.addWidget(self.task_name_input)
        basic_layout.addLayout(name_layout)
        
        # 任务描述
        desc_layout = QHBoxLayout()
        desc_layout.addWidget(QLabel("任务描述:"))
        self.task_desc_input = QLineEdit()
        desc_layout.addWidget(self.task_desc_input)
        basic_layout.addLayout(desc_layout)
        
        layout.addWidget(basic_group)
        
        # 触发条件
        trigger_group = QWidget()
        trigger_layout = QVBoxLayout(trigger_group)
        trigger_layout.addWidget(QLabel("触发条件:"))
        
        # 触发类型
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("触发类型:"))
        self.trigger_type_combo = QComboBox()
        self.trigger_type_combo.addItems(["定时执行", "间隔执行", "每日执行", "每周执行", "每月执行"])
        self.trigger_type_combo.currentTextChanged.connect(self.toggle_trigger_options)
        type_layout.addWidget(self.trigger_type_combo)
        trigger_layout.addLayout(type_layout)
        
        # 定时执行
        self.scheduled_layout = QHBoxLayout()
        self.scheduled_layout.addWidget(QLabel("执行时间:"))
        self.scheduled_datetime = QDateTimeEdit()
        self.scheduled_datetime.setDateTime(QDateTime.currentDateTime().addSecs(3600))  # 默认1小时后
        self.scheduled_layout.addWidget(self.scheduled_datetime)
        trigger_layout.addLayout(self.scheduled_layout)
        
        # 间隔执行
        self.interval_layout = QHBoxLayout()
        self.interval_layout.addWidget(QLabel("间隔时间:"))
        self.interval_spin = QSpinBox()
        self.interval_spin.setMinimum(1)
        self.interval_spin.setMaximum(86400)  # 最多86400秒(24小时)
        self.interval_spin.setValue(3600)  # 默认1小时
        self.interval_layout.addWidget(self.interval_spin)
        
        self.interval_unit_combo = QComboBox()
        self.interval_unit_combo.addItems(["秒", "分钟", "小时"])
        self.interval_unit_combo.setCurrentIndex(2)  # 默认小时
        self.interval_layout.addWidget(self.interval_unit_combo)
        trigger_layout.addLayout(self.interval_layout)
        
        # 每日执行
        self.daily_layout = QHBoxLayout()
        self.daily_layout.addWidget(QLabel("执行时间:"))
        self.daily_time = QDateTimeEdit()
        self.daily_time.setTime(QTime(9, 0))  # 默认上午9点
        self.daily_layout.addWidget(self.daily_time)
        trigger_layout.addLayout(self.daily_layout)
        
        # 每周执行
        self.weekly_layout = QVBoxLayout()
        
        weekday_layout = QHBoxLayout()
        weekday_layout.addWidget(QLabel("星期:"))
        self.weekday_combo = QComboBox()
        self.weekday_combo.addItems(["周一", "周二", "周三", "周四", "周五", "周六", "周日"])
        weekday_layout.addWidget(self.weekday_combo)
        self.weekly_layout.addLayout(weekday_layout)
        
        week_time_layout = QHBoxLayout()
        week_time_layout.addWidget(QLabel("时间:"))
        self.weekly_time = QDateTimeEdit()
        self.weekly_time.setTime(QTime(9, 0))  # 默认上午9点
        week_time_layout.addWidget(self.weekly_time)
        self.weekly_layout.addLayout(week_time_layout)
        
        trigger_layout.addLayout(self.weekly_layout)
        
        # 每月执行
        self.monthly_layout = QVBoxLayout()
        
        month_day_layout = QHBoxLayout()
        month_day_layout.addWidget(QLabel("日期:"))
        self.month_day_spin = QSpinBox()
        self.month_day_spin.setMinimum(1)
        self.month_day_spin.setMaximum(31)
        self.month_day_spin.setValue(1)  # 默认每月1日
        month_day_layout.addWidget(self.month_day_spin)
        self.monthly_layout.addLayout(month_day_layout)
        
        month_time_layout = QHBoxLayout()
        month_time_layout.addWidget(QLabel("时间:"))
        self.monthly_time = QDateTimeEdit()
        self.monthly_time.setTime(QTime(9, 0))  # 默认上午9点
        month_time_layout.addWidget(self.monthly_time)
        month_time_layout.addWidget(self.monthly_time)
        self.monthly_layout.addLayout(month_time_layout)
        
        trigger_layout.addLayout(self.monthly_layout)
        
        layout.addWidget(trigger_group)
        
        # 执行操作
        action_group = QWidget()
        action_layout = QVBoxLayout(action_group)
        action_layout.addWidget(QLabel("执行操作:"))
        
        # 操作类型
        action_type_layout = QHBoxLayout()
        action_type_layout.addWidget(QLabel("操作类型:"))
        self.action_type_combo = QComboBox()
        self.action_type_combo.addItems(["运行程序", "打开文件", "执行脚本", "发送通知"])
        self.action_type_combo.currentTextChanged.connect(self.toggle_action_options)
        action_type_layout.addWidget(self.action_type_combo)
        action_layout.addLayout(action_type_layout)
        
        # 运行程序
        self.program_layout = QVBoxLayout()
        
        program_path_layout = QHBoxLayout()
        program_path_layout.addWidget(QLabel("程序路径:"))
        self.program_path_input = QLineEdit()
        program_path_layout.addWidget(self.program_path_input)
        
        self.browse_program_btn = QPushButton("浏览")
        self.browse_program_btn.clicked.connect(self.browse_program)
        program_path_layout.addWidget(self.browse_program_btn)
        
        self.program_layout.addLayout(program_path_layout)
        
        program_args_layout = QHBoxLayout()
        program_args_layout.addWidget(QLabel("参数:"))
        self.program_args_input = QLineEdit()
        program_args_layout.addWidget(self.program_args_input)
        self.program_layout.addLayout(program_args_layout)
        
        action_layout.addLayout(self.program_layout)
        
        # 打开文件
        self.file_layout = QVBoxLayout()
        
        file_path_layout = QHBoxLayout()
        file_path_layout.addWidget(QLabel("文件路径:"))
        self.file_path_input = QLineEdit()
        file_path_layout.addWidget(self.file_path_input)
        
        self.browse_file_btn = QPushButton("浏览")
        self.browse_file_btn.clicked.connect(self.browse_file)
        file_path_layout.addWidget(self.browse_file_btn)
        
        self.file_layout.addLayout(file_path_layout)
        action_layout.addLayout(self.file_layout)
        
        # 执行脚本
        self.script_layout = QVBoxLayout()
        
        script_path_layout = QHBoxLayout()
        script_path_layout.addWidget(QLabel("脚本路径:"))
        self.script_path_input = QLineEdit()
        script_path_layout.addWidget(self.script_path_input)
        
        self.browse_script_btn = QPushButton("浏览")
        self.browse_script_btn.clicked.connect(self.browse_script)
        script_path_layout.addWidget(self.browse_script_btn)
        
        self.script_layout.addLayout(script_path_layout)
        
        script_args_layout = QHBoxLayout()
        script_args_layout.addWidget(QLabel("参数:"))
        self.script_args_input = QLineEdit()
        script_args_layout.addWidget(self.script_args_input)
        self.script_layout.addLayout(script_args_layout)
        
        action_layout.addLayout(self.script_layout)
        
        # 发送通知
        self.notify_layout = QVBoxLayout()
        
        notify_message_layout = QHBoxLayout()
        notify_message_layout.addWidget(QLabel("通知消息:"))
        self.notify_message_input = QLineEdit()
        notify_message_layout.addWidget(self.notify_message_input)
        self.notify_layout.addLayout(notify_message_layout)
        
        action_layout.addLayout(self.notify_layout)
        
        layout.addWidget(action_group)
        
        # 其他选项
        other_group = QWidget()
        other_layout = QVBoxLayout(other_group)
        other_layout.addWidget(QLabel("其他选项:"))
        
        self.enabled_checkbox = QCheckBox("启用任务")
        self.enabled_checkbox.setChecked(True)
        other_layout.addWidget(self.enabled_checkbox)
        
        self.recurring_checkbox = QCheckBox("循环执行")
        self.recurring_checkbox.setChecked(True)
        other_layout.addWidget(self.recurring_checkbox)
        
        layout.addWidget(other_group)
        
        # 创建按钮
        self.create_task_btn = QPushButton("创建任务")
        self.create_task_btn.clicked.connect(self.create_task)
        layout.addWidget(self.create_task_btn)
        
        # 初始化控件状态
        self.toggle_trigger_options(self.trigger_type_combo.currentText())
        self.toggle_action_options(self.action_type_combo.currentText())
        
    def toggle_trigger_options(self, trigger_type):
        """根据触发类型切换选项"""
        # 默认隐藏所有选项
        self.scheduled_layout.parent().setVisible(False)
        self.interval_layout.parent().setVisible(False)
        self.daily_layout.parent().setVisible(False)
        self.weekly_layout.parent().setVisible(False)
        self.monthly_layout.parent().setVisible(False)
        
        # 显示对应选项
        if trigger_type == "定时执行":
            self.scheduled_layout.parent().setVisible(True)
        elif trigger_type == "间隔执行":
            self.interval_layout.parent().setVisible(True)
        elif trigger_type == "每日执行":
            self.daily_layout.parent().setVisible(True)
        elif trigger_type == "每周执行":
            self.weekly_layout.parent().setVisible(True)
        elif trigger_type == "每月执行":
            self.monthly_layout.parent().setVisible(True)
            
    def toggle_action_options(self, action_type):
        """根据操作类型切换选项"""
        # 默认隐藏所有选项
        self.program_layout.setVisible(False)
        self.file_layout.setVisible(False)
        self.script_layout.setVisible(False)
        self.notify_layout.setVisible(False)
        
        # 显示对应选项
        if action_type == "运行程序":
            self.program_layout.setVisible(True)
        elif action_type == "打开文件":
            self.file_layout.setVisible(True)
        elif action_type == "执行脚本":
            self.script_layout.setVisible(True)
        elif action_type == "发送通知":
            self.notify_layout.setVisible(True)
            
    def browse_program(self):
        """浏览选择程序"""
        if platform.system() == "Windows":
            filter_str = "可执行文件 (*.exe);;所有文件 (*.*)"
        else:
            filter_str = "所有文件 (*.*)"
            
        file_path = QFileDialog.getOpenFileName(self, "选择程序", "", filter_str)[0]
        if file_path:
            self.program_path_input.setText(file_path)
            
    def browse_file(self):
        """浏览选择文件"""
        file_path = QFileDialog.getOpenFileName(self, "选择文件")[0]
        if file_path:
            self.file_path_input.setText(file_path)
            
    def browse_script(self):
        """浏览选择脚本"""
        filter_str = "脚本文件 (*.bat *.sh *.py);;所有文件 (*.*)"
        file_path = QFileDialog.getOpenFileName(self, "选择脚本", "", filter_str)[0]
        if file_path:
            self.script_path_input.setText(file_path)
            
    def create_task(self):
        """创建任务"""
        # 获取基本信息
        task_name = self.task_name_input.text().strip()
        if not task_name:
            self.show_warning("请输入任务名称")
            return
            
        task_desc = self.task_desc_input.text().strip()
        
        # 获取触发条件
        trigger_type = self.trigger_type_combo.currentText()
        
        if trigger_type == "定时执行":
            next_run = self.scheduled_datetime.dateTime().toPython()
            trigger_data = {
                "type": "scheduled",
                "next_run": next_run.isoformat()
            }
        elif trigger_type == "间隔执行":
            interval_value = self.interval_spin.value()
            interval_unit = self.interval_unit_combo.currentText()
            
            # 转换为秒
            if interval_unit == "分钟":
                interval_seconds = interval_value * 60
            elif interval_unit == "小时":
                interval_seconds = interval_value * 3600
            else:  # 秒
                interval_seconds = interval_value
                
            trigger_data = {
                "type": "interval",
                "interval": interval_seconds,
                "next_run": (datetime.now() + timedelta(seconds=interval_seconds)).isoformat()
            }
        elif trigger_type == "每日执行":
            time = self.daily_time.time().toPython()
            today = datetime.now().date()
            next_run = datetime.combine(today, time)
            if next_run <= datetime.now():
                # 如果今天的时间已过，则从明天开始
                next_run = datetime.combine(today + timedelta(days=1), time)
                
            trigger_data = {
                "type": "daily",
                "time": time.strftime("%H:%M"),
                "next_run": next_run.isoformat()
            }
        elif trigger_type == "每周执行":
            weekday = self.weekday_combo.currentIndex()
            time = self.weekly_time.time().toPython()
            
            # 计算下一个指定星期几的日期
            today = datetime.now().date()
            today_weekday = today.weekday()  # 0=周一, 6=周日
            
            days_ahead = (weekday - today_weekday) % 7
            if days_ahead == 0:  # 今天是目标星期几
                # 检查今天的时间是否已过
                today_time = datetime.combine(today, time)
                if today_time <= datetime.now():
                    days_ahead = 7  # 下周
                    
            next_date = today + timedelta(days=days_ahead)
            next_run = datetime.combine(next_date, time)
            
            trigger_data = {
                "type": "weekly",
                "weekday": weekday,
                "time": time.strftime("%H:%M"),
                "next_run": next_run.isoformat()
            }
        elif trigger_type == "每月执行":
            day = self.month_day_spin.value()
            time = self.monthly_time.time().toPython()
            
            # 计算下一个指定日期
            today = datetime.now().date()
            if today.day <= day:
                # 本月还未到指定日期
                if day > 28:  # 处理月份天数问题
                    # 简化处理：尝试设置为本月最后一天
                    next_month = today.replace(day=28) + timedelta(days=4)  # 确保进入下个月
                    last_day = next_month - timedelta(days=next_month.day)
                    if day > last_day.day:
                        day = last_day.day
                next_date = today.replace(day=day)
            else:
                # 本月已过，设置为下个月
                next_month = today.replace(day=1) + timedelta(days=31)  # 确保进入下个月
                next_month = next_month.replace(day=1)
                
                if day > 28:  # 处理月份天数问题
                    # 简化处理：尝试设置为下月最后一天
                    last_day = next_month + timedelta(days=31)  # 确保进入再下个月
                    last_day = last_day - timedelta(days=last_day.day)
                    if day > last_day.day:
                        day = last_day.day
                        
                next_date = next_month.replace(day=day)
                
            next_run = datetime.combine(next_date, time)
            
            trigger_data = {
                "type": "monthly",
                "day": day,
                "time": time.strftime("%H:%M"),
                "next_run": next_run.isoformat()
            }
            
        # 获取操作
        action_type = self.action_type_combo.currentText()
        
        if action_type == "运行程序":
            action_data = {
                "type": "program",
                "path": self.program_path_input.text().strip(),
                "args": self.program_args_input.text().strip()
            }
        elif action_type == "打开文件":
            action_data = {
                "type": "file",
                "path": self.file_path_input.text().strip()
            }
        elif action_type == "执行脚本":
            action_data = {
                "type": "script",
                "path": self.script_path_input.text().strip(),
                "args": self.script_args_input.text().strip()
            }
        elif action_type == "发送通知":
            action_data = {
                "type": "notify",
                "message": self.notify_message_input.text().strip()
            }
            
        # 创建任务
        task = {
            "name": task_name,
            "description": task_desc,
            "trigger": trigger_data,
            "action": action_data,
            "enabled": self.enabled_checkbox.isChecked(),
            "recurring": self.recurring_checkbox.isChecked(),
            "created_at": datetime.now().isoformat(),
            "last_run": None,
            "status": "pending"
        }
        
        # 添加到任务列表
        self.tasks.append(task)
        
        # 保存任务
        self.save_tasks()
        
        # 更新任务列表
        self.refresh_tasks()
        
        # 切换到任务列表选项卡
        self.tab_widget.setCurrentIndex(0)
        
        self.show_info(f"任务 '{task_name}' 创建成功")
        
    def load_tasks(self):
        """加载任务"""
        try:
            # 尝试从文件加载任务
            tasks_file = os.path.join(os.path.expanduser("~"), "auto_tasks.json")
            if os.path.exists(tasks_file):
                with open(tasks_file, "r", encoding="utf-8") as f:
                    self.tasks = json.load(f)
            else:
                self.tasks = []
        except Exception as e:
            print(f"加载任务失败: {str(e)}")
            self.tasks = []
            
        self.refresh_tasks()
        
    def save_tasks(self):
        """保存任务"""
        try:
            # 保存任务到文件
            tasks_file = os.path.join(os.path.expanduser("~"), "auto_tasks.json")
            with open(tasks_file, "w", encoding="utf-8") as f:
                json.dump(self.tasks, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"保存任务失败: {str(e)}")
            
    def refresh_tasks(self):
        """刷新任务列表"""
        # 设置表格
        self.tasks_table.setRowCount(len(self.tasks))
        
        for i, task in enumerate(self.tasks):
            # 任务名称
            self.tasks_table.setItem(i, 0, QTableWidgetItem(task["name"]))
            
            # 触发条件
            trigger_type = task["trigger"]["type"]
            trigger_text = ""
            
            if trigger_type == "scheduled":
                next_run = datetime.fromisoformat(task["trigger"]["next_run"])
                trigger_text = f"定时执行 ({next_run.strftime('%Y-%m-%d %H:%M')})"
            elif trigger_type == "interval":
                interval = task["trigger"]["interval"]
                if interval < 60:
                    trigger_text = f"间隔执行 ({interval}秒)"
                elif interval < 3600:
                    trigger_text = f"间隔执行 ({interval//60}分钟)"
                else:
                    trigger_text = f"间隔执行 ({interval//3600}小时)"
            elif trigger_type == "daily":
                trigger_text = f"每日执行 ({task['trigger']['time']})"
            elif trigger_type == "weekly":
                weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
                trigger_text = f"每周执行 ({weekdays[task['trigger']['weekday']]} {task['trigger']['time']})"
            elif trigger_type == "monthly":
                trigger_text = f"每月执行 ({task['trigger']['day']}日 {task['trigger']['time']})"
                
            self.tasks_table.setItem(i, 1, QTableWidgetItem(trigger_text))
            
            # 下次执行时间
            if "next_run" in task["trigger"]:
                next_run = datetime.fromisoformat(task["trigger"]["next_run"])
                self.tasks_table.setItem(i, 2, QTableWidgetItem(next_run.strftime("%Y-%m-%d %H:%M:%S")))
            else:
                self.tasks_table.setItem(i, 2, QTableWidgetItem("-"))
            
            # 执行状态
            status = "未运行" if task["status"] == "pending" else "已运行"
            if not task["enabled"]:
                status = "已禁用"
            self.tasks_table.setItem(i, 3, QTableWidgetItem(status))
            
            # 操作按钮
            btn_widget = QWidget()
            btn_layout = QHBoxLayout(btn_widget)
            btn_layout.setContentsMargins(0, 0, 0, 0)
            
            enable_btn = QPushButton("启用" if not task["enabled"] else "禁用")
            enable_btn.setMaximumWidth(60)
            enable_btn.clicked.connect(lambda checked, idx=i: self.toggle_task_enabled(idx))
            btn_layout.addWidget(enable_btn)
            
            self.tasks_table.setCellWidget(i, 4, btn_widget)
            
    def edit_task(self):
        """编辑任务"""
        current_row = self.tasks_table.currentRow()
        if current_row < 0:
            self.show_warning("请先选择要编辑的任务")
            return
            
        task = self.tasks[current_row]
        
        # 切换到创建选项卡
        self.tab_widget.setCurrentIndex(1)
        
        # 填充任务信息
        self.task_name_input.setText(task["name"])
        self.task_desc_input.setText(task["description"])
        self.enabled_checkbox.setChecked(task["enabled"])
        self.recurring_checkbox.setChecked(task["recurring"])
        
        # 填充触发条件
        trigger_type = task["trigger"]["type"]
        
        trigger_type_map = {
            "scheduled": "定时执行",
            "interval": "间隔执行",
            "daily": "每日执行",
            "weekly": "每周执行",
            "monthly": "每月执行"
        }
        
        self.trigger_type_combo.setCurrentText(trigger_type_map.get(trigger_type, "定时执行"))
        self.toggle_trigger_options(self.trigger_type_combo.currentText())
        
        if trigger_type == "scheduled":
            next_run = datetime.fromisoformat(task["trigger"]["next_run"])
            self.scheduled_datetime.setDateTime(QDateTime.fromString(next_run.isoformat(), Qt.ISODate))
        elif trigger_type == "interval":
            interval = task["trigger"]["interval"]
            if interval >= 3600:
                self.interval_spin.setValue(interval // 3600)
                self.interval_unit_combo.setCurrentText("小时")
            elif interval >= 60:
                self.interval_spin.setValue(interval // 60)
                self.interval_unit_combo.setCurrentText("分钟")
            else:
                self.interval_spin.setValue(interval)
                self.interval_unit_combo.setCurrentText("秒")
        elif trigger_type == "daily":
            time_str = task["trigger"]["time"]
            self.daily_time.setTime(QTime.fromString(time_str, "hh:mm"))
        elif trigger_type == "weekly":
            self.weekday_combo.setCurrentIndex(task["trigger"]["weekday"])
            time_str = task["trigger"]["time"]
            self.weekly_time.setTime(QTime.fromString(time_str, "hh:mm"))
        elif trigger_type == "monthly":
            self.month_day_spin.setValue(task["trigger"]["day"])
            time_str = task["trigger"]["time"]
            self.monthly_time.setTime(QTime.fromString(time_str, "hh:mm"))
            
        # 填充操作
        action_type = task["action"]["type"]
        
        action_type_map = {
            "program": "运行程序",
            "file": "打开文件",
            "script": "执行脚本",
            "notify": "发送通知"
        }
        
        self.action_type_combo.setCurrentText(action_type_map.get(action_type, "运行程序"))
        self.toggle_action_options(self.action_type_combo.currentText())
        
        if action_type == "program":
            self.program_path_input.setText(task["action"]["path"])
            self.program_args_input.setText(task["action"]["args"])
        elif action_type == "file":
            self.file_path_input.setText(task["action"]["path"])
        elif action_type == "script":
            self.script_path_input.setText(task["action"]["path"])
            self.script_args_input.setText(task["action"]["args"])
        elif action_type == "notify":
            self.notify_message_input.setText(task["action"]["message"])
            
        # 删除原任务
        self.tasks.pop(current_row)
        
    def delete_task(self):
        """删除任务"""
        current_row = self.tasks_table.currentRow()
        if current_row < 0:
            self.show_warning("请先选择要删除的任务")
            return
            
        task = self.tasks[current_row]
        reply = QMessageBox.question(
            self, "确认删除", 
            f"确定要删除任务 '{task['name']}' 吗？",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.tasks.pop(current_row)
            self.save_tasks()
            self.refresh_tasks()
            
    def toggle_task_enabled(self, index):
        """切换任务启用状态"""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["enabled"] = not self.tasks[index]["enabled"]
            self.save_tasks()
            self.refresh_tasks()
            
    def run_task_now(self):
        """立即执行任务"""
        current_row = self.tasks_table.currentRow()
        if current_row < 0:
            self.show_warning("请先选择要执行的任务")
            return
            
        task = self.tasks[current_row]
        self.execute_task(task)
        
        # 更新任务状态
        self.tasks[current_row]["last_run"] = datetime.now().isoformat()
        self.tasks[current_row]["status"] = "running"
        self.save_tasks()
        self.refresh_tasks()
        
    def check_scheduled_tasks(self):
        """检查计划执行的任务"""
        current_time = datetime.now()
        
        for task in self.tasks:
            if not task["enabled"]:
                continue
                
            if task["status"] == "running":
                continue
                
            if "next_run" not in task["trigger"]:
                continue
                
            try:
                next_run = datetime.fromisoformat(task["trigger"]["next_run"])
                
                if current_time >= next_run:
                    # 执行任务
                    self.execute_task(task)
                    
                    # 更新任务状态
                    task["last_run"] = current_time.isoformat()
                    
                    # 计算下次执行时间
                    if task["recurring"]:
                        self.update_next_run(task)
                    else:
                        task["status"] = "completed"
                    
                    # 保存任务
                    self.save_tasks()
                    self.refresh_tasks()
                    
            except Exception as e:
                print(f"检查任务 {task['name']} 时出错: {str(e)}")
                
    def execute_task(self, task):
        """执行任务"""
        try:
            action_type = task["action"]["type"]
            
            if action_type == "program":
                # 运行程序
                path = task["action"]["path"]
                args = task["action"]["args"].split() if task["action"]["args"] else []
                
                if platform.system() == "Windows":
                    subprocess.Popen([path] + args, shell=True)
                else:
                    subprocess.Popen([path] + args)
                    
            elif action_type == "file":
                # 打开文件
                path = task["action"]["path"]
                
                if platform.system() == "Windows":
                    os.startfile(path)
                elif platform.system() == "Darwin":  # macOS
                    subprocess.run(["open", path])
                else:  # Linux
                    subprocess.run(["xdg-open", path])
                    
            elif action_type == "script":
                # 执行脚本
                path = task["action"]["path"]
                args = task["action"]["args"].split() if task["action"]["args"] else []
                
                if platform.system() == "Windows":
                    subprocess.Popen([path] + args, shell=True)
                else:
                    subprocess.Popen([path] + args)
                    
            elif action_type == "notify":
                # 发送通知
                message = task["action"]["message"]
                self.show_notification(task["name"], message)
                
            # 更新状态标签
            self.status_label.setText(f"已执行任务: {task['name']}")
            
        except Exception as e:
            self.show_error(f"执行任务 {task['name']} 时出错: {str(e)}")
            
    def update_next_run(self, task):
        """更新任务的下次执行时间"""
        trigger_type = task["trigger"]["type"]
        current_time = datetime.now()
        
        if trigger_type == "scheduled":
            # 定时执行，不需要更新（单次执行）
            task["status"] = "completed"
            
        elif trigger_type == "interval":
            # 间隔执行
            interval = task["trigger"]["interval"]
            next_run = current_time + timedelta(seconds=interval)
            task["trigger"]["next_run"] = next_run.isoformat()
            
        elif trigger_type == "daily":
            # 每日执行
            time_str = task["trigger"]["time"]
            hours, minutes = map(int, time_str.split(":"))
            
            today = current_time.date()
            next_run = datetime.combine(today, datetime.min.time().replace(hour=hours, minute=minutes))
            
            if next_run <= current_time:
                # 如果今天的时间已过，则从明天开始
                next_run = datetime.combine(today + timedelta(days=1), datetime.min.time().replace(hour=hours, minute=minutes))
                
            task["trigger"]["next_run"] = next_run.isoformat()
            
        elif trigger_type == "weekly":
            # 每周执行
            weekday = task["trigger"]["weekday"]
            time_str = task["trigger"]["time"]
            hours, minutes = map(int, time_str.split(":"))
            
            today = current_time.date()
            today_weekday = today.weekday()  # 0=周一, 6=周日
            
            days_ahead = (weekday - today_weekday) % 7
            if days_ahead == 0:  # 今天是目标星期几
                # 检查今天的时间是否已过
                today_time = datetime.combine(today, datetime.min.time().replace(hour=hours, minute=minutes))
                if today_time <= current_time:
                    days_ahead = 7  # 下周
                    
            next_date = today + timedelta(days=days_ahead)
            next_run = datetime.combine(next_date, datetime.min.time().replace(hour=hours, minute=minutes))
            
            task["trigger"]["next_run"] = next_run.isoformat()
            
        elif trigger_type == "monthly":
            # 每月执行
            day = task["trigger"]["day"]
            time_str = task["trigger"]["time"]
            hours, minutes = map(int, time_str.split(":"))
            
            # 计算下一个指定日期
            today = current_time.date()
            if today.day <= day:
                # 本月还未到指定日期
                if day > 28:  # 处理月份天数问题
                    # 简化处理：尝试设置为本月最后一天
                    next_month = today.replace(day=28) + timedelta(days=4)  # 确保进入下个月
                    last_day = next_month - timedelta(days=next_month.day)
                    if day > last_day.day:
                        day = last_day.day
                next_date = today.replace(day=day)
            else:
                # 本月已过，设置为下个月
                next_month = today.replace(day=1) + timedelta(days=31)  # 确保进入下个月
                next_month = next_month.replace(day=1)
                
                if day > 28:  # 处理月份天数问题
                    # 简化处理：尝试设置为下月最后一天
                    last_day = next_month + timedelta(days=31)  # 确保进入再下个月
                    last_day = last_day - timedelta(days=last_day.day)
                    if day > last_day.day:
                        day = last_day.day
                        
                next_date = next_month.replace(day=day)
                
            next_run = datetime.combine(next_date, datetime.min.time().replace(hour=hours, minute=minutes))
            
            task["trigger"]["next_run"] = next_run.isoformat()
            
    def show_notification(self, title, message):
        """显示通知"""
        try:
            if platform.system() == "Windows":
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=10)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["osascript", "-e", f'display notification "{message}" with title "{title}"'])
            else:  # Linux
                subprocess.run(["notify-send", title, message])
        except:
            # 如果系统通知不可用，使用状态栏显示
            self.status_label.setText(f"{title}: {message}")


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    from PySide6.QtCore import QTime
    app = QApplication(sys.argv)
    window = AutoTaskWindow()
    window.show()
    sys.exit(app.exec())