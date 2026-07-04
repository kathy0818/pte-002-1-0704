#!/usr/bin/env python3
"""把本套已收录的部分合并成一本【总整理卷】（自包含 .tex + img/），输出到 整理卷/总整理卷/。

用法:
    python3 build/flatten_all.py <EXAM>
例:
    python3 build/flatten_all.py 43B

- 内联 ptestyle.sty，依次拼 cover + 目录/概览 + 听力 + 阅读 + 口语（听·读·说，本套未收录写作，
  口语仅收录 DI）。
- 口语含 DI 配图 → 同时把 build/paper/img/ 拷到 整理卷/总整理卷/img/，整体自包含。
- 生成后到该目录 `xelatex` 跑两遍（目录页码要第二遍才对），再把 PDF 复制到 整理卷/ 根。
"""
import sys, pathlib, shutil

EXAM = sys.argv[1] if len(sys.argv) > 1 else "43B"
root = pathlib.Path(__file__).resolve().parent.parent
base = root / "build" / "paper"

sty = (base / "ptestyle.sty").read_text(encoding="utf-8")
keep = [l for l in sty.splitlines()
        if not l.strip().startswith(r"\ProvidesPackage") and l.strip() != r"\endinput"]
sty_inline = "\n".join(keep).rstrip()
cover = (base / "cover.tex").read_text(encoding="utf-8").rstrip()

# 顺序：听 → 读 → 说（DI）。本套未做写作，口语仅收录 DI。
order = ["listening", "reading", "speaking"]
bodies = []
for sec in order:
    bodies.append(f"% ===== sec_{sec}_body.tex =====\n"
                  + (base / f"sec_{sec}_body.tex").read_text(encoding="utf-8").rstrip())
bodies_tex = "\n\n\\clearpage\n".join(bodies)

toc_overview = r"""\clearpage
\tableofcontents
\bigskip

{\large\bfseries\color{cAccent}本卷概览}\par\smallskip
{\small
\begin{tabularx}{\linewidth}{@{}l c >{\RaggedRight\arraybackslash}X r@{}}
\rowcolor{cHead}\textcolor{white}{\bfseries 部分} & \textcolor{white}{\bfseries 题量} & \textcolor{white}{\bfseries 题型构成} & \textcolor{white}{\bfseries 本项得分}\\
听力 Listening & 15 & SST · MCM-L\,$\times$2 · FIB-L\,$\times$2 · HCS\,$\times$2 · MCS-L\,$\times$2 · SMW · HIW\,$\times$2 · WFD\,$\times$3 & 32 / 90\\
阅读 Reading & 15 & FIB\,$\times$5 · MCM-R\,$\times$2 · RO\,$\times$2 · FIBD\&D\,$\times$4 · MCS-R\,$\times$2 & 51 / 90\\
口语 Speaking（仅 DI）& \phantom{0}5 & DI\,$\times$5（RA/RS/RTS/ASQ 等题型未收录）& 12 / 90\phantom{$^*$}\\
\end{tabularx}}
\par\smallskip
{\footnotesize\color{gray}本次模考总分 29（听力 32 / 阅读 51 / 口语 12 / 写作 21，写作未收录本卷）。口语一栏
12/90 为该考生口语部分\emph{官方总分}（含未收录的 RA/RS/RTS/ASQ 等题型），非本卷 5 道 DI 的得分总和。
颜色与标注沿用各部分；本合订本顺序为「听·读·说（DI）」。}"""

out = (
    f"% PTE Core 模考 {EXAM} —— 总整理卷（听·读·说(DI) 合订，自包含；本套未收录写作）\n"
    f"% 编译: xelatex 本文件.tex（跑两遍，目录页码才对）；依赖同目录 img/。\n"
    "\\documentclass[11pt]{article}\n\n"
    "% --------- 样式（原 ptestyle.sty，已内联）---------\n" + sty_inline + "\n"
    "\\renewcommand{\\contentsname}{目录\\quad Contents}\n\n"
    "\\begin{document}\n\n"
    "% --------- 封面（原 cover.tex）---------\n" + cover + "\n\n"
    "% --------- 目录 + 本卷概览 ---------\n" + toc_overview + "\n\n"
    "\\clearpage\n% --------- 已收录部分正文 ---------\n" + bodies_tex + "\n\n"
    "\\end{document}\n"
)

outdir = root / "整理卷" / "总整理卷"
outdir.mkdir(parents=True, exist_ok=True)
stem = f"PTE模考{EXAM}_总整理卷"
(outdir / f"{stem}.tex").write_text(out, encoding="utf-8")
if (base / "img").is_dir():
    shutil.copytree(base / "img", outdir / "img", dirs_exist_ok=True)
print(outdir / f"{stem}.tex")
