#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import codecs
import unicodedata
from string import Template

out = codecs.getwriter('utf-8')(sys.stdout)

summary_pre=r'''
\begin{table}[ht]
  \resizebox{\textwidth}{!}{%
  \begin{tabular}{llllll}
'''

summary_post=r'''
  \end{tabular}}
\end{table}
'''

verb_table_template=Template(r'''
\begin{table}[ht]
  \resizebox{\textwidth}{!}{%
  \begin{tabular}{|l|l|l|l|}
  \hline
  \multicolumn{4}{|c|}{} \\
  \multicolumn{4}{|c|}{\huge{$title}} \\
  \multicolumn{4}{|c|}{} \\
  \hline
  \multicolumn{4}{|c|}{$head} \\
  \hline
  \multicolumn{2}{|c|}{\textbf{Form}} & \textbf{Positive} & \textbf{Negative} \\
  \hline
  Present & Plain   & $pres_plain_pos  & $pres_plain_neg \\
          & Polite  & $pres_polite_pos & $pres_polite_neg \\
  \hline
  Past    & Plain   & $past_plain_pos & $past_plain_neg \\
          & Polite  & $past_polite_pos & $past_polite_neg \\
  \hline
  \multicolumn{2}{|c}{Te-Form} & \multicolumn{2}{|c|}{$te_form} \\
  \hline
  \end{tabular}}
\end{table}
''')

na_table=r'''
\begin{table}[ht]
  \resizebox{\textwidth}{!}{%
  \begin{tabular}{|l|l|l|l|}
  \hline
  \multicolumn{4}{|c|}{} \\
  \multicolumn{4}{|c|}{\huge{@0}} \\
  \multicolumn{4}{|c|}{} \\
  \hline
  \multicolumn{4}{|c|}{@1} \\
  \hline
  \multicolumn{2}{|l|}{\textbf{Form}} & \textbf{Positive} & \textbf{Negative} \\
  \hline
  Present & Plain   & @2 & @3 \\
          & Polite  & @4 & @5 \\
  \hline
  Past    & Plain   & @6 & @7 \\
          & Polite  & @8 & @9 \\
  \hline
  \end{tabular}}
\end{table}
'''

i_table=r'''
\begin{table}[ht]
  \resizebox{\textwidth}{!}{%
  \begin{tabular}{|l|l|l|l|}
  \hline
  \multicolumn{4}{|c|}{} \\
  \multicolumn{4}{|c|}{\huge{@2-}} \\
  \multicolumn{4}{|c|}{} \\
  \hline
  \multicolumn{4}{|c|}{@1-} \\
  \hline
  \multicolumn{2}{|l|}{\textbf{Form}} & \textbf{Positive} & \textbf{Negative} \\
  \hline
  Present & Plain   & @2- & @3- \\
          & Polite  & @4- & @5- \\
          &         &     & @6- \\
  \hline
  Past    & Plain   & @7- & @8-  \\
          & Polite  & @9- & @10- \\
          &         &     & @11- \\
  \hline
  \end{tabular}}
\end{table}
'''

tmp=r'''
\documentclass{article}
\usepackage{fontspec}
\usepackage{ctable}
\setmainfont{Sazanami Mincho}

\title{\huge{日本語}}
\author{Fredrik Nilsson}

\begin{document}
\maketitle
\newpage
\tableofcontents
\clearpage
\newpage
'''

latex_pre=unicode(tmp, 'utf-8')

del tmp

latex_post=r'''
\end{document}
'''
