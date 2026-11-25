import os

def build_blog():
    print("正在生成静态博客...")
    
    # 读取模板
    with open("templates/post.html", "r", encoding="utf-8") as f:
        template = f.read()
        
    # 读取文章内容
    with open("content/terraform.md", "r", encoding="utf-8") as f:
        body_content = f.read()
        
    # 替换模板变量
    html_output = template.replace("{{ title }}", "什么是 Terraform？")
    html_output = html_output.replace("{{ content|safe }}", body_content)
    
    # 输出为最终的 index.html
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_output)
        
    print("博客生成成功！已输出 index.html")

if __name__ == "__main__":
    build_blog()