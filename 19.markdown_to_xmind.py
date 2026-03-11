import os
import re
from datetime import datetime
from pathlib import Path
import zipfile
import json
import uuid

class MarkdownToXMind:
    def __init__(self):
        self.topics = []
        
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

    def add_topic(self, text, level):
        """添加主题到列表"""
        self.topics.append({
            "level": level,
            "content": text
        })

    def create_content_json(self, title: str = "Root"):
        """创建 content.json"""
        # 创建基本结构
        root_sheet = {
            "id": str(uuid.uuid4()),
            "class": "sheet",
            "title": "Sheet 1",
            "rootTopic": {
                "id": str(uuid.uuid4()),
                "class": "topic",
                "title": title,
                "children": {
                    "attached": []
                },
                "extensions": [],
                "style": {
                    "id": str(uuid.uuid4())
                }
            },
            "extensions": [],
            "style": {
                "id": str(uuid.uuid4())
            }
        }
        
        # 构建主题层级
        topic_map = {0: root_sheet["rootTopic"]}
        
        for topic in self.topics:
            level = topic["level"]
            parent_level = level - 1
            
            # 创建新主题
            new_topic = {
                "id": str(uuid.uuid4()),
                "class": "topic",
                "title": topic["content"],
                "style": {
                    "id": str(uuid.uuid4())
                },
                "extensions": []
            }
            
            # 找到父主题
            while parent_level >= 0 and parent_level not in topic_map:
                parent_level -= 1
            
            if parent_level >= 0:
                parent = topic_map[parent_level]
                if "children" not in parent:
                    parent["children"] = {"attached": []}
                parent["children"]["attached"].append(new_topic)
            
            # 更新主题映射
            topic_map[level] = new_topic
        
        return json.dumps([root_sheet], ensure_ascii=False, indent=2)

    def convert(self, markdown_text: str, output_file: str):
        """转换Markdown为XMind格式"""
        try:
            # 清空主题列表
            self.topics = []
            
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
                
                # 添加主题
                self.add_topic(content, level)
            
            # 创建ZIP文件
            with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zf:
                # 写入content.json
                zf.writestr('content.json', 
                          self.create_content_json("手机号验证码登录测试"))
                
                # 写入metadata.json
                metadata = {
                    "creator": {
                        "name": "Markdown to XMind",
                        "version": "1.0"
                    },
                    "createTime": int(datetime.now().timestamp() * 1000),
                    "modifyTime": int(datetime.now().timestamp() * 1000)
                }
                zf.writestr('metadata.json', json.dumps(metadata, ensure_ascii=False, indent=2))
                
                # 写入manifest.json
                manifest = {
                    "file-entries": {
                        "content.json": {
                            "filename": "content.json",
                            "mediaType": "application/json",
                            "modified": int(datetime.now().timestamp() * 1000)
                        },
                        "metadata.json": {
                            "filename": "metadata.json",
                            "mediaType": "application/json",
                            "modified": int(datetime.now().timestamp() * 1000)
                        }
                    }
                }
                zf.writestr('manifest.json', json.dumps(manifest, ensure_ascii=False, indent=2))
            
            print(f"已成功转换并保存到: {output_file}")
            
        except Exception as e:
            print(f"转换过程中出现错误: {str(e)}")
            raise

def convert_markdown_to_xmind(input_file: str):
    """转换Markdown文件为XMind格式"""
    try:
        input_path = Path(input_file)
        if not input_path.exists():
            raise FileNotFoundError(f"找不到输入文件: {input_file}")
        
        with open(input_path, 'r', encoding='utf-8') as f:
            markdown_text = f.read()
        
        output_path = input_path.with_suffix('.xmind')
        converter = MarkdownToXMind()
        converter.convert(markdown_text, str(output_path))
        
    except Exception as e:
        print(f"文件处理错误: {str(e)}")
        raise

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("使用方法: python script.py <markdown文件路径>")
        print("示例: python script.py /path/to/your/test.md")
        sys.exit(1)
    
    try:
        convert_markdown_to_xmind(sys.argv[1])
    except Exception as e:
        print(f"程序执行出错: {str(e)}")
        import traceback
        traceback.print_exc()