import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from pathlib import Path
from storage import load_expenses, save_expense, save_all_expenses
from expense_manager import create_expense
from ml_categorizer import predict_category
from analytics import (
    spending_overview,
    category_breakdown,
    monthly_breakdown,
    detect_unusual_expenses
)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Smart Expense Analyzer",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# PREMIUM DARK THEME
# --------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 15% 0%, rgba(16,185,129,0.13) 0%, transparent 38%),
        radial-gradient(ellipse at 90% 10%, rgba(214,183,121,0.08) 0%, transparent 32%),
        #090D0B;
    color: #F5F5F0;
}

[data-testid="stHeader"] {
    background: rgba(8, 13, 25, 0.75);
}

.block-container {
    padding-top: 2.2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111A15, #0B100D);
    border-right: 1px solid rgba(148, 163, 184, 0.12);
}

[data-testid="stSidebar"] * {
    color: #F5F5F0;
}

h1, h2, h3 {
    color: #F5F5F0 !important;
    letter-spacing: -0.7px;
}

p, label {
    color: #B7C2B9;
}

.hero {
    padding: 25px 28px;
    border: 1px solid rgba(148, 163, 184, 0.16);
    border-radius: 22px;
    background: linear-gradient(
        115deg,
        rgba(16, 185, 129, 0.12),
        rgba(214, 183, 121, 0.08)
    );
    margin-bottom: 25px;
}

.hero-label {
    color: #D6B779;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
}

.hero-title {
    font-size: 32px;
    font-weight: 800;
    color: #ffffff;
    margin-top: 8px;
}

.hero-subtitle {
    color: #a9bad2;
    font-size: 14px;
    margin-top: 7px;
}

[data-testid="stMetric"] {
    background: linear-gradient(
        145deg,
        rgba(21, 29, 25, 0.96),
        rgba(17, 26, 21, 0.98)
    );
    border: 1px solid rgba(16, 185, 129, 0.20);
    padding: 19px 20px;
    border-radius: 17px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.17);
    transition: all 0.25s ease;
}

[data-testid="stMetric"]:hover {
    border-color: rgba(16, 185, 129, 0.75);
    transform: translateY(-4px);
    box-shadow: 0 12px 35px rgba(16, 185, 129, 0.12);
}

[data-testid="stMetricLabel"] {
    color: #A8B5AA !important;
}

[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-weight: 800;
}

[data-testid="stPlotlyChart"] {
    background: rgba(16, 27, 47, 0.75);
    border: 1px solid rgba(148, 163, 184, 0.13);
    border-radius: 18px;
    padding: 10px;
}

div.stButton > button {
    border: 1px solid rgba(56, 189, 248, 0.3);
    border-radius: 10px;
    background: linear-gradient(110deg, #10B981, #D6B779);
    color: white;
    font-weight: 600;
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    border-color: #D6B779;
    box-shadow: 0 0 20px rgba(16, 185, 129, 0.25);
    transform: translateY(-2px);
}

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"],
.stDateInput input {
    background: #111c30 !important;
    color: white !important;
    border-color: #34463B !important;
    border-radius: 9px !important;
}

[data-testid="stDataFrame"] {
    border: 1px solid rgba(148, 163, 184, 0.17);
    border-radius: 14px;
    overflow: hidden;
}

.section-heading {
    font-size: 19px;
    font-weight: 700;
    color: #F5F5F0;
    margin: 14px 0 12px 0;
}

.insight-card {
    background: linear-gradient(
        120deg,
        rgba(21, 38, 29, 0.92),
        rgba(48, 43, 29, 0.55)
    );
    border: 1px solid rgba(56, 189, 248, 0.2);
    border-radius: 15px;
    padding: 17px;
    margin-bottom: 12px;
}

.small-muted {
    color: #9BA99F;
    font-size: 12px;
}

hr {
    border-color: rgba(148, 163, 184, 0.14);
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# DATA
# --------------------------------------------------

expenses = load_expenses()

CATEGORIES = [
    "Food",
    "Transport",
    "Bills",
    "Shopping",
    "Health",
    "Education",
    "Entertainment"
]

overview = spending_overview(expenses)
category_data = category_breakdown(expenses)
monthly_data = monthly_breakdown(expenses)
unusual = detect_unusual_expenses(expenses)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown("## 💎 Smart Analyzer")
    st.caption("PERSONAL FINANCE INTELLIGENCE")

    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "Overview",
            "Transactions",
            "AI Insights"
        ],
        label_visibility="visible"
    )

    st.divider()

    st.markdown("### ➕ Quick Add Expense")

    with st.form("quick_add_form"):

        amount = st.number_input(
            "Amount (PKR)",
            min_value=1.0,
            step=100.0
        )

        description = st.text_input(
            "Description",
            placeholder="e.g. Uber ride"
        )

        category = st.selectbox(
            "Category",
            CATEGORIES
        )

        ai_save = st.form_submit_button(
            "✨ Predict with AI & Save",
            width="stretch"
        )

        manual_save = st.form_submit_button(
            "Save Selected Category",
            width="stretch"
        )

        if ai_save or manual_save:

            if not description.strip():
                st.error("Please enter a description.")

            else:
                try:

                    if ai_save:
                        final_category = predict_category(description)
                    else:
                        final_category = category

                    new_expense = create_expense(
                        amount,
                        final_category,
                        description
                    )

                    save_expense(new_expense)

                    st.success(
                        f"Saved successfully: {final_category}"
                    )

                    st.rerun()

                except Exception as error:
                    st.error(f"Unable to save expense: {error}")

    st.divider()

    st.markdown(
        '<div class="small-muted">BUILT WITH PYTHON · ML · STREAMLIT</div>',
        unsafe_allow_html=True
    )


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="hero">
    <div class="hero-label">PERSONAL FINANCE INTELLIGENCE</div>
    <div class="hero-title">Smart Expense Analyzer 💎</div>
    <div class="hero-subtitle">
        Understand your spending. Discover patterns.
        Make smarter financial decisions.
    </div>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# OVERVIEW PAGE
