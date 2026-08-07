from __future__ import annotations
import argparse, concurrent.futures, hashlib, json, os, re
from collections import Counter
from pathlib import Path
import pymupdf

SRC=Path(r"D:\数学建模优秀论文分析\高教社杯全国大学生数学建模竞赛优秀论文")
VAULT=Path(r"C:\Users\17888\Documents\0.数学建模知识库\0.数学建模")
PROJECT=VAULT/"06-Projects"/"优秀论文批量拆解"
CACHE=PROJECT/"Data"/"Extracted"
OUT=VAULT/"04-Research"/"04-竞赛真题研究"/"03-优秀获奖论文拆解"/"批量标准化拆解"
CATS={"A":"连续型模型","B":"离散型模型","C":"数据分析与数据挖掘","D":"综合决策与评价","E":"社会环境政策与系统仿真","F":"博弈与对策"}
TITLE_OVERRIDES={
"2012国赛国家一等奖A题优秀论文5_20220719111558.pdf":"葡萄酒的评价",
"2010B：上海世博会影响力的定量评估.pdf":"上海世博会影响力的定量评估"}

# 名称、匹配式、类别、已有知识节点
RAW=r"""偏微分方程|偏微分方程|(?<![A-Za-z])PDE(?![A-Za-z])|A|偏微分方程
常微分方程|常微分方程|微分方程组|(?<![A-Za-z])ODE(?![A-Za-z])|A|常微分方程
有限差分法|有限差分|A|模型-有限差分法
动力学模型|动力学模型|运动学模型|力学模型|A|微分方程动力学 Hub
热传导模型|热传导|传热模型|炉温|A|模型-热传导模型
扩散模型|扩散方程|污染物扩散|对流扩散|A|扩散动力学模型
SIR传染病模型|SIR|SEIR|传染病模型|A|SIR与SIS传染病模型
Logistic模型|Logistic模型|种群增长|A|种群增长Logistic模型
几何模型|几何模型|解析几何|空间几何|几何关系|A|模型-几何模型
线性规划|线性规划|B|线性规划
非线性规划|非线性规划|B|非线性规划
优化模型|优化模型|目标函数|最小费用|最小成本|费用最少|总费用最小|min\s*[A-Za-z]|B|模型-优化模型
整数规划|整数规划|0-1规划|混合整数|B|整数规划与0-1规划
多目标规划|多目标规划|多目标优化|Pareto|B|多目标规划
动态规划|动态规划|Bellman|B|动态规划
图论模型|图论|网络模型|复杂网络|B|图论网络 Hub
最短路径|最短路径|Dijkstra|Floyd|B|最短路径
网络流|网络流|最大流|最小费用流|B|网络流
路径规划|车辆路径|路径规划|旅行商|TSP|VRP|B|模型-车辆路径规划
排队论|排队论|排队模型|B|排队论模型
遗传算法|遗传算法|(?<![A-Za-z])GA(?![A-Za-z])|B|遗传算法GA
粒子群算法|粒子群|(?<![A-Za-z])PSO(?![A-Za-z])|B|粒子群PSO
模拟退火|模拟退火|(?<![A-Za-z])SA(?![A-Za-z])|B|模拟退火SA
蚁群算法|蚁群算法|(?<![A-Za-z])ACO(?![A-Za-z])|B|蚁群算法ACO
回归分析|回归分析|线性回归|多元回归|逐步回归|C|回归分析
Logistic回归|Logistic回归|逻辑回归|C|模型-Logistic回归
时间序列|时间序列|ARIMA|指数平滑|C|预测与时间序列
灰色预测|灰色预测|GM(1,1)|C|灰色预测GM
插值与拟合|插值|曲线拟合|样条|C|插值与拟合
主成分分析|主成分分析|PCA|C|主成分分析PCA
聚类分析|聚类分析|K-means|K均值|系统聚类|C|聚类分析
支持向量机|支持向量机|SVM|C|支持向量机SVM
随机森林|随机森林|Random Forest|C|模型-随机森林
决策树|决策树|CART|C|模型-决策树
神经网络|神经网络|BP网络|LSTM|RBF网络|C|神经网络
相关分析|相关分析|Pearson|Spearman|C|模型-相关分析
层次分析法|层次分析法|AHP|D|AHP层次分析法
熵权法|熵权法|熵值法|D|熵权法
TOPSIS|TOPSIS|优劣解距离|D|TOPSIS优劣解距离法
灰色关联分析|灰色关联|D|灰色关联分析
模糊综合评价|模糊综合评价|模糊评价|D|模糊综合评价
综合评价模型|综合评价|评价指标体系|综合评分|D|评价模型 Hub
蒙特卡洛模拟|蒙特卡洛|Monte Carlo|随机模拟|E|蒙特卡洛方法
系统动力学|系统动力学|因果回路|存量流量|E|模型-系统动力学
元胞自动机|元胞自动机|cellular autom|E|元胞自动机
马尔可夫模型|马尔可夫|Markov|MDP|E|马尔可夫决策过程MDP
博弈论|博弈论|博弈模型|支付矩阵|纳什均衡|Nash|F|博弈论基础
演化博弈|演化博弈|复制动态|F|博弈论 Hub"""
MODELS=[]
for row in RAW.splitlines():
    a=row.split("|"); MODELS.append((a[0],"|".join(a[1:-2]),a[-2],a[-1]))

