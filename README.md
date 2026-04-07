# Algorithm Name

Shuttle Stop Crowd Ranking with Merge Sort

Chosen Algorithm

- This project uses Merge Sort because it is efficient and well-suited for sorting structured data like shuttle stops with crowd counts. Merge Sort works by dividing the list into smaller parts, sorting them, and then merging them back together.

It is a good choice for this problem because:

- it guarantees consistent performance
- it clearly shows step-by-step comparisons for visualization
- it works well with unsorted input data
- This makes it ideal for demonstrating both sorting logic and computational thinking.

# Demo video/gif/screenshot of test

- Normal Case

  - (normal.png)

- Edge Case (Single Stop)

  - (edge.png)

- Error Case (Invalid Input)

   - (error.png)

# Problem Breakdown & Computational Thinking

  - Decomposition

The problem is broken into smaller steps:

1. Take user input from the textbox.
2. Split the input into multiple lines.
3. Validate each line to ensure it follows the format stop_name,crowd_count.
4. Convert valid input into a list of shuttle stop records.
5. Apply Merge Sort to the list based on crowd count.
6. Record each step of the sorting process.
7. Display the final ranked list to the user.


  - Pattern Recognition

The algorithm follows repeating patterns:

- the list is repeatedly split into smaller halves
- pairs of values are compared during merging
- the stop with the higher crowd count is placed first
- this process repeats until the entire list is sorted

  - Abstraction

The program focuses only on important details:

-  stop name
- crowd count
- comparisons between stops
- the merging process
- final ranking


  - The program hides unnecessary details such as:
- internal memory operations
- low-level Python behavior
- implementation complexity that does not help user understanding
- Algorithm Design (Input → Process → Output)

Input:
- The user enters shuttle stops in the format stop_name,crowd_count.

Process:
- The program validates the input, stores it in a list, and applies Merge Sort while tracking each step of the process.

Output:

- Step-by-step Merge Sort explanation
- Final ranked list of shuttle stops from highest to lowest crowd count

### Flowchart

(flowchart.png)

## Steps to Run

1. Requirements

- Python 3 installed
- Internet connection (for Gradio interface)

2. Install Dependencies

  - Open a terminal in the project folder and run:


- pip install -r requirements.txt

  - 3. Run the Application

Run the program using:

- python app.py

or (if needed):

- python3 app.py

  - 4.  Open the App

- After running the program, a Gradio link will appear in the terminal (e.g., http://127.0.0.1:7860) Open this link in your browser

  - 5. How to Use
Enter shuttle stops in the format:

- stop_name,crowd_count

Example:

Main Hall,45

Library,12

Residence,60

ARC,30

  - 6. Output
The app will:

- display step-by-step Merge Sort operations show the final ranked list from highest to lowest crowd count

Hugging Face Link

https://huggingface.co/spaces/yasoon123/cisc121-shuttle-merge-sort


Author & AI Acknowledgment

Author: Yaseen Masoud

AI Use:

AI tools were used to assist with debugging, improving code structure, and helping me with my explanations. All code and concepts were reviewed and understood before submission.