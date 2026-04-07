import gradio as gr

def parse_input(user_text):
    if not user_text.strip():
        return None, "Error: Input is empty."

    lines = user_text.strip().split("\n")
    stops = []

    for line in lines:
        parts = line.split(",")

        if len(parts) != 2:
            return None, "Error: Each line must be in the format stop_name,crowd_count"

        stop_name = parts[0].strip()
        crowd_text = parts[1].strip()

        if stop_name == "":
            return None, "Error: Stop name cannot be empty."

        if not crowd_text.isdigit():
            return None, "Error: Crowd count must be a non-negative integer."

        crowd_count = int(crowd_text)
        stops.append({"stop_name": stop_name, "crowd_count": crowd_count})

    return stops, None


def merge(left, right, steps):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        steps.append(
            f"Comparing {left[i]['stop_name']} ({left[i]['crowd_count']}) "
            f"and {right[j]['stop_name']} ({right[j]['crowd_count']})"
        )

        if left[i]["crowd_count"] >= right[j]["crowd_count"]:
            result.append(left[i])
            steps.append(f"Added {left[i]['stop_name']} to merged list")
            i += 1
        else:
            result.append(right[j])
            steps.append(f"Added {right[j]['stop_name']} to merged list")
            j += 1

    while i < len(left):
        result.append(left[i])
        steps.append(f"Added remaining {left[i]['stop_name']} to merged list")
        i += 1

    while j < len(right):
        result.append(right[j])
        steps.append(f"Added remaining {right[j]['stop_name']} to merged list")
        j += 1

    merged_names = [f"{item['stop_name']} ({item['crowd_count']})" for item in result]
    steps.append("Merged result: " + ", ".join(merged_names))

    return result


def merge_sort(stops, steps):
    if len(stops) <= 1:
        return stops

    mid = len(stops) // 2
    left_half = stops[:mid]
    right_half = stops[mid:]

    left_names = [f"{item['stop_name']} ({item['crowd_count']})" for item in left_half]
    right_names = [f"{item['stop_name']} ({item['crowd_count']})" for item in right_half]
    steps.append("Splitting into: [" + ", ".join(left_names) + "] and [" + ", ".join(right_names) + "]")

    sorted_left = merge_sort(left_half, steps)
    sorted_right = merge_sort(right_half, steps)

    return merge(sorted_left, sorted_right, steps)


def format_final_ranking(sorted_stops):
    output = []
    for index, stop in enumerate(sorted_stops, start=1):
        output.append(f"{index}. {stop['stop_name']} — {stop['crowd_count']}")
    return "\n".join(output)


def run_sort(user_text):
    stops, error = parse_input(user_text)

    if error:
        return error, ""

    steps = []
    sorted_stops = merge_sort(stops, steps)

    steps_output = "\n".join(steps)
    final_output = format_final_ranking(sorted_stops)

    return steps_output, final_output


demo = gr.Interface(
    fn=run_sort,
    inputs=gr.Textbox(
        lines=10,
        label="Enter shuttle stops",
        placeholder="Main Hall,45\nLibrary,12\nResidence,60\nARC,30"
    ),
    outputs=[
        gr.Textbox(label="Merge Sort Steps"),
        gr.Textbox(label="Final Ranked Stops")
    ],
    title="Shuttle Stop Crowd Ranking with Merge Sort",
    description="Enter one shuttle stop per line in the format: stop_name,crowd_count"
)

demo.launch()