REASON={
"A":"状态变量随时间或空间连续变化，题目给出了可用于守恒、传递或动力学关系的机理条件",
"B":"核心任务是从有限方案中选择、分配或排序，并同时满足目标函数与离散或资源约束",
"C":"结论主要由样本数据、特征关系和样本内外预测或分类性能支撑",
"D":"题目需要把多维指标转换为权重、综合得分与可解释排序",
"E":"对象包含长期反馈、情景假设与政策干预，需要比较多情景演化结果",
"F":"多个主体的收益相互依赖，结论取决于策略组合、信息结构与均衡"}
GUIDE={
"A":["模型建立后绘制物理结构、坐标系或受力示意图","求解后绘制状态量随时间或空间变化曲线","检验部分绘制参数扰动—输出响应曲线并制误差表"],
"B":["问题抽象后绘制网络、路径或调度结构图","算法说明处绘制状态转移或求解流程图","结果部分制方案对比表、资源分配表，并绘制收敛曲线或路线图"],
"C":["数据理解阶段绘制缺失率、分布、箱线图与相关热图","建模阶段制特征与模型选择表","结果阶段绘制预测—真实值、残差、混淆矩阵或特征重要性图并制指标对比表"],
"D":["指标构建处绘制指标层次结构图","权重计算后制权重与一致性检验表","结果阶段绘制排序图、雷达图，并制权重扰动稳健性表"],
"E":["问题机制处绘制因果回路、利益相关者或系统边界图","情景设定处制基准/乐观/悲观参数表","结果阶段绘制多情景演化曲线、空间分布图或政策权衡图"],
"F":["模型建立处制参与者—策略—收益表或支付矩阵","均衡分析处绘制最优反应或策略演化图","检验部分制不同参数与信息结构下的均衡对比表"]}

def digest(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""): h.update(b)
    return h.hexdigest()

def norm(s): return re.sub(r"\n{3,}","\n\n",re.sub(r"[ \t]+"," ",s.replace("\u3000"," ").replace("\x00"," "))).strip()
OCR=None
def init_ocr():
    global OCR
    os.environ["OMP_NUM_THREADS"]="1"
    from rapidocr_onnxruntime import RapidOCR
    OCR=RapidOCR()

def extract_one(arg):
    ps,h=arg; p=Path(ps); dest=CACHE/f"{h}.json"
    if dest.exists(): return "cached"
    try:
        d=pymupdf.open(p); native=[norm(x.get_text("text")) for x in d]
        if sum(map(len,native[:5]))>=500: pages=[{"page":i+1,"text":t} for i,t in enumerate(native)]; mode="embedded-text"
        else:
            import numpy as np
            ids=sorted({i for i in [0,1,int(len(d)*.62),max(0,len(d)-3)] if i<len(d)}); pages=[]
            for i in ids:
                pix=d[i].get_pixmap(matrix=pymupdf.Matrix(1.35,1.35),alpha=False)
                img=np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.height,pix.width,pix.n)
                r,_=OCR(img); pages.append({"page":i+1,"text":norm("\n".join(x[1] for x in (r or [])))})
            mode="selected-page-ocr"
        data={"source":str(p),"sha256":h,"pages_total":len(d),"mode":mode,"pages":pages}
    except Exception as e: data={"source":str(p),"sha256":h,"pages_total":0,"mode":"error","pages":[],"error":repr(e)}
    dest.parent.mkdir(parents=True,exist_ok=True); dest.write_text(json.dumps(data,ensure_ascii=False),encoding="utf-8"); return data["mode"]

