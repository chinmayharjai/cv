%% resume.cls
%% -----------------------------------------------------------------------------
%% A lightweight, single-page resume class for Chinmay Harjai's CVs.
%%
%% This file holds ALL formatting: fonts, margins, colours, section styling and
%% the custom commands used to build a resume. Content lives in the separate
%% *.tex files (e.g. ai_engineer_resume.tex). To restyle every resume at once,
%% edit this file. To change what a resume *says*, edit the content file and
%% leave this one untouched.
%%
%% Compiles with pdflatex on Overleaf or any standard TeX distribution.
%% Only depends on common packages (no external fonts required).
%% -----------------------------------------------------------------------------
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{resume}[2026/07/13 Simple single-page resume class]

% Base the class on the standard article class at 11pt.
\LoadClass[11pt,a4paper]{article}

% ---- Packages --------------------------------------------------------------
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage[hmargin=1.35cm,vmargin=0.75cm]{geometry} % page margins
\RequirePackage{titlesec}      % section title styling
\RequirePackage{enumitem}      % tight bullet lists
\RequirePackage{hyperref}      % clickable links
\RequirePackage{xcolor}        % colours
\RequirePackage{fontawesome5}  % contact icons (email, phone, github, ...)
\RequirePackage{tabularx}      % header layout
\RequirePackage{parskip}       % sensible paragraph spacing

% ---- Colours ---------------------------------------------------------------
% Change these two lines to re-theme every resume built with this class.
\definecolor{accent}{HTML}{1A5276} % headings & links (deep blue)
\definecolor{text}{HTML}{222222}   % body text

\color{text}

% ---- Link styling ----------------------------------------------------------
\hypersetup{
  colorlinks=true,
  urlcolor=accent,
  linkcolor=accent,
  pdfborder={0 0 0}
}

% ---- Remove default page numbers -------------------------------------------
\pagestyle{empty}

% ---- Section headings ------------------------------------------------------
% Small-caps, accent-coloured heading with a rule underneath.
\titleformat{\section}
  {\normalfont\large\bfseries\color{accent}\scshape}
  {}{0em}{}[\vspace{-0.4em}\color{accent}\hrule\vspace{0.2em}]
\titlespacing{\section}{0pt}{0.55em}{0.3em}

% ---- List defaults ---------------------------------------------------------
% Tight, compact bullets used throughout the resume.
\setlist[itemize]{
  leftmargin=1.15em,
  topsep=0pt,
  itemsep=1pt,
  parsep=0pt,
  label=\textcolor{accent}{\small\textbullet}
}

% Trim paragraph spacing (set by the parskip package) for a tighter layout.
\setlength{\parskip}{0.35em}

% =============================================================================
%  CUSTOM COMMANDS  --  use these in the content files
% =============================================================================

% \name{Full Name} -- big, centred name at the top of the resume.
\newcommand{\name}[1]{%
  \begin{center}\Huge\bfseries\color{accent}\scshape #1\end{center}%
  \vspace{-0.6em}%
}

% \contact{ ... } -- centred contact line. Build it from the helper commands
% below, separated by \contactsep. Example:
%   \contact{\phone{+91 ...} \contactsep \email{a@b.com} \contactsep
%            \github{user}{GitHub} \contactsep \linkedin{url}{LinkedIn}}
\newcommand{\contact}[1]{%
  \begin{center}\small #1\end{center}%
  \vspace{0.2em}%
}
\newcommand{\contactsep}{\quad\textbar\quad}

% Individual contact items (icon + text). Edit the icon here to restyle all.
\newcommand{\phone}[1]{\faPhone*\ #1}
\newcommand{\email}[1]{\faEnvelope\ \href{mailto:#1}{#1}}
\newcommand{\github}[2]{\faGithub\ \href{https://github.com/#1}{#2}}
\newcommand{\linkedin}[2]{\faLinkedin\ \href{#1}{#2}}
\newcommand{\website}[2]{\faGlobe\ \href{#1}{#2}}

% \entry{Title}{Meta} -- a bold left-aligned title with right-aligned meta
% (dates / location), used for jobs. Follow it with an itemize list.
\newcommand{\entry}[2]{%
  \vspace{0.2em}%
  \noindent\begin{tabularx}{\linewidth}{@{}X r@{}}
    \textbf{#1} & \textit{#2}
  \end{tabularx}%
  \vspace{-0.2em}%
}

% \project{Name} and \projectlink{Name}{url} -- a bold project heading.
\newcommand{\project}[1]{\vspace{0.2em}\noindent\textbf{#1}\vspace{-0.1em}}
\newcommand{\projectlink}[2]{%
  \vspace{0.2em}\noindent\textbf{#1}\ \href{#2}{\small\faLink}\vspace{-0.1em}%
}

% \skill{Category}{items} -- one bullet line in the skills section.
\newcommand{\skill}[2]{\item \textbf{#1:} #2}

% \education{Degree}{Institution}{Year} -- one education line.
\newcommand{\education}[3]{\item \textbf{#1}, #2 \hfill \textit{#3}}

% Tighten spacing between a heading and the following list.
\newcommand{\resumelist}{\vspace{-0.2em}}
