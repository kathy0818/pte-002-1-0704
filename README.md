# PTE Core 备考素材整理 / PTE Core Prep Materials

本仓库把 PTE **学术类**模考（完整模考 **43B**，8.7 新考试版本；提交 2026-07-03 17:45；总分 **29**：听力 32 / 阅读 51 / 口语 12 / 写作 21）的逐题裁剪截图，排版成干净可打印的**错题与详解·整理卷 PDF**（做法与命名沿用姊妹仓库 `pte-002-0628` 的 2B 套）。

This repo typesets the per-question crops of a PTE **Academic** mock exam (full mock **43B**) into clean, printable **"wrong-answer & explanation" review PDFs**, following the same process/conventions as the sibling repo's 2B set.

---

## ⭐ 整理卷成品 / Typeset review PDFs（产物）

```
整理卷/
├─ PTE模考43B_阅读_整理卷.pdf     ★ 阅读，已完成（15 题，14 页）
├─ PTE模考43B_听力_整理卷.pdf     ★ 听力，已完成（15 题，12 页）
├─ PTE模考43B_口语_整理卷.pdf     ★ 口语，仅收录 DI 看图说话 5 题（5 页，含配图）
├─ PTE模考43B_总整理卷.pdf         ★ 合订本：听·读·说(DI)，30 页
├─ 阅读/ 听力/ 口语/               各 part 的版本存档（000_….tex + .pdf）
└─ 总整理卷/                       合订本源文件（.tex + img/）
```

> **本次范围**：只做了**阅读**与**听力**全部 15 题，口语只收录 **DI 看图说话 5 题**（RA/RS/RTS/ASQ 等口语其它题型、写作均未收录）。
> **进度：✅ 阅读（000）、✅ 听力（000）、✅ 口语 DI（000）、✅ 合订本 全部完成。**

### ⚠️ 已知缺口 / Known gaps

| 部分 | 缺什么 | 已知信息 | 状态 |
|------|--------|---------|------|
| 阅读 R01（FIB #1076）| 第 3–5 空的四选项列表（干扰项）被平台悬浮条挡住 | 正确答案已知：has shed / commitment / urgency | 已在整理卷中标注，待平台"查看原题"补全 |
| 阅读 R14（MCS-R #45）| 选项 A 文字被平台悬浮条挡住 | 正确答案已知：A | 已标注，待补全 |
| 听力 Q1（SST #712）| 录音原文文字稿（音频无法转文字）| 你的作答全文已有 | 已标注，待平台"查看原题"补全 |
| 口语 DI 全部 5 题 | 只有合并总分（如 10/90），无 Content/Pronunciation/Fluency 逐项分；无参考范文 | 作答文字稿(ASR)、配图、录音均已收录 | 据实收录，未展开部分留待补充 |

出新版本 / 有新素材补齐时，流程见 `交接文档/00_总交接文档.md`。

---

## 📁 原始裁剪素材 / Cropped source materials（本仓库另一半内容）

本仓库同时保留了模考的整页长截图，按 **PTE Core** 需要的题型，逐题裁剪成单独图片（每张都**带答案/解析**），是上面整理卷排版时使用的原始素材。

This repo also keeps the full-page PTE mock-exam screenshots sliced into **one image per question** (each **includes the answer / feedback**) — the raw material used to typeset the review PDFs above.

---

## 📁 目录结构 / Folder structure

```
original_screenshots/     原始整页截图（未改动）/ untouched full-page originals
    听力1.jpeg  听力2.jpeg        (Listening pages 1–2)
    阅读1.jpeg  阅读2.jpeg        (Reading   pages 1–2)
    口语2.jpeg  口语3.jpeg        (Speaking  pages 2–3)
    SST.png                       (SST 的 AI 评分弹窗 / SST AI-scoring popup)

cropped_questions/        逐题裁剪结果（我要求的）/ per-question crops (the requested output)
    listening/   15 题 + 1 张 SST 评分详情 / 15 questions + 1 SST scoring detail
    reading/     15 题 / 15 questions
    speaking_DI/  5 题（仅 DI 看图说话）/ 5 questions (Describe Image only)
```

命名规则 / Naming: `序号_题型_题库编号_标题.png`  →  e.g. `L07_HCS_81_What_Democracy_Breeds.png`
（`L`=Listening, `R`=Reading, `DI`=Describe Image；题库编号即平台的 `#id`。）

---

## 🎧 Listening（听力，15 题）