def unique_pdfs():
    inv=PROJECT/"Data"/"inventory.json"
    if inv.exists():
        data=json.loads(inv.read_text(encoding="utf-8"))
        return [(Path(x["path"]),x["sha256"]) for x in data["chosen"]],data["duplicates"]
    g={}
    for p in SRC.rglob("*.pdf"): g.setdefault(digest(p),[]).append(p)
    chosen=[]; dup=[]
    for h,ps in g.items():
        q=max(ps,key=lambda p:(("一等奖" in p.name or "二等奖" in p.name),len(p.stem))); chosen.append((q,h))
        dup += [{"duplicate":str(p),"canonical":str(q),"sha256":h} for p in ps if p!=q]
    chosen=sorted(chosen); inv.parent.mkdir(parents=True,exist_ok=True)
    inv.write_text(json.dumps({"chosen":[{"path":str(p),"sha256":h} for p,h in chosen],"duplicates":dup},ensure_ascii=False,indent=2),encoding="utf-8")
    return chosen,dup

def strip_impl(x):
    x=re.sub(r"(?:并|再|然后)?(?:利用|运用|采用|通过)?(?:MATLAB|LINGO|SPSS|PYTHON|EXCEL|R语言|SAS)(?:软件|程序|函数|工具|平台)?(?:编程)?(?:进行)?(?:求解|计算|实现)?","经数学求解",x,flags=re.I)
    x=x.replace("用经数学求解","经数学求解")
    return re.sub(r"(?:代码|程序)(?:见|详见)附录[^。；]*[。；]?","",x)
def sents(t):
    out=[]
    for x in re.split(r"(?<=[。！？；])",t):
        x=strip_impl(re.sub(r"\s+","",x))
        x=re.sub(r"\*{2,}","〔显著性星号〕",x)
        if len(x)>12 and not re.search(r"承诺书|参赛报名号|参赛队员|所属学校|指导教师|从A/B/C/D中选择",x): out.append(x)
    return out
def select(t,pats,n=5):
    z=[]
    for s in sents(t):
        if any(re.search(p,s,re.I) for p in pats):
            s=s[:180]+("…" if len(s)>180 else "")
            if s not in z:z.append(s)
            if len(z)>=n:break
    return z
def abstract(t):
    m=re.search(r"摘\s*要\s*(.*?)(?:关\s*键\s*词|关键词|\n\s*1[\.、 ])",t,re.S); return (m.group(1) if m else t[:3500])[:5000]
def models(t):
    z=[]
    for name,pat,cat,target in MODELS:
        ms=list(re.finditer(pat,t,re.I))
        if ms:z.append({"name":name,"cat":cat,"target":target,"n":len(ms),"pos":ms[0].start()})
    return sorted(z,key=lambda x:(-x["n"],x["pos"]))
