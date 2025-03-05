from Module3.chat_with_gpt import system_prompts, chat_with_gpt
from src.open_api_client import get_openai_client
from pprint import pprint

client = get_openai_client()

system_prompt = ("Using the given instructions, "
                 "write only the code content which will be pasted into a Python file.")

def write_to_file(filename, content):
    # w: Write = Create a new file if it does not exist:
    with open(filename, "w") as file:
        file.write(content)


def prompt_basic():
    user_prompt = ("Create a Python dictionary where each student ID maps "
    "to another dictionary containing: "
    "'name': Student’s name (string), "
    "'grades': A list of grades (integers), "
    "'gpa': The GPA, calculated as (sum of grades / number of grades) / 25, "
    "rounded to two decimal places.")
    response = ask_chat(user_prompt)
    pprint(response + "\n")
    write_to_file("prompt_basic.py", response)

def prompt_comprehension():
    user_prompt = (
        "Create a Python dictionary where each student ID maps to another dictionary containing: "
        "'name': Student’s name (string), 'grades': A list of grades (integers), "
        "'gpa': The GPA, calculated as (sum of grades / number of grades) / 25, "
        "rounded to two decimal places. Use dictionary comprehension to construct the dictionary."
    )
    response = ask_chat(user_prompt)
    pprint(response + "\n")
    write_to_file("prompt_comprehension.py", response)

def prompt_readability():
    user_prompt = (
        "Create a Python dictionary where each student ID maps to another dictionary containing: "
        "'name': Student’s name (string), 'grades': A list of grades (integers), "
        "'gpa': The GPA, calculated as (sum of grades / number of grades) / 25, "
        "rounded to two decimal places. Use dictionary comprehension, and then format the output "
        "using print() so that the student data is displayed in a well-structured format."
    )
    response = ask_chat(user_prompt)
    pprint(response + "\n")
    write_to_file("prompt_readability.py", response)

def prompt_unit_test():
    user_prompt = (
        "Create a Python dictionary where each student ID maps to another dictionary containing: "
        "'name': Student’s name (string), 'grades': A list of grades (integers), "
        "'gpa': The GPA, calculated as (sum of grades / number of grades) / 25, "
        "rounded to two decimal places. Use dictionary comprehension to create it. "
        "Then, write unit tests using unittest to verify that: "
        "- The dictionary contains the correct number of students. "
        "- Each student has a 'name', 'grades', and 'gpa'. "
        "- The 'grades' list contains only integers. "
        "Ensure test coverage using IntelliJ’s built-in coverage tool."
    )
    response = ask_chat(user_prompt)
    pprint(response + "\n")
    write_to_file("prompt_unit_test.py", response)


def ask_chat(user_prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content

# calls each of the functions:
def main():
    prompt_basic()
    prompt_comprehension()
    prompt_readability()
    prompt_unit_test()

if __name__=="__main__":
    main()