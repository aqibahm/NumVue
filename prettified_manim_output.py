def prettify_output(data):
    # Header
    output = "\n**CompletedProcess Details**:\n\n"

    # Args
    output += "- **Args**:\n"
    for arg in data["args"]:
        output += f"  - `{arg}`\n"
    output += "\n"

    # Return Code
    output += f"- **Return Code**: {data['returncode']}\n\n"

    # Stdout
    output += "- **stdout**:\n\n```\n"
    stdout_lines = data["stdout"].split("\n")
    for line in stdout_lines:
        line = line.strip()
        if line:
            if "ERROR" in line or "INFO" in line:
                date, log_type, content, source = line.split()
                output += f"[{date} {log_type}]: {content}\n"
                output += f"Source: {source.split(':')[0]}\n\n"
            else:
                output += f"{line}\n"
    output += "```\n\n"

    # Stderr
    output += "- **stderr**:\n\n```\n"
    stderr_lines = data["stderr"].split("\n")
    for line in stderr_lines:
        line = line.strip()
        if line:
            output += f"{line}\n"
    output += "```\n\n"

    return output


data = {
    "args": ['manim', '-qh', './utils/manim_scripts/sample_code.py', 'output_video'],
    "returncode": 0,
    "stdout": '''Manim Community v0.17.3
[09/29/23 22:59:56] ERROR                                                                                   module_ops.py:90
                                output_video is not in the script                                                           \n                                                                                                                            \n[09/29/23 22:59:57] INFO     Animation 0 : Using cached data (hash : 3522960179_103788008_1128061663)   cairo_renderer.py:78\n                    INFO     Animation 1 : Using cached data (hash : 996697702_3397463857_365116514)    cairo_renderer.py:78\n                    INFO     Combining to Movie file.                                               scene_file_writer.py:617\n                    INFO                                                                            scene_file_writer.py:736\n                             File ready at                                                                                  \n                             '/Users/aqibahmed/NumVue/media/videos/sample_code/1080p60/GeneratedCod                         \n                             e.mp4'                                                                                         \n                                                                                                                            \n                    INFO     Rendered GeneratedCode                                                             scene.py:241\n                             Played 2 animations                                                                            \n''',
    "stderr": '''
Animation 0: Create(VGroup of 100 submobjects):   0%|          | 0/1 [00:00<?, ?it/s]
                                                                                     \n'''
}

print(prettify_output(data))
