import xmind

def parse_markdown(md_content):
    """
    解析Markdown内容，返回层级结构
    """
    result = []
    stack = [result]
    
    for line in md_content.split('\n'):
        if not line.strip():
            continue
            
        # 判断标题级别
        if line.startswith('#'):
            level = line.count('#') - 1
            content = line.lstrip('#').strip()
        else:
            # 处理列表项
            level = (len(line) - len(line.lstrip())) // 4
            content = line.lstrip().lstrip('-*').strip()
        
        # 调整堆栈
        while len(stack) > level + 1:
            stack.pop()
            
        # 创建新节点
        node = {'title': content, 'children': []}
        stack[-1].append(node)
        stack.append(node['children'])
        
    return result

def create_xmind(md_content, output_file):
    """
    将Markdown内容转换为XMind文件
    """
    # 解析Markdown
    structure = parse_markdown(md_content)
    print(structure)
    
    # 创建新的XMind工作簿
    workbook = xmind.load(output_file)
    sheet = workbook.getPrimarySheet()
    
    # 设置根节点
    root_topic = sheet.getRootTopic()
    if structure:
        root_topic.setTitle(structure[0]['title'])
        add_children(root_topic, structure[0]['children'])
    else:
        root_topic.setTitle("未命名")
    
    # 确保文件扩展名正确
    if not output_file.endswith('.xmind'):
        output_file += '.xmind'
    
    # 保存文件
    xmind.save(workbook, path=output_file)
    print(f"XMind文件已成功保存到：{output_file}")

def add_children(parent_topic, children):
    """
    递归添加子节点
    """
    for child in children:
        child_topic = parent_topic.addSubTopic()
        child_topic.setTitle(child['title'])
        if child['children']:
            add_children(child_topic, child['children'])

def convert_md_to_xmind(md_file, xmind_file):
    """
    主函数：将Markdown文件转换为XMind文件
    """
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    create_xmind(md_content, xmind_file)

if __name__ == '__main__':
    # 示例用法
    md_file = '/Users/qimao/Downloads/项目计划.md'
    xmind_file = '/Users/qimao/Downloads/项目计划.xmind'
    convert_md_to_xmind(md_file, xmind_file)