| # | 文件 / File | 题型 / Type | 题目 / Title |
|---|---|---|---|
| 01 | L01_SST_712_Environmental_Conservation | SST | Environmental Conservation |
| 01b | L01b_SST_712_AI_scoring_detail | SST | 上题的 AI 评分详情 / AI scoring detail |
| 02 | L02_MCM-L_102_Time_Famine | MCM-L | Time Famine |
| 03 | L03_MCM-L_106_Hair | MCM-L | Hair |
| 04 | L04_FIB-L_4 | FIB-L | — |
| 05 | L05_FIB-L_7_Language_Learning | FIB-L | Language Learning |
| 06 | L06_HCS_80_Mental_Health | HCS | Mental Health |
| 07 | L07_HCS_81_What_Democracy_Breeds | HCS | What Democracy Breeds |
| 08 | L08_MCS-L_123_Parties | MCS-L | Parties |
| 09 | L09_MCS-L_122_Washington | MCS-L | Washington |
| 10 | L10_SMW_36_Stress | SMW | Stress |
| 11 | L11_HIW_216_T_Cell | HIW | T Cell |
| 12 | L12_HIW_179_Bone_and_Weight | HIW | Bone and Weight |
| 13 | L13_WFD_3208 | WFD | — |
| 14 | L14_WFD_3197 | WFD | — |
| 15 | L15_WFD_3191 | WFD | — |

## 📖 Reading（阅读，15 题）

| # | 文件 / File | 题型 / Type | 题目 / Title |
|---|---|---|---|
| 01 | R01_FIB_1076_Honorary_Fellowship | FIB (R&W) | Honorary Fellowship |
| 02 | R02_FIB_1072_Secret_Farm | FIB (R&W) | Secret Farm |
| 03 | R03_FIB_1058_Urban_Transformation | FIB (R&W) | Urban Transformation |
| 04 | R04_FIB_1045_Social_Media | FIB (R&W) | Social Media |
| 05 | R05_FIB_1040_Drought-resistant_Crops | FIB (R&W) | Drought-resistant Crops |
| 06 | R06_MCM-R_23 | MCM-R | — |
| 07 | R07_MCM-R_34_Paintings | MCM-R | Paintings |
| 08 | R08_RO_835_Livestock | RO | Livestock |
| 09 | R09_RO_827_Fossil_Fuel | RO | Fossil Fuel |
| 10 | R10_FIBDD_1110_Deep-sea_Fish | FIB (R) drag&drop | Deep-sea Fish |
| 11 | R11_FIBDD_1109_Music_Show | FIB (R) drag&drop | Music Show |
| 12 | R12_FIBDD_1108_Sufficient_Sleep | FIB (R) drag&drop | Sufficient Sleep |
| 13 | R13_FIBDD_1068_Chemical_Cauldron | FIB (R) drag&drop | Chemical Cauldron |
| 14 | R14_MCS-R_45 | MCS-R | — |
| 15 | R15_MCS-R_38 | MCS-R | — |

## 🗣️ Speaking — Describe Image（口语，仅 DI，5 题 / DI only）

| # | 文件 / File | 题型 / Type | 题目 / Title |
|---|---|---|---|
| 01 | DI01_1189_Pet_Services | DI | Pet Services (饼图 / pie) |
| 02 | DI02_1186_Estate_Sales | DI | Estate Sales (柱状图 / bar) |
| 03 | DI03_1148_Electricity_Usage | DI | Electricity Usage (折线图 / line) |
| 04 | DI04_949_Crop_Distribution | DI | Crop Distribution (世界地图 / map) |
| 05 | DI05_1160_Riverside_Town | DI | Riverside Town (图片 / photo) |

> 口语部分只保留了 DI（看图说话）题；RS / RL / ASQ / SGD 等其它口语题型按要求未裁剪。
> Speaking keeps only DI (Describe Image); other speaking types (RS/RL/ASQ/SGD) were skipped as requested.

---

## 🛠️ 处理说明 / Processing notes
- 每张裁剪图都从题号标题开始，到该题的**评分/答案行**结束。/ Each crop runs from the numbered title down to that question's score/answer line.
- 已自动**去掉页脚、翻页条**，并**擦除**盖在题目上的站点顶部导航条与右侧浮动按钮。/ Footers, pagination bars, the overlapping site nav-bar, and the floating side-button were removed automatically.
- 原始截图完整保留在 `original_screenshots/`，未做任何修改。/ Originals are kept untouched in `original_screenshots/`.
