#!/usr/bin/env python3
"""
Portfolio Generator - Converts resume PDFs to personal portfolio HTML pages
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime

def extract_title_from_filename(filename):
    """Extract a readable title from PDF filename."""
    # Remove .pdf extension
    name = filename.replace('.pdf', '')
    # Replace underscores and dashes with spaces
    name = name.replace('_', ' ').replace('-', ' ')
    # Capitalize words
    name = ' '.join(word.capitalize() for word in name.split())
    return name

def get_resume_metadata(filename):
    """Extract metadata from resume filename."""
    return {
        'filename': filename,
        'title': extract_title_from_filename(filename),
        'filepath': f'{filename}',
        'type': 'resume'
    }

def generate_portfolio_page(resume_list, output_dir='portfolios'):
    """Generate portfolio HTML pages from resume list."""
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    for resume in resume_list:
        filename = resume['filename']
        title = resume['title']
        
        # Create filename for the portfolio page
        portfolio_name = re.sub(r'[^a-zA-Z0-9_-]', '_', title.lower()) + '.html'
        portfolio_path = os.path.join(output_dir, portfolio_name)
        
        html_content = f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Portfolio</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px 20px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .resume-section {{
            margin-bottom: 30px;
        }}
        
        .resume-section h2 {{
            color: #667eea;
            margin-bottom: 15px;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
        }}
        
        .pdf-viewer {{
            width: 100%;
            height: 600px;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin: 20px 0;
        }}
        
        .pdf-link {{
            display: inline-block;
            margin: 20px 0;
            padding: 12px 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: transform 0.2s, box-shadow 0.2s;
            font-weight: bold;
        }}
        
        .pdf-link:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }}
        
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            border-top: 1px solid #ddd;
        }}
        
        .back-link {{
            display: inline-block;
            margin-bottom: 20px;
            padding: 10px 20px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: background 0.2s;
        }}
        
        .back-link:hover {{
            background: #764ba2;
        }}
        
        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 1.8em;
            }}
            
            .content {{
                padding: 20px;
            }}
            
            .pdf-viewer {{
                height: 400px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{title}</h1>
            <p>Professional Resume & Portfolio</p>
        </div>
        
        <div class="content">
            <a href="index.html" class="back-link">← Back to Home</a>
            
            <div class="resume-section">
                <h2>Resume Document</h2>
                <p>View and download the complete resume below:</p>
                <a href="{filename}" class="pdf-link" download>📥 Download Resume PDF</a>
                
                <iframe class="pdf-viewer" src="{filename}#toolbar=0" type="application/pdf"></iframe>
            </div>
            
            <div class="resume-section">
                <h2>About This Profile</h2>
                <p>This portfolio page is automatically generated from your resume PDF. 
                   The resume is embedded below for easy viewing and can be downloaded directly.</p>
            </div>
        </div>
        
        <div class="footer">
            <p>Generated on {datetime.now().strftime('%B %d, %Y')} | 
               <a href="index.html" style="color: #667eea; text-decoration: none;">Back to Portfolio</a></p>
        </div>
    </div>
</body>
</html>"""
        
        # Write the HTML file
        with open(portfolio_path, 'w') as f:
            f.write(html_content)
        
        print(f"✓ Generated: {portfolio_path}")
    
    return [re.sub(r'[^a-zA-Z0-9_-]', '_', resume['title'].lower()) + '.html' 
            for resume in resume_list]

