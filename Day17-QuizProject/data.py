# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
#              "you are free to take it home to eat.", "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
#      "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"},
# ]
import requests
from CONSTANTS import *

# Define the API endpoint
url = 'https://opentdb.com/api.php'

# Set parameters for the request for True/False questions
params = {
    'amount': NO_QUESTION,
    'category': CATEGORY,
    'difficulty': 'easy',
    'type': 'boolean',
}

# Fetch the data
response = requests.get(url, params=params)

question_data = []

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON response
    questions = data['results']

    # Print or process the questions
    for question in questions:
        # print("Question:", question['question'])
        # print("Correct Answer:", question['correct_answer'])  # "True" or "False"
        question_data.append({'text': question['question'], 'answer': question['correct_answer']})
else:
    print("Error fetching data:", response.status_code)
