---
title: Actual Measurement of Tongyi Qianwen's Code Capabilities: How Strong is the Qwen3-Coder Series Really?
date: 2026-04-08 00:42:00
tags: [Tongyi Qianwen code capabilities, Qwen3Coder review, Alibaba Cloud CodingPlan, Tongyi Qianwen programming, domestic AI programming model]
categories: [AI Programming, Model Reviews]
---

<!-- more -->
Hello everyone, this is Programmer Wanfeng.

One of the biggest selling points of Alibaba Cloud Coding Plan is **the code capabilities of the Tongyi Qianwen series**.

Especially Qwen3-Coder-Next and Qwen3-Coder-Plus, which are claimed to be specially optimized for programming. Today I'll do an actual test to see how strong they really are.

## 1. Evaluation Dimension Description

I tested Tongyi Qianwen's code capabilities from 5 dimensions:

1. **Code generation quality**: Whether the generated code is correct and standardized
2. **Chinese understanding ability**: Understanding of Chinese comments and requirement descriptions
3. **Algorithm ability**: Solutions to data structure and algorithm problems
4. **Code explanation ability**: Analysis and explanation of existing code
5. **Actual project ability**: Handling of complex business scenarios

## 2. Actual Test Comparison

### Test 1: Python data processing

**Prompt**: Write a Python function that reads an Excel file, filters out rows where a certain column is greater than 100, and saves them as a new file

#### Qwen3-Coder-Plus

```python
import pandas as pd

def filter_excel_by_column(input_file, output_file, column_name, threshold=100):
    """
    Read Excel file, filter rows where the specified column is greater than the threshold
    
    Args:
        input_file: Input Excel file path
        output_file: Output Excel file path
        column_name: Name of the column to filter
        threshold: Threshold value, default 100
    
    Returns:
        int: Number of rows after filtering
    """
    try:
        # Read Excel file
        df = pd.read_excel(input_file)
        
        # Check if column exists
        if column_name not in df.columns:
            raise ValueError(f"Column '{column_name}' does not exist, available columns: {list(df.columns)}")
        
        # Filter data
        filtered_df = df[df[column_name] > threshold]
        
        # Save results
        filtered_df.to_excel(output_file, index=False)
        
        print(f"Filtering completed: Original {len(df)} rows, {len(filtered_df)} rows after filtering")
        return len(filtered_df)
        
    except Exception as e:
        print(f"Processing error: {e}")
        return 0

# Usage example
if __name__ == "__main__":
    filter_excel_by_column("data.xlsx", "filtered.xlsx", "sales")
```

**Evaluation**:
- ✅ Complete code with exception handling
- ✅ Detailed comments, standardized docstrings
- ✅ Natural and smooth Chinese comments
- ✅ Considers edge cases (column does not exist)
- ✅ Includes usage example

#### Qwen3.5-Plus

```python
import pandas as pd

def filter_excel(input_file, column_name, threshold=100):
    df = pd.read_excel(input_file)
    filtered = df[df[column_name] > threshold]
    filtered.to_excel("output.xlsx", index=False)
    return filtered
```

**Evaluation**:
- ✅ Concise code, correct core logic
- ⚠️ Missing exception handling
- ⚠️ Few comments

**Test 1 conclusion**: Qwen3-Coder-Plus > Qwen3.5-Plus

### Test 2: Algorithm problem solution

**Prompt**: Implement quicksort in Python, requiring in-place sorting, and explain the time complexity

#### Qwen3-Coder-Plus

Not only gave a correct quicksort implementation, but also:
- Provided both recursive and iterative writing methods
- Detailed analysis of time complexity (best O(nlogn), average O(nlogn), worst O(n²))
- Discussed space complexity
- Gave optimization suggestions (three-way median method, randomized pivot)
- Included complete test code

**Evaluation**: Algorithm ability is really strong, explanation is clear, comprehensive consideration.

#### Qwen3-Max

Code is correct, explanation is clear, but fewer optimization suggestions.

**Test 2 conclusion**: Qwen3-Coder-Plus > Qwen3-Max

### Test 3: Chinese requirement understanding

**Prompt**: Help me write a Python script that batch compresses all images in a folder, requires maintaining the original format, and the compressed size does not exceed 500KB

#### Qwen3-Coder-Plus

```python
import os
from PIL import Image
import glob

def compress_images(folder_path, max_size_kb=500, quality=85):
    """
    Batch compress images in a folder
    
    Args:
        folder_path: Path to image folder
        max_size_kb: Maximum file size (KB)
        quality: Compression quality (1-100)
    """
    # Supported image formats
    supported_formats = ('*.jpg', '*.jpeg', '*.png', '*.bmp', '*.tiff')
    
    image_files = []
    for pattern in supported_formats:
        image_files.extend(glob.glob(os.path.join(folder_path, pattern)))
    
    print(f"Found {len(image_files)} images")
    
    for img_path in image_files:
        try:
            # Get file information
            original_size = os.path.getsize(img_path) / 1024  # KB
            file_ext = os.path.splitext(img_path)[1].lower()
            
            # If already below threshold, skip
            if original_size <= max_size_kb:
                print(f"Skipped (already meets requirement): {os.path.basename(img_path)}")
                continue
            
            # Open image
            with Image.open(img_path) as img:
                # Convert to RGB (handle formats like RGBA)
                if img.mode in ('RGBA', 'LA', 'P'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[-1] if img.mode != 'P' else None)
                    img = background
                
                # Gradually reduce quality until size requirement is met
                temp_quality = quality
                while temp_quality > 10:
                    # Save to temporary file
                    temp_path = img_path + '.temp'
                    
                    if file_ext in ('.jpg', '.jpeg'):
                        img.save(temp_path, 'JPEG', quality=temp_quality, optimize=True)
                    elif file_ext == '.png':
                        img.save(temp_path, 'PNG', optimize=True)
                    else:
                        img.save(temp_path, quality=temp_quality)
                    
                    # Check size
                    new_size = os.path.getsize(temp_path) / 1024
                    
                    if new_size <= max_size_kb:
                        # Replace original file
                        os.replace(temp_path, img_path)
                        print(f"Compression successful: {os.path.basename(img_path)} "
                              f"({original_size:.1f}KB -> {new_size:.1f}KB)")
                        break
                    else:
                        os.remove(temp_path)
                        temp_quality -= 5
                else:
                    print(f"Cannot compress to target size: {os.path.basename(img_path)}")
                    
        except Exception as e:
            print(f"Processing failed {os.path.basename(img_path)}: {e}")

# Usage example
if __name__ == "__main__":
    compress_images("./images", max_size_kb=500)
```

