import os
import re

def fix_yaml_front_matter(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            return False
        
        end_marker = content.find('\n---\n')
        if end_marker == -1:
            return False
        
        front_matter = content[:end_marker]
        body = content[end_marker+5:]
        
        lines = front_matter.split('\n')
        fixed_lines = []
        
        for line in lines:
            if line.strip() == '---':
                fixed_lines.append(line)
                continue
            
            match = re.match(r'^(\s*)(\w+):\s*(.*)$', line)
            if match:
                indent = match.group(1)
                key = match.group(2)
                value = match.group(3).strip()
                
                if value.startswith('[') and value.endswith(']'):
                    items = value[1:-1].split(',')
                    cleaned_items = []
                    for item in items:
                        item = item.strip()
                        if item:
                            if item.startswith('"') and item.endswith('"'):
                                item = item[1:-1]
                            cleaned_items.append(f'"{item}"')
                    fixed_value = '[' + ', '.join(cleaned_items) + ']'
                    fixed_lines.append(f'{indent}{key}: {fixed_value}')
                else:
                    if ':' in value and not (value.startswith('"') and value.endswith('"')):
                        fixed_lines.append(f'{indent}{key}: "{value}"')
                    else:
                        fixed_lines.append(line)
            else:
                fixed_lines.append(line)
        
        new_front_matter = '\n'.join(fixed_lines)
        new_content = f'{new_front_matter}\n---\n{body}'
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Fixed: {file_path}')
            return True
        
        return False
    except Exception as e:
        print(f'Error processing {file_path}: {e}')
        return False

def find_markdown_files(root_dir):
    markdown_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.md'):
                markdown_files.append(os.path.join(dirpath, filename))
    return markdown_files

if __name__ == '__main__':
    root_dir = 'source/_posts'
    files = find_markdown_files(root_dir)
    print(f'Found {len(files)} markdown files')
    
    fixed_count = 0
    for file_path in files:
        if fix_yaml_front_matter(file_path):
            fixed_count += 1
    
    print(f'Fixed {fixed_count} files')