# --------------------------------------------------

if page == "Overview":

    st.markdown(
        '<div class="section-heading">Financial Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "TOTAL SPENDING",
        f"PKR {overview['total']:,.0f}"
    )

    col2.metric(
        "AVERAGE EXPENSE",
        f"PKR {overview['average']:,.0f}"
    )

    col3.metric(
        "TRANSACTIONS",
        overview["count"]
    )

    col4.metric(
        "TOP CATEGORY",
        overview["highest_category"] or "N/A"
    )

    st.divider()

    left, right = st.columns([1, 1])

    # CATEGORY DONUT
    with left:

        st.markdown("### Spending Distribution")

        if category_data:

            fig = go.Figure(
                data=[
                    go.Pie(
                        labels=list(category_data.keys()),
                        values=list(category_data.values()),
                        hole=0.68,
                        textinfo="percent",
                        hovertemplate=(
                            "<b>%{label}</b><br>"
                            "Amount: PKR %{value:,.0f}<br>"
                            "Share: %{percent}"
                            "<extra></extra>"
                        ),
                        marker=dict(
                            colors=["#10B981", "#D6B779", "#78C9A5", "#537B63", "#A6B89D", "#8D7954", "#DCE8D8"],
                            line=dict(
                                color="#090D0B",
                                width=3
                            )
                        )
                    )
                ]
            )

            fig.update_layout(
                template="plotly_dark",
                colorway=["#10B981", "#D6B779", "#78C9A5", "#537B63", "#A6B89D"],
                font=dict(color="#F5F5F0"),
                height=340,
                showlegend=True,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                margin=dict(l=10, r=10, t=20, b=10),
                legend=dict(
                    orientation="h",
                    y=-0.12
                )
            )

            st.plotly_chart(
                fig,
                width="stretch",
                config={"displayModeBar": False}
            )

        else:
            st.info("Add expenses to see category distribution.")

    # MONTHLY BAR CHART
    with right:

        st.markdown("### Monthly Spending Trend")

        if monthly_data:

            months = list(monthly_data.keys())
            values = list(monthly_data.values())

            fig = go.Figure()

            fig.add_trace(
                go.Bar(
                    x=months,
                    y=values,
                    marker=dict(
                        color=values,
                        colorscale=[
                            [0, "#10B981"],
                            [0.5, "#6366f1"],
                            [1, "#a78bfa"]
                        ],
                        line=dict(width=0)
                    ),
                    hovertemplate=(
                        "<b>%{x}</b><br>"
                        "Spending: PKR %{y:,.0f}"
                        "<extra></extra>"
                    )
                )
            )

            fig.update_layout(
                template="plotly_dark",
                colorway=["#10B981", "#D6B779", "#78C9A5", "#537B63", "#A6B89D"],
                font=dict(color="#F5F5F0"),
                height=340,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                margin=dict(l=15, r=15, t=20, b=15),
                yaxis_title="Amount (PKR)",
                xaxis_title="Month",
                showlegend=False
            )

            st.plotly_chart(
                fig,
                width="stretch",
                config={"displayModeBar": False}
            )

        else:
            st.info("Monthly analytics will appear here.")

    st.divider()

    st.markdown("### Recent Transactions")

    if expenses:

        recent = pd.DataFrame(expenses[-5:][::-1])

        st.dataframe(
            recent,
            width="stretch",
            hide_index=True
        )

    else:
        st.info("No transactions recorded yet.")


