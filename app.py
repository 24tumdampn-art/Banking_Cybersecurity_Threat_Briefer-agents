import streamlit as st
from dotenv import load_dotenv
from agents.researcher import run_researcher
from agents.analyst import run_analyst
from agents.writer import run_writer
from agents.judge import run_judge
from agents.compliance import run_compliance_check

load_dotenv()

st.set_page_config(
    page_title="Banking Threat Briefer",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS + Animations ──────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@400;600;700&display=swap');

/* Animated background */
@keyframes bgMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Scanning line animation */
@keyframes scan {
    0% { transform: translateY(-100%); opacity: 0; }
    10% { opacity: 1; }
    90% { opacity: 1; }
    100% { transform: translateY(100vh); opacity: 0; }
}

/* Pulse animation */
@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.7; transform: scale(1.05); }
}

/* Glow animation */
@keyframes glow {
    0%, 100% { box-shadow: 0 0 10px rgba(0,212,255,0.3); }
    50% { box-shadow: 0 0 30px rgba(0,212,255,0.7), 0 0 60px rgba(0,212,255,0.3); }
}

/* Typing cursor blink */
@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
}

/* Float animation */
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
}

/* Fade in up */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Slide in left */
@keyframes slideInLeft {
    from { opacity: 0; transform: translateX(-30px); }
    to { opacity: 1; transform: translateX(0); }
}

/* Rotate */
@keyframes rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

/* Matrix rain effect */
@keyframes matrixFall {
    0% { transform: translateY(-100%); opacity: 1; }
    100% { transform: translateY(100vh); opacity: 0; }
}

/* Progress bar fill */
@keyframes fillBar {
    from { width: 0%; }
    to { width: var(--target-width); }
}

/* Flicker */
@keyframes flicker {
    0%, 95%, 100% { opacity: 1; }
    96% { opacity: 0.4; }
    97% { opacity: 1; }
    98% { opacity: 0.2; }
    99% { opacity: 1; }
}

