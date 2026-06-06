import pickle
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.project-title {
    text-align: center;
    font-size: 60px;
    font-weight: 800;
    background: linear-gradient(90deg,#00C9FF,#92FE9D);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
}

.project-subtitle {
    text-align: center;
    font-size: 20px;
    color: #B0B0B0;
    margin-bottom: 25px;
}

.movie-card {
    background: linear-gradient(135deg,#232526,#414345);
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 12px;
    border-left: 6px solid #00C9FF;
    box-shadow: 0px 4px 15px rgba(0,201,255,0.25);
}

.movie-name {
    color: #00E5FF;
    font-size: 22px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
movies = pickle.load(open(r'C:\Users\asus\Desktop\mmmc_project\movie_list.pkl', 'rb'))
similarity = pickle.load(open(r'C:\Users\asus\Desktop\mmmc_project\similarity.pkl', 'rb'))


# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommendations = []

    for i in distances[1:6]:
        recommendations.append(
            movies.iloc[i[0]]['title']
        )

    return recommendations

# ---------------- HEADER ----------------
st.markdown(
    """
    <div class="project-title">
        AI Movie Recommendation System
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="project-subtitle">
        Intelligent Movie Suggestions Using Machine Learning and Content-Based Filtering
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- METRICS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Movies Available", len(movies))

with col2:
    st.metric("Recommendations", "Top 5")

with col3:
    st.metric("Technique", "Content-Based")

st.divider()

# # ---------------- MOVIE SELECTION ----------------
# movie_list = movies['title'].values

# selected_movie = st.selectbox(
#     "Choose a Movie",
#     movie_list
# )

# ---------------- ABOUT PROJECT ----------------
with st.expander("About This Project"):
    st.write("""
    This Movie Recommendation System uses Content-Based Filtering
    to recommend similar movies based on movie features and similarity scores.

    Technologies Used:
    - Python
    - Pandas
    - Scikit-Learn
    - Streamlit

    Machine Learning Technique:
    - Feature Engineering
    - Cosine Similarity
    - Recommendation Systems
    """)

# ---------------- MOVIE SELECTION ----------------
movie_list = movies['title'].values
st.markdown("### 🔍 Search Your Favourite Movie")

selected_movie = st.selectbox(
    "Select a Movie",
    movie_list
)


# ---------------- BUTTON ----------------
if st.button("Generate Recommendations", use_container_width=True):

    recommendations = recommend(selected_movie)

    st.subheader("🎯 Recommended Movies")

    for idx, movie in enumerate(recommendations, start=1):
        st.markdown(
            f"""
            <div class="movie-card">
                <div class="movie-name">
                    #{idx} &nbsp; {movie}
                </div>
            </div>
            """,
            unsafe_allow_html=True
    )

st.divider()

st.caption(
    "Developed using Python, Machine Learning, Pandas, Scikit-Learn and Streamlit"
)