"""
基础UI组件模块
提供统一的UI风格和常用组件
"""

import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QLabel, QPushButton, QLineEdit, 
                              QTextEdit, QFileDialog, QMessageBox, QProgressBar,
                              QFrame, QGroupBox, QComboBox, QSpinBox, QCheckBox)
from PySide6.QtCore import Qt, QTimer, Signal, QObject
from PySide6.QtGui import QFont, QIcon, QPalette, QColor
import os


class ToolSignals(QObject):
    """自定义信号类"""
    # 进度信号：当前进度, 总进度, 状态信息
    progress = Signal(int, int, str)
    # 完成信号：成功/失败, 消息
    finished = Signal(bool, str)


class BaseMainWindow(QMainWindow):
    """主窗口基类"""
    
    def __init__(self, title, width=800, height=600):
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(width, height)
        self.setup_ui()
        self.load_styles()
        self.center_window()
        
    def setup_ui(self):
        """设置UI界面"""
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # 主布局
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)
        
        # 标题栏
        self.title_label = QLabel(self.windowTitle())
        self.title_label.setObjectName("title_label")
        self.main_layout.addWidget(self.title_label)
        
        # 分割线
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.main_layout.addWidget(self.line)
        
        # 内容区域（由子类实现）
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.main_layout.addWidget(self.content_widget)
        
        # 底部操作区域
        self.bottom_widget = QWidget()
        self.bottom_layout = QHBoxLayout(self.bottom_widget)
        self.main_layout.addWidget(self.bottom_widget)
        
    def center_window(self):
        """窗口居中显示"""
        frame_geometry = self.frameGeometry()
        screen_center = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())
        
    def load_styles(self):
        """加载样式表"""
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            style_file = os.path.join(current_dir, "styles.qss")
            if os.path.exists(style_file):
                with open(style_file, "r", encoding="utf-8") as f:
                    self.setStyleSheet(f.read())
        except Exception as e:
            print(f"加载样式表失败: {e}")
            
    def show_info(self, message):
        """显示信息消息"""
        QMessageBox.information(self, "提示", message)
        
    def show_warning(self, message):
        """显示警告消息"""
        QMessageBox.warning(self, "警告", message)
        
    def show_error(self, message):
        """显示错误消息"""
        QMessageBox.critical(self, "错误", message)
        
    def get_open_files(self, title="选择文件", filter_str="所有文件 (*.*)"):
        """获取选中的文件路径列表"""
        files, _ = QFileDialog.getOpenFileNames(self, title, "", filter_str)
        return files
        
    def get_save_path(self, title="保存文件", filter_str="所有文件 (*.*)", default_name=""):
        """获取保存路径"""
        file_path, _ = QFileDialog.getSaveFileName(self, title, default_name, filter_str)
        return file_path
        
    def get_directory(self, title="选择文件夹"):
        """获取文件夹路径"""
        directory = QFileDialog.getExistingDirectory(self, title)
        return directory


class FileSelectionWidget(QGroupBox):
    """文件选择组件"""
    
    def __init__(self, title="文件选择", multi_selection=False):
        super().__init__(title)
        self.multi_selection = multi_selection
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 文件路径显示区
        self.file_display = QTextEdit()
        self.file_display.setMaximumHeight(100)
        self.file_display.setReadOnly(True)
        layout.addWidget(self.file_display)
        
        # 按钮区域
        btn_layout = QHBoxLayout()
        
        self.select_btn = QPushButton("选择文件")
        self.select_btn.clicked.connect(self.select_files)
        btn_layout.addWidget(self.select_btn)
        
        self.clear_btn = QPushButton("清空")
        self.clear_btn.clicked.connect(self.clear_files)
        btn_layout.addWidget(self.clear_btn)
        
        layout.addLayout(btn_layout)
        
        # 存储选择的文件路径
        self.file_paths = []
        
    def select_files(self):
        """选择文件"""
        if self.multi_selection:
            files = QFileDialog.getOpenFileNames(self, "选择文件")[0]
        else:
            file = QFileDialog.getOpenFileName(self, "选择文件")[0]
            files = [file] if file else []
            
        if files:
            self.file_paths = files
            self.update_display()
            
    def clear_files(self):
        """清空文件选择"""
        self.file_paths = []
        self.file_display.clear()
        
    def update_display(self):
        """更新文件显示"""
        self.file_display.clear()
        for file in self.file_paths:
            self.file_display.append(file)
            
    def get_files(self):
        """获取选择的文件列表"""
        return self.file_paths


