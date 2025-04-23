import streamlit as st

hq_bonus = 1.2

stats_col, recipe_col = st.columns([0.3, 0.7])
with stats_col:
    stats_container = st.container(border=True)
    cms = stats_container.text_input("Craftsmanship")
    ctl = stats_container.text_input("Control")
    cp = stats_container.text_input("CP")

with recipe_col:
    recipe_container = st.container(border=True)
    recipe_col1, recipe_col2 = recipe_container.columns([0.1, 0.9])
    with recipe_col1:
        recipe_image = st.image(
            "https://i.redd.it/n4ekwnitpdsa1.jpg", use_container_width=True
        )
    with recipe_col2:
        recipe_name = st.selectbox("Choose a recipe", ("r1", "r2"))
    progress_container = st.container(border=True)
    progress = progress_container.progress(value=0, text="Progress")
    quality = progress_container.progress(value=0, text="Quality")
actions_container = st.container(border=True)
current_sim = actions_container.container(border=True, height=500)
action_list = actions_container.container(border=True)
action_col1, action_col2, action_col3, action_col4 = action_list.columns(4)
with action_col1:
    crop = st.image("https://i.redd.it/n4ekwnitpdsa1.jpg", use_container_width=True)
with action_col2:
    crop2 = st.image("https://i.redd.it/n4ekwnitpdsa1.jpg", use_container_width=True)
