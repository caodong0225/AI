"""
	ui转换成py的转换工具
"""

import os
import os.path

# UI文件所在的路径 
dir_path = './'


# 列出目录下的所有ui文件
def list_ui_file():
	list_ui = []
	files = os.listdir(dir_path)
	for filename in files:
		if os.path.splitext(filename)[1] == '.ui':
			list_ui.append(filename)
	return list_ui


# 把后缀为ui的文件改成后缀为py的文件名
def trans_py_file(filename):
	return os.path.splitext(filename)[0] + '.py'


# 调用系统命令把ui转换成py
def run_main():
	list_ui = list_ui_file()
	for ui_file in list_ui:
		pyfile = trans_py_file(ui_file)
		cmd = 'pyuic5 -o {pyfile} {uifile}'.format(pyfile=pyfile, uifile=ui_file)
		print(cmd)
		os.system(cmd)
	# py -3 -m PyQt5.uic.pyuic untitled.ui -o untitle.py


# 程序的主入口
if __name__ == "__main__":
	run_main()
