/* ---------------- GLOBAL THEME ---------------- */
body {
    background-color: #0e1117;
    color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
}

/* ---------------- MAIN CONTAINER ---------------- */
.main {
    background: linear-gradient(135deg, #0e1117, #111827);
}

/* ---------------- HEADINGS ---------------- */
h1, h2, h3 {
    color: #2ecc71;
    font-weight: 700;
}

/* ---------------- METRIC CARDS ---------------- */
[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}

/* ---------------- BUTTON ---------------- */
.stButton > button {
    background: linear-gradient(90deg, #2ecc71, #27ae60);
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
    transition: 0.3s ease;
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 15px rgba(46, 204, 113, 0.5);
}

/* ---------------- SIDEBAR ---------------- */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* ---------------- INPUT BOX ---------------- */
input {
    border-radius: 10px !important;
    border: 1px solid #2ecc71 !important;
}

/* ---------------- INFO BOXES ---------------- */
.stAlert {
    border-radius: 12px;
}

/* ---------------- FOOTER ---------------- */
footer {
    visibility: hidden;
}

/* ---------------- CHART AREA ---------------- */
.plot-container {
    background: rgba(255,255,255,0.03);
    padding: 10px;
    border-radius: 12px;
}
