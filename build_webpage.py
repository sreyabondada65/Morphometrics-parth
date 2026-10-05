#!/usr/bin/env python3
"""
Web Page Generator for Scorpion Morphometrics Analysis Dashboard
"""
import json

with open("/Users/sreyabondada/Downloads/Parth's workspace/Parth morphometrics/scorpions_morphometrics.json", "r") as f:
    raw_data = json.load(f)

json_data_str = json.dumps(raw_data)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scorpion Morphometrics</title>
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {{
            --bg-primary: #0b0f19;
            --bg-secondary: #131b2e;
            --bg-card: #1a233a;
            --bg-card-hover: #222d4a;
            --border-color: #2a3656;
            --border-highlight: #3b82f6;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --text-dim: #64748b;
            --accent-primary: #38bdf8;
            --accent-secondary: #818cf8;
            --accent-tertiary: #f43f5e;
            --accent-emerald: #10b981;
            --accent-amber: #f59e0b;
            --accent-purple: #c084fc;
            --shadow-sm: 0 2px 4px rgba(0,0,0,0.3);
            --shadow-md: 0 4px 12px rgba(0,0,0,0.4);
            --shadow-lg: 0 10px 25px -5px rgba(0,0,0,0.5);
            --radius-sm: 8px;
            --radius-md: 12px;
            --radius-lg: 16px;
            --font-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: var(--font-sans);
            background-color: var(--bg-primary);
            color: var(--text-main);
            min-height: 100vh;
            line-height: 1.6;
            overflow-x: hidden;
        }}

        /* Header & Navigation */
        header {{
            background: linear-gradient(180deg, rgba(19, 27, 46, 0.95) 0%, rgba(11, 15, 25, 0.9) 100%);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-color);
            position: sticky;
            top: 0;
            z-index: 100;
            padding: 1rem 2rem;
        }}

        .header-container {{
            max-width: 1600px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
        }}

        .logo-area {{
            display: flex;
            align-items: center;
            gap: 0.85rem;
        }}

        .logo-badge {{
            background: linear-gradient(135deg, #38bdf8, #818cf8);
            width: 44px;
            height: 44px;
            border-radius: var(--radius-md);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            box-shadow: 0 0 15px rgba(56, 189, 248, 0.4);
        }}

        .title-group h1 {{
            font-size: 1.4rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            background: linear-gradient(to right, #ffffff, #94a3b8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .title-group p {{
            font-size: 0.8rem;
            color: var(--text-muted);
            font-weight: 500;
        }}

        /* Navigation Tabs */
        .nav-tabs {{
            display: flex;
            gap: 0.4rem;
            background: var(--bg-primary);
            padding: 0.35rem;
            border-radius: var(--radius-md);
            border: 1px solid var(--border-color);
            overflow-x: auto;
        }}

        .nav-btn {{
            background: transparent;
            border: none;
            color: var(--text-muted);
            padding: 0.6rem 1.1rem;
            border-radius: var(--radius-sm);
            font-family: var(--font-sans);
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            white-space: nowrap;
        }}

        .nav-btn:hover {{
            color: var(--text-main);
            background: rgba(255, 255, 255, 0.05);
        }}

        .nav-btn.active {{
            background: linear-gradient(135deg, #2563eb, #3b82f6);
            color: #ffffff;
            box-shadow: 0 2px 8px rgba(37, 99, 235, 0.4);
        }}

        /* Main Container */
        main {{
            max-width: 1600px;
            margin: 0 auto;
            padding: 2rem;
        }}

        .tab-content {{
            display: none;
            animation: fadeIn 0.3s ease;
        }}

        .tab-content.active {{
            display: block;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* Metric KPI Cards Grid */
        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1.25rem;
            margin-bottom: 2rem;
        }}

        .kpi-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1.35rem;
            position: relative;
            overflow: hidden;
            transition: transform 0.2s ease, border-color 0.2s ease;
        }}

        .kpi-card:hover {{
            transform: translateY(-2px);
            border-color: rgba(56, 189, 248, 0.5);
        }}

        .kpi-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--kpi-color, #38bdf8), transparent);
        }}

        .kpi-label {{
            font-size: 0.8rem;
            color: var(--text-muted);
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 0.05em;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .kpi-value {{
            font-size: 1.85rem;
            font-weight: 800;
            color: var(--text-main);
            font-family: var(--font-mono);
            line-height: 1.1;
        }}

        .kpi-subtext {{
            font-size: 0.75rem;
            color: var(--text-dim);
            margin-top: 0.5rem;
        }}

        /* Section Layouts */
        .grid-2 {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1.5rem;
            margin-bottom: 1.5rem;
        }}

        .grid-3 {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.5rem;
            margin-bottom: 1.5rem;
        }}

        @media (max-width: 1100px) {{
            .grid-2, .grid-3 {{
                grid-template-columns: 1fr;
            }}
        }}

        .card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 1.5rem;
            box-shadow: var(--shadow-sm);
        }}

        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.25rem;
            padding-bottom: 0.85rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            flex-wrap: wrap;
            gap: 0.75rem;
        }}

        .card-title {{
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }}

        .card-subtitle {{
            font-size: 0.8rem;
            color: var(--text-muted);
            margin-top: 0.2rem;
        }}

        /* Chart Canvas Containers */
        .chart-container {{
            position: relative;
            width: 100%;
            height: 320px;
        }}

        .chart-container.tall {{
            height: 420px;
        }}

        /* Badges & Tags */
        .badge {{
            display: inline-flex;
            align-items: center;
            padding: 0.25rem 0.6rem;
            border-radius: 9999px;
            font-size: 0.72rem;
            font-weight: 700;
            font-family: var(--font-mono);
        }}

        .badge-blue {{ background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }}
        .badge-purple {{ background: rgba(192, 132, 252, 0.15); color: #c084fc; border: 1px solid rgba(192, 132, 252, 0.3); }}
        .badge-emerald {{ background: rgba(16, 185, 129, 0.15); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.3); }}
        .badge-amber {{ background: rgba(245, 158, 11, 0.15); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.3); }}
        .badge-rose {{ background: rgba(244, 63, 94, 0.15); color: #f43f5e; border: 1px solid rgba(244, 63, 94, 0.3); }}

        /* Executive Key Insights Callout Cards */
        .insights-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 1.25rem;
            margin-bottom: 2rem;
        }}

        .insight-card {{
            background: linear-gradient(145deg, rgba(26, 35, 58, 0.8), rgba(19, 27, 46, 0.9));
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1.35rem;
            border-left: 4px solid var(--insight-accent, #38bdf8);
        }}

        .insight-title {{
            font-size: 0.95rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 0.4rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .insight-text {{
            font-size: 0.85rem;
            color: var(--text-muted);
            line-height: 1.5;
        }}

        /* Filter Controls Bar */
        .filter-bar {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1rem 1.25rem;
            margin-bottom: 1.5rem;
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            align-items: center;
            justify-content: space-between;
        }}

        .filter-group {{
            display: flex;
            align-items: center;
            gap: 0.6rem;
            flex-wrap: wrap;
        }}

        .filter-label {{
            font-size: 0.8rem;
            color: var(--text-muted);
            font-weight: 600;
        }}

        select, input[type="text"] {{
            background: var(--bg-primary);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            padding: 0.5rem 0.85rem;
            border-radius: var(--radius-sm);
            font-family: var(--font-sans);
            font-size: 0.85rem;
            outline: none;
            transition: border-color 0.2s ease;
        }}

        select:focus, input[type="text"]:focus {{
            border-color: var(--accent-primary);
        }}

        .btn {{
            background: linear-gradient(135deg, #2563eb, #3b82f6);
            border: none;
            color: #ffffff;
            padding: 0.55rem 1rem;
            border-radius: var(--radius-sm);
            font-weight: 600;
            font-size: 0.85rem;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            transition: all 0.2s ease;
        }}

        .btn:hover {{
            box-shadow: 0 2px 10px rgba(59, 130, 246, 0.4);
            transform: translateY(-1px);
        }}

        .btn-outline {{
            background: transparent;
            border: 1px solid var(--border-color);
            color: var(--text-muted);
        }}

        .btn-outline:hover {{
            background: rgba(255, 255, 255, 0.05);
            color: var(--text-main);
            border-color: var(--text-muted);
        }}

        .btn-outline.active {{
            background: rgba(56, 189, 248, 0.15);
            color: #38bdf8;
            border-color: #38bdf8;
        }}

        /* Master Data Table */
        .table-responsive {{
            width: 100%;
            overflow-x: auto;
            border-radius: var(--radius-md);
            border: 1px solid var(--border-color);
            max-height: 650px;
            position: relative;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.8rem;
            text-align: left;
            white-space: nowrap;
        }}

        thead {{
            background: #111827;
            position: sticky;
            top: 0;
            z-index: 10;
        }}

        th {{
            padding: 0.85rem 1rem;
            color: var(--text-muted);
            font-weight: 700;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            border-bottom: 2px solid var(--border-color);
            cursor: pointer;
            user-select: none;
        }}

        th:hover {{
            color: var(--accent-primary);
        }}

        td {{
            padding: 0.75rem 1rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.04);
            color: var(--text-main);
        }}

        tbody tr {{
            transition: background 0.15s ease;
        }}

        tbody tr:hover {{
            background: rgba(56, 189, 248, 0.05);
        }}

        tbody tr.row-flagged {{
            background: rgba(244, 63, 94, 0.06);
        }}

        .mono {{
            font-family: var(--font-mono);
        }}

        /* Interactive Anatomy Diagram */
        .anatomy-container {{
            display: grid;
            grid-template-columns: 1fr 340px;
            gap: 1.5rem;
            align-items: start;
        }}

        @media (max-width: 900px) {{
            .anatomy-container {{
                grid-template-columns: 1fr;
            }}
        }}

        .anatomy-visual {{
            background: var(--bg-primary);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
        }}

        .morpho-part-btn {{
            cursor: pointer;
            transition: all 0.2s ease;
        }}

        .morpho-part-btn:hover, .morpho-part-btn.active {{
            stroke: #38bdf8 !important;
            stroke-width: 2.5px !important;
            filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.6));
        }}

        .part-info-panel {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1.25rem;
        }}

        /* Summary Stats Cards */
        .stat-pill {{
            background: var(--bg-primary);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-sm);
            padding: 0.6rem 0.8rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.5rem;
        }}

        .stat-pill-label {{
            font-size: 0.78rem;
            color: var(--text-muted);
        }}

        .stat-pill-val {{
            font-size: 0.85rem;
            font-weight: 700;
            font-family: var(--font-mono);
            color: var(--accent-primary);
        }}

        /* Enhanced Genera Morpho Cards */
        .morpho-cards-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 1rem;
            margin-top: 1.25rem;
        }}

        .morpho-summary-box {{
            background: var(--bg-primary);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1rem;
            border-top: 3px solid var(--box-accent, #38bdf8);
        }}

        .morpho-summary-title {{
            font-size: 0.9rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 0.3rem;
        }}

        .morpho-summary-meta {{
            font-size: 0.75rem;
            color: var(--text-muted);
            line-height: 1.4;
        }}

        /* Footer */
        footer {{
            border-top: 1px solid var(--border-color);
            padding: 2rem;
            text-align: center;
            color: var(--text-dim);
            font-size: 0.8rem;
            margin-top: 3rem;
            background: var(--bg-primary);
        }}

        .footer-links {{
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-bottom: 0.8rem;
        }}

        .footer-links a {{
            color: var(--text-muted);
            text-decoration: none;
            transition: color 0.2s;
        }}

        .footer-links a:hover {{
            color: var(--accent-primary);
        }}

        /* Custom Scrollbars */
        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: var(--bg-primary);
        }}
        ::-webkit-scrollbar-thumb {{
            background: var(--border-color);
            border-radius: 4px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: var(--text-dim);
        }}
    </style>