# --------------------------------------------------
# TRANSACTIONS PAGE
# --------------------------------------------------

elif page == "Transactions":

    st.markdown("## 📋 Transaction Management")
    st.caption("Search, filter, export and manage your expenses.")

    if expenses:

        df = pd.DataFrame(expenses)

        search = st.text_input(
            "🔎 Search description",
            placeholder="Search expenses..."
        )

        available_categories = [
            "All"
        ] + sorted(df["category"].unique().tolist())

        selected_filter = st.selectbox(
            "Filter by category",
            available_categories
        )

        filtered = df.copy()

        if search:
            filtered = filtered[
                filtered["description"].str.contains(
                    search,
                    case=False,
                    na=False
                )
            ]

        if selected_filter != "All":
            filtered = filtered[
                filtered["category"] == selected_filter
            ]

        st.metric(
            "Filtered Spending",
            f"PKR {filtered['amount'].sum():,.2f}"
        )

        st.dataframe(
            filtered,
            width="stretch",
            hide_index=True
        )

        csv_data = filtered.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇️ Export Filtered CSV",
            data=csv_data,
            file_name="smart_expense_report.csv",
            mime="text/csv",
            width="stretch"
        )

        st.divider()

        st.markdown("### Delete a Transaction")

        options = {
            (
                f"{i} | {item['date']} | "
                f"{item['description']} | "
                f"PKR {float(item['amount']):,.0f}"
            ): i
            for i, item in enumerate(expenses)
        }

        selected_transaction = st.selectbox(
            "Select transaction",
            list(options.keys())
        )

        if st.button(
            "🗑️ Delete Selected Transaction",
            type="primary"
        ):

            index = options[selected_transaction]

            updated_expenses = [
                item
                for i, item in enumerate(expenses)
                if i != index
            ]

            save_all_expenses(updated_expenses)

            st.success("Transaction deleted successfully.")
            st.rerun()

    else:
        st.info("No transactions available yet.")


# --------------------------------------------------
# AI INSIGHTS PAGE
# --------------------------------------------------

elif page == "AI Insights":

    st.markdown("## 🧠 AI Financial Intelligence")
    st.caption("Explore spending patterns and unusual transactions.")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Category Intelligence")

        if category_data:

            highest = max(
                category_data,
                key=category_data.get
            )

            st.markdown(
                f"""
                <div class="insight-card">
                    <div class="small-muted">HIGHEST SPENDING CATEGORY</div>
                    <h2>{highest}</h2>
                    <h3>PKR {category_data[highest]:,.2f}</h3>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                f"You have recorded {overview['count']} expenses "
                f"with total spending of PKR {overview['total']:,.2f}."
            )

        else:
            st.info("Add expenses to generate insights.")

    with col2:

        st.markdown("### Unusual Expense Detection")

        if unusual:

            st.warning(
                f"{len(unusual)} unusual transaction(s) detected."
            )

            for item in unusual:

                st.markdown(
                    f"""
                    <div class="insight-card">
                        <b>{item['description']}</b>
                        <h3>PKR {float(item['amount']):,.2f}</h3>
                        <span class="small-muted">
                            {item['category']} · {item['date']}
                        </span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.success(
                "No unusual expenses detected by the current rule."
            )

            st.caption(
                "Note: Current detection uses a simple average-based "
                "threshold, not a trained anomaly-detection model."
            )

    st.divider()

    st.markdown("### AI Expense Category Predictor")

    test_description = st.text_input(
        "Describe an expense",
        placeholder="e.g. Monthly electricity payment"
    )

    if st.button("Predict Expense Category"):

        if test_description.strip():

            try:
                prediction = predict_category(test_description)

                st.success(
                    f"Predicted category: **{prediction}**"
                )

            except Exception as error:
                st.error(f"Prediction failed: {error}")

        else:
            st.warning("Enter an expense description first.")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown(
    """
    <div style="text-align:center; padding:12px;">
        <div style="color:#D6B779; font-weight:700;">
            SMART EXPENSE ANALYZER
        </div>
        <div class="small-muted">
            Python · Scikit-learn · Plotly · Streamlit
        </div>
        <div class="small-muted">
            AI-powered personal finance analytics
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
