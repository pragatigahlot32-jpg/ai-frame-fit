
# import streamlit as st
# import tensorflow as tf
# import numpy as np
# import json
# from PIL import Image
# from pathlib import Path

# # =====================================
# # PAGE SETTINGS
# # =====================================

# st.set_page_config(
#     page_title="AI Glasses Recommendation",
#     page_icon="👓",
#     layout="wide"
# )

# # =====================================
# # PROJECT PATH
# # =====================================

# BASE_DIR = Path(__file__).parent
# FRAME_DIR = BASE_DIR / "frames"

# # =====================================
# # WEBSITE DESIGN
# # =====================================

# st.markdown("""
# <style>

# .stApp {
#     background: linear-gradient(
#         120deg,
#         #ffe4ef,
#         #e9d5ff
#     );
# }

# h1, h2, h3 {
#     color: #792c91;
# }

# .stButton button {
#     background-color: #a855a5;
#     color: white;
#     border-radius: 12px;
# }

# .stButton button:hover {
#     background-color: #792c91;
#     color: white;
# }

# .recommend-title {
#     color: #792c91;
#     font-size: 25px;
#     font-weight: bold;
# }

# </style>
# """, unsafe_allow_html=True)

# # =====================================
# # TITLE
# # =====================================

# st.title("👓 AI Glasses Recommendation")

# st.subheader(
#     "Find Perfect Glasses According To Your Face Shape"
# )

# st.write(
#     "Upload your photo and discover "
#     "the most suitable glasses frames for your face!"
# )

# st.markdown("---")

# # =====================================
# # LOAD MODELS
# # =====================================

# @st.cache_resource
# def load_models():

#     face_model = tf.keras.models.load_model(
#         BASE_DIR / "face_shape_model.keras"
#     )

#     glass_model = tf.keras.models.load_model(
#         BASE_DIR / "glass_model.keras"
#     )

#     return face_model, glass_model


# # =====================================
# # LOAD CLASS NAMES
# # =====================================

# @st.cache_data
# def load_classes():

#     with open(BASE_DIR / "classes.json", "r") as f:
#         face_classes = json.load(f)

#     with open(BASE_DIR / "classes2.json", "r") as f:
#         glass_classes = json.load(f)

#     return face_classes, glass_classes


# # =====================================
# # LOAD DATA
# # =====================================

# try:

#     face_model, glass_model = load_models()

#     face_classes, glass_classes = load_classes()

# except Exception as e:

#     st.error(f"Model loading error: {e}")
#     st.stop()


# # =====================================
# # LOCAL FRAME IMAGES
# # =====================================


# # =====================================
# # LOCAL FRAME IMAGES
# # =====================================

# import os

# FRAME_DIR = BASE_DIR / "frames"

# # Automatically find image files
# available_images = {}

# for file in os.listdir(FRAME_DIR):

#     if file.lower().endswith((".jpg", ".jpeg", ".png")):

#         key = file.lower().strip()

#         available_images[key] = FRAME_DIR / file


# def get_frame_image(filename):

#     # Ignore extra spaces and capitalization
#     key = filename.lower().strip()

#     if key in available_images:
#         return available_images[key]

#     # Find matching filename without spaces
#     for actual_name, path in available_images.items():

#         if actual_name.replace(" ", "") == key.replace(" ", ""):
#             return path

#     return None


# # =====================================
# # FRAME RECOMMENDATIONS
# # =====================================

# frames = {

#     "round": [
#         ("Rectangle Frames", "rectangle.jpg"),
#         ("Geometric Frames", "geometric.jpg"),
#         ("Wayfarer Frames", "wayfarer.jpg")
#     ],

#     "oval": [
#         ("Round Frames", "round.jpg"),
#         ("Cat Eye Frames", "cat eye.jpg"),
#         ("Square Frames", "square.jpg")
#     ],

#     "square": [
#         ("Round Frames", "round.jpg"),
#         ("Oval Frames", "oval.jpg"),
#         ("Cat Eye Frames", "cat eye.jpg")
#     ],

#     "heart": [
#         ("Oval Frames", "oval.jpg"),
#         ("Round Frames", "round.jpg"),
#         ("Aviator Frames", "Aviator.jpg")
#     ],

