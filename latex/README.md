# LaTeX Résumé Templates — Chinmay Harjai

Two single-page résumés built on **one shared template** so the look stays
consistent no matter how much you edit the text.

| File | What it is |
|------|-----------|
| `resume.cls` | The **template** — all formatting (fonts, colours, spacing, section styling, custom commands). |
| `ai_engineer_resume.tex` | **Content only** for the AI Engineer résumé. |
| `data_science_resume.tex` | **Content only** for the Data Science résumé. |
| `ai_engineer_resume.pdf` / `data_science_resume.pdf` | The compiled output. |

## The golden rule

- ✅ **Edit the `.tex` files** to change what a résumé *says* (jobs, projects, skills).
- 🎨 **Edit `resume.cls`** to change how *every* résumé *looks* (colour, margins, fonts).
- 🚫 **Don't put formatting (font sizes, spacing, colours) inside the `.tex` files.**
  Keeping style out of the content files is what stops you from "spoiling" the
  template — the two files can never drift out of sync.

## How to compile

### Option A — Overleaf (no install, easiest)
1. Go to [overleaf.com](https://www.overleaf.com) → **New Project → Upload Project**.
2. Upload `resume.cls` **together with** the `.tex` file you want.
3. Set the main document to `ai_engineer_resume.tex` (or the data-science one) and click **Recompile**.

### Option B — Locally
You need a TeX distribution (TeX Live / MiKTeX) with the `fontawesome5` package.
```bash
pdflatex ai_engineer_resume.tex
pdflatex data_science_resume.tex
```

## Editing cheat-sheet

Every résumé is assembled from a few simple commands defined in `resume.cls`.
Just fill in the text — the styling is handled for you.

```latex
% Header
\name{Chinmay Harjai}
\contact{%
  \phone{+91 7878709846} \contactsep
  \email{chinmayharjai@gmail.com} \contactsep
  \github{chinmayharjai}{GitHub} \contactsep
  \linkedin{https://www.linkedin.com/in/chinmayharjai}{LinkedIn}%
}

% A section
\section{Experience}

% A job: \entry{Title}{Dates / location}
\entry{ICICI Bank \textnormal{— Data Engineer, Mumbai}}{July 2025 -- Present}
\begin{itemize}
  \item First achievement...
  \item Second achievement...
\end{itemize}

% A project heading (plain, or with a clickable repo link)
\project{My Project Name}
\projectlink{My Project Name}{https://github.com/you/repo}

% Education: \education{Degree}{Institution}{Year}
\education{BTech, Electrical Engineering}{National Institute of Technology, Jaipur}{2025}

% A skills line: \skill{Category}{comma, separated, items}
\skill{Programming Languages}{Python, SQL}
```

### Common tweaks

| I want to... | Do this |
|--------------|---------|
| Add a bullet | Add another `\item ...` inside an `itemize` block. |
| Add a project | Copy a `\project{...}` block with its `itemize` list. |
| Change the accent colour | Edit the `accent` colour near the top of `resume.cls`. |
| Change page margins | Edit the `geometry` line in `resume.cls`. |
| Reorder sections | Move whole `\section{...}` blocks in the `.tex` file. |

## Keeping it to one page

Both résumés are tuned to fit on a single page. If you add a lot of content and
it overflows, prefer trimming wording first. If you must reclaim space globally,
adjust the spacing values in `resume.cls` (the `geometry` margins, the
`\titlespacing` for sections, or the `itemize` `itemsep`) — one change there
keeps both résumés consistent.

## Special characters

In LaTeX these characters must be escaped in your text: `& % $ # _ { }`.
Write them as `\&`, `\%`, `\$`, `\#`, `\_`, `\{`, `\}`. (For example, `AI & ML`
is written `AI \& ML`, and `60%` is written `60\%`.)
