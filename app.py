import subprocess
import os
import openai
import streamlit as st
import re
import time

# 1. Wire manim output to GPT in case of errors.
# 2. Visit docs to learn more about manim command verbosity.

# Helper Functions:
openai_api_key = st.secrets["OPENAI_API_KEY"]

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

if "first_run" not in st.session_state:
    st.session_state["first_run"] = True

if st.session_state["first_run"]:
    video_path = "./media/videos/sample_code/1080p60/GeneratedCode.mp4"
    if os.path.exists(video_path):
        os.remove(video_path)
        print("Existing video file removed for first run.")

# Visual Controls:
if "show_manim_viewer" not in st.session_state:
    st.session_state["show_manim_viewer"] = False
    print("Current st.session_state['show_manim_viewer']", st.session_state['show_manim_viewer'], "of type ", type(st.session_state["show_manim_viewer"]))

if "show_chat_input" not in st.session_state:
    st.session_state["show_chat_input"] = True
    print("Current st.session_state['show_manim_viewer']", st.session_state['show_manim_viewer'], "of type ", type(st.session_state["show_manim_viewer"]))

# if st.session_state.messages:
    # st.chat_message(st.session_state.messages[-1]["role"]).write(st.session_state.messages[-1]["content"])

# TODO:
# 1. Add st.status()
# 2. Create hierarchy of animation elements in manim.
# 3. Extract animation requirements from prompt.
# 4. Based on hierarchical animation specifics, Langchain parser relevant manim docs to extract relevant elements and their syntax.
# 5. Produce code using the relevant docs, including all the elements extracted in step 2.
# 6. Return animation video.
# 7. Return manim verbose logs.

def extract_code(text):
    pattern = r'```python(.*?)```'
    matches = re.findall(pattern, text, re.DOTALL)
    return matches

def search_file_for_string(filename, target_string):
    matched_lines = []

    with open(filename, 'r') as file:
        # Read each line
        for line in file:
            if target_string in line:
                matched_lines.append(line)
            print(line, end='')
    return matched_lines

def create_chat_model(openai_api_key, prompt_):
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key

    prompt = "Using Manim CE and Python, generate only the scene class with all relevant import statements, use 'axes.plot()' and 'self.add(axes)' instead of 'self.get_graph()' for visualizing axes, use Create() instead of ShowCreation(), use ParametricFunction() instead of self.get_parametric_function(), uses Axes.add_coordinates() to add coordinate labels, starting the code as 'class GeneratedCode(ThreeDScene):' " + prompt_

    st.session_state.messages.append({"role": "user", "content": prompt})
    # st.chat_message("user").write(prompt_)

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", temperature = 0, messages=st.session_state.messages)

    return response.choices[0].message

def process_gpt_response(msg):
    print(msg)
    codes = extract_code(msg["content"])
    for code in codes:
        print(code.strip())
        print('------')
        print("Extracted code data type: ", type(codes))

    # Create or overwrite a new Python file and write the string to it
        with open('./utils/manim_scripts/sample_code.py', 'w') as file:
            for code in codes:
                file.write(code.strip())

        print("File 'new_file.py' has been written.")

def extract_class_name(filename):
    target = 'class'
    matches = search_file_for_string(filename, target)

    if matches:
        print(f"\n\nFound '{target}' in the following lines:")
        for line in matches:
            print("\n", line)
    else:
        print(f"'{target}' not found in {filename}.")

    # Naive implementation for now:
    class_name = matches[0].split(' ')[1].split('(')[0]
    if class_name or class_name != '':
        print("\n Class Name: ", class_name)
        # Class name found in GPT response, show manim_viewer
        return class_name

    else:
        raise Exception('The variable does not exist.')

def manim_viewer():
    # This is hardcoded for now:
    class_name = "GeneratedCode"

    # Streamlit app title
    st.title("Voilà!")

    # Streamlit widgets for user interaction
    if st.button("Bake Animation 🎂"):
        # Check if the user provided a valid Manim script path

        manim_script_path = "./utils/manim_scripts/sample_code.py"
        video_path = "./media/videos/sample_code/1080p60/" + class_name.strip() + ".mp4"
        print("Video Path: ", video_path)
        if os.path.exists(video_path):
            os.remove(video_path)

        # Run the Manim script in a subprocess
        with subprocess.Popen(["manim", "-qh", manim_script_path, "output_video"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text = True) as process:
            # Continuously check if the video animation is ready
            with st.spinner("Baking animation!"):
                while process.poll() is None:
                    continue
                # Show progress indicator in Streamlit
            st.text("Freshly baked, for you.")

        print(video_path)
        print(os.getcwd())
        # Check the subprocess return code (0 means success)
        if os.path.exists(video_path):
            print("File Exists!")
            with st.expander("Cake"):
                st.video(video_path)
        else:
            print("\nVideo file not found.")


def chat_input(prompt_):
    msg = create_chat_model(openai_api_key, prompt_)

    process_gpt_response(msg)

    filename = './utils/manim_scripts/sample_code.py'
    class_name = extract_class_name(filename)
    st.session_state["show_manim_viewer"] = True
    st.session_state["show_chat_input"] = False
    print("Current st.session_state['show_manim_viewer']", st.session_state['show_manim_viewer'], "of type ", type(st.session_state["show_manim_viewer"]))

    if not class_name:
        raise Exception("Relevant class not found inside generated code.")

    st.experimental_rerun()

def reset_view():
    st.session_state["show_chat_input"] = True
    st.session_state["show_manim_viewer"] = False
    st.session_state["first_run"] = False

st.title("👁️ NumVue")

if st.session_state["show_chat_input"]:
    prompt_ = st.text_input("What shall we imagine?")
    submit_button = st.button("Imagine!")
    if submit_button:
        if prompt_:
            with st.spinner("Crafting animation!"):
                chat_input(prompt_)
        else:
            st.error("Please enter a description and try again.")

if st.session_state["show_manim_viewer"]:
    manim_viewer()

    if st.button("Re-Imagine"):
        reset_view()
        st.experimental_rerun()