def classify(title,t,ms):
    c=Counter()
    for m in ms:c[m["cat"]]+=min(4,1+m["n"]//3)
    pats={"A":"压力|温度|轨迹|运动|物理|工程|流量|传热|扩散|力学","B":"调度|路径|配送|排班|选址|资源分配|组合优化","C":"数据|预测|分类|聚类|识别|特征|拟合|回归","D":"评价|评估|指标体系|排序|权重","E":"政策|可持续|生态|环境|人口|社会|经济|碳排放","F":"对策|竞争|冲突|多方利益|博弈"}
    for k,p in pats.items(): c[k]+=min(3,len(re.findall(p,title+t[:8000])))
    if not c:c["C"]=1
    x=[k for k,_ in c.most_common()]; return x[0],x[1:3]
def title_of(p,pages):
    if p.name in TITLE_OVERRIDES:return TITLE_OVERRIDES[p.name]
    def candidates(text):
        m=re.search(r"摘\s*要",text); pre=text[:m.start()] if m else text
        out=[]
        for line in pre.splitlines():
            x=re.sub(r"\s+","",line).strip("-—_：:《》.。")
            if 4<=len(x)<=48 and not re.search(r"承诺|编号|大学生数学建模|竞赛组委会|参赛队员|指导教师|学校|评阅|打印|日期|签名|第\d+页|我们完全明白|论文版权",x) and not re.fullmatch(r"[\d\W]+",x): out.append(x)
        return out, bool(m)
    for page in pages[:8]:
        cs,has_abstract=candidates(page["text"])
        if has_abstract and cs:return cs[-1]
    for page in pages[:3]:
        cs,_=candidates(page["text"])
        if cs:return min(cs,key=lambda x:(abs(len(x)-16),len(x)))
    x=re.sub(r"^(?:20\d{2})?.*?[A-FＥ]题?","",p.stem); return x[:50] or p.stem+"【标题解析缺失，人工补全】"
def problems(t):
    a=abstract(t); z=[]
    for sentence in sents(a):
        m=re.match(r"(?:针对|对于|在)?问题\s*([一二三四五六七八九十123456789])\s*[：:，,]?",sentence)
        if m:z.append((m.group(1),sentence[m.end():][:420]))
    if not z:z=[(str(i+1),x) for i,x in enumerate(select(a,["建立|求解|确定|预测|评价|分析"],4))]
    return z[:9]
def metadata(p,t):
    y=(re.search(r"20\d{2}",str(p)) or ["年份待核"])[0]; stem=p.stem.upper().replace("Ｅ","E")
    q=next((m.group(1) for pat in [r"20\d{2}.*?([A-F])题?",r"^([A-F])\d{2,3}",r"([A-F])题"] if (m:=re.search(pat,stem))),"题号待核")
    probe=p.name+t[:2000]; award="国家一等奖" if re.search("国家?一等|国赛一等|国一",probe) else "国家二等奖" if re.search("国家?二等|国赛二等|国二",probe) else "奖项待核"
    pid=(re.search(r"([A-F]\d{2,3})",stem) or [f"{y}-{q}-{hashlib.md5(p.name.encode()).hexdigest()[:5]}"])[0]
    return y,q,award,pid
def safe(x):
    x=re.sub(r"[\x00-\x1f\x7f]","",x)
    x=re.sub(r'[<>:"/\\|?*]','',re.sub(r"\s+","",x)).strip(". ")[:28]
    return x or "标题待核"

def make_note(d):
    p=Path(d["source"]); pages=d["pages"]; full="\n".join(f'[PDF第{x["page"]}页]\n{x["text"]}' for x in pages); ti=title_of(p,pages); y,q,award,pid=metadata(p,full)
    ms=models(full); primary,secondary=classify(ti,full,ms); names=[x["name"] for x in ms[:8]] or ["【模型名称解析缺失，人工补全】"]; probs=problems(full)
    solve=select(full,["采用|利用|通过|求解|迭代|优化|拟合|检验"],6); res=select(abstract(full)+full[-5000:],["结果表明|结果显示|得出|求得|最优|最少|结论"],6); ana=select(full,["灵敏度|敏感性|稳健|鲁棒|误差|残差|检验|验证"],5); assumptions=select(full,["模型假设|假设|忽略|不考虑"],4)
    figs=select(full,[r"图\s*\d+|如图"],4); tabs=select(full,[r"表\s*\d+|如下表"],4); miss="【解析缺失，人工补全】"; cat=f"{primary}类 {CATS[primary]}"
    L=["---","type: award-paper-review",f'paper_id: "{pid}"',f'year: "{y}"',f'problem: "{q}"',f'award: "{award}"',f'primary_category: "{cat}"',f'extraction_mode: "{d["mode"]}"',f'source_sha256: "{d["sha256"]}"',"status: machine-reviewed-needs-human-formula-check","tags: [competition/国赛, workflow/优秀论文拆解, area/数学建模]","---",f"# 论文标题：{ti}","## 基础元数据","- 竞赛：全国大学生数学建模竞赛",f"- 年份：{y}",f"- 题号：{q}",f"- 奖项：{award}",f"- 选题归类：{cat}"+(f"；次类别：{'、'.join(c+'类 '+CATS[c] for c in secondary)}" if secondary else ""),f"- 核心关键词：{'、'.join(names[:6])}",f"- 原始来源：{p}",f"- 解析说明：{d['mode']}；总页数 {d['pages_total']}；提取页 {','.join(str(x['page']) for x in pages)}","","## 1 赛题问题提炼"]
    L += [f"- 子问题{i}：{x}" for i,(_,x) in enumerate(probs,1)] or [f"- {miss}未稳定识别子问题边界。"]
    L += ["","## 2 模型整体框架",f"- 模型链：{' → '.join(names)}","- 逻辑递进：题意与数据/机理抽象 → 分问建模 → 求解 → 结果检验 → 回答题目。","- 有效模型假设："]
    L += ([f"  - {x}" for x in assumptions] if assumptions else [f"  - {miss}未在提取页稳定定位完整假设段。"]) + ["- 符号说明：","","| 符号 | 含义 | 单位/取值域 |","|---|---|---|",f"| {miss} | 原文符号表或公式未能可靠转换 | 待人工核对 |","","## 3 各子问题建模思路【核心模块】"]
    for i,(_,x) in enumerate(probs or [("1",miss)],1):
        lm=[m["name"] for m in models(x)[:4]] or names[:2]; anchor=next((r["page"] for r in pages if x[:8] and x[:8] in r["text"]),pages[0]["page"] if pages else "待核")
        L.append(f"- 子问题{i}：选用模型为{'、'.join(lm)}；建模逻辑为{x}；模型选择理由：{REASON[primary]}；核心数学公式：{miss}；证据位置：PDF第{anchor}页附近。")
    L += ["","## 4 求解与计算思路"]+( [f"- {x}" for x in solve] if solve else [f"- {miss}未稳定定位求解说明。"] )+["- 仅保留数学处理与求解路线，已跳过代码、软件函数和编程步骤。","","## 5 结果与分析","- 核心结论："]
    L += ([f"  - {x}" for x in res] if res else [f"  - {miss}未稳定识别定量结论。"])+["- 分析工作："]+([f"  - {x}" for x in ana] if ana else ["  - 可解析文本中未定位到明确的灵敏度、稳健性或误差分析；不等于原文一定缺失。"])
    L += ["","## 6 模型评价","- 模型优点：",("  - 摘要按子问题交代方法与结果，模型链与任务对应较清楚。" if len(probs)>=2 else "  - 当前抽取范围不足以可靠归纳全部优点。"),f"  - 组合使用{'、'.join(names[:4])}处理题目。","- 模型存在不足与改进方向："]
    if d["mode"]=="selected-page-ocr":L.append("  - 扫描版仅对代表页 OCR，公式、符号和中间论证链需人工逐页复核。")
    if not ana:L.append("  - 建议补充参数扰动、样本外验证或误差分解。")
    L += ["  - 检查假设、变量、目标、约束、输出和结论是否逐项闭环。","","## 7 论文复用&写作亮点（知识库专用）",f"- 适用场景：以{CATS[primary]}为主的问题；数据结构、变量类型或机制不同不得直接套用。","- 结构亮点：摘要宜按“子问题—模型—求解—关键结果”，正文宜按“问题分析—假设与符号—建模—求解—检验—评价”闭环。","- 原文图表线索："]
    L += ([f"  - {x}" for x in figs] if figs else ["  - 提取页未稳定识别图题，需核对原文。"])+["- 原文表格线索："]+([f"  - {x}" for x in tabs] if tabs else ["  - 提取页未稳定识别表题，需核对原文。"])+["- 建议的图表落点："]+[f"  - {x}" for x in GUIDE[primary]]+["- 客观缺口：所有“解析缺失”项必须回到原 PDF 补全，严禁反推或编造。","","## 8 双向链接标签"]
    L += [f"[[{m['target']}|模型-{m['name']}]]" for m in ms[:8]] or ["[[模型-待人工补全]]"]
    L += [f"[[论文模型分类-{primary}类{CATS[primary]}]]",f"[[赛题-国赛{y}第{q}题]]","[[论文写作 Hub|写作-数模论文模板]]",""]
    return "\n".join(L),{"title":ti,"year":y,"problem":q,"award":award,"paper_id":pid,"primary":primary,"secondary":secondary,"models":names,"source":str(p),"mode":d["mode"],"sha256":d["sha256"]}

def extract(workers):
    chosen,dup=unique_pdfs(); CACHE.mkdir(parents=True,exist_ok=True); counts=Counter()
    pending=[(p,h) for p,h in chosen if not (CACHE/f"{h}.json").exists()]
    counts["cached"]=len(chosen)-len(pending); print(f"[cached/{len(chosen)}] {counts['cached']}",flush=True)
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers,initializer=init_ocr) as ex:
        jobs=[ex.submit(extract_one,(str(p),h)) for p,h in pending]
        for i,job in enumerate(concurrent.futures.as_completed(jobs),1):
            mode=job.result(); counts[mode]+=1; print(f"[{i}/{len(pending)}] {mode}",flush=True)
    (PROJECT/"Data"/"duplicates.json").write_text(json.dumps(dup,ensure_ascii=False,indent=2),encoding="utf-8"); print(dict(counts))
def build():
    OUT.mkdir(parents=True,exist_ok=True)
    expected=VAULT/"04-Research"/"04-竞赛真题研究"/"03-优秀获奖论文拆解"/"批量标准化拆解"
    if OUT.resolve()!=expected.resolve(): raise RuntimeError("Refusing to clean unexpected output directory")
    for old in OUT.rglob("G-*.md"): old.unlink()
    [ (OUT/f"{c}类-{n}").mkdir(exist_ok=True) for c,n in CATS.items() ]; recs=[]; used_stems=set()
    for f in sorted(CACHE.glob("*.json")):
        note,r=make_note(json.loads(f.read_text(encoding="utf-8"))); short={"国家一等奖":"国一","国家二等奖":"国二"}.get(r["award"],"奖项待核"); out=OUT/f"{r['primary']}类-{CATS[r['primary']]}"/f"G-{r['year']}-{r['problem']}-{short}-{safe(r['title'])}.md"
        if out.stem.lower() in used_stems:out=out.with_stem(out.stem+"-"+r["paper_id"])
        used_stems.add(out.stem.lower())
        out.write_text(note,encoding="utf-8"); r["note"]=str(out); recs.append(r)
    recs.sort(key=lambda r:(r["primary"],r["year"],r["problem"],r["title"])); counts=Counter(r["primary"] for r in recs)
    idx=["# 优秀论文模型分类索引","","分类依据是主要模型机制，不等同于赛题字母；次类别记录在单篇元数据中。",""]
    for c,n in CATS.items():
        idx += [f"## {c}类 {n}（{counts[c]}篇）","","| 年份 | 题号 | 奖项 | 论文 | 主要模型 |","|---|---|---|---|---|"]
        for r in [x for x in recs if x["primary"]==c]:
            rel=Path(r["note"]).relative_to(VAULT).with_suffix("").as_posix(); idx.append(f"| {r['year']} | {r['problem']} | {r['award']} | [[{rel}|{r['title']}]] | {'、'.join(r['models'][:5])} |")
        idx.append("")
    (OUT/"优秀论文模型分类索引.md").write_text("\n".join(idx),encoding="utf-8")
    for c,n in CATS.items():
        hub=[f"# 论文模型分类-{c}类{n}","",f"- 分类定义：以{n}为论文主要建模机制。","- 分类原则：按主导数学机制归类，赛题字母仅作元数据，不直接决定类别。",f"- 总篇数：{counts[c]}","",f"## {c}类论文","",f"完整表格见 [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/批量标准化拆解/优秀论文模型分类索引#{c}类 {n}（{counts[c]}篇）|分类索引]]。",""]
        for r in [x for x in recs if x["primary"]==c]:
            rel=Path(r["note"]).relative_to(VAULT).with_suffix("").as_posix(); hub.append(f"- [[{rel}|{r['title']}]]：{'、'.join(r['models'][:5])}")
        (OUT/f"论文模型分类-{c}类{n}.md").write_text("\n".join(hub)+"\n",encoding="utf-8")
    nodes=OUT/"知识节点"; model_dir=nodes/"模型"; problem_dir=nodes/"赛题"; model_dir.mkdir(parents=True,exist_ok=True); problem_dir.mkdir(parents=True,exist_ok=True)
    for old in nodes.rglob("*.md"): old.unlink()
    existing={p.stem for p in VAULT.rglob("*.md") if nodes not in p.parents}
    target_for={name:target for name,_,_,target in MODELS}; by_model={}
    for r in recs:
        for name in r["models"]:
            target=target_for.get(name,"模型-待人工补全"); by_model.setdefault(target,[]).append(r)
    for target,items in by_model.items():
        if target in existing:continue
        lines=[f"# {target}","","- 节点类型：模型/算法","- 说明：由优秀论文批量拆解自动建立的反向索引；具体定义、公式与适用条件需进入单篇笔记和原 PDF 复核。","","## 相关论文",""]
        for r in items:
            rel=Path(r["note"]).relative_to(VAULT).with_suffix("").as_posix(); lines.append(f"- [[{rel}|{r['title']}]]")
        (model_dir/f"{target}.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    by_problem={}
    for r in recs:by_problem.setdefault(f"赛题-国赛{r['year']}第{r['problem']}题",[]).append(r)
    for target,items in by_problem.items():
        if target in existing:continue
        lines=[f"# {target}","","- 节点类型：竞赛赛题","- 说明：按论文元数据自动汇集；题号待核节点必须回到原文件名或赛题资料核实。","","## 相关优秀论文",""]
        for r in items:
            rel=Path(r["note"]).relative_to(VAULT).with_suffix("").as_posix(); lines.append(f"- [[{rel}|{r['title']}]]")
        (problem_dir/f"{target}.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    dup=json.loads((PROJECT/"Data"/"duplicates.json").read_text(encoding="utf-8")); ocr=sum(r["mode"]=="selected-page-ocr" for r in recs); pending=sum(r["award"]=="奖项待核" for r in recs); qpending=sum(r["problem"]=="题号待核" for r in recs); mpending=sum(r["models"][0].startswith("【") for r in recs)
    rep=["# 优秀论文批量处理汇总报告","",f"- 原始 PDF：{len(recs)+len(dup)} 份",f"- 去重后论文：{len(recs)} 篇",f"- 重复文件：{len(dup)} 份",f"- 扫描版代表页 OCR：{ocr} 篇",f"- 奖项待核：{pending} 篇","- 公式与符号：全部需对照原 PDF 人工复核","- 未处理：RAR 32 份、ZIP 4 份、DOC 6 份、DOCX 3 份","","## 分类统计","","| 类别 | 篇数 |","|---|---:|"]+[f"| {c}类 {n} | {counts[c]} |" for c,n in CATS.items()]+["","## 输出文件",""]+[f"- {Path(r['note']).name}" for r in recs]+["","## 缺失内容统计","",f"- 公式与符号需人工复核：{len(recs)} 篇。",f"- 扫描版中间页未逐页 OCR：{ocr} 篇。",f"- 奖项待核：{pending} 篇。",f"- 题号待核：{qpending} 篇。",f"- 未稳定识别具体模型名称：{mpending} 篇。","- 所有缺失项均已保留原始来源路径和人工补全标记。",""]
    (OUT/"处理汇总报告.md").write_text("\n".join(rep),encoding="utf-8"); (PROJECT/"Data"/"manifest.json").write_text(json.dumps(recs,ensure_ascii=False,indent=2),encoding="utf-8"); print(json.dumps({"notes":len(recs),"counts":dict(counts),"out":str(OUT)},ensure_ascii=False))
def main():
    a=argparse.ArgumentParser(); a.add_argument("action",choices=["extract","build","all"]); a.add_argument("--workers",type=int,default=4); x=a.parse_args()
    if x.action in ("extract","all"):extract(x.workers)
    if x.action in ("build","all"):build()
if __name__=="__main__":main()