class ProgressWidget(QWidget):
    """进度显示组件"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 进度条
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        layout.addWidget(self.progress_bar)
        
        # 状态标签
        self.status_label = QLabel("准备就绪")
        layout.addWidget(self.status_label)
        
    def update_progress(self, value, maximum=100, status=""):
        """更新进度"""
        self.progress_bar.setMaximum(maximum)
        self.progress_bar.setValue(value)
        if status:
            self.status_label.setText(status)
            
    def reset(self):
        """重置进度"""
        self.progress_bar.setValue(0)
        self.status_label.setText("准备就绪")


class OperationWidget(QGroupBox):
    """操作区域组件"""
    
    def __init__(self, title="操作"):
        super().__init__(title)
        self.signals = ToolSignals()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 参数设置区域（由子类扩展）
        self.param_widget = QWidget()
        self.param_layout = QVBoxLayout(self.param_widget)
        layout.addWidget(self.param_widget)
        
        # 进度显示
        self.progress = ProgressWidget()
        layout.addWidget(self.progress)
        
        # 按钮区域
        btn_layout = QHBoxLayout()
        
        self.start_btn = QPushButton("开始执行")
        self.start_btn.clicked.connect(self.start_operation)
        btn_layout.addWidget(self.start_btn)
        
        self.cancel_btn = QPushButton("取消")
        self.cancel_btn.clicked.connect(self.cancel_operation)
        self.cancel_btn.setEnabled(False)
        btn_layout.addWidget(self.cancel_btn)
        
        layout.addLayout(btn_layout)
        
        # 状态标志
        self.is_running = False
        
    def start_operation(self):
        """开始操作（由子类实现）"""
        pass
        
    def cancel_operation(self):
        """取消操作"""
        self.is_running = False
        self.start_btn.setEnabled(True)
        self.cancel_btn.setEnabled(False)
        
    def set_running_state(self, running):
        """设置运行状态"""
        self.is_running = running
        self.start_btn.setEnabled(not running)
        self.cancel_btn.setEnabled(running)
        if not running:
            self.progress.reset()


# 示例：创建一个简单的工具窗口
class SimpleToolWindow(BaseMainWindow):
    """简单工具窗口示例"""
    
    def __init__(self, title):
        super().__init__(title, 800, 600)
        self.setup_content()
        
    def setup_content(self):
        """设置内容区域"""
        # 文件选择组件
        self.file_selector = FileSelectionWidget("选择Excel文件", multi_selection=True)
        self.content_layout.addWidget(self.file_selector)
        
        # 操作区域
        self.operation = OperationWidget("操作设置")
        self.operation.start_operation = self.start_operation
        self.operation.signals.progress.connect(self.update_progress)
        self.operation.signals.finished.connect(self.operation_finished)
        self.content_layout.addWidget(self.operation)
        
    def start_operation(self):
        """开始操作"""
        files = self.file_selector.get_files()
        if not files:
            self.show_warning("请先选择文件")
            return
            
        self.operation.set_running_state(True)
        self.operation.signals.progress.emit(0, 100, "开始处理...")
        
        # 模拟处理过程
        QTimer.singleShot(100, self.process_files)
        
    def process_files(self):
        """处理文件"""
        files = self.file_selector.get_files()
        total = len(files)
        
        for i, file in enumerate(files):
            # 模拟处理
            import time
            time.sleep(0.5)
            
            # 更新进度
            progress = int((i + 1) / total * 100)
            self.operation.signals.progress.emit(
                progress, 100, f"正在处理: {os.path.basename(file)}"
            )
            
            if not self.operation.is_running:
                break
        
        # 完成
        if self.operation.is_running:
            self.operation.signals.finished.emit(True, "处理完成")
        else:
            self.operation.signals.finished.emit(False, "用户取消操作")
            
    def update_progress(self, current, total, status):
        """更新进度"""
        self.operation.progress.update_progress(current, total, status)
        
    def operation_finished(self, success, message):
        """操作完成"""
        self.operation.set_running_state(False)
        if success:
            self.show_info(message)
        else:
            self.show_warning(message)