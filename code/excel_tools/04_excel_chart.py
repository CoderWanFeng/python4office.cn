#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Excel图表生成工具
功能：根据Excel数据生成各类图表，支持多种图表类型和自定义样式
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QSpinBox, QCheckBox, QFileDialog, QMessageBox
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont

# 设置matplotlib使用非交互式后端
matplotlib.use('Qt5Agg')

# 添加父目录到路径，以便导入common模块
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.ui_base import BaseMainWindow, FileSelectionWidget, OperationWidget

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False


class ExcelChartWindow(BaseMainWindow):
    """Excel图表生成工具主窗口"""
    
    def __init__(self):
        super().__init__("Excel图表生成工具", 1000, 700)
        self.df = None  # 存储当前读取的Excel数据
        self.figure = None  # 存储matplotlib图形
        
    def setup_content(self):
        """设置内容区域"""
        # 文件选择组件
        self.file_selector = FileSelectionWidget("选择要生成图表的Excel文件", multi_selection=False)
        self.file_selector.select_files = self.load_excel_file  # 重写选择文件方法
        self.content_layout.addWidget(self.file_selector)
        
        # 图表选项组件
        self.chart_options = ChartOptionsWidget()
        self.chart_options.generate_clicked.connect(self.generate_chart)
        self.content_layout.addWidget(self.chart_options)
        
        # 图表显示区域
        self.chart_display = ChartDisplayWidget()
        self.content_layout.addWidget(self.chart_display)
        
        # 操作区域
        self.operation = OperationWidget("图表操作")
        self.operation.start_operation = self.start_operation
        self.operation.signals.progress.connect(self.update_progress)
        self.operation.signals.finished.connect(self.operation_finished)
        self.content_layout.addWidget(self.operation)
        
    def load_excel_file(self):
        """加载Excel文件"""
        files = QFileDialog.getOpenFileNames(self, "选择Excel文件", "", "Excel文件 (*.xlsx *.xls)")[0]
        
        if not files:
            return
            
        file_path = files[0]
        self.file_selector.file_paths = files
        self.file_selector.update_display()
        
        try:
            # 读取Excel文件
            self.df = pd.read_excel(file_path)
            
            # 更新图表选项
            self.chart_options.update_columns(self.df.columns.tolist())
            
            # 更新状态
            self.statusBar().showMessage(f"已加载文件: {os.path.basename(file_path)}, 共 {len(self.df)} 行数据")
            
        except Exception as e:
            self.show_error(f"加载Excel文件失败: {str(e)}")
            
    def generate_chart(self):
        """生成图表"""
        if self.df is None:
            self.show_warning("请先加载Excel文件")
            return
            
        try:
            # 获取图表配置
            config = self.chart_options.get_chart_config()
            
            # 提取配置参数
            chart_type = config["chart_type"]
            x_column = config["x_column"]
            y_columns = config["y_columns"]
            title = config["title"]
            x_label = config["x_label"]
            y_label = config["y_label"]
            show_grid = config["show_grid"]
            show_legend = config["show_legend"]
            color_scheme = config["color_scheme"]
            
            # 验证必要参数
            if not y_columns:
                self.show_warning("请至少选择一个Y轴数据列")
                return
            
            # 创建图形
            self.figure = Figure(figsize=(10, 6))
            ax = self.figure.add_subplot(111)
            
            # 准备数据
            x_data = self.df[x_column].tolist() if x_column else range(len(self.df))
            
            # 根据图表类型绘制
            if chart_type == "折线图":
                for i, col in enumerate(y_columns):
                    y_data = self.df[col].tolist()
                    color = plt.cm.get_cmap(color_scheme)(i / max(len(y_columns), 1))
                    ax.plot(x_data, y_data, label=col, color=color, marker='o', markersize=4)
                    
            elif chart_type == "柱状图":
                if len(y_columns) == 1:
                    # 单系列柱状图
                    y_data = self.df[y_columns[0]].tolist()
                    color = plt.cm.get_cmap(color_scheme)(0)
                    ax.bar(x_data, y_data, label=y_columns[0], color=color)
                else:
                    # 多系列柱状图
                    x_indices = range(len(x_data))
                    bar_width = 0.8 / len(y_columns)
                    
                    for i, col in enumerate(y_columns):
                        y_data = self.df[col].tolist()
                        color = plt.cm.get_cmap(color_scheme)(i / max(len(y_columns), 1))
                        offset = (i - len(y_columns)/2 + 0.5) * bar_width
                        ax.bar([x + offset for x in x_indices], y_data, 
                               bar_width, label=col, color=color)
                    
                    # 设置X轴刻度
                    if x_column:
                        ax.set_xticks(x_indices)
                        ax.set_xticklabels(x_data)
                        
            elif chart_type == "饼图":
                if len(y_columns) == 1:
                    # 单系列饼图
                    y_data = self.df[y_columns[0]].tolist()
                    labels = self.df[x_column].tolist() if x_column else None
                    colors = plt.cm.get_cmap(color_scheme)(range(len(y_data)))
                    ax.pie(y_data, labels=labels, autopct='%1.1f%%', colors=colors)
                    ax.axis('equal')  # 确保饼图是圆形
                else:
                    self.show_warning("饼图只支持单个Y轴数据列")
                    return
                    
            elif chart_type == "散点图":
                if len(y_columns) >= 1:
                    y_data = self.df[y_columns[0]].tolist()
                    color = plt.cm.get_cmap(color_scheme)(0)
                    ax.scatter(x_data, y_data, label=y_columns[0], color=color, alpha=0.7)
                    
                    if len(y_columns) > 1:
                        # 如果有多个Y轴列，用不同的颜色表示第三维度
                        z_data = self.df[y_columns[1]].tolist()
                        scatter = ax.scatter(x_data, y_data, c=z_data, cmap=color_scheme, alpha=0.7)
                        self.figure.colorbar(scatter, ax=ax, label=y_columns[1])
                        ax.legend([y_columns[0], y_columns[1]])
                else:
                    self.show_warning("散点图至少需要一个Y轴数据列")
                    return
                    
            elif chart_type == "面积图":
                for i, col in enumerate(y_columns):
                    y_data = self.df[col].tolist()
                    color = plt.cm.get_cmap(color_scheme)(i / max(len(y_columns), 1))
                    ax.fill_between(x_data, y_data, alpha=0.5, color=color, label=col)
                    
            # 设置图表属性
            ax.set_title(title, fontsize=14, fontweight='bold')
            ax.set_xlabel(x_label, fontsize=12)
            ax.set_ylabel(y_label, fontsize=12)
            
            if show_grid:
                ax.grid(True, linestyle='--', alpha=0.7)
                
            if show_legend and len(y_columns) > 1:
                ax.legend()
                
            # 调整布局
            self.figure.tight_layout()
            
            # 更新显示
            self.chart_display.update_figure(self.figure)
            
            # 更新状态
            self.statusBar().showMessage(f"图表生成完成: {title}")
            
        except Exception as e:
            self.show_error(f"生成图表过程中出错: {str(e)}")
            
    def start_operation(self):
        """开始操作（保存图表）"""
        if self.figure is None:
            self.show_warning("请先生成图表")
            return
            
        # 获取保存路径
        save_path = self.get_save_path("保存图表", "PNG图片 (*.png)", "图表.png")
        if not save_path:
            return
            
        # 开始保存
        self.operation.set_running_state(True)
        self.operation.signals.progress.emit(0, 100, "正在保存图表...")
        
        # 使用定时器异步执行
        QTimer.singleShot(100, lambda: self.save_chart(save_path))
        
    def save_chart(self, save_path):
        """保存图表"""
        try:
            self.operation.signals.progress.emit(50, 100, "正在写入图片文件...")
            
            # 保存图表
            self.figure.savefig(save_path, dpi=300, bbox_inches='tight')
            
            # 完成
            if self.operation.is_running:
                self.operation.signals.finished.emit(True, f"图表已保存到: {save_path}")
            else:
                self.operation.signals.finished.emit(False, "用户取消操作")
                
        except Exception as e:
            self.operation.signals.finished.emit(False, f"保存过程中出错: {str(e)}")
            
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