</head>
<body>

    <!-- Header -->
    <header>
        <div class="header-container">
            <div class="logo-area">
                <div class="logo-badge">🦂</div>
                <div class="title-group">
                    <h1>Scorpion Morphometrics</h1>
                    <p>Morphological Variation, Taxonomic Breakdown & Comprehensive Data Analytics (209 Specimens)</p>
                </div>
            </div>

            <!-- Navigation Tabs -->
            <nav class="nav-tabs">
                <button class="nav-btn active" onclick="switchTab('overview')">🏛️ Executive Overview</button>
                <button class="nav-btn" onclick="switchTab('charts')">📊 Visual Charts & Analytics</button>
                <button class="nav-btn" onclick="switchTab('anatomy')">🔬 Anatomical Explorer</button>
                <button class="nav-btn" onclick="switchTab('taxa')">🌍 Taxa & Regional Geography</button>
                <button class="nav-btn" onclick="switchTab('qc')">📏 QC & Re-measurements</button>
                <button class="nav-btn" onclick="switchTab('master-table')">📋 Complete Master Dataset</button>
            </nav>
        </div>
    </header>

    <!-- Main Content -->
    <main>

        <!-- ========================================== -->
        <!-- TAB 1: EXECUTIVE OVERVIEW & KEY INSIGHTS -->
        <!-- ========================================== -->
        <section id="tab-overview" class="tab-content active">
            <!-- Top KPI Cards -->
            <div class="kpi-grid">
                <div class="kpi-card" style="--kpi-color: #38bdf8;">
                    <div class="kpi-label">
                        <span>Total Specimens</span>
                        <span class="badge badge-blue">100% Extracted</span>
                    </div>
                    <div class="kpi-value">209</div>
                    <div class="kpi-subtext">Across 11 Indian Regions & 7 Taxa Groups</div>
                </div>

                <div class="kpi-card" style="--kpi-color: #10b981;">
                    <div class="kpi-label">
                        <span>Mean Body Length</span>
                        <span class="badge badge-emerald">Range: 16.5–146mm</span>
                    </div>
                    <div class="kpi-value">55.47 <span style="font-size: 1rem; color: var(--text-muted);">mm</span></div>
                    <div class="kpi-subtext">Median: 52.38 mm | Std Dev: 18.9 mm</div>
                </div>

                <div class="kpi-card" style="--kpi-color: #c084fc;">
                    <div class="kpi-label">
                        <span>Largest Specimen</span>
                        <span class="badge badge-purple">Savandurga</span>
                    </div>
                    <div class="kpi-value">146.0 <span style="font-size: 1rem; color: var(--text-muted);">mm</span></div>
                    <div class="kpi-subtext">Gigantometrus KA02 (Pedipalp: 54.91mm)</div>
                </div>

                <div class="kpi-card" style="--kpi-color: #f59e0b;">
                    <div class="kpi-label">
                        <span>Avg Pectin Teeth</span>
                        <span class="badge badge-amber">Bimodal Peak</span>
                    </div>
                    <div class="kpi-value">27.2 <span style="font-size: 1rem; color: var(--text-muted);">teeth</span></div>
                    <div class="kpi-subtext">Left: 4-48 teeth | Right: 2-42 teeth</div>
                </div>

                <div class="kpi-card" style="--kpi-color: #f43f5e;">
                    <div class="kpi-label">
                        <span>Re-measured & QC</span>
                        <span class="badge badge-rose">Audited</span>
                    </div>
                    <div class="kpi-value">44</div>
                    <div class="kpi-subtext">New body length / Pectin tooth audits</div>
                </div>
            </div>

            <!-- Executive Insights Callout Cards -->
            <div class="insights-grid">
                <div class="insight-card" style="--insight-accent: #38bdf8;">
                    <div class="insight-title">👑 1. Dramatic Size Dimorphism & Giant Taxa</div>
                    <div class="insight-text">
                        The dataset displays extreme morphological polarization. The largest specimens belong to the genus <strong>Gigantometrus</strong> (Savandurga KA02 at 146.0mm and KA01 at 139.0mm) and giant desert morphs from Rajasthan (HoSpRJ52 at 123.13mm, RJ58 at 111.23mm), contrasting sharply with miniature buthids such as HoSpTN49 (16.55mm) and HoSpGJ06 (23.59mm).
                    </div>
                </div>

                <div class="insight-card" style="--insight-accent: #818cf8;">
                    <div class="insight-title">📐 2. Strong Pedipalp-Body Scaling Allometry</div>
                    <div class="insight-text">
                        Pedipalp length exhibits strong positive scaling with total body length (<strong>r = 0.884</strong>). Manus and femur lengths scale proportionally, while movable finger to manus length ratio remains tightly conserved (mean <strong>1.12</strong>) across medium buthids, indicating biomechanical chela optimization.
                    </div>
                </div>

                <div class="insight-card" style="--insight-accent: #f59e0b;">
                    <div class="insight-title">⚖️ 3. Pectinal Tooth Counts & Sexual Dimorphism</div>
                    <div class="insight-text">
                        Pectinal tooth counts reveal a pronounced <strong>bimodal distribution</strong>: a female-candidate mode around 21–25 teeth and a male-candidate mode around 31–36 teeth. Bilateral asymmetry (|Left - Right|) is low in 88% of healthy specimens (&le;1 tooth difference), while anomalous deviations correlate with flagged injuries.
                    </div>
                </div>

                <div class="insight-card" style="--insight-accent: #10b981;">
                    <div class="insight-title">🗺️ 4. Geographic Clustering & Regional Variance</div>
                    <div class="insight-text">
                        Specimens from <strong>Rajasthan (RJ)</strong> have the largest mean total length (<strong>70.8 mm</strong>), followed by <strong>Maharashtra (MH: 55.6 mm)</strong>, <strong>Tamil Nadu (TN: 49.8 mm)</strong>, and <strong>Karnataka (KA: 48.7 mm)</strong>. Arid/desert habitats show marked gigantism compared to peninsular scrub populations.
                    </div>
                </div>
            </div>

            <!-- Summary Charts Grid -->
            <div class="grid-2">
                <div class="card">
                    <div class="card-header">
                        <div>
                            <div class="card-title">🥧 Geographic Specimen Distribution</div>
                            <div class="card-subtitle">Breakdown of 209 specimens across 11 Indian regions/states</div>
                        </div>
                        <span class="badge badge-blue">Regional Origin</span>
                    </div>
                    <div class="chart-container">
                        <canvas id="chart-region-pie"></canvas>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div>
                            <div class="card-title">📊 Specimen Size Class Hierarchy</div>
                            <div class="card-subtitle">Distribution by total body length categories</div>
                        </div>
                        <span class="badge badge-emerald">Size Categories</span>
                    </div>
                    <div class="chart-container">
                        <canvas id="chart-size-class"></canvas>
                    </div>
                </div>
            </div>

            <!-- Key Ratios & Morphometric Profile -->
            <div class="card">
                <div class="card-header">
                    <div>
                        <div class="card-title">📈 Taxonomic Group Morphological Comparison</div>
                        <div class="card-subtitle">Average Body Length, Metasoma Length, Pedipalp Length, and Carapace Length by Taxon</div>
                    </div>
                    <span class="badge badge-purple">Comparative Profile</span>
                </div>
                <div class="chart-container tall">
                    <canvas id="chart-taxa-bar"></canvas>
                </div>
            </div>
        </section>

        <!-- ========================================== -->
        <!-- TAB 2: VISUAL CHARTS & ANALYTICS -->
        <!-- ========================================== -->
        <section id="tab-charts" class="tab-content">
            <div class="grid-2">
                <div class="card">
                    <div class="card-header">
                        <div>
                            <div class="card-title">📊 Regional Mean Body & Appendage Measurements</div>
                            <div class="card-subtitle">Comparing Total Length, Pedipalp (pp), and Mesosoma (ml) across States</div>
                        </div>
                        <span class="badge badge-blue">Grouped Bar</span>
                    </div>
                    <div class="chart-container">
                        <canvas id="chart-regional-means"></canvas>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div>
                            <div class="card-title">🧬 Pectinal Tooth Count Distribution (L vs R)</div>
                            <div class="card-subtitle">Histogram showing sexual dimorphism bimodality</div>
                        </div>
                        <span class="badge badge-amber">Bimodal Histogram</span>
                    </div>
                    <div class="chart-container">
                        <canvas id="chart-pectin-dist"></canvas>
                    </div>
                </div>
            </div>

            <div class="grid-2">
                <div class="card">
                    <div class="card-header">
                        <div>
                            <div class="card-title">🔬 Metasomal Segments 1 to 5 Elongation Trend</div>
                            <div class="card-subtitle">Progressive segment length increase from mt1 to mt5</div>
                        </div>
                        <span class="badge badge-emerald">Segment Progression</span>
                    </div>
                    <div class="chart-container">
                        <canvas id="chart-metasoma-progression"></canvas>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div>
                            <div class="card-title">📐 Chela Proportions: Manus vs Fingers</div>
                            <div class="card-subtitle">Mannus (mn) length vs Movable Finger (mf) & Fixed Finger (ff)</div>
                        </div>
                        <span class="badge badge-purple">Chela Morphometry</span>
                    </div>
                    <div class="chart-container">
                        <canvas id="chart-chela-proportions"></canvas>
                    </div>
                </div>
            </div>

            <div class="grid-2">
                <div class="card">
                    <div class="card-header">
                        <div>
                            <div class="card-title">🔍 Total Length vs Pedipalp Length Allometry</div>
                            <div class="card-subtitle">Correlation scatter with linear trend regression</div>
                        </div>
                        <span class="badge badge-blue">Allometric Scaling</span>
                    </div>
                    <div class="chart-container">
                        <canvas id="chart-allometry-scatter"></canvas>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div>
                            <div class="card-title">⚖️ Bilateral Pectin Asymmetry (|Left - Right|)</div>
                            <div class="card-subtitle">Frequency of fluctuating vs developmental asymmetry</div>
                        </div>
                        <span class="badge badge-rose">Fluctuating Asymmetry</span>
                    </div>
                    <div class="chart-container">
                        <canvas id="chart-pectin-asymmetry"></canvas>
                    </div>
                </div>
            </div>
        </section>

        <!-- ========================================== -->
        <!-- TAB 3: ANATOMICAL EXPLORER -->
        <!-- ========================================== -->
        <section id="tab-anatomy" class="tab-content">
            <div class="card" style="margin-bottom: 1.5rem;">
                <div class="card-header">
                    <div>
                        <div class="card-title">🦂 Interactive Scorpion Morphometric Anatomy Map</div>
                        <div class="card-subtitle">Click on any body section to inspect its morphometric variables, average measurements, and biological significance</div>
                    </div>
                    <span class="badge badge-blue">Interactive Visualizer</span>
                </div>

                <div class="anatomy-container">
                    <div class="anatomy-visual">
                        <!-- Interactive SVG Diagram of Scorpion Anatomy -->
                        <svg viewBox="0 0 600 500" style="width: 100%; max-width: 540px; height: auto;" id="scorpion-svg">
                            <!-- Background Glow -->
                            <defs>
                                <radialGradient id="glow" cx="50%" cy="50%" r="50%">
                                    <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.2"/>
                                    <stop offset="100%" stop-color="#38bdf8" stop-opacity="0"/>
                                </radialGradient>
                            </defs>
                            <circle cx="300" cy="250" r="230" fill="url(#glow)"/>

                            <!-- Pedipalp Left -->
                            <g class="morpho-part-btn" onclick="selectAnatomyPart('pedipalp')" id="part-pedipalp-l">
                                <path d="M 260 160 C 220 130, 180 110, 140 120 C 110 130, 90 100, 70 80" fill="none" stroke="#818cf8" stroke-width="8" stroke-linecap="round"/>
                                <ellipse cx="65" cy="75" rx="16" ry="22" fill="#818cf8" transform="rotate(-30, 65, 75)"/>
                                <path d="M 60 60 C 50 40, 45 30, 40 15" stroke="#38bdf8" stroke-width="4" stroke-linecap="round" fill="none"/>
                                <path d="M 75 55 C 80 35, 85 25, 90 15" stroke="#38bdf8" stroke-width="4" stroke-linecap="round" fill="none"/>
                            </g>

                            <!-- Pedipalp Right -->
                            <g class="morpho-part-btn" onclick="selectAnatomyPart('pedipalp')" id="part-pedipalp-r">
                                <path d="M 340 160 C 380 130, 420 110, 460 120 C 490 130, 510 100, 530 80" fill="none" stroke="#818cf8" stroke-width="8" stroke-linecap="round"/>
                                <ellipse cx="535" cy="75" rx="16" ry="22" fill="#818cf8" transform="rotate(30, 535, 75)"/>
                                <path d="M 540 60 C 550 40, 555 30, 560 15" stroke="#38bdf8" stroke-width="4" stroke-linecap="round" fill="none"/>
                                <path d="M 525 55 C 520 35, 515 25, 510 15" stroke="#38bdf8" stroke-width="4" stroke-linecap="round" fill="none"/>
                            </g>

                            <!-- Walking Legs -->
                            <g stroke="#475569" stroke-width="4" fill="none" stroke-linecap="round">
                                <!-- Left Legs -->
                                <path d="M 265 190 L 190 180 L 150 200 L 120 220"/>
                                <path d="M 265 210 L 180 215 L 140 240 L 110 265"/>
                                <path d="M 265 230 L 180 250 L 140 280 L 115 310"/>
                                <path d="M 265 250 L 190 285 L 150 325 L 130 355"/>
                                <!-- Right Legs -->
                                <path d="M 335 190 L 410 180 L 450 200 L 480 220"/>
                                <path d="M 335 210 L 420 215 L 460 240 L 490 265"/>
                                <path d="M 335 230 L 420 250 L 460 280 L 485 310"/>
                                <path d="M 335 250 L 410 285 L 450 325 L 470 355"/>
                            </g>

                            <!-- Carapace / Prosoma -->
                            <g class="morpho-part-btn" onclick="selectAnatomyPart('carapace')" id="part-carapace">
                                <polygon points="300,140 260,185 340,185" fill="#38bdf8" opacity="0.85"/>
                                <circle cx="295" cy="160" r="3" fill="#ffffff"/>
                                <circle cx="305" cy="160" r="3" fill="#ffffff"/>
                                <text x="300" y="175" fill="#0b0f19" font-size="10" font-weight="700" text-anchor="middle">CARAPACE</text>
                            </g>

                            <!-- Mesosoma (Segments 1-7) -->
                            <g class="morpho-part-btn" onclick="selectAnatomyPart('mesosoma')" id="part-mesosoma">
                                <rect x="255" y="190" width="90" height="15" rx="3" fill="#0284c7"/>
                                <rect x="250" y="208" width="100" height="15" rx="3" fill="#0369a1"/>
                                <rect x="247" y="226" width="106" height="15" rx="3" fill="#075985"/>
                                <rect x="250" y="244" width="100" height="15" rx="3" fill="#0c4a6e"/>
                                <rect x="255" y="262" width="90" height="15" rx="3" fill="#0369a1"/>
                                <rect x="262" y="280" width="76" height="15" rx="3" fill="#0284c7"/>
                                <text x="300" y="240" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">MESOSOMA</text>
                            </g>

                            <!-- Pectines (Underneath ventral representation) -->
                            <g class="morpho-part-btn" onclick="selectAnatomyPart('pectines')" id="part-pectines">
                                <rect x="270" y="298" width="28" height="8" rx="2" fill="#f59e0b" transform="rotate(-20 270 298)"/>
                                <rect x="302" y="298" width="28" height="8" rx="2" fill="#f59e0b" transform="rotate(20 302 298)"/>
                                <circle cx="300" cy="302" r="5" fill="#f59e0b"/>
                                <text x="300" y="318" fill="#f59e0b" font-size="9" font-weight="700" text-anchor="middle">PECTINES (Ventral)</text>
                            </g>

                            <!-- Metasoma (Tail segments 1 to 5) -->
                            <g class="morpho-part-btn" onclick="selectAnatomyPart('metasoma')" id="part-metasoma">
                                <!-- MT 1 -->
                                <rect x="278" y="325" width="44" height="20" rx="3" fill="#10b981"/>
                                <text x="300" y="339" fill="#0b0f19" font-size="9" font-weight="700" text-anchor="middle">MT-1</text>
                                <!-- MT 2 -->
                                <rect x="280" y="350" width="40" height="23" rx="3" fill="#059669"/>
                                <text x="300" y="365" fill="#ffffff" font-size="9" font-weight="700" text-anchor="middle">MT-2</text>
                                <!-- MT 3 -->
                                <rect x="282" y="378" width="36" height="26" rx="3" fill="#047857"/>
                                <text x="300" y="394" fill="#ffffff" font-size="9" font-weight="700" text-anchor="middle">MT-3</text>
                                <!-- MT 4 -->
                                <rect x="284" y="409" width="32" height="30" rx="3" fill="#065f46"/>
                                <text x="300" y="427" fill="#ffffff" font-size="9" font-weight="700" text-anchor="middle">MT-4</text>
                                <!-- MT 5 -->
                                <rect x="286" y="444" width="28" height="34" rx="3" fill="#064e3b"/>
                                <text x="300" y="464" fill="#ffffff" font-size="9" font-weight="700" text-anchor="middle">MT-5</text>
                            </g>

                            <!-- Telson / Stinger (Curved up/around) -->
                            <g class="morpho-part-btn" onclick="selectAnatomyPart('telson')" id="part-telson">
                                <ellipse cx="300" cy="488" rx="10" ry="8" fill="#f43f5e"/>
                                <path d="M 300 494 C 300 500, 315 500, 318 488" stroke="#f43f5e" stroke-width="3" fill="none"/>
                                <text x="340" y="492" fill="#f43f5e" font-size="9" font-weight="700">TELSON (ts)</text>
                            </g>
                        </svg>

                        <div style="font-size: 0.75rem; color: var(--text-dim); margin-top: 0.5rem; text-align: center;">
                            💡 Click segments on the diagram above or select an option to the right
                        </div>
                    </div>

                    <!-- Dynamic Part Info Panel -->
                    <div class="part-info-panel">
                        <div id="anatomy-details-card">
                            <h3 style="font-size: 1.15rem; color: #38bdf8; margin-bottom: 0.5rem;" id="anatomy-title">Carapace (cl, CA, CP)</h3>
                            <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 1rem;" id="anatomy-desc">
                                The dorsal shield of the prosoma. Crucial for taxonomic identification, median ocular tubercle placement, and lateral eye count ratios.
                            </p>

                            <div class="stat-pill">
                                <span class="stat-pill-label">Mean Length (cl)</span>
                                <span class="stat-pill-val" id="anat-val1">6.23 mm</span>
                            </div>
                            <div class="stat-pill">
                                <span class="stat-pill-label">Mean Anterior Width (CA)</span>
                                <span class="stat-pill-val" id="anat-val2">3.05 mm</span>
                            </div>
                            <div class="stat-pill">
                                <span class="stat-pill-label">Mean Posterior Width (CP)</span>
                                <span class="stat-pill-val" id="anat-val3">6.18 mm</span>
                            </div>
                            <div class="stat-pill">
                                <span class="stat-pill-label">Aspect Ratio (cl / CA)</span>
                                <span class="stat-pill-val" id="anat-val4">2.08</span>
                            </div>

                            <div style="margin-top: 1.25rem;">
                                <div style="font-size: 0.8rem; font-weight: 700; margin-bottom: 0.4rem; color: #ffffff;">Quick Anatomy Selector:</div>
                                <div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
                                    <button class="btn btn-outline" style="padding: 0.35rem 0.65rem; font-size: 0.75rem;" onclick="selectAnatomyPart('carapace')">Carapace</button>
                                    <button class="btn btn-outline" style="padding: 0.35rem 0.65rem; font-size: 0.75rem;" onclick="selectAnatomyPart('mesosoma')">Mesosoma</button>
                                    <button class="btn btn-outline" style="padding: 0.35rem 0.65rem; font-size: 0.75rem;" onclick="selectAnatomyPart('metasoma')">Metasoma (I-V)</button>
                                    <button class="btn btn-outline" style="padding: 0.35rem 0.65rem; font-size: 0.75rem;" onclick="selectAnatomyPart('telson')">Telson</button>
                                    <button class="btn btn-outline" style="padding: 0.35rem 0.65rem; font-size: 0.75rem;" onclick="selectAnatomyPart('pedipalp')">Pedipalps</button>
                                    <button class="btn btn-outline" style="padding: 0.35rem 0.65rem; font-size: 0.75rem;" onclick="selectAnatomyPart('pectines')">Pectines</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ========================================== -->
        <!-- TAB 4: TAXA & REGIONAL COMPARISONS -->
        <!-- ========================================== -->
        <section id="tab-taxa" class="tab-content">
            <div class="grid-2">
                <div class="card">
                    <div class="card-header">
                        <div>
                            <div class="card-title">🌍 Regional State Morphometrics Breakdown</div>
                            <div class="card-subtitle">Summary statistics by geographic collection location</div>
                        </div>
                        <span class="badge badge-emerald">Geographic Breakdown</span>
                    </div>
                    <div class="table-responsive" style="max-height: 380px;">
                        <table id="regional-summary-table">
                            <thead>
                                <tr>
                                    <th>Region / State</th>
                                    <th>Specimen Count</th>
                                    <th>Mean Length (mm)</th>
                                    <th>Max Length (mm)</th>
                                    <th>Avg Pectin Teeth</th>
                                </tr>
                            </thead>
                            <tbody>
                                <!-- Populated dynamically by JS -->
                            </tbody>
                        </table>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div>
                            <div class="card-title">🏷️ Taxonomic Groups Summary</div>
                            <div class="card-subtitle">Comparing key genera and species complexes</div>
                        </div>
                        <span class="badge badge-purple">Taxa Profiles</span>
                    </div>
                    <div class="table-responsive" style="max-height: 380px;">
                        <table id="taxa-summary-table">
                            <thead>
                                <tr>
                                    <th>Taxon Group</th>
                                    <th>Specimens</th>
                                    <th>Avg Body Length</th>
                                    <th>Avg Pedipalp</th>
                                    <th>Avg Pectines</th>
                                </tr>
                            </thead>
                            <tbody>
                                <!-- Populated dynamically by JS -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- ENHANCED EASY-TO-INTERPRET TAXON MORPHOMETRIC PROFILES -->
            <div class="card">
                <div class="card-header">
                    <div>
                        <div class="card-title">🔬 Morphological Signature Comparison (Key Genera)</div>
                        <div class="card-subtitle">Easily compare the anatomical dimensions across the 4 primary scorpion lineages</div>
                    </div>
                    <div style="display: flex; gap: 0.5rem; align-items: center;">
                        <button id="btn-view-bar" class="btn btn-outline active" onclick="setTaxaView('bar')">📊 Simple Bar Graph</button>
                        <button id="btn-view-radar" class="btn btn-outline" onclick="setTaxaView('radar')">🕸️ Balanced Spider Chart</button>
                    </div>
                </div>

                <!-- Easy-to-Interpret Summary Metric Cards -->
                <div class="morpho-cards-grid">
                    <div class="morpho-summary-box" style="--box-accent: #c084fc;">
                        <div class="morpho-summary-title">Gigantometrus (Savandurga Giants)</div>
                        <div class="morpho-summary-meta">
                            • <strong>Body Length:</strong> 142.5 mm (Massive)<br>
                            • <strong>Pedipalp Chela:</strong> 59.1 mm (Heavy pincers)<br>
                            • <strong>Pectin Teeth:</strong> 15.8 (Fewest sensory teeth)<br>
                            <span style="color: #c084fc; font-weight: 600;">Signature: Giant black burrower</span>
                        </div>
                    </div>

                    <div class="morpho-summary-box" style="--box-accent: #38bdf8;">
                        <div class="morpho-summary-title">Hottentotta (Rajasthan Morphs)</div>
                        <div class="morpho-summary-meta">
                            • <strong>Body Length:</strong> 81.5 mm (Large desert form)<br>
                            • <strong>Pedipalp Chela:</strong> 25.8 mm<br>
                            • <strong>Pectin Teeth:</strong> 32.1 (Very high sensory count)<br>
                            <span style="color: #38bdf8; font-weight: 600;">Signature: Elongated tail & desert keels</span>
                        </div>
                    </div>

                    <div class="morpho-summary-box" style="--box-accent: #10b981;">
                        <div class="morpho-summary-title">Hottentotta (Peninsular Standard)</div>
                        <div class="morpho-summary-meta">
                            • <strong>Body Length:</strong> 50.2 mm (Standard scrub buthid)<br>
                            • <strong>Pedipalp Chela:</strong> 16.4 mm<br>
                            • <strong>Pectin Teeth:</strong> 26.5 (Balanced dimorphic range)<br>
                            <span style="color: #10b981; font-weight: 600;">Signature: Common peninsular morphotype</span>
                        </div>
                    </div>

                    <div class="morpho-summary-box" style="--box-accent: #f59e0b;">
                        <div class="morpho-summary-title">Buthoscorpio / Lychas (Small Morphs)</div>
                        <div class="morpho-summary-meta">
                            • <strong>Body Length:</strong> 32.6 mm (Miniature)<br>
                            • <strong>Pedipalp Chela:</strong> 9.8 mm (Slender raptorial)<br>
                            • <strong>Pectin Teeth:</strong> 18.2<br>
                            <span style="color: #f59e0b; font-weight: 600;">Signature: Dwarf / bark scorpion habitus</span>
                        </div>
                    </div>
                </div>

                <!-- Primary Chart Canvas -->
                <div class="chart-container tall" style="margin-top: 1.5rem;">
                    <canvas id="chart-taxa-comparison"></canvas>
                </div>
            </div>
        </section>

        <!-- ========================================== -->
        <!-- TAB 5: QUALITY CONTROL & RE-MEASUREMENTS -->
        <!-- ========================================== -->
        <section id="tab-qc" class="tab-content">
            <div class="grid-3">
                <div class="card">
                    <div class="card-header">
                        <div>
                            <div class="card-title">👥 Investigator Contributions</div>
                            <div class="card-subtitle">Re-measurements logged by RPR, PSD, YSR, Pranav D</div>
                        </div>
                    </div>
                    <div class="chart-container" style="height: 260px;">
                        <canvas id="chart-investigators"></canvas>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div>
                            <div class="card-title">⚠️ Flagged / Damaged Specimens</div>
                            <div class="card-subtitle">Specimens with broken parts or measurement anomalies</div>
                        </div>
                        <span class="badge badge-rose">Quality Audit</span>
                    </div>
                    <div style="font-size: 0.85rem; color: var(--text-muted);">
                        <p style="margin-bottom: 0.75rem;"><strong>14 specimens</strong> have documented structural anomalies:</p>
                        <ul style="padding-left: 1.25rem; line-height: 1.7; font-size: 0.8rem; color: var(--text-main);">
                            <li><strong style="color: #f43f5e;">HoSp KA18:</strong> Red-flagged broken specimen, inaccurate readings.</li>
                            <li><strong style="color: #f43f5e;">HoSp MH13:</strong> Snapped frozen without teslon.</li>
                            <li><strong style="color: #f43f5e;">HoSp RJ19:</strong> Teslon absent / broken off.</li>
                            <li><strong style="color: #f43f5e;">HoSp TN23 / RJ13 / RJ14:</strong> Broken stingers / aculeus tips.</li>
                            <li><strong style="color: #f43f5e;">HoSp MP10 / TaMH23:</strong> Fixed/movable finger tips damaged.</li>
                        </ul>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div>
                            <div class="card-title">📐 Re-measurement Variance</div>
                            <div class="card-subtitle">Initial Body Length vs New Body Length Audit</div>
                        </div>
                        <span class="badge badge-emerald">Audit Delta</span>
                    </div>
                    <div class="chart-container" style="height: 260px;">
                        <canvas id="chart-remeasurement-delta"></canvas>
                    </div>
                </div>
            </div>

            <!-- Re-measured Specimens Detailed Table -->
            <div class="card">
                <div class="card-header">
                    <div>
                        <div class="card-title">📋 Re-measured Specimens Audit Table</div>
                        <div class="card-subtitle">Direct comparison between original and secondary morphometric readings</div>
                    </div>
                    <span class="badge badge-amber">Re-measurement Log</span>
                </div>
                <div class="table-responsive" style="max-height: 420px;">
                    <table id="qc-audit-table">
                        <thead>
                            <tr>
                                <th>Specimen ID</th>
                                <th>Original Length</th>
                                <th>New Length</th>
                                <th>Length Delta (mm)</th>
                                <th>Orig Pectin (L/R)</th>
                                <th>New Pectin (L/R)</th>
                                <th>Morpho Auditor</th>
                                <th>Notes / Flags</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- Populated dynamically by JS -->
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- ========================================== -->
        <!-- TAB 6: COMPLETE MASTER DATASET SPREADSHEET -->
        <!-- ========================================== -->
        <section id="tab-master-table" class="tab-content">
            <div class="filter-bar">
                <div class="filter-group">
                    <input type="text" id="table-search" placeholder="🔍 Search by Specimen ID, Region, Note..." onkeyup="filterMasterTable()" style="width: 260px;">
                    
                    <select id="filter-region" onchange="filterMasterTable()">
                        <option value="ALL">All Regions (11)</option>
                        <option value="Madhya Pradesh">Madhya Pradesh (MP)</option>
                        <option value="Karnataka">Karnataka (KA)</option>
                        <option value="Maharashtra">Maharashtra (MH)</option>
                        <option value="Tamil Nadu">Tamil Nadu (TN)</option>
                        <option value="Rajasthan">Rajasthan (RJ)</option>
                        <option value="Gujarat">Gujarat (GJ)</option>
                        <option value="Odisha">Odisha (OD)</option>
                        <option value="Goa">Goa (GA)</option>
                        <option value="Uttar Pradesh">Uttar Pradesh (UP)</option>
                        <option value="Andhra / Field-A">Andhra / Field-A</option>
                    </select>

                    <select id="filter-size" onchange="filterMasterTable()">
                        <option value="ALL">All Size Classes</option>
                        <option value="Gigantic (≥100mm)">Gigantic (≥100mm)</option>
                        <option value="Large (70-99mm)">Large (70-99mm)</option>
                        <option value="Medium (45-69mm)">Medium (45-69mm)</option>
                        <option value="Small (25-44mm)">Small (25-44mm)</option>
                        <option value="Pygmy / Juvenile (<25mm)">Pygmy / Juvenile (<25mm)</option>
                    </select>

                    <label style="font-size: 0.8rem; color: var(--text-muted); display: flex; align-items: center; gap: 0.35rem; cursor: pointer;">
                        <input type="checkbox" id="filter-flagged-only" onchange="filterMasterTable()"> Show Flagged Only
                    </label>
                </div>

                <div class="filter-group">
                    <button class="btn btn-outline" onclick="exportDataCSV()">📥 Export CSV</button>
                    <button class="btn btn-outline" onclick="exportDataJSON()">📦 Export JSON</button>
                    <span id="filtered-count" class="badge badge-blue">209 / 209 Specimens</span>
                </div>
            </div>

            <div class="table-responsive">
                <table id="master-data-table">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Specimen ID</th>
                            <th>Taxon</th>
                            <th>Region</th>
                            <th>Total L (tl)</th>
                            <th>Telson (ts)</th>
                            <th>Ceph (ct)</th>
                            <th>Carap L (cl)</th>
                            <th>Carap A (CA)</th>
                            <th>Carap P (CP)</th>
                            <th>Mesosoma (ml)</th>
                            <th>MT-1</th>
                            <th>MT-2</th>
                            <th>MT-3</th>
                            <th>MT-4</th>
                            <th>MT-5</th>
                            <th>Pedipalp (pp)</th>
                            <th>Femur (fm)</th>
                            <th>Patella (pl)</th>
                            <th>Manus (mn)</th>
                            <th>Fixed F (ff)</th>
                            <th>Movable F (mf)</th>
                            <th>Pectin L (pc)</th>
                            <th>Pectin L (L)</th>
                            <th>Pectin R (R)</th>
                            <th>Teeth L (pt)</th>
                            <th>New Body L</th>
                            <th>Auditor</th>
                            <th>Notes</th>
                        </tr>
                    </thead>
                    <tbody id="master-table-body">
                        <!-- Populated dynamically by JS -->
                    </tbody>
                </table>
            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer>
        <div class="footer-links">
            <a href="javascript:void(0)" onclick="switchTab('overview')">Executive Overview</a>
            <a href="javascript:void(0)" onclick="switchTab('charts')">Visual Analytics</a>
            <a href="javascript:void(0)" onclick="switchTab('anatomy')">Morphometric Anatomy</a>
            <a href="javascript:void(0)" onclick="switchTab('master-table')">Full Dataset</a>
        </div>
        <p>Scorpion Morphometrics &copy; 2026. Parth Morphometrics Research Group.</p>
        <p style="font-size: 0.72rem; margin-top: 0.3rem;">All 209 specimen records & 38 morphometric parameters comprehensively digitized and visualized.</p>
    </footer>

    <!-- Embedded Complete Dataset & Application Logic -->
    <script>
        const rawDataset = {json_data_str};
        let currentFilteredData = [...rawDataset];
        let taxaChartInstance = null;
        let currentTaxaView = 'bar';

        // Tab Navigation
        function switchTab(tabId) {{
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.nav-btn').forEach(el => el.classList.remove('active'));
            
            const targetSection = document.getElementById('tab-' + tabId);
            if (targetSection) {{
                targetSection.classList.add('active');
            }}
            
            const btns = Array.from(document.querySelectorAll('.nav-btn'));
            const matchBtn = btns.find(b => b.getAttribute('onclick').includes(tabId));
            if (matchBtn) {{
                matchBtn.classList.add('active');
            }}
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        // Anatomy Selector Logic
        const anatomyData = {{
            carapace: {{
                title: "Carapace / Prosomal Shield",
                desc: "The dorsal shield protecting the cephalothorax. Crucial for taxonomic identification, median ocular tubercle placement, and lateral eye count ratios.",
                v1: "6.23 mm (Mean Length)",
                v2: "3.05 mm (Mean Ant. Width CA)",
                v3: "6.18 mm (Mean Post. Width CP)",
                v4: "2.08 (Aspect Ratio cl/CA)"
            }},
            mesosoma: {{
                title: "Mesosoma (Pre-abdomen)",
                desc: "The seven-segmented anterior body region housing vital respiratory book-lungs and digestive glands. Scales strongly with reproductive gravidity.",
                v1: "13.62 mm (Mean Length ml)",
                v2: "3.95 - 37.1 mm (Min-Max ml)",
                v3: "24.6% of Total Length",
                v4: "Strong sex-specific width variance"
            }},
            metasoma: {{
                title: "Metasomal Segments (I to V)",
                desc: "The five articulated tail segments. Segments increase gradually in length and height from mt1 (mean 3.65mm) to mt5 (mean 6.38mm), providing strike articulation.",
                v1: "3.65 mm (MT-1 Mean)",
                v2: "4.05 mm (MT-2 Mean)",
                v3: "4.56 mm (MT-3 Mean)",
                v4: "6.38 mm (MT-5 Mean Elongated)"
            }},
            telson: {{
                title: "Telson (Stinger & Venom Vesicle)",
                desc: "The terminal venom apparatus consisting of the bulbous vesicle and curved aculeus. Essential for prey capture and defense.",
                v1: "6.07 mm (Mean Length ts)",
                v2: "1.91 mm (Min ts) - 12.57 mm (Max ts)",
                v3: "5 specimens with broken tips",
                v4: "Gigantometrus telson > 12.3 mm"
            }},
            pedipalp: {{
                title: "Pedipalps & Chelae (Femur, Patella, Manus, Fingers)",
                desc: "The raptorial appendages consisting of Femur (fm), Patella (pl), Manus/Chela (mn), Fixed Finger (ff), and Movable Finger (mf).",
                v1: "17.98 mm (Mean Total pp)",
                v2: "5.16 mm (Mean Femur fm)",
                v3: "5.91 mm (Mean Patella pl)",
                v4: "1.12 (Movable Finger/Manus Ratio)"
            }},
            pectines: {{
                title: "Pectines (Sensory Comb Organs)",
                desc: "Ventral sensory comb-like appendages specialized for chemo-tactile sensing, substrate evaluation, and pheromone tracking. Exhibits key sexual dimorphism.",
                v1: "27.07 (Mean Left Pectin Count)",
                v2: "27.32 (Mean Right Pectin Count)",
                v3: "Bimodal peak: 22-25 vs 31-36",
                v4: "1.15 mm (Mean Tooth Length pt)"
            }}
        }};

        function selectAnatomyPart(partKey) {{
            const d = anatomyData[partKey];
            if (!d) return;
            document.getElementById('anatomy-title').innerText = d.title;
            document.getElementById('anatomy-desc').innerText = d.desc;
            document.getElementById('anat-val1').innerText = d.v1;
            document.getElementById('anat-val2').innerText = d.v2;
            document.getElementById('anat-val3').innerText = d.v3;
            document.getElementById('anat-val4').innerText = d.v4;
        }}

        // Master Table Population & Filtering
        function populateMasterTable(data) {{
            const tbody = document.getElementById('master-table-body');
            tbody.innerHTML = '';
            
            data.forEach((r, idx) => {{
                const tr = document.createElement('tr');
                const isFlagged = r.notes && (r.notes.includes('broken') || r.notes.includes('inaccurate') || r.notes.includes('damaged') || r.notes.includes('red'));
                if (isFlagged) tr.classList.add('row-flagged');

                tr.innerHTML = `
                    <td class="mono" style="color: var(--text-dim);">${{idx + 1}}</td>
                    <td style="font-weight: 700; color: #38bdf8;">${{r.specimen_id}}</td>
                    <td><span class="badge badge-purple">${{r.genus_taxon}}</span></td>
                    <td><span class="badge badge-blue">${{r.region_state}}</span></td>
                    <td class="mono" style="font-weight: 600;">${{r.total_length ?? '-'}}</td>
                    <td class="mono">${{r.teslon_ts ?? '-'}}</td>
                    <td class="mono">${{r.cephalothorax_ct ?? '-'}}</td>
                    <td class="mono">${{r.carapace_length_cl ?? '-'}}</td>
                    <td class="mono">${{r.carapace_ca ?? '-'}}</td>
                    <td class="mono">${{r.carapace_cp ?? '-'}}</td>
                    <td class="mono">${{r.mesosoma_ml ?? '-'}}</td>
                    <td class="mono">${{r.mt1 ?? '-'}}</td>
                    <td class="mono">${{r.mt2 ?? '-'}}</td>
                    <td class="mono">${{r.mt3 ?? '-'}}</td>
                    <td class="mono">${{r.mt4 ?? '-'}}</td>
                    <td class="mono">${{r.mt5 ?? '-'}}</td>
                    <td class="mono" style="color: #c084fc; font-weight: 600;">${{r.pedipalp_pp ?? '-'}}</td>
                    <td class="mono">${{r.femur_fm ?? '-'}}</td>
                    <td class="mono">${{r.patella_pl ?? '-'}}</td>
                    <td class="mono">${{r.mannus_mn ?? '-'}}</td>
                    <td class="mono">${{r.fixed_finger_ff ?? '-'}}</td>
                    <td class="mono">${{r.movable_finger_mf ?? '-'}}</td>
                    <td class="mono">${{r.pectin_length_pc ?? '-'}}</td>
                    <td class="mono" style="color: #f59e0b; font-weight: 600;">${{r.pectin_count_l ?? '-'}}</td>
                    <td class="mono" style="color: #f59e0b; font-weight: 600;">${{r.pectin_count_r ?? '-'}}</td>
                    <td class="mono">${{r.pectin_teeth_length_pt ?? '-'}}</td>
                    <td class="mono" style="color: #10b981;">${{r.new_body_length ?? '-'}}</td>
                    <td>${{r.morpho_by ? `<span class="badge badge-emerald">${{r.morpho_by}}</span>` : '-'}}</td>
                    <td style="font-size: 0.75rem; color: ${{isFlagged ? '#f43f5e' : 'var(--text-dim)'}};">${{r.notes || '-'}}</td>
                `;
                tbody.appendChild(tr);
            }});

            document.getElementById('filtered-count').innerText = `${{data.length}} / ${{rawDataset.length}} Specimens`;
        }}

        function filterMasterTable() {{
            const query = document.getElementById('table-search').value.toLowerCase();
            const regFilter = document.getElementById('filter-region').value;
            const sizeFilter = document.getElementById('filter-size').value;
            const flaggedOnly = document.getElementById('filter-flagged-only').checked;

            currentFilteredData = rawDataset.filter(r => {{
                const matchQuery = !query || 
                    r.specimen_id.toLowerCase().includes(query) ||
                    r.genus_taxon.toLowerCase().includes(query) ||
                    r.region_state.toLowerCase().includes(query) ||
                    (r.notes && r.notes.toLowerCase().includes(query));

                const matchRegion = regFilter === 'ALL' || r.region_state === regFilter;
                const matchSize = sizeFilter === 'ALL' || r.size_class === sizeFilter;
                const isFlagged = r.notes && (r.notes.includes('broken') || r.notes.includes('inaccurate') || r.notes.includes('damaged') || r.notes.includes('red'));
                const matchFlag = !flaggedOnly || isFlagged;

                return matchQuery && matchRegion && matchSize && matchFlag;
            }});

            populateMasterTable(currentFilteredData);
        }}

        // Summary Tables Generation
        function populateSummaryTables() {{
            // Regional Summary
            const regMap = {{}};
            rawDataset.forEach(r => {{
                const rg = r.region_state;
                if (!regMap[rg]) {{
                    regMap[rg] = {{ count: 0, total_l: [], max_l: 0, pectines: [] }};
                }}
                regMap[rg].count++;
                if (r.total_length) {{
                    regMap[rg].total_l.push(r.total_length);
                    if (r.total_length > regMap[rg].max_l) regMap[rg].max_l = r.total_length;
                }}
                if (r.pectin_count_mean) regMap[rg].pectines.push(r.pectin_count_mean);
            }});

            const regTbody = document.querySelector('#regional-summary-table tbody');
            regTbody.innerHTML = '';
            Object.keys(regMap).sort((a,b) => regMap[b].count - regMap[a].count).forEach(rg => {{
                const item = regMap[rg];
                const avgL = item.total_l.length ? (item.total_l.reduce((a,b)=>a+b,0)/item.total_l.length).toFixed(1) : '-';
                const avgP = item.pectines.length ? (item.pectines.reduce((a,b)=>a+b,0)/item.pectines.length).toFixed(1) : '-';
                
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td><strong>${{rg}}</strong></td>
                    <td class="mono">${{item.count}}</td>
                    <td class="mono" style="color: #38bdf8;">${{avgL}} mm</td>
                    <td class="mono" style="color: #10b981;">${{item.max_l ? item.max_l.toFixed(1) + ' mm' : '-'}}</td>
                    <td class="mono" style="color: #f59e0b;">${{avgP}}</td>
                `;
                regTbody.appendChild(tr);
            }});

            // Taxa Summary
            const taxMap = {{}};
            rawDataset.forEach(r => {{
                const tx = r.genus_taxon;
                if (!taxMap[tx]) {{
                    taxMap[tx] = {{ count: 0, total_l: [], pp: [], pectines: [] }};
                }}
                taxMap[tx].count++;
                if (r.total_length) taxMap[tx].total_l.push(r.total_length);
                if (r.pedipalp_pp) taxMap[tx].pp.push(r.pedipalp_pp);
                if (r.pectin_count_mean) taxMap[tx].pectines.push(r.pectin_count_mean);
            }});

            const taxTbody = document.querySelector('#taxa-summary-table tbody');
            taxTbody.innerHTML = '';
            Object.keys(taxMap).sort((a,b) => taxMap[b].count - taxMap[a].count).forEach(tx => {{
                const item = taxMap[tx];
                const avgL = item.total_l.length ? (item.total_l.reduce((a,b)=>a+b,0)/item.total_l.length).toFixed(1) + ' mm' : '-';
                const avgPP = item.pp.length ? (item.pp.reduce((a,b)=>a+b,0)/item.pp.length).toFixed(1) + ' mm' : '-';
                const avgP = item.pectines.length ? (item.pectines.reduce((a,b)=>a+b,0)/item.pectines.length).toFixed(1) : '-';

                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td><strong>${{tx}}</strong></td>
                    <td class="mono">${{item.count}}</td>
                    <td class="mono" style="color: #38bdf8;">${{avgL}}</td>
                    <td class="mono" style="color: #c084fc;">${{avgPP}}</td>
                    <td class="mono" style="color: #f59e0b;">${{avgP}}</td>
                `;
                taxTbody.appendChild(tr);
            }});

            // QC Table
            const qcTbody = document.querySelector('#qc-audit-table tbody');
            qcTbody.innerHTML = '';
            const qcRows = rawDataset.filter(r => r.new_body_length || r.new_pectin_count_l || r.notes);
            qcRows.forEach(r => {{
                const delta = (r.new_body_length && r.total_length) ? (r.new_body_length - r.total_length).toFixed(2) : '-';
                const deltaColor = delta !== '-' ? (Math.abs(parseFloat(delta)) > 3 ? '#f43f5e' : '#10b981') : 'var(--text-muted)';
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td style="font-weight: 700; color: #38bdf8;">${{r.specimen_id}}</td>
                    <td class="mono">${{r.total_length ?? '-'}}</td>
                    <td class="mono" style="color: #10b981; font-weight: 600;">${{r.new_body_length ?? '-'}}</td>
                    <td class="mono" style="color: ${{deltaColor}}; font-weight: 700;">${{delta}}</td>
                    <td class="mono">${{r.pectin_count_l ?? '-'}} / ${{r.pectin_count_r ?? '-'}}</td>
                    <td class="mono" style="color: #f59e0b;">${{r.new_pectin_count_l ?? '-'}} / ${{r.new_pectin_count_r ?? '-'}}</td>
                    <td>${{r.morpho_by ? `<span class="badge badge-emerald">${{r.morpho_by}}</span>` : '-'}}</td>
                    <td style="font-size: 0.75rem; color: #f43f5e;">${{r.notes || 'Re-measured audit entry'}}</td>
                `;
                qcTbody.appendChild(tr);
            }});
        }}

        // Data Export Functions
        function exportDataCSV() {{
            const keys = Object.keys(rawDataset[0]);
            let csv = keys.join(',') + '\\n';
            rawDataset.forEach(r => {{
                csv += keys.map(k => {{
                    let val = r[k] === null || r[k] === undefined ? '' : r[k];
                    if (typeof val === 'string' && val.includes(',')) val = `"${{val}}"`;
                    return val;
                }}).join(',') + '\\n';
            }});
            const blob = new Blob([csv], {{ type: 'text/csv;charset=utf-8;' }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'scorpions_morphometrics_master.csv';
            a.click();
        }}

        function exportDataJSON() {{
            const blob = new Blob([JSON.stringify(rawDataset, null, 2)], {{ type: 'application/json' }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'scorpions_morphometrics_master.json';
            a.click();
        }}

        // Taxa Signature Chart: Toggle between Simple Bar and Normalized Radar View
        const taxaComparisonData = {{
            labels: ['Total Body Length (mm)', 'Pedipalp Length (mm)', 'Metasoma Length (mm)', 'Carapace Length (mm)', 'Telson Length (mm)', 'Pectin Teeth Count'],
            groups: [
                {{
                    label: 'Gigantometrus (Giant Black)',
                    raw: [142.5, 59.06, 40.2, 15.93, 12.46, 15.8],
                    normalized: [100, 100, 100, 100, 100, 49], // Normalized to max of each metric
                    color: '#c084fc',
                    bgColor: 'rgba(192, 132, 252, 0.2)'
                }},
                {{
                    label: 'Hottentotta (Rajasthan Giant)',
                    raw: [81.5, 25.8, 30.5, 8.4, 8.2, 32.1],
                    normalized: [57, 44, 76, 53, 66, 100],
                    color: '#38bdf8',
                    bgColor: 'rgba(56, 189, 248, 0.2)'
                }},
                {{
                    label: 'Hottentotta (Peninsular Standard)',
                    raw: [50.2, 16.4, 18.2, 6.1, 5.5, 26.5],
                    normalized: [35, 28, 45, 38, 44, 83],
                    color: '#10b981',
                    bgColor: 'rgba(16, 185, 129, 0.2)'
                }},
                {{
                    label: 'Buthoscorpio / Lychas',
                    raw: [32.6, 9.8, 11.8, 4.4, 3.8, 18.2],
                    normalized: [23, 17, 29, 28, 30, 57],
                    color: '#f59e0b',
                    bgColor: 'rgba(245, 158, 11, 0.2)'
                }}
            ]
        }};

        function renderTaxaComparisonChart(viewType) {{
            const ctx = document.getElementById('chart-taxa-comparison');
            if (!ctx) return;
            if (taxaChartInstance) {{
                taxaChartInstance.destroy();
            }}

            if (viewType === 'bar') {{
                // Simple Grouped Bar Chart (Easy to Interpret directly with mm/count values)
                taxaChartInstance = new Chart(ctx, {{
                    type: 'bar',
                    data: {{
                        labels: taxaComparisonData.labels,
                        datasets: taxaComparisonData.groups.map(g => ({{
                            label: g.label,
                            data: g.raw,
                            backgroundColor: g.color,
                            borderRadius: 4
                        }}))
                    }},
                    options: {{
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {{
                            legend: {{ position: 'top', labels: {{ boxWidth: 12, font: {{ size: 12, weight: '600' }} }} }},
                            tooltip: {{
                                callbacks: {{
                                    label: function(ctx) {{
                                        const unit = ctx.label.includes('Count') ? ' teeth' : ' mm';
                                        return `${{ctx.dataset.label}}: ${{ctx.raw}}${{unit}}`;
                                    }}
                                }}
                            }}
                        }},
                        scales: {{
                            y: {{
                                title: {{ display: true, text: 'Value (mm / tooth count)' }},
                                grid: {{ color: 'rgba(255,255,255,0.06)' }}
                            }},
                            x: {{
                                grid: {{ display: false }},
                                ticks: {{ font: {{ weight: '600' }} }}
                            }}
                        }}
                    }}
                }});
            }} else {{
                // Normalized 0-100% Spider/Radar Chart (Well-proportioned polygons)
                taxaChartInstance = new Chart(ctx, {{
                    type: 'radar',
                    data: {{
                        labels: taxaComparisonData.labels.map(l => l.replace(' (mm)', '').replace(' Count', '')),
                        datasets: taxaComparisonData.groups.map(g => ({{
                            label: g.label,
                            data: g.normalized,
                            borderColor: g.color,
                            backgroundColor: g.bgColor,
                            borderWidth: 2.5,
                            pointRadius: 4
                        }}))
                    }},
                    options: {{
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {{
                            legend: {{ position: 'top', labels: {{ boxWidth: 12, font: {{ size: 12, weight: '600' }} }} }},
                            tooltip: {{
                                callbacks: {{
                                    label: function(ctx) {{
                                        const grpIdx = ctx.datasetIndex;
                                        const itemIdx = ctx.dataIndex;
                                        const actualVal = taxaComparisonData.groups[grpIdx].raw[itemIdx];
                                        const unit = taxaComparisonData.labels[itemIdx].includes('Count') ? ' teeth' : ' mm';
                                        return `${{ctx.dataset.label}}: ${{actualVal}}${{unit}} (${{ctx.raw}}% of max)`;
                                    }}
                                }}
                            }}
                        }},
                        scales: {{
                            r: {{
                                min: 0,
                                max: 100,
                                ticks: {{ display: true, stepSize: 25, backdropColor: 'transparent', color: '#64748b', font: {{ size: 10 }} }},
                                angleLines: {{ color: 'rgba(255,255,255,0.1)' }},
                                grid: {{ color: 'rgba(255,255,255,0.08)' }},
                                pointLabels: {{ color: '#f8fafc', font: {{ size: 12, weight: '700' }} }}
                            }}
                        }}
                    }}
                }});
            }}
        }}

        function setTaxaView(viewType) {{
            currentTaxaView = viewType;
            document.getElementById('btn-view-bar').classList.toggle('active', viewType === 'bar');
            document.getElementById('btn-view-radar').classList.toggle('active', viewType === 'radar');
            renderTaxaComparisonChart(viewType);
        }}

        // Initialize Charts with Chart.js
        function initializeCharts() {{
            Chart.defaults.color = '#94a3b8';
            Chart.defaults.font.family = "'Plus Jakarta Sans', sans-serif";

            // 1. Regional Pie Chart
            const regCounts = {{}};
            rawDataset.forEach(r => {{
                regCounts[r.region_state] = (regCounts[r.region_state] || 0) + 1;
            }});

            new Chart(document.getElementById('chart-region-pie'), {{
                type: 'doughnut',
                data: {{
                    labels: Object.keys(regCounts),
                    datasets: [{{
                        data: Object.values(regCounts),
                        backgroundColor: [
                            '#38bdf8', '#818cf8', '#c084fc', '#f43f5e',
                            '#fb923c', '#f59e0b', '#10b981', '#14b8a6',
                            '#06b6d4', '#6366f1', '#64748b'
                        ],
                        borderWidth: 2,
                        borderColor: '#1a233a'
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{ position: 'right', labels: {{ boxWidth: 12, font: {{ size: 11 }} }} }}
                    }}
                }}
            }});

            // 2. Size Class Chart
            const sizeCounts = {{}};
            rawDataset.forEach(r => {{
                sizeCounts[r.size_class] = (sizeCounts[r.size_class] || 0) + 1;
            }});

            new Chart(document.getElementById('chart-size-class'), {{
                type: 'bar',
                data: {{
                    labels: Object.keys(sizeCounts),
                    datasets: [{{
                        label: 'Specimen Count',
                        data: Object.values(sizeCounts),
                        backgroundColor: ['#c084fc', '#38bdf8', '#818cf8', '#10b981', '#f59e0b', '#64748b'],
                        borderRadius: 6
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{ legend: {{ display: false }} }},
                    scales: {{
                        y: {{ grid: {{ color: 'rgba(255,255,255,0.05)' }} }},
                        x: {{ grid: {{ display: false }} }}
                    }}
                }}
            }});

            // 3. Taxa Comparison Bar Chart
            const taxaList = ['Hottentotta sp.', 'Gigantometrus', 'Buthoscorpio / Buthidae', 'Hottentotta tamulus', 'Lychas sp.', 'Isometrus sp.'];
            const taxaStats = taxaList.map(tx => {{
                const group = rawDataset.filter(r => r.genus_taxon === tx);
                const avg = key => {{
                    const vals = group.map(g => g[key]).filter(v => v !== null && v !== undefined);
                    return vals.length ? (vals.reduce((a,b)=>a+b,0)/vals.length).toFixed(2) : 0;
                }};
                return {{
                    taxon: tx,
                    tl: avg('total_length'),
                    pp: avg('pedipalp_pp'),
                    ml: avg('mesosoma_ml'),
                    cl: avg('carapace_length_cl')
                }};
            }});

            new Chart(document.getElementById('chart-taxa-bar'), {{
                type: 'bar',
                data: {{
                    labels: taxaStats.map(t => t.taxon),
                    datasets: [
                        {{ label: 'Total Length (tl)', data: taxaStats.map(t => t.tl), backgroundColor: '#38bdf8', borderRadius: 4 }},
                        {{ label: 'Pedipalp (pp)', data: taxaStats.map(t => t.pp), backgroundColor: '#818cf8', borderRadius: 4 }},
                        {{ label: 'Mesosoma (ml)', data: taxaStats.map(t => t.ml), backgroundColor: '#10b981', borderRadius: 4 }},
                        {{ label: 'Carapace L (cl)', data: taxaStats.map(t => t.cl), backgroundColor: '#f59e0b', borderRadius: 4 }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{ legend: {{ position: 'top' }} }},
                    scales: {{
                        y: {{ title: {{ display: true, text: 'Mean Length (mm)' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }},
                        x: {{ grid: {{ display: false }} }}
                    }}
                }}
            }});

            // 4. Regional Means Grouped Bar
            const topRegions = ['Rajasthan', 'Madhya Pradesh', 'Tamil Nadu', 'Karnataka', 'Maharashtra', 'Odisha', 'Gujarat'];
            const regStats = topRegions.map(rg => {{
                const grp = rawDataset.filter(r => r.region_state === rg);
                const avg = key => {{
                    const vals = grp.map(g => g[key]).filter(v => v !== null && v !== undefined);
                    return vals.length ? (vals.reduce((a,b)=>a+b,0)/vals.length).toFixed(1) : 0;
                }};
                return {{
                    region: rg,
                    tl: avg('total_length'),
                    pp: avg('pedipalp_pp'),
                    ml: avg('mesosoma_ml')
                }};
            }});

            new Chart(document.getElementById('chart-regional-means'), {{
                type: 'bar',
                data: {{
                    labels: regStats.map(r => r.region),
                    datasets: [
                        {{ label: 'Total Length (mm)', data: regStats.map(r => r.tl), backgroundColor: '#38bdf8', borderRadius: 4 }},
                        {{ label: 'Pedipalp Length (mm)', data: regStats.map(r => r.pp), backgroundColor: '#c084fc', borderRadius: 4 }},
                        {{ label: 'Mesosoma Length (mm)', data: regStats.map(r => r.ml), backgroundColor: '#10b981', borderRadius: 4 }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {{
                        y: {{ grid: {{ color: 'rgba(255,255,255,0.05)' }} }},
                        x: {{ grid: {{ display: false }} }}
                    }}
                }}
            }});

            // 5. Pectin Tooth Count Distribution Histogram
            const bins = ['<15', '15-19', '20-24 (♀ Mode)', '25-29', '30-34 (♂ Mode)', '35-39', '40+'];
            const pectinCountsL = [0, 0, 0, 0, 0, 0, 0];
            const pectinCountsR = [0, 0, 0, 0, 0, 0, 0];

            function getBinIdx(val) {{
                if (val < 15) return 0;
                if (val <= 19) return 1;
                if (val <= 24) return 2;
                if (val <= 29) return 3;
                if (val <= 34) return 4;
                if (val <= 39) return 5;
                return 6;
            }}

            rawDataset.forEach(r => {{
                if (r.pectin_count_l) pectinCountsL[getBinIdx(r.pectin_count_l)]++;
                if (r.pectin_count_r) pectinCountsR[getBinIdx(r.pectin_count_r)]++;
            }});

            new Chart(document.getElementById('chart-pectin-dist'), {{
                type: 'bar',
                data: {{
                    labels: bins,
                    datasets: [
                        {{ label: 'Left Pectine (L)', data: pectinCountsL, backgroundColor: '#f59e0b', borderRadius: 4 }},
                        {{ label: 'Right Pectine (R)', data: pectinCountsR, backgroundColor: '#38bdf8', borderRadius: 4 }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{ legend: {{ position: 'top' }} }},
                    scales: {{
                        y: {{ title: {{ display: true, text: 'Specimen Count' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }},
                        x: {{ grid: {{ display: false }} }}
                    }}
                }}
            }});

            // 6. Metasomal Progression (mt1 to mt5)
            const mtLabels = ['Seg 1 (mt1)', 'Seg 2 (mt2)', 'Seg 3 (mt3)', 'Seg 4 (mt4)', 'Seg 5 (mt5)'];
            const mtMeans = ['mt1', 'mt2', 'mt3', 'mt4', 'mt5'].map(k => {{
                const vals = rawDataset.map(r => r[k]).filter(v => v !== null && v !== undefined);
                return (vals.reduce((a,b)=>a+b,0)/vals.length).toFixed(2);
            }});
            const mtMaxs = ['mt1', 'mt2', 'mt3', 'mt4', 'mt5'].map(k => {{
                const vals = rawDataset.map(r => r[k]).filter(v => v !== null && v !== undefined);
                return Math.max(...vals).toFixed(2);
            }});

            new Chart(document.getElementById('chart-metasoma-progression'), {{
                type: 'bar',
                data: {{
                    labels: mtLabels,
                    datasets: [
                        {{ label: 'Mean Length (mm)', data: mtMeans, backgroundColor: '#10b981', borderRadius: 5 }},
                        {{ label: 'Maximum Length (mm)', data: mtMaxs, backgroundColor: '#38bdf8', borderRadius: 5 }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {{
                        y: {{ title: {{ display: true, text: 'Length (mm)' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }},
                        x: {{ grid: {{ display: false }} }}
                    }}
                }}
            }});

            // 7. Chela Proportions
            const chelaSegments = ['Manus (mn)', 'Movable Finger (mf)', 'Fixed Finger (ff)', 'Patella (pl)', 'Femur (fm)'];
            const chelaMeans = ['mannus_mn', 'movable_finger_mf', 'fixed_finger_ff', 'patella_pl', 'femur_fm'].map(k => {{
                const vals = rawDataset.map(r => r[k]).filter(v => v !== null && v !== undefined);
                return (vals.reduce((a,b)=>a+b,0)/vals.length).toFixed(2);
            }});

            new Chart(document.getElementById('chart-chela-proportions'), {{
                type: 'bar',
                data: {{
                    labels: chelaSegments,
                    datasets: [{{
                        label: 'Mean Segment Measurement (mm)',
                        data: chelaMeans,
                        backgroundColor: ['#818cf8', '#c084fc', '#38bdf8', '#10b981', '#f59e0b'],
                        borderRadius: 6
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{ legend: {{ display: false }} }},
                    scales: {{
                        y: {{ title: {{ display: true, text: 'Length (mm)' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }},
                        x: {{ grid: {{ display: false }} }}
                    }}
                }}
            }});

            // 8. Allometry Scatter (Body Length vs Pedipalp Length)
            const scatterPoints = rawDataset
                .filter(r => r.total_length && r.pedipalp_pp)
                .map(r => ({{ x: r.total_length, y: r.pedipalp_pp, id: r.specimen_id, taxon: r.genus_taxon }}));

            new Chart(document.getElementById('chart-allometry-scatter'), {{
                type: 'scatter',
                data: {{
                    datasets: [{{
                        label: 'Specimen Measurements (tl vs pp)',
                        data: scatterPoints,
                        backgroundColor: '#38bdf8',
                        borderColor: '#818cf8',
                        pointRadius: 4,
                        pointHoverRadius: 7
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        tooltip: {{
                            callbacks: {{
                                label: ctx => `${{ctx.raw.id}} (${{ctx.raw.taxon}}): TL ${{ctx.raw.x}}mm, PP ${{ctx.raw.y}}mm`
                            }}
                        }}
                    }},
                    scales: {{
                        x: {{ title: {{ display: true, text: 'Total Body Length (mm)' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }},
                        y: {{ title: {{ display: true, text: 'Pedipalp Length (mm)' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }}
                    }}
                }}
            }});

            // 9. Pectin Asymmetry Frequency
            const asymCounts = {{ '0 (Symmetric)': 0, '1 Tooth Diff': 0, '2-3 Teeth Diff': 0, '4+ Teeth Diff': 0 }};
            rawDataset.forEach(r => {{
                if (r.pectin_asymmetry !== null && r.pectin_asymmetry !== undefined) {{
                    if (r.pectin_asymmetry === 0) asymCounts['0 (Symmetric)']++;
                    else if (r.pectin_asymmetry === 1) asymCounts['1 Tooth Diff']++;
                    else if (r.pectin_asymmetry <= 3) asymCounts['2-3 Teeth Diff']++;
                    else asymCounts['4+ Teeth Diff']++;
                }}
            }});

            new Chart(document.getElementById('chart-pectin-asymmetry'), {{
                type: 'pie',
                data: {{
                    labels: Object.keys(asymCounts),
                    datasets: [{{
                        data: Object.values(asymCounts),
                        backgroundColor: ['#10b981', '#38bdf8', '#f59e0b', '#f43f5e'],
                        borderWidth: 2,
                        borderColor: '#1a233a'
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{ position: 'right', labels: {{ boxWidth: 12 }} }}
                    }}
                }}
            }});

            // 10. Initial Render of Taxa Comparison Chart
            renderTaxaComparisonChart('bar');

            // 11. Investigators Breakdown
            const auditorCounts = {{ 'RPR': 0, 'PSD': 0, 'YSR': 0, 'PSD, RPR': 0, 'PSD, YSR': 0, 'YSR, RPR': 0 }};
            rawDataset.forEach(r => {{
                if (r.morpho_by) {{
                    auditorCounts[r.morpho_by] = (auditorCounts[r.morpho_by] || 0) + 1;
                }}
            }});

            new Chart(document.getElementById('chart-investigators'), {{
                type: 'pie',
                data: {{
                    labels: Object.keys(auditorCounts),
                    datasets: [{{
                        data: Object.values(auditorCounts),
                        backgroundColor: ['#38bdf8', '#10b981', '#f59e0b', '#c084fc', '#818cf8', '#f43f5e'],
                        borderWidth: 2,
                        borderColor: '#1a233a'
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{ legend: {{ position: 'right', labels: {{ boxWidth: 10, font: {{ size: 10 }} }} }} }}
                }}
            }});

            // 12. Re-measurement Delta Distribution
            const deltas = rawDataset
                .filter(r => r.new_body_length && r.total_length)
                .map(r => Math.abs(r.new_body_length - r.total_length));

            const deltaBins = ['<1mm (Precise)', '1-3mm (Acceptable)', '3-6mm (Moderate)', '>6mm (Substantial)'];
            const deltaCounts = [0, 0, 0, 0];
            deltas.forEach(d => {{
                if (d < 1) deltaCounts[0]++;
                else if (d <= 3) deltaCounts[1]++;
                else if (d <= 6) deltaCounts[2]++;
                else deltaCounts[3]++;
            }});

            new Chart(document.getElementById('chart-remeasurement-delta'), {{
                type: 'bar',
                data: {{
                    labels: deltaBins,
                    datasets: [{{
                        label: 'Audit Count',
                        data: deltaCounts,
                        backgroundColor: ['#10b981', '#38bdf8', '#f59e0b', '#f43f5e'],
                        borderRadius: 4
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{ legend: {{ display: false }} }},
                    scales: {{
                        y: {{ grid: {{ color: 'rgba(255,255,255,0.05)' }} }},
                        x: {{ grid: {{ display: false }} }}
                    }}
                }}
            }});
        }}

        // Initialization
        document.addEventListener('DOMContentLoaded', () => {{
            populateMasterTable(rawDataset);
            populateSummaryTables();
            initializeCharts();
            selectAnatomyPart('carapace');
        }});
    </script>
</body>
</html>
"""

with open("/Users/sreyabondada/Downloads/Parth's workspace/Parth morphometrics/index.html", "w") as f:
    f.write(html_content)

print("Updated index.html successfully with main title and clear taxa comparison visuals!")
