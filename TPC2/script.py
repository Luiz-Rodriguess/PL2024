import re

def foo(line:str):
    html = ''
    
    # Heading
    if re.search(r'#+ .+',line):
        headingLevel = line.count('#')
        html += f'<h{headingLevel}>{line.strip('#')}</h{headingLevel}>'
    
    # Link
    if re.search(r'.+[^!]\[.+\].+',line):
        text = re.sub(r'\[.+\]|\(.+\)','',line).strip()
        link = re.findall(r'\((.+)\)',line)[0]
        alt = re.findall(r'\[(.+)\]',line)[0]
        html += f'{text} <a href="{link}">{alt}</a>'
    
    # Image
    if re.search(r'.+!\[.+\].+',line):
        text = re.sub(r'\(.+\)|!\[.+\]','',line).strip()
        link = re.findall(r'\((.+)\)',line)[0]
        alt = re.findall(r'!\[(.+)\]',line)[0]
        html += f'{text} <img src="{link}" alt="{alt}"/>'
    
    # Bold 
    if re.search(r'\*{2}[^*]+\*{2}',line):
        text = re.sub(r'\*{2}','<b>',line,count=1)
        text = re.sub(r'\*{2}','</b>',text,count=1)
        html += text
    
    # Italics
    if re.search(r'\*[^*\s]+\*',line):
        text = re.sub(r'\*','<i>',line,count=1)
        text = re.sub(r'\*','</i>',text,count=1)
        html += text
    
    # Ordered list
    if re.search(r'\d\..+',line):
        text = re.sub(r'\d\. ','',line)
        html += f'<ol><li>{text}</li></ol>'

    if html:
        if html[0] != '<':
            html = f'<p>{html}</p>'
    
    return html

def main():
    html = """ <!DOCTYPE html>
        <html lang='pt-PT'>
        <head>
            <title>Rua</title>
            <meta charset="utf-8"/>
        <body>
        """
    
    with open('markdown-sample.md','r') as file:
        lastLine = '' 
        for line in file:
            line = line.strip()
            if line:
                currLine = foo(line)
                aux = currLine
                if '<ol>' in lastLine and '<ol>' in currLine:
                    currLine = re.sub('<ol>','',currLine)
                if '</ol>' in lastLine and '</ol>' in currLine:
                    html = re.sub('</ol>','',html)
                html += currLine
                lastLine = aux
        
    
    with open('webPage.html','w') as file:
        file.write(html)

if __name__ == '__main__':
    main()