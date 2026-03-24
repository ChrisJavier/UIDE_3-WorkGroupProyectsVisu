# ── Colors ─────────────────────────────────────────────────────────────────────
Colors = {
    "bg":      "#0f1117",
    "card":    "#1a1d27",
    "border":  "#2a2d3e",
    "primary": "#6c63ff",
    "success": "#00d4aa",
    "warning": "#ffd166",
    "danger":  "#ef476f",
    "text":    "#e8eaf6",
    "muted":   "#8b8fa8",
}

LAYOUT_BASE = dict(
    plot_bgcolor  = Colors["card"],
    paper_bgcolor = Colors["card"],
    font          = dict(color=Colors["text"], family="Inter, sans-serif", size=12),
    colorway      = [Colors["primary"], Colors["success"], Colors["warning"],
                     Colors["danger"], "#48bfe3", "#f4a261"],
    xaxis         = dict(gridcolor=Colors["border"], linecolor=Colors["border"]),
    yaxis         = dict(gridcolor=Colors["border"], linecolor=Colors["border"]),
    legend        = dict(bgcolor=Colors["card"], bordercolor=Colors["border"]),
    margin        = dict(l=40, r=20, t=50, b=40),
)