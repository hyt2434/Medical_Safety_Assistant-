"""Build the portrait model/specification section from the original specification."""
from pathlib import Path
import re

root = Path(__file__).resolve().parent
source = (root / 'sections/02-use-case-specifications.tex').read_text(encoding='utf-8')
source = source.replace(r'\section{Use-case Specifications}', r'\section{Use-case Models and Specifications}')
macro = r'''
\renewcommand{\arraystretch}{1.05}
\setlength{\parskip}{2pt}
% Extend only the figure into the margins: 19 cm on a 21 cm portrait A4 page.
\newcommand{\InlineUCModel}[1]{%
  \par\noindent
  \begin{minipage}{\linewidth}
    \centering
    \makebox[\linewidth][c]{%
      \includegraphics[width=19cm,height=0.60\textheight,keepaspectratio]{UC_#1.pdf}%
    }
    \captionsetup{hypcap=false}
    \captionof{figure}{UC-#1: detailed use-case model.}
    \label{fig:uc-model-#1}
  \end{minipage}
  \par\smallskip
}
'''
source = macro + source
source = source.replace(r'\par\smallskip', r'\par')
source = re.sub(r'\\\\\s*\\hline\s*(\\textbf\{(?:Pre-conditions|Post-conditions)\})', lambda m: '\\\\* \\hline\n' + m[1], source)
source, count = re.subn(r'(\\label\{uc:uc-(\d{2})\})', lambda m: m[1] + '\n\\InlineUCModel{' + m[2] + '}\n', source)
assert count == 18, count
for number in ('02', '03', '04', '05', '06', '14', '18'):
    start = source.index('\\label{uc:uc-' + number + '}')
    alt = source.index(r'\textbf{Alternative Flows}', start)
    source = source[:alt] + '\\end{longtable}\n\\clearpage\n\\noindent\\textbf{UC-' + number + ': Specification (continued)}\n\\begin{longtable}{|p{0.20\\textwidth}|p{0.71\\textwidth}|}\n\\hline\n' + source[alt:]
(root / 'sections/03-use-cases-combined.tex').write_text(source, encoding='utf-8')
