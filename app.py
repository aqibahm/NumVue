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

def wait_for_file(file_path, timeout=3):
    """
    Waits for a file to become available for up to `timeout` seconds.

    Args:
    - file_path (str): Path to the file you're waiting for.
    - timeout (int): Number of seconds to wait for the file. Default is 3 seconds.

    Returns:
    - bool: True if the file becomes available within the timeout, False otherwise.
    """
    end_time = time.time() + timeout
    while time.time() < end_time:
        if os.path.exists(file_path):
            return True
        time.sleep(0.1)  # Check every 100 milliseconds
    return False

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

    prompt = "Using Manim CE and Python, with the output inside ``` ```, without the import statement, leaving no lines of code outside the context of the Scene Class, and ensuring that all relevant library functions and elements are used to provide a comprehensive animation (including axes, lighting, transformation, motion, labels), generate only the scene class with all relevant import statements and helper functions, name the parent class 'GeneratedCode', use 'axes.plot()' and 'self.add(axes)' instead of '.get_graph()' for visualizing axes, use Create() instead of ShowCreation(), use ParametricFunction() instead of self.get_parametric_function(), uses Axes.add_coordinates() to add coordinate labels, starting the code as 'class GeneratedCode(ThreeDScene) (also, do not use a main function for anything, and add the statements 'config.max_files_cached = 1000' and 'import numpy as np' at the top of the file. Ensure that the result is an animation. For t_range or range parameters, pass an np.array(start, end, step) object. When making graphs from axes, use axes.plot() instead of axes.get_graph(). For plotting parametric functions, use this notation 'axes.plot(lambda x: f(x), x_range=[start, stop], use_smoothing=True)' to denote the plotted function. If the prompt has a function, ensure that the function is shown as being plotted over time. Include the following for axes instantiation: x_range = [], y_range=[], tips=bool, axis_config={'include_numbers': True}, y_axis_config= {}. Ensure that play() is invoked for all objects. Do not use any variation of the 'main' or '__main__' function to render the animation. The returned code should only have the Scene class. For obtaining a function's points, only use lambda functions. Use only 'Mobjects', such as Dot, Line, Text, etc. Assume that the script is called from the terminal, so do not include 'if __name__ == __main__: GeneratedCode().render()', the rendering occurs separately from the code.):' "
    st.session_state.messages.append({"role": "assistant", "content": prompt})
    st.session_state.messages.append({"role": "user", "content": prompt_})
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
            file.write("import numpy as np\n")
            file.write("from manim import *\n")
            file.write("config.max_files_cached = 1000\n")

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

def run_manim(script_path, output_path, quality="ql"):
    """
    Run a Manim script and render the video output to a specified path without playing it.

    Args:
    - script_path (str): Path to the Manim script to be executed.
    - output_path (str): Directory where the rendered video will be saved.
    - quality (str): Quality of the rendered video (e.g., "ql" for low quality).

    Returns:
    - tuple: stdout and stderr of the executed script.
    """
    if os.path.exists(output_path):
        os.remove(output_path)

    cmd = [
        "manim",
        "-o",
        output_path,
        f"-{quality}",
        script_path,
        "GeneratedCode"
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        print(f"Manim script execution failed with error: {e}")
        return e.stdout, e.stderr

def manim_viewer():
    manim_script_path = "./utils/manim_scripts/sample_code.py"
    class_name = extract_class_name(manim_script_path)
    video_path = "./media/videos/sample_code/1080p60/" + class_name.strip() + ".mp4"

    # Streamlit app title
    st.title("Voilà!")

    # Streamlit widgets for user interaction
    if st.button("Bake Animation 🎂"):
        # Check if the user provided a valid Manim script path

        print("Video Path: ", video_path)
        if os.path.exists(video_path):
            os.remove(video_path)

        # Run the Manim script in a subprocess
        # script_command = ["manim", "-o", video_path, "-qh", manim_script_path]
        with st.spinner("Baking animation!"):
            # Example usage:
            stdout, stderr = run_manim(manim_script_path, "GeneratedCode", "qh")
            print("STDOUT:", stdout)
            print("STDERR:", stderr)
            # result = subprocess.run(script_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text = True)
            # # TODO - Fix this:
            # print(result.stdout)

        file_available = wait_for_file(video_path)
        if file_available:
            st.text("Freshly baked, for you.")
            print("File is available!")
            with st.expander("Cake"):
                st.video(video_path)
        else:
            print("File not found after waiting for 3 seconds.")


def chat_input(prompt_):
    msg = create_chat_model(openai_api_key, prompt_)

    process_gpt_response(msg)

    filename = './utils/manim_scripts/sample_code.py'

    st.session_state["show_manim_viewer"] = True
    st.session_state["show_chat_input"] = False
    print("Current st.session_state['show_manim_viewer']", st.session_state['show_manim_viewer'], "of type ", type(st.session_state["show_manim_viewer"]))

    class_name = extract_class_name(filename)

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