def update_portfolio_index(resume_list, profile_image='chinmay_harjai.png'):
    """Update the main index.html to include portfolio links."""
    
    portfolios = generate_portfolio_page(resume_list)
    
    portfolio_links_html = '\n'.join([
        f'                    <li><a href="portfolios/{portfolio}">{resume["title"]}</a></li>'
        for portfolio, resume in zip(portfolios, resume_list)
    ])
    
    main_html = f"""<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chinmay Harjai - Portfolio</title>
  <style>
    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }}
    
    body {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      min-height: 100vh;
      padding: 20px;
      color: #333;
    }}
    
    .container {{
      max-width: 900px;
      margin: 0 auto;
      background: white;
      border-radius: 10px;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
      overflow: hidden;
    }}
    
    table {{
      width: 100%;
      padding: 30px;
    }}
    
    img {{
      border-radius: 50%;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }}
    
    h1 {{
      font-size: 2.5em;
      color: #667eea;
      margin-bottom: 10px;
    }}
    
    h3 {{
      color: #667eea;
      margin-top: 20px;
      margin-bottom: 15px;
      border-bottom: 2px solid #667eea;
      padding-bottom: 10px;
    }}
    
    hr {{
      border: none;
      border-top: 2px solid #eee;
      margin: 20px 0;
    }}
    
    a {{
      color: #764ba2;
      text-decoration: none;
      transition: color 0.2s;
    }}
    
    a:hover {{
      color: #667eea;
      text-decoration: underline;
    }}
    
    ul, ol {{
      margin-left: 20px;
    }}
    
    li {{
      margin-bottom: 8px;
    }}
    
    table[border] {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
    }}
    
    table[border] th,
    table[border] td {{
      border: 1px solid #667eea;
      padding: 10px;
      text-align: left;
    }}
    
    table[border] th {{
      background: #f8f9fa;
      font-weight: bold;
      color: #667eea;
    }}
    
    .portfolios-section {{
      background: #f8f9fa;
      padding: 20px;
      margin: 20px 30px;
      border-radius: 5px;
      border-left: 4px solid #667eea;
    }}
    
    .portfolios-section h3 {{
      margin-top: 0;
    }}
    
    .portfolios-section ul {{
      list-style: none;
      margin-left: 0;
    }}
    
    .portfolios-section li {{
      padding: 8px 0;
    }}
    
    .portfolios-section a {{
      display: inline-block;
      padding: 8px 15px;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      border-radius: 3px;
      transition: transform 0.2s;
    }}
    
    .portfolios-section a:hover {{
      color: white;
      text-decoration: none;
      transform: translateX(5px);
    }}
    
    @media (max-width: 768px) {{
      h1 {{
        font-size: 1.8em;
      }}
      
      table {{
        padding: 15px;
      }}
    }}
  </style>
</head>

<body>
  <div class="container">
    <table cellspacing="20">
      <tr>
        <td style="width: 200px; text-align: center;">
          <img src="chinmay_harjai.png" alt="Chinmay Harjai profile picture" height="200">
        </td>
        <td>
          <h1>Chinmay Harjai</h1>
          <br>
          <p><i>One of the founders of 
            <a href="https://www.youtube.com/channel/UCapf407ATCS8zESwLbFxfzA">unicorn club mnit jaipur</a>
          </i></p>
          <br>
          <p><i>Upskilling with web development and emerging technologies</i></p>
        </td>
      </tr>
    </table>
    
    <hr>
    
    <div style="padding: 0 30px;">
      <h3>📋 Professional Portfolios</h3>
      <div class="portfolios-section">
        <ul>
{portfolio_links_html}
        </ul>
      </div>
    </div>
    
    <hr style="margin: 0 30px;">
    
    <table cellspacing="20" style="padding: 30px;">
      <tr>
        <td style="vertical-align: top;">
          <h3>Working on Projects</h3>
          <ul>
            <li><a href="https://instagram.com/__the28__?igshid=YmMyMTA2M2Y=">The 28</a> fashion brand branding</li>
            <li>Unicorn club video creation <br>
              <a href="https://youtu.be/2LSnasuwAiU">Bharat pe case study by unicorn</a>
            </li>
            <li>Learning web development and AI</li>
          </ul>
        </td>
      </tr>
    </table>
    
    <hr style="margin: 0 30px;">
    
    <table cellspacing="20" style="padding: 0 30px;">
      <tr>
        <td>
          <a href="hobbies.html">🎯 Hobbies</a>&nbsp;&nbsp;|&nbsp;&nbsp;
          <a href="contact_me.html">📧 Contact Me</a>
        </td>
      </tr>
    </table>
    
    <hr style="margin: 0 30px;">
    
    <table cellspacing="20" style="padding: 30px;">
      <tr>
        <td>
          <h3>Skills</h3>
          <table cellspacing="10">
            <tr>
              <td>Speaking/Communication</td>
              <td>⭐⭐⭐⭐⭐</td>
              <td>Content Writing</td>
              <td>⭐⭐⭐⭐⭐</td>
            </tr>
            <tr>
              <td>Chess</td>
              <td>⭐⭐⭐</td>
              <td>YT Video Creation</td>
              <td>⭐⭐⭐⭐</td>
            </tr>
            <tr>
              <td>Web Development</td>
              <td>⭐⭐⭐</td>
              <td>Video Editing</td>
              <td>⭐⭐⭐</td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
    
    <hr style="margin: 0 30px;">
    
    <table cellspacing="20" style="padding: 30px;">
      <tr>
        <td>
          <h3>Work Experience</h3>
          <table border="1">
            <thead>
              <tr>
                <th>Time Period</th>
                <th>Work</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>2019-2021</td>
                <td>Dedicated preparation of JEE</td>
              </tr>
              <tr>
                <td>2021-2022</td>
                <td>Learned Python, founded Unicorn Club, learned web development, 
                  worked with <a href="https://instagram.com/__the28__?igshid=YmMyMTA2M2Y=">The 28</a> fashion startup</td>
              </tr>
              <tr>
                <td>2022-Present</td>
                <td>Continuing web development, exploring AI/ML technologies, content creation</td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </table>
  </div>
</body>

</html>"""
    
    with open('index.html', 'w') as f:
        f.write(main_html)
    
    print(f"✓ Updated: index.html with {len(resume_list)} portfolios")

def main():
    """Main function to discover resumes and generate portfolios."""
    
    # Find all PDF files in current directory
    pdf_files = list(Path('.').glob('*.pdf'))
    
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return
    
    # Extract resume metadata
    resumes = [get_resume_metadata(pdf.name) for pdf in pdf_files]
    
    print(f"Found {len(resumes)} resume(s):\n")
    for resume in resumes:
        print(f"  - {resume['title']} ({resume['filename']})")
    
    print("\nGenerating portfolio pages...\n")
    
    # Generate portfolio pages
    update_portfolio_index(resumes)
    
    print("\n✓ Portfolio generation complete!")
    print(f"  - Generated {len(resumes)} portfolio page(s)")
    print("  - Updated index.html with portfolio links")

if __name__ == '__main__':
    main()
