# To use the footer, simply call footer() at the end of your Streamlit app.
# footer.py
import streamlit as st
from htbuilder import HtmlElement, img, a, br, styles


def image(src, **style):
    return img(src=src, style=styles(**style))


def link(url, text_or_image, **style):
    return a(_href=url, _target="_blank", style=styles(**style))(text_or_image)


def layout(*args):
    style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stApp { padding-bottom: 180px; }  /* ensures content doesn’t hide behind footer */

        /* Footer style */
        .custom-footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background: #333;  /* light gray background */
            box-shadow: 0 -2px 8px rgba(0,0,0,0.1); /* subtle shadow */
            # color: #333;
            text-align: center;
            padding: 12px 10px;
            font-size: 14px;
            z-index: 9999;
        }

        a { text-decoration: none; color: #0A66C2; transition: 0.3s; }
        a:hover { color: #FF4B4B; }
        img { vertical-align: middle; margin: 0 4px; }
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)

    body_html = ""
    for arg in args:
        if isinstance(arg, str):
            body_html += arg
        else:
            body_html += str(arg)

    footer_html = f'<div class="custom-footer">{body_html}</div>'
    st.markdown(footer_html, unsafe_allow_html=True)


def footer():
    myargs = [
        "Developed by Sahil Barke | Data Source: ",
        link(
            "https://huggingface.co/datasets/adarshzolekar/foods-nutrition-dataset",
            "HuggingFace",
        ),
        br(),
        "Made with ❤️ using Streamlit",
        br(),
        link(
            "https://github.com/sahilbarke",
            image(
                "https://cdn-icons-png.flaticon.com/512/25/25231.png",
                width="20px",
                height="20px",
            ),
        ),
        " | ",
        link(
            "https://www.linkedin.com/in/sahil-barke/",
            image(
                "https://cdn-icons-png.flaticon.com/512/174/174857.png",
                width="20px",
                height="20px",
            ),
        ),
        " | ",
        link(
            "https://twitter.com/yourusername",
            image(
                "https://cdn-icons-png.flaticon.com/512/733/733579.png",
                width="20px",
                height="20px",
            ),
        ),
    ]
    layout(*myargs)