class ChartOptionsWidget(QWidget):
    """图表选项设置组件"""
    generate_clicked = Signal()
    
    def __init__(self):
        super().__init__()
        self.columns = []  # 存储可用的列名
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 图表类型选择
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("图表类型:"))
        self.chart_type_combo = QComboBox()
        self.chart_type_combo.addItems(["折线图", "柱状图", "饼图", "散点图", "面积图"])
        type_layout.addWidget(self.chart_type_combo)
        layout.addLayout(type_layout)
        
        # 数据列选择
        columns_layout = QVBoxLayout()
        
        # X轴数据
        x_layout = QHBoxLayout()
        x_layout.addWidget(QLabel("X轴数据:"))
        self.x_column_combo = QComboBox()
        self.x_column_combo.addItem("(使用索引)")
        x_layout.addWidget(self.x_column_combo)
        columns_layout.addLayout(x_layout)
        
        # Y轴数据
        y_layout = QHBoxLayout()
        y_layout.addWidget(QLabel("Y轴数据:"))
        self.y_columns_list = ListSelectionWidget()
        y_layout.addWidget(self.y_columns_list)
        columns_layout.addLayout(y_layout)
        
        layout.addLayout(columns_layout)
        
        # 图表样式设置
        style_group = QWidget()
        style_layout = QVBoxLayout(style_group)
        
        # 标题和轴标签
        title_layout = QHBoxLayout()
        title_layout.addWidget(QLabel("图表标题:"))
        self.title_input = QLineEdit("数据图表")
        title_layout.addWidget(self.title_input)
        style_layout.addLayout(title_layout)
        
        x_label_layout = QHBoxLayout()
        x_label_layout.addWidget(QLabel("X轴标签:"))
        self.x_label_input = QLineEdit("X轴")
        x_label_layout.addWidget(self.x_label_input)
        style_layout.addLayout(x_label_layout)
        
        y_label_layout = QHBoxLayout()
        y_label_layout.addWidget(QLabel("Y轴标签:"))
        self.y_label_input = QLineEdit("Y轴")
        y_label_layout.addWidget(self.y_label_input)
        style_layout.addLayout(y_label_layout)
        
        layout.addWidget(style_group)
        
        # 其他选项
        options_layout = QHBoxLayout()
        
        self.grid_checkbox = QCheckBox("显示网格")
        self.grid_checkbox.setChecked(True)
        options_layout.addWidget(self.grid_checkbox)
        
        self.legend_checkbox = QCheckBox("显示图例")
        self.legend_checkbox.setChecked(True)
        options_layout.addWidget(self.legend_checkbox)
        
        options_layout.addStretch()
        layout.addLayout(options_layout)
        
        # 颜色方案选择
        color_layout = QHBoxLayout()
        color_layout.addWidget(QLabel("颜色方案:"))
        self.color_combo = QComboBox()
        self.color_combo.addItems(["viridis", "plasma", "inferno", "magma", "cool", "rainbow", "tab10"])
        color_layout.addWidget(self.color_combo)
        layout.addLayout(color_layout)
        
        # 生成按钮
        generate_btn = QPushButton("生成图表")
        generate_btn.clicked.connect(self.generate_clicked.emit)
        layout.addWidget(generate_btn)
        
    def update_columns(self, columns):
        """更新可用列名"""
        self.columns = columns
        
        # 更新X轴选项
        self.x_column_combo.clear()
        self.x_column_combo.addItem("(使用索引)")
        self.x_column_combo.addItems(columns)
        
        # 更新Y轴选项
        self.y_columns_list.update_items(columns)
        
    def get_chart_config(self):
        """获取图表配置"""
        return {
            "chart_type": self.chart_type_combo.currentText(),
            "x_column": self.x_column_combo.currentText() if self.x_column_combo.currentIndex() > 0 else None,
            "y_columns": self.y_columns_list.get_selected_items(),
            "title": self.title_input.text(),
            "x_label": self.x_label_input.text(),
            "y_label": self.y_label_input.text(),
            "show_grid": self.grid_checkbox.isChecked(),
            "show_legend": self.legend_checkbox.isChecked(),
            "color_scheme": self.color_combo.currentText()
        }


