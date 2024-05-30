# OBJECTS

```latex
% A COMMENT

\\documentclass[12pt]{extarticle}
% 12pt is general font size, which can be picked from established values, up to 20pt, for extarticle, i.e. extension of article
% article, paper are types of document
% stuff in [square brackets] are parameters, optional

% Language setting
% Replace `english' with e.g. `spanish' to change the document language
\usepackage[english]{babel}

% Set page size and margins
% Replace `letterpaper' with `a4paper' for UK/EU standard size
\usepackage[letterpaper,top=2cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{geometry}

% packages
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage[colorlinks=true, allcolors=blue]{hyperref}
\usepackage{amssymb}
\usepackage{float}

\title{Your Paper}
\author{You}

\begin{document}
\maketitle

\begin{abstract}
Your abstract.
\end{abstract}

\section{Section's title}

\subsection{Subsection's title}

\subsubsection{Subsubsection's title}
...text...
Another line, here, is displayed next to the previous, if there isn't a line break like \\
And here's a double line break, to separate the texts \\
\\
here.

Here are formatters, like \textit{italic}, .

\begin{enumerate}
	\item numbered list item
	\item math expressions:
	\begin{enumerate}
		\item an inline math expression, formatted as special text $k$;
		\item pedix and apix: $a_1$, $a^2$...
		\item ...with more complex expression as apix/pedix: $a^{{x+1}/2}$
		\item math formatted letters, like sets $\mathbb{N}$, $\mathbb{R}$;

	\end{enumerate}
\end{enumerate}

Here's an image. $[H]$ (in square brackets) is a float parameter (requires pkg float), and it forces the image to be placed exactly where it is in the code.
\begin{figure}[H]
    \centering
    \includegraphics{your_image.png}
    \caption{caption displayed}
    \label{fig:enter-label}
\end{figure}

\end{document}
```