#     "oblong": [
#         ("Oversized Frames", "oversize.jpg"),
#         ("Aviator Frames", "Aviator.jpg"),
#         ("Cat Eye Frames", "cat eye.jpg")
#     ],

#     "diamond": [
#         ("Cat Eye Frames", "cat eye.jpg"),
#         ("Oval Frames", "oval.jpg"),
#         ("Browline Frames", "browline.jpg")
#     ]
# }

       




# # =====================================
# # IMAGE UPLOAD
# # =====================================

# st.header("📸 Upload Your Face Image")

# uploaded_file = st.file_uploader(
#     "Choose your image",
#     type=["jpg", "jpeg", "png"]
# )


# # =====================================
# # PREDICTION
# # =====================================

# if uploaded_file is not None:

#     try:

#         image = Image.open(uploaded_file).convert("RGB")

#         st.markdown("---")

#         col1, col2 = st.columns(2)

#         with col1:

#             st.image(
#                 image,
#                 caption="Your Uploaded Photo",
#                 use_container_width=True
#             )

#         # PREPROCESS IMAGE

#         img = image.resize((64, 64))

#         x = np.array(
#             img,
#             dtype=np.float32
#         )

#         x = np.expand_dims(x, axis=0)

#         # =================================
#         # AI PREDICTION
#         # =================================

#         with st.spinner("✨ AI is analyzing your face..."):

#             face_pred = face_model.predict(
#                 x,
#                 verbose=0
#             )

#             face_index = int(np.argmax(face_pred))

#             face_shape = str(
#                 face_classes[face_index]
#             )

#             glass_pred = glass_model.predict(
#                 x,
#                 verbose=0
#             )

#             glass_index = int(np.argmax(glass_pred))

#             glass_type = str(
#                 glass_classes[glass_index]
#             )

#         # =================================
#         # DISPLAY PREDICTION
#         # =================================

#         with col2:

#             st.header("✨ AI Prediction")

#             st.success(
#                 f"Face Shape: {face_shape}"
#             )

#             st.info(
#                 f"Glasses Category: {glass_type}"
#             )

#             face_confidence = round(
#                 float(np.max(face_pred)) * 100,
#                 2
#             )

#             glass_confidence = round(
#                 float(np.max(glass_pred)) * 100,
#                 2
#             )

#             st.write(
#                 "Face Shape Confidence:",
#                 f"{face_confidence}%"
#             )

#             st.progress(
#                 face_confidence / 100
#             )

#             st.write(
#                 "Glasses Confidence:",
#                 f"{glass_confidence}%"
#             )

#             st.progress(
#                 glass_confidence / 100
#             )

#         # =================================
#         # FRAME RECOMMENDATIONS
#         # =================================

#         shape = (
#             face_shape.lower()
#             .replace(" ", "")
#             .replace("_", "")
#         )

#         selected_frames = frames.get(
#             shape,
#             frames["oval"]
#         )

#         st.markdown("---")

#         st.header(
#             "💜 Your Recommended Glasses Frames"
#         )

#         st.write(
#             "These frames are recommended "
#             "according to your predicted face shape."
#         )

#         cols = st.columns(3)

#         for i, (name, filename) in enumerate(selected_frames):

#             image_path = FRAME_DIR / filename

#             with cols[i]:

#                 if image_path.exists():

#                     frame_image = Image.open(
#                         image_path
#                     )

#                     st.image(
#                         frame_image,
#                         caption=name,
#                         use_container_width=True
#                     )

#                     st.markdown(
#                         f"**{name}**"
#                     )

#                 else:

#                     st.warning(
#                         f"Image not found: {filename}"
#                     )

#         # =================================
#         # SUCCESS MESSAGE
#         # =================================

#         st.markdown("---")

#         st.success(
#             "💜 Your personalized glasses "
#             "recommendations are ready!"
#         )

#         st.caption(
#             "AI recommendations are suggestions "
#             "based on predicted face shape."
#         )

#     except Exception as e:

#         st.error(
#             f"Something went wrong: {e}"
#         )

# else:

