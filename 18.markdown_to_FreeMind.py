import os
import re,sys
from xml.etree import ElementTree as ET
from xml.dom import minidom
from datetime import datetime
from pathlib import Path

class MarkdownToFreeMind:
    def __init__(self):
        self.root = None
        
    def create_xml(self, title: str = "Root"):
        """创建FreeMind格式的XML文档"""
        # 创建根元素
        self.root = ET.Element("map")
        self.root.set("version", "1.0.1")
        
        # 创建根节点
        root_node = ET.SubElement(self.root, "node")
        root_node.set("TEXT", title)
        root_node.set("CREATED", str(int(datetime.now().timestamp() * 1000)))
        root_node.set("ID", "ID_" + str(hash(title)))
        
        return root_node

    def parse_line(self, line: str) -> tuple:
        """解析Markdown行"""
        # 处理标题
        header_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if header_match:
            level = len(header_match.group(1))
            content = header_match.group(2)
            return level, content.strip()
        
        # 处理列表项
        list_match = re.match(r'^(\s*[-*]\s+)(.+)$', line)
        if list_match:
            indent = len(list_match.group(1)) - 1
            level = (indent // 2) + 7
            content = list_match.group(2).strip()
            return level, content
        
        return None, None

    def add_node(self, parent, text):
        """添加FreeMind节点"""
        node = ET.SubElement(parent, "node")
        node.set("TEXT", text)
        node.set("CREATED", str(int(datetime.now().timestamp() * 1000)))
        node.set("ID", "ID_" + str(hash(text)))
        return node

    def convert(self, markdown_text: str, output_file: str):
        """转换Markdown为FreeMind格式"""
        try:
            # 创建XML文档
            root_node = self.create_xml("手机号验证码登录测试")
            
            # 用于跟踪节点层级
            nodes_stack = [(0, root_node)]
            
            # 处理每一行
            lines = markdown_text.strip().split('\n')
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                level, content = self.parse_line(line)
                if level is None:
                    continue
                
                # 移除加粗标记
                content = content.replace('**', '')
                
                # 找到正确的父节点
                while nodes_stack and nodes_stack[-1][0] >= level:
                    nodes_stack.pop()
                
                if not nodes_stack:
                    nodes_stack.append((0, root_node))
                
                # 创建新节点
                parent_node = nodes_stack[-1][1]
                new_node = self.add_node(parent_node, content)
                
                # 将新节点添加到栈中
                nodes_stack.append((level, new_node))
            
            # 生成格式化的XML
            xml_str = minidom.parseString(ET.tostring(self.root, encoding='unicode')).toprettyxml(indent="  ")
            
            # 保存文件
            if not output_file.endswith('.mm'):
                output_file = output_file + '.mm'
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(xml_str)
                
            print(f"已成功转换并保存到: {output_file}")
            
        except Exception as e:
            print(f"转换过程中出现错误: {str(e)}")
            raise

def convert_markdown_to_mindmap(input_file: str):
    """
    转换Markdown文件为FreeMind格式
    将输出文件保存在输入文件的相同目录下
    """
    try:
        # 处理输入文件路径
        input_path = Path(input_file)
        if not input_path.exists():
            raise FileNotFoundError(f"找不到输入文件: {input_file}")
        
        # 读取输入文件
        with open(input_path, 'r', encoding='utf-8') as f:
            markdown_text = f.read()
        
        # 生成输出文件路径（与输入文件在同一目录，仅改变扩展名）
        output_path = input_path.with_suffix('.mm')
        
        # 转换并保存
        converter = MarkdownToFreeMind()
        converter.convert(markdown_text, str(output_path))
        
    except Exception as e:
        print(f"文件处理错误: {str(e)}")
        raise

def main():
    """主函数，处理命令行参数"""
    import sys
    
    if len(sys.argv) != 2:
        print("使用方法: python script.py <markdown文件路径>")
        print("示例: python script.py /path/to/your/test.md")
        return
    
    input_file = sys.argv[1]
    try:
        convert_markdown_to_mindmap(input_file)
    except Exception as e:
        print(f"程序执行出错: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # 如果直接运行脚本且没有提供参数，使用示例数据
    if len(sys.argv) == 1:
        try:
            # 示例Markdown文本
            test_markdown = """
# 手机号验证码登录测试

## 1. 输入验证测试

### 1.1 手机号输入验证
- **正常场景**
  - 输入11位有效手机号
- **异常场景**
  - 输入10位号码（位数不足）
  - 输入12位号码（位数过多）
            """
            
            # 在当前目录创建测试文件
            test_file = Path('test.md')
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(test_markdown)
            
            # 转换文件
            convert_markdown_to_mindmap(str(test_file))
            
        except Exception as e:
            print(f"程序执行出错: {str(e)}")
            import traceback
            traceback.print_exc()
    else:
        main()