class ListSelectionWidget(QWidget):
    """列表选择小部件"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # 按钮布局
        btn_layout = QHBoxLayout()
        
        self.add_btn = QPushButton(">> 添加")
        self.add_btn.clicked.connect(self.add_item)
        btn_layout.addWidget(self.add_btn)
        
        self.remove_btn = QPushButton("<< 移除")
        self.remove_btn.clicked.connect(self.remove_item)
        btn_layout.addWidget(self.remove_btn)
        
        layout.addLayout(btn_layout)
        
        # 列表布局
        lists_layout = QHBoxLayout()
        
        # 可用列
        available_layout = QVBoxLayout()
        available_layout.addWidget(QLabel("可用列:"))
        self.available_list = QListWidget()
        available_layout.addWidget(self.available_list)
        lists_layout.addLayout(available_layout)
        
        # 已选择列
        selected_layout = QVBoxLayout()
        selected_layout.addWidget(QLabel("已选择列:"))
        self.selected_list = QListWidget()
        selected_layout.addWidget(self.selected_list)
        lists_layout.addLayout(selected_layout)
        
        layout.addLayout(lists_layout)
        
    def update_items(self, items):
        """更新可用项目"""
        self.available_list.clear()
        self.available_list.addItems(items)
        
    def add_item(self):
        """添加选中项到已选择列表"""
        current_row = self.available_list.currentRow()
        if current_row >= 0:
            item = self.available_list.takeItem(current_row)
            self.selected_list.addItem(item)
            
    def remove_item(self):
        """移除选中项到可用列表"""
        current_row = self.selected_list.currentRow()
        if current_row >= 0:
            item = self.selected_list.takeItem(current_row)
            self.available_list.addItem(item)
            
    def get_selected_items(self):
        """获取已选择的项目"""
        items = []
        for i in range(self.selected_list.count()):
            items.append(self.selected_list.item(i).text())
        return items


class ChartDisplayWidget(QWidget):
    """图表显示组件"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.canvas = None
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 标题
        title_label = QLabel("图表预览")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("", 12, QFont.Bold))
        layout.addWidget(title_label)
        
        # 画布区域
        self.canvas_container = QWidget()
        self.canvas_layout = QVBoxLayout(self.canvas_container)
        layout.addWidget(self.canvas_container)
        
    def update_figure(self, figure):
        """更新图形显示"""
        # 清除旧画布
        if self.canvas:
            self.canvas_layout.removeWidget(self.canvas)
            self.canvas.deleteLater()
            
        # 创建新画布
        self.canvas = FigureCanvas(figure)
        self.canvas_layout.addWidget(self.canvas)
        self.canvas.draw()


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = ExcelChartWindow()
    window.show()
    sys.exit(app.exec())