/* Number count up */
@keyframes countUp {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Main app */
.stApp {
    background: #050d1a;
    font-family: 'Rajdhani', sans-serif;
}

/* Scanning line overlay */
.scan-line {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, transparent, #00d4ff, transparent);
    animation: scan 4s linear infinite;
    z-index: 999;
    pointer-events: none;
}

/* Header */
.main-header {
    text-align: center;
    padding: 2.5rem 0 1.5rem 0;
    animation: fadeInUp 0.8s ease forwards;
}

.header-icon {
    font-size: 56px;
    animation: float 3s ease-in-out infinite;
    display: inline-block;
}

.header-title {
    font-size: 2.8rem;
    font-weight: 800;
    background: linear-gradient(135deg, #00d4ff 0%, #ffffff 50%, #00d4ff 100%);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: bgMove 4s linear infinite, flicker 8s infinite;
    letter-spacing: 2px;
    margin: 0;
    font-family: 'Rajdhani', sans-serif;
}

.header-subtitle {
    color: #1e4a6b;
    font-size: 12px;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-top: 8px;
    font-family: 'Share Tech Mono', monospace;
    animation: fadeInUp 0.8s ease 0.3s both;
}

/* Terminal typing effect */
.terminal-text {
    font-family: 'Share Tech Mono', monospace;
    color: #00d4ff;
    font-size: 13px;
    background: rgba(0, 212, 255, 0.05);
    border: 1px solid rgba(0, 212, 255, 0.2);
    border-radius: 8px;
    padding: 12px 16px;
    margin: 1rem 0;
}

.terminal-text::after {
    content: '█';
    animation: blink 1s infinite;
    color: #00d4ff;
}

/* Agent pipeline */
.pipeline-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
    padding: 1.5rem 0;
    animation: fadeInUp 0.8s ease 0.5s both;
}

.pipeline-node {
    background: rgba(0,212,255,0.06);
    border: 1px solid rgba(0,212,255,0.25);
    border-radius: 10px;
    padding: 10px 18px;
    font-size: 13px;
    color: #00d4ff;
    font-family: 'Share Tech Mono', monospace;
    animation: glow 3s ease-in-out infinite;
    transition: all 0.3s ease;
    cursor: default;
}

.pipeline-node:hover {
    background: rgba(0,212,255,0.15);
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(0,212,255,0.3);
}

.pipeline-arrow {
    color: #1e3a5f;
    font-size: 18px;
    animation: pulse 2s ease-in-out infinite;
}

/* Run button */
.stButton > button {
    background: linear-gradient(135deg, #003d5c, #006699, #00d4ff) !important;
    background-size: 200% auto !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    border: 1px solid rgba(0,212,255,0.4) !important;
    border-radius: 12px !important;
    padding: 14px 28px !important;
    width: 100% !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
    transition: all 0.4s ease !important;
    animation: glow 2s ease-in-out infinite !important;
    font-family: 'Share Tech Mono', monospace !important;
}

.stButton > button:hover {
    background-position: right center !important;
    transform: translateY(-3px) !important;
    box-shadow: 0 15px 40px rgba(0,212,255,0.5) !important;
    letter-spacing: 4px !important;
}

/* Status box */
[data-testid="stStatus"] {
    background: rgba(0,212,255,0.03) !important;
    border: 1px solid rgba(0,212,255,0.2) !important;
    border-radius: 14px !important;
    font-family: 'Share Tech Mono', monospace !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(0,212,255,0.03);
    border-radius: 12px;
    padding: 4px;
    border: 1px solid rgba(0,212,255,0.1);
}

.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    color: #1e4a6b;
    font-weight: 700;
    font-size: 14px;
    padding: 10px 24px;
    font-family: 'Rajdhani', sans-serif;
    letter-spacing: 1px;
    transition: all 0.3s ease;
}

.stTabs [aria-selected="true"] {
    background: rgba(0,212,255,0.12) !important;
    color: #00d4ff !important;
    box-shadow: 0 0 15px rgba(0,212,255,0.2) !important;
}

/* Score cards */
.score-card {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px;
    padding: 24px 20px;
    text-align: center;
    animation: fadeInUp 0.6s ease forwards;
    transition: all 0.3s ease;
    height: 100%;
}

.score-card:hover {
    transform: translateY(-5px);
    border-color: rgba(0,212,255,0.3);
    box-shadow: 0 10px 30px rgba(0,212,255,0.1);
}

.score-number {
    font-size: 42px;
    font-weight: 800;
    font-family: 'Share Tech Mono', monospace;
    animation: countUp 0.8s ease forwards;
}

/* Compliance items */
.compliance-item-risk {
    background: rgba(239,68,68,0.04);
    border-left: 3px solid #ef4444;
    border-radius: 0 10px 10px 0;
    padding: 10px 14px;
    margin-bottom: 8px;
    color: #fca5a5;
    font-size: 13px;
    animation: slideInLeft 0.4s ease forwards;
    transition: all 0.3s ease;
}

.compliance-item-risk:hover {
    background: rgba(239,68,68,0.1);
    transform: translateX(4px);
}

.compliance-item-safe {
    background: rgba(16,185,129,0.04);
    border-left: 3px solid #10b981;
    border-radius: 0 10px 10px 0;
    padding: 10px 14px;
    margin-bottom: 8px;
    color: #6ee7b7;
    font-size: 13px;
    animation: slideInLeft 0.4s ease forwards;
    transition: all 0.3s ease;
}

.compliance-item-safe:hover {
    background: rgba(16,185,129,0.1);
    transform: translateX(4px);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: rgba(5, 13, 26, 0.98) !important;
    border-right: 1px solid rgba(0,212,255,0.1) !important;
}

/* Divider */
hr { border-color: rgba(0,212,255,0.08) !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #050d1a; }
::-webkit-scrollbar-thumb { background: #00d4ff33; border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: #00d4ff66; }

/* Grade badge */
.grade-badge {
    display: inline-block;
    font-size: 64px;
    font-weight: 800;
    font-family: 'Share Tech Mono', monospace;
    animation: pulse 2s ease-in-out infinite, countUp 0.8s ease forwards;
}

/* Briefing content */
.briefing-container {
    background: rgba(255,255,255,0.01);
    border: 1px solid rgba(0,212,255,0.1);
    border-radius: 16px;
    padding: 32px;
    margin-top: 1rem;
    animation: fadeInUp 0.6s ease forwards;
    font-family: 'Rajdhani', sans-serif;
    font-size: 15px;
    line-height: 1.8;
}

/* Priority action */
.priority-box {
    background: rgba(239,68,68,0.06);
    border: 1px solid rgba(239,68,68,0.25);
    border-radius: 12px;
    padding: 16px 20px;
    margin: 1rem 0;
    animation: pulse 3s ease-in-out infinite;
}

/* Score banner */
.score-banner {
    background: rgba(255,255,255,0.01);
    border: 1px solid rgba(0,212,255,0.12);
    border-radius: 18px;
    padding: 28px 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
    gap: 16px;
    animation: fadeInUp 0.6s ease forwards;
}
</style>

<!-- Scanning line -->
<div class="scan-line"></div>
""", unsafe_allow_html=True)


# ── Header ────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <div class="header-icon">🏦</div>
    <h1 class="header-title">Banking Threat Briefer</h1>
    <p class="header-subtitle">
        Multi-Agent AI System · Real-Time Intelligence · RBI / PCI-DSS Compliance
    </p>
</div>
""", unsafe_allow_html=True)

# Terminal text
st.markdown("""
<div class="terminal-text">
    > SYSTEM INITIALIZED · 5 AGENTS READY · TAVILY SEARCH CONNECTED · GROQ LLM ONLINE
</div>
""", unsafe_allow_html=True)

st.divider()

# ── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:1rem 0 0.5rem 0; 
                animation: fadeInUp 0.6s ease forwards;">
        <div style="font-size:28px; animation: float 3s ease-in-out infinite; 
                    display:inline-block;">🛡️</div>
        <div style="color:#00d4ff; font-size:13px; font-weight:700;
                    letter-spacing:3px; text-transform:uppercase;
                    font-family:'Share Tech Mono',monospace; margin-top:8px;">
            Agent Pipeline
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    agents_info = [
        ("🔍", "Threat Researcher", "Tavily live search", "0.1s"),
        ("🛡️", "Vulnerability Analyst", "CVE identification", "0.2s"),
        ("📋", "Briefing Writer", "Report generation", "0.3s"),
        ("⚖️", "LLM-as-Judge", "Quality scoring", "0.4s"),
        ("✅", "Compliance Checker", "RBI + PCI-DSS", "0.5s"),
    ]

    for icon, name, desc, delay in agents_info:
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:12px;
                    padding:12px 8px;
                    border-bottom:1px solid rgba(0,212,255,0.06);
                    animation: slideInLeft 0.5s ease {delay} both;
                    transition: all 0.3s ease;
                    cursor:default;"
             onmouseover="this.style.background='rgba(0,212,255,0.05)'"
             onmouseout="this.style.background='transparent'">
            <span style="font-size:22px;">{icon}</span>
            <div>
                <div style="color:#c8d8e8; font-size:13px; font-weight:700;
                            font-family:'Rajdhani',sans-serif; letter-spacing:1px;">
                    {name}
                </div>
                <div style="color:#1e4a6b; font-size:11px;
                            font-family:'Share Tech Mono',monospace;">
                    {desc}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style="padding:14px; background:rgba(0,212,255,0.04);
                border:1px solid rgba(0,212,255,0.12);
                border-radius:12px; animation:glow 3s ease-in-out infinite;">
        <div style="color:#00d4ff; font-size:11px; font-weight:700;
                    letter-spacing:2px; text-transform:uppercase;
                    font-family:'Share Tech Mono',monospace; margin-bottom:10px;">
            ⚡ Tech Stack
        </div>
        <div style="color:#1e4a6b; font-size:12px; line-height:2.2;
                    font-family:'Share Tech Mono',monospace;">
            🐍 Python 3.12<br>
            🌐 Streamlit<br>
            🤖 Groq · Llama 3.3 70B<br>
            🔍 Tavily Search API<br>
            🚀 Railway Deployment
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── Pipeline Visual ───────────────────────────────────────
st.markdown("""
<div class="pipeline-container">
    <div class="pipeline-node">🔍 Researcher</div>
    <div class="pipeline-arrow">⟶</div>
    <div class="pipeline-node">🛡️ Analyst</div>
    <div class="pipeline-arrow">⟶</div>
    <div class="pipeline-node">📋 Writer</div>
    <div class="pipeline-arrow">⟶</div>
    <div class="pipeline-node">⚖️ Judge</div>
    <div class="pipeline-arrow">⟶</div>
    <div class="pipeline-node">✅ Compliance</div>
</div>
""", unsafe_allow_html=True)


# ── Run Button ────────────────────────────────────────────
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    run_clicked = st.button(
        "⚡ INITIATE THREAT ANALYSIS",
        use_container_width=True
    )

st.divider()


# ── Run Agents ────────────────────────────────────────────
if run_clicked:

    with st.status("🤖 AGENTS ONLINE — ANALYZING...", expanded=True) as status:
        st.write("🔍 **Agent 1 — Threat Researcher** · Searching live banking threats via Tavily...")
        research = run_researcher()
        st.write("✅ Agent 1 complete — threat data collected")

        st.write("🛡️ **Agent 2 — Vulnerability Analyst** · Identifying CVEs and attack vectors...")
        vulns = run_analyst(research)
        st.write("✅ Agent 2 complete — vulnerabilities mapped")

        st.write("📋 **Agent 3 — Briefing Writer** · Compiling professional report...")
        briefing = run_writer(research, vulns)
        st.write("✅ Agent 3 complete — briefing generated")

        st.write("⚖️ **Agent 4 — LLM Judge** · Evaluating report quality...")
        scores = run_judge(briefing)
        st.write("✅ Agent 4 complete — quality scored")

        st.write("✅ **Agent 5 — Compliance Checker** · Running RBI + PCI-DSS assessment...")
        compliance = run_compliance_check(briefing)
        st.write("✅ Agent 5 complete — compliance mapped")

        status.update(
            label="✅ ALL AGENTS COMPLETE — BRIEFING READY",
            state="complete"
        )

    st.divider()

    # ── Score Banner ──────────────────────────────────────
    overall = scores.get("overall", 0)
    grade = scores.get("grade", "N/A")
    grade_color = {
        "A": "#10b981", "B": "#00d4ff",
        "C": "#f59e0b", "D": "#ef4444"
    }.get(grade, "#64748b")

    st.markdown(f"""
    <div class="score-banner">
        <div>
            <div style="color:#1e4a6b; font-size:11px; letter-spacing:3px;
                        text-transform:uppercase; font-family:'Share Tech Mono',monospace;">
                ▶ ANALYSIS COMPLETE
            </div>
            <div style="color:#e2e8f0; font-size:22px; font-weight:700;
                        margin:8px 0 4px 0; font-family:'Rajdhani',sans-serif;">
                Banking Sector — Real-Time Threat Briefing
            </div>
            <div style="color:#1e4a6b; font-size:13px;
                        font-family:'Share Tech Mono',monospace;">
                {scores.get('feedback', '')}
            </div>
        </div>
        <div style="text-align:center;">
            <div class="grade-badge" style="color:{grade_color};">{grade}</div>
            <div style="color:#1e4a6b; font-size:12px;
                        font-family:'Share Tech Mono',monospace;">
                {overall}/10 SCORE
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Tabs ──────────────────────────────────────────────
    tab1, tab2, tab3 = st.tabs([
        "📋  Threat Briefing",
        "⚖️  Judge Scores",
        "📜  Compliance Report"
    ])

    with tab1:
        st.markdown(f"""
        <div class="briefing-container">
            {briefing.replace(chr(10), '<br>')}
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown("<br>", unsafe_allow_html=True)

        metrics = [
            ("🎯", "Accuracy", "accuracy",
             "Real & current threats"),
            ("📊", "Completeness", "completeness",
             "Full coverage"),
            ("⚡", "Actionability", "actionability",
             "Practical steps"),
            ("🏦", "Banking Relevance", "banking_relevance",
             "Sector specific"),
        ]

        cols = st.columns(4)
        for i, (icon, label, key, desc) in enumerate(metrics):
            score = scores.get(key, 0)
            pct = score * 10
            color = (
                "#10b981" if score >= 8
                else "#f59e0b" if score >= 6
                else "#ef4444"
            )
            with cols[i]:
                st.markdown(f"""
                <div class="score-card" style="animation-delay:{i*0.15}s">
                    <div style="font-size:28px; margin-bottom:8px;">{icon}</div>
                    <div class="score-number" style="color:{color};">
                        {score}/10
                    </div>
                    <div style="color:#c8d8e8; font-size:14px; font-weight:700;
                                margin:8px 0 4px 0; font-family:'Rajdhani',sans-serif;
                                letter-spacing:1px;">
                        {label}
                    </div>
                    <div style="color:#1e4a6b; font-size:11px; margin-bottom:14px;
                                font-family:'Share Tech Mono',monospace;">
                        {desc}
                    </div>
                    <div style="background:rgba(255,255,255,0.04);
                                border-radius:99px; height:6px;">
                        <div style="width:{pct}%; height:6px; border-radius:99px;
                                    background:{color};
                                    transition: width 1.5s ease;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div style="background:rgba(0,212,255,0.04);
                    border:1px solid rgba(0,212,255,0.15);
                    border-radius:12px; padding:18px 24px; text-align:center;
                    animation: glow 3s ease-in-out infinite;">
            <span style="color:#1e4a6b; font-family:'Share Tech Mono',monospace;
                         font-size:12px;">JUDGE FEEDBACK · </span>
            <span style="color:#94a3b8; font-family:'Rajdhani',sans-serif;
                         font-size:15px;">
                {scores.get('feedback', '')}
            </span>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown("<br>", unsafe_allow_html=True)

        rbi = compliance.get("rbi", {})
        pci = compliance.get("pci_dss", {})
        rbi_score = rbi.get("score", 0)
        pci_score = pci.get("score", 0)
        rbi_color = (
            "#10b981" if rbi_score >= 70
            else "#f59e0b" if rbi_score >= 50
            else "#ef4444"
        )
        pci_color = (
            "#10b981" if pci_score >= 70
            else "#f59e0b" if pci_score >= 50
            else "#ef4444"
        )

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="score-card">
                <div style="font-size:48px; font-weight:800; color:{rbi_color};
                            font-family:'Share Tech Mono',monospace;
                            animation: countUp 0.8s ease forwards;">
                    {rbi_score}
                </div>
                <div style="color:#1e4a6b; font-size:11px;
                            font-family:'Share Tech Mono',monospace;">
                    / 100
                </div>
                <div style="color:#c8d8e8; font-size:16px; font-weight:700;
                            margin:10px 0 4px 0; font-family:'Rajdhani',sans-serif;">
                    🏛️ RBI Compliance
                </div>
                <div style="background:rgba(255,255,255,0.04);
                            border-radius:99px; height:8px; margin-top:14px;">
                    <div style="width:{rbi_score}%; height:8px; border-radius:99px;
                                background:{rbi_color};"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="score-card">
                <div style="font-size:48px; font-weight:800; color:{pci_color};
                            font-family:'Share Tech Mono',monospace;
                            animation: countUp 0.8s ease forwards;">
                    {pci_score}
                </div>
                <div style="color:#1e4a6b; font-size:11px;
                            font-family:'Share Tech Mono',monospace;">
                    / 100
                </div>
                <div style="color:#c8d8e8; font-size:16px; font-weight:700;
                            margin:10px 0 4px 0; font-family:'Rajdhani',sans-serif;">
                    💳 PCI-DSS Compliance
                </div>
                <div style="background:rgba(255,255,255,0.04);
                            border-radius:99px; height:8px; margin-top:14px;">
                    <div style="width:{pci_score}%; height:8px; border-radius:99px;
                                background:{pci_color};"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(f"""
        <div class="priority-box">
            <span style="color:#fca5a5; font-weight:700;
                         font-family:'Share Tech Mono',monospace;
                         font-size:12px; letter-spacing:2px;">
                🚨 PRIORITY ACTION ·
            </span>
            <span style="color:#94a3b8; font-family:'Rajdhani',sans-serif;
                         font-size:15px;">
                {compliance.get('priority_action', '')}
            </span>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div style="color:#00d4ff; font-size:14px; font-weight:700;
                        letter-spacing:2px; text-transform:uppercase;
                        font-family:'Share Tech Mono',monospace;
                        margin-bottom:12px;">
                🏛️ RBI Controls
            </div>
            """, unsafe_allow_html=True)
            for item in rbi.get("at_risk", []):
                st.markdown(f"""
                <div class="compliance-item-risk">🔴 {item}</div>
                """, unsafe_allow_html=True)
            for item in rbi.get("compliant", []):
                st.markdown(f"""
                <div class="compliance-item-safe">🟢 {item}</div>
                """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div style="color:#00d4ff; font-size:14px; font-weight:700;
                        letter-spacing:2px; text-transform:uppercase;
                        font-family:'Share Tech Mono',monospace;
                        margin-bottom:12px;">
                💳 PCI-DSS Controls
            </div>
            """, unsafe_allow_html=True)
            for item in pci.get("at_risk", []):
                st.markdown(f"""
                <div class="compliance-item-risk">🔴 {item}</div>
                """, unsafe_allow_html=True)
            for item in pci.get("compliant", []):
                st.markdown(f"""
                <div class="compliance-item-safe">🟢 {item}</div>
                """, unsafe_allow_html=True)

    # Footer
    st.divider()
    st.markdown("""
    <div style="text-align:center; padding:1rem 0;">
        <div style="color:#0a1f35; font-size:11px; letter-spacing:3px;
                    text-transform:uppercase; font-family:'Share Tech Mono',monospace;">
            Banking Threat Briefer · Multi-Agent AI · 
            Streamlit + Groq + Tavily · All Rights Reserved
        </div>
    </div>
    """, unsafe_allow_html=True)