#     st.info(
#         "👆 Please upload your face image "
#         "to get AI glasses recommendations."
#     )


import streamlit as st
import tensorflow as tf
import numpy as np
import json
from PIL import Image
from pathlib import Path

# =====================================
# PAGE SETTINGS
# =====================================

st.set_page_config(
    page_title="AI Glasses Recommendation",
    page_icon="👓",
    layout="wide"
)

# =====================================
# PROJECT PATH
# =====================================

BASE_DIR = Path(__file__).parent
FRAME_DIR = BASE_DIR / "frames"

# =====================================
# WEBSITE DESIGN
# =====================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        120deg,
        #ffe4ef,
        #e9d5ff
    );
}

h1, h2, h3 {
    color: #792c91;
}

.stButton button {
    background-color: #a855a5;
    color: white;
    border-radius: 12px;
}

.stButton button:hover {
    background-color: #792c91;
    color: white;
}

.recommend-title {
    color: #792c91;
    font-size: 25px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# TITLE
# =====================================

st.title("👓 AI Glasses Recommendation")

st.subheader(
    "Find Perfect Glasses According To Your Face Shape"
)

st.write(
    "Upload your photo and discover "
    "the most suitable glasses frames for your face!"
)

st.markdown("---")

# =====================================
# LOAD MODELS
# =====================================

@st.cache_resource
def load_models():

    face_model = tf.keras.models.load_model(
        BASE_DIR / "face_shape_model.keras"
    )

    glass_model = tf.keras.models.load_model(
        BASE_DIR / "glass_model.keras"
    )

    return face_model, glass_model


# =====================================
# LOAD CLASS NAMES
# =====================================

@st.cache_data
def load_classes():

    with open(BASE_DIR / "classes.json", "r") as f:
        face_classes = json.load(f)

    with open(BASE_DIR / "classes2.json", "r") as f:
        glass_classes = json.load(f)

    return face_classes, glass_classes


# =====================================
# LOAD DATA
# =====================================

try:

    face_model, glass_model = load_models()

    face_classes, glass_classes = load_classes()

except Exception as e:

    st.error(f"Model loading error: {e}")
    st.stop()


# =====================================
# LOCAL FRAME IMAGES
# =====================================

frames = {

    "round": [
        ("Rectangle Frames", r"C:\Users\nsp gaming laptop\OneDrive\Desktop\final streamlit\frames\rectangle.jpg"),
        ("Geometric Frames", r"C:\Users\nsp gaming laptop\OneDrive\Desktop\final streamlit\frames\geometric.jpg"),
        ("Wayfarer Frames", r"C:\Users\nsp gaming laptop\OneDrive\Desktop\final streamlit\frames\wayfarer.jpg")
    ],

    "oval": [
        ("Round Frames", r"C:\Users\nsp gaming laptop\OneDrive\Desktop\final streamlit\frames\round.jpg"),
        ("Cat Eye Frames", r"C:\Users\nsp gaming laptop\OneDrive\Desktop\final streamlit\frames\cat eye.jpg"),
        ("Square Frames", r"C:\Users\nsp gaming laptop\OneDrive\Desktop\final streamlit\frames\square.jpg")
    ],

    "square": [
        ("Round Frames", r"C:\Users\nsp gaming laptop\OneDrive\Desktop\final streamlit\frames\round.jpg"),
        ("Oval Frames", r"C:\Users\nsp gaming laptop\OneDrive\Desktop\final streamlit\frames\oval.jpg"),
        ("Cat Eye Frames", r"C:\Users\nsp gaming laptop\OneDrive\Desktop\final streamlit\frames\cat eye.jpg")
    ],

    "heart": [
        ("Oval Frames", r"C:\Users\nsp gaming laptop\OneDrive\Desktop\final streamlit\frames\oval.jpg"),
        ("Round Frames", r"C:\Users\nsp gaming laptop\OneDrive\Desktop\final streamlit\frames\round.jpg"),
        ("Aviator Frames", r"C:\Users\nsp gaming laptop\OneDrive\Desktop\final streamlit\frames\Aviator.jpg")
    ],

    "oblong": [
        ("Oversized Frames", r"C:\Users\nsp gaming laptop\OneDrive\Desktop\final streamlit\frames\oversize.jpg"),
        ("Aviator Frames", r"C:\Users\nsp gaming laptop\OneDrive\Desktop\final streamlit\frames\Aviator.jpg"),
        ("Cat Eye Frames", r"C:\Users\nsp gaming laptop\OneDrive\Desktop\final streamlit\frames\cat eye.jpg")
    ],

    "diamond": [
        ("Cat Eye Frames", r"C:\Users\nsp gaming laptop\OneDrive\Desktop\final streamlit\frames\cat eye.jpg"),
        ("Oval Frames", r"C:\Users\nsp gaming laptop\OneDrive\Desktop\final streamlit\frames\oval.jpg"),
        ("Browline Frames", r"C:\Users\nsp gaming laptop\OneDrive\Desktop\final streamlit\frames\browline.jpg")
    ]

}


# =====================================
# IMAGE UPLOAD
# =====================================

st.header("📸 Upload Your Face Image")

uploaded_file = st.file_uploader(
    "Choose your image",
    type=["jpg", "jpeg", "png"]
)


# =====================================
# PREDICTION
# =====================================

if uploaded_file is not None:

    try:

        image = Image.open(uploaded_file).convert("RGB")

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:

            st.image(
                image,
                caption="Your Uploaded Photo",
                use_container_width=True
            )

        # PREPROCESS IMAGE

        img = image.resize((64, 64))

        x = np.array(
            img,
            dtype=np.float32
        )

        x = np.expand_dims(x, axis=0)

        # =================================
        # AI PREDICTION
        # =================================

        with st.spinner("✨ AI is analyzing your face..."):

            face_pred = face_model.predict(
                x,
                verbose=0
            )

            face_index = int(np.argmax(face_pred))

            face_shape = str(
                face_classes[face_index]
            )

            glass_pred = glass_model.predict(
                x,
                verbose=0
            )

            glass_index = int(np.argmax(glass_pred))

            glass_type = str(
                glass_classes[glass_index]
            )

        # =================================
        # DISPLAY PREDICTION
        # =================================

        with col2:

            st.header("✨ AI Prediction")

            st.success(
                f"Face Shape: {face_shape}"
            )

            st.info(
                f"Glasses Category: {glass_type}"
            )

            face_confidence = round(
                float(np.max(face_pred)) * 100,
                2
            )

            glass_confidence = round(
                float(np.max(glass_pred)) * 100,
                2
            )

            st.write(
                "Face Shape Confidence:",
                f"{face_confidence}%"
            )

            st.progress(
                face_confidence / 100
            )

            st.write(
                "Glasses Confidence:",
                f"{glass_confidence}%"
            )

            st.progress(
                glass_confidence / 100
            )

        # =================================
        # FRAME RECOMMENDATIONS
        # =================================

        shape = (
            face_shape.lower()
            .replace(" ", "")
            .replace("_", "")
        )

        selected_frames = frames.get(
            shape,
            frames["oval"]
        )

        st.markdown("---")

        st.header(
            "💜 Your Recommended Glasses Frames"
        )

        st.write(
            "These frames are recommended "
            "according to your predicted face shape."
        )

        cols = st.columns(3)

        for i, (name, filename) in enumerate(selected_frames):

            image_path = FRAME_DIR / filename

            with cols[i]:

                if image_path.exists():

                    frame_image = Image.open(
                        image_path
                    )

                    st.image(
                        frame_image,
                        caption=name,
                        use_container_width=True
                    )

                    st.markdown(
                        f"**{name}**"
                    )

                else:

                    st.warning(
                        f"Image not found: {filename}"
                    )

        # =================================
        # SUCCESS MESSAGE
        # =================================

        st.markdown("---")

        st.success(
            "💜 Your personalized glasses "
            "recommendations are ready!"
        )

        st.caption(
            "AI recommendations are suggestions "
            "based on predicted face shape."
        )

    except Exception as e:

        st.error(
            f"Something went wrong: {e}"
        )

else:

    st.info(
        "👆 Please upload your face image "
        "to get AI glasses recommendations."
    )

