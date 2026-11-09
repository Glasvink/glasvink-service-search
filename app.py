import streamlit as st
from pathlib import Path
from search_engine import semantic_search


# --------------------------------------------------
# 1. Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Glasvink – Service zoeken",
    page_icon="🪟",
    layout="centered"
)


# --------------------------------------------------
# 2. Glasvink styling
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #F7FAF7;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
}

h1, h2, h3 {
    color: #176B45 !important;
}

div.stButton > button,
div.stLinkButton > a {
    background-color: #176B45;
    color: white;
    border: 2px solid #F2C94C;
    border-radius: 10px;
    font-weight: bold;
    padding: 0.6rem 1.5rem;
}

div.stButton > button:hover,
div.stLinkButton > a:hover {
    background-color: #125638;
    color: white;
    border-color: #F2C94C;
}

div[data-testid="stTextInput"] input {
    border: 1px solid #176B45;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# 3. Display Glasvink logo
# --------------------------------------------------

logo_path = Path(__file__).parent / "glasvink_logo.png"

if logo_path.is_file():

    left, center, right = st.columns([1, 2, 1])

    with center:
        st.image(
            str(logo_path),
            width=420,
            alt="Glasvink logo"
        )

else:
    st.warning(
        "Glasvink logo niet gevonden. "
        "Controleer of glasvink_logo.png in de projectmap staat."
    )


# --------------------------------------------------
# 4. Page heading and introduction
# --------------------------------------------------

st.subheader(
    "De juiste glas- en kozijnservice vinden"
)

st.write(
    "Welke glas- of kozijnservice zoekt u? "
    "Typ uw vraag hieronder."
)


# --------------------------------------------------
# 5. Search input
# --------------------------------------------------

query = st.text_input(
    "Uw zoekopdracht",
    placeholder="Bijvoorbeeld: Ik zoek HR++ glas"
)


# --------------------------------------------------
# 6. Search button and search functionality
# --------------------------------------------------

if st.button("Zoeken", type="primary"):

    if not query.strip():

        st.warning(
            "Vul eerst een zoekopdracht in."
        )

    else:

        with st.spinner(
            "We zoeken de beste diensten voor u..."
        ):

            results = semantic_search(
                query.strip(),
                top_k=1,
                threshold=0.40
            )

        # ------------------------------------------
        # 7. Display search results
        # ------------------------------------------

        if results:

            st.subheader("Beste passende dienst")

            best_result = results[0]

            with st.container(border=True):

                st.markdown(
                    f"**{best_result['document']}**"
                )

                st.write(
                    "Wilt u meer informatie of een "
                    "vrijblijvende offerte?"
                )

                st.link_button(
                    "Neem contact op met Glasvink",
                    "mailto:info@glasvink.nl"
                )

        # ------------------------------------------
        # 8. No results found
        # ------------------------------------------

        else:

            st.info(
                "Geen passende diensten gevonden. "
                "Neem gerust contact op met Glasvink."
            )


# --------------------------------------------------
# 9. Footer
# --------------------------------------------------

st.divider()

st.markdown(
    "Heeft u vragen? Neem gerust contact met ons op via "
    "[info@glasvink.nl](mailto:info@glasvink.nl)."
)
