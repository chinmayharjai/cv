# Portfolio Generator for Resume PDFs

Automatically generates a professional personal portfolio website from resume PDF files.

## Features

✨ **Automatic Portfolio Generation**
- Scans for PDF files in the `New_Cv` branch
- Extracts resume titles from filenames
- Creates individual portfolio pages for each resume
- Updates main portfolio hub (`index.html`)

🚀 **GitHub Actions Integration**
- Automatically triggers when new PDFs are added
- Generates portfolio pages on every PDF push
- Creates attractive, responsive portfolio pages
- Commits changes automatically

📱 **Responsive Design**
- Mobile-friendly portfolio pages
- Gradient backgrounds with modern styling
- PDF embedded viewers
- Download links for each resume

## How It Works

### 1. Add Resume PDFs
Push PDF files to the `New_Cv` branch:
```bash
git push origin New_Cv
```

Example filenames:
- `AI_ENGINEER_resume_Chinmay_updated-1.pdf`
- `MS_data_Science_resume_Chinmay.pdf`
- `Full_Stack_Developer_Resume.pdf`

### 2. Automatic Workflow Trigger
The GitHub Actions workflow automatically:
- Detects new PDF uploads
- Runs the portfolio generator script
- Creates individual portfolio pages in `portfolios/` directory
- Updates the main `index.html` with portfolio links
- Commits and pushes the changes

### 3. View Your Portfolio
- **Main Hub:** `index.html` - Shows all available portfolios
- **Individual Pages:** `portfolios/ai_engineer_resume_chinmay_updated_1.html` - Specific resume portfolios

## File Structure

```
New_Cv/
├── scripts/
│   └── generate_portfolio.py       # Portfolio generation script
├── .github/
│   └── workflows/
│       └── generate-portfolio.yml  # GitHub Actions workflow
├── portfolios/                     # Generated portfolio pages (auto-created)
│   ├── ai_engineer_resume*.html
│   └── ms_data_science_resume*.html
├── index.html                      # Main portfolio hub (auto-updated)
├── *.pdf                          # Your resume PDFs
└── README.md                       # This file
```

## Workflow Trigger

The GitHub Actions workflow is triggered by:
- ✅ Push to `New_Cv` branch with `*.pdf` files
- ✅ Manual trigger via `workflow_dispatch`

### Workflow Steps

1. **Checkout Code** - Fetches the latest code
2. **Setup Python** - Prepares Python 3.10 environment
3. **Check for PDFs** - Scans for PDF files
4. **Create Directories** - Sets up `portfolios/` folder
5. **Generate Portfolios** - Runs the portfolio generator script
6. **Commit Changes** - Pushes updated files to the repository
7. **Create Summary** - Generates workflow summary

## Portfolio Features

Each generated portfolio page includes:

- 📄 **Resume Viewer** - Embedded PDF viewer
- ⬇️ **Download Link** - Download the original PDF
- 🎨 **Modern Design** - Gradient backgrounds and professional styling
- 📱 **Responsive Layout** - Works on all devices
- 🔗 **Navigation** - Links back to main portfolio hub
- ✨ **Professional Footer** - Generation timestamp and metadata

## Customization

### Modify Portfolio Template
Edit the HTML template in `scripts/generate_portfolio.py` in the `generate_portfolio_page()` function to customize:
- Colors and gradients
- Layout and spacing
- Additional sections
- Social links
- Contact information

### Modify Main Index
The main `index.html` is generated with:
- Your profile picture (`chinmay_harjai.png`)
- Skills section with ratings
- Work experience timeline
- Project links
- Contact information

## Manual Execution

To manually generate portfolios without pushing files:

```bash
# Clone/pull the latest code
git clone -b New_Cv https://github.com/chinmayharjai/cv.git
cd cv

# Run the portfolio generator
python scripts/generate_portfolio.py

# Check generated files
ls portfolios/
cat index.html
```

## Example Workflow Output

```
Found 2 resume(s):

  - AI Engineer Resume Chinmay Updated 1 (AI_ENGINEER_resume_Chinmay_updated-1.pdf)
  - MS Data Science Resume Chinmay (MS_data_Science_resume_Chinmay.pdf)

Generating portfolio pages...

✓ Generated: portfolios/ai_engineer_resume_chinmay_updated_1.html
✓ Generated: portfolios/ms_data_science_resume_chinmay.html
✓ Updated: index.html with 2 portfolios

✓ Portfolio generation complete!
  - Generated 2 portfolio page(s)
  - Updated index.html with portfolio links
```

## Troubleshooting

### Workflow Fails to Trigger
- Ensure PDFs are added to the root directory
- Check that the push is to the `New_Cv` branch
- Verify workflow file is in `.github/workflows/`

### Portfolio Pages Not Generated
- Check GitHub Actions logs for errors
- Ensure PDF filenames are valid
- Verify `scripts/generate_portfolio.py` exists

### Files Not Committed
- Check git configuration in the workflow
- Ensure branch protections allow workflow commits
- Verify `GITHUB_TOKEN` has write permissions

## Future Enhancements

- 🔍 Extract text from PDFs for indexing
- 🎯 Generate multiple portfolio layouts
- 📊 Add analytics tracking
- 🌐 Deploy to GitHub Pages automatically
- 📧 Send notifications on portfolio updates
- 🎨 Add more theme options

## License

This project is open source and available under the MIT License.

---

**Generated on:** June 17, 2026  
**Maintained by:** Chinmay Harjai  
**Repository:** [chinmayharjai/cv](https://github.com/chinmayharjai/cv)