**Evaluation**:
- ✅ Fully understood both requirements of "maintain original format" and "not exceed 500KB"
- ✅ Considers multiple image formats
- ✅ Has intelligent compression strategy (gradually reduce quality)
- ✅ Natural and smooth Chinese comments
- ✅ Has detailed progress output

**Test 3 conclusion**: Chinese requirement understanding ability is very excellent

### Test 4: Code explanation

**Prompt**: Explain the function of the following code, and point out potential problems

```python
def process_data(data):
    result = []
    for item in data:
        if item['status'] == 'active':
            result.append(item)
    return result
```

#### Qwen3-Coder-Plus's answer

**Code function**:
This code filters out items with status 'active' from a list of dictionaries and returns a new list.

**Potential problems**:
1. **Missing null check**: If `item` does not have a 'status' key, it will throw a KeyError
2. **Case sensitivity**: 'active' and 'Active' will be considered different
3. **Performance issue**: For large data volumes, using a generator is more efficient
4. **No input validation**: `data` may not be a list

**Improvement suggestions**:
```python
def process_data(data):
    if not isinstance(data, list):
        raise ValueError("data must be a list")
    
    for item in data:
        if not isinstance(item, dict):
            continue
        status = item.get('status', '').lower()
        if status == 'active':
            yield item  # Using generator saves more memory
```

**Evaluation**: Comprehensive analysis, the problems pointed out are very practical, and the improved code quality is high.

## 3. Comprehensive Rating

| Dimension | Qwen3-Coder-Plus | Qwen3-Coder-Next | Qwen3.5-Plus | Qwen3-Max |
|-----------|------------------|------------------|--------------|-----------|
| Code generation | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Chinese understanding | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Algorithm ability | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Code explanation | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Project practice | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

## 4. Usage Suggestions

### Daily development
→ **Qwen3-Coder-Plus**
Reason: Highest code quality, standardized comments, suitable for production environment.

### Rapid prototyping
→ **Qwen3-Coder-Next**
Reason: Special optimization for programming, fast response speed.

### Complex business
→ **Qwen3-Max**
Reason: Strongest comprehensive ability, more accurate understanding of complex requirements.

### General scenarios
→ **Qwen3.5-Plus**
Reason: Fast speed, low cost, sufficient for daily use.

## 5. How to experience?

### Alibaba Cloud Coding Plan
👉 **[Click to subscribe to Alibaba Cloud Coding Plan](https://www.aliyun.com/benefit/scene/codingplan?userCode=t6duaoe1)**

One subscription, unlimited use of the entire Tongyi Qianwen series.

## 6. Final Thoughts

Tongyi Qianwen's code capabilities, especially the Qwen3-Coder series, really surprised me.

Natural Chinese comments, standardized code, comprehensive consideration — these are what domestic developers really need.

**Domestic AI models have truly stood up.**

Speaking of this, let me insert a message.

**On April 12, I will participate in Tencent Cloud Community's "Lobster Open Class" in Zhengzhou**, sharing "AI Practice Guide for One-Person Companies" on site, including how to use domestic models like Tongyi Qianwen to improve development efficiency.

If you happen to be in Zhengzhou, welcome to come and communicate on site.

👉 **Registration link: https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg**

AI is a lever, not an opponent.

The choice is in your hands.

---

## 🎁 Bonus Time

I'll send you a **"Tongyi Qianwen Programming Tips Manual"**:
- Quick reference table for applicable scenarios of each model
- Prompt optimization tips
- Practical code examples

👉 [Click to get it for free](https://www.python-office.com/openclaw/)

---

## 📚 Want to learn AI programming systematically?

<p align="center" id='AI编程训练营'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png" width="80%"/>
    </a>   
</p>

**"30 Lectures · AI Programming Training Camp"** — Master AI programming practice from 0 to 1.

---

> Also, everyone go give Xiaoming's Xiaohongshu account below a like~!

[Xiaohongshu QR Code]

---

[Official Account QR Code]

---

**🧧 Get a red envelope before you leave~**

[Red Envelope QR Code]

---

Programmer Wanfeng, focuses on AI programming training, a Python programmer who switched from a law master's degree, author of the open source project [python-office](https://www.python-office.com/).

---

## 🤖 Developer Productivity Tools

👉 Want to try **MiniMax Token Plan**? [Click here for 10% off](https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link)

💡 **Pay-per-use pricing — super cost-effective!** Think of it like a farmers market: buy a ticket, and all the veggies are free. Pay based on actual usage, no limits, no monthly fees. Perfect for developers!

