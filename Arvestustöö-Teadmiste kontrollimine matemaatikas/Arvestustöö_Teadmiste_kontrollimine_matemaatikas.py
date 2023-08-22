import tkinter as tk
import random

class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz")

        self.color_themes = {
            "Light": {"bg": "white", "fg": "black"},
            "Dark": {"bg": "black", "fg": "white"}
        }

        self.language_options = {
            "English": {"start": "Start Quiz", "select_difficulty": "Select Difficulty:", "num_operations": "Number of Operations:", "min_number": "Min Number:", "max_number": "Max Number:", "color_theme": "Select Color Theme:", "language": "Select Language:"},
            "Estonian": {"start": "Alusta Testi", "select_difficulty": "Vali Raskustase:", "num_operations": "Tehtete Arv:", "min_number": "Minimaalne Arv:", "max_number": "Maksimaalne Arv:", "color_theme": "Vali Värviteema:", "language": "Vali Keel:"}
        }

        self.language_var = tk.StringVar()
        self.language_var.set("English")

        self.color_theme_var = tk.StringVar()
        self.color_theme_var.set("Light")

        self.difficulty_var = tk.StringVar()
        self.num_operations_var = tk.IntVar()
        self.min_number_var = tk.IntVar()
        self.max_number_var = tk.IntVar()

        self.difficulty_var.set("Easy")
        self.num_operations_var.set(5)
        self.min_number_var.set(1)
        self.max_number_var.set(10)

        self.difficulty_label = tk.Label(root, text=self.language_options[self.language_var.get()]["select_difficulty"], bg=self.color_themes[self.color_theme_var.get()]["bg"], fg=self.color_themes[self.color_theme_var.get()]["fg"])
        self.difficulty_label.pack()

        self.difficulty_menu = tk.OptionMenu(root, self.difficulty_var, "Easy", "Medium", "Hard")
        self.difficulty_menu.config(bg=self.color_themes[self.color_theme_var.get()]["bg"], fg=self.color_themes[self.color_theme_var.get()]["fg"])
        self.difficulty_menu.pack()

        self.num_operations_label = tk.Label(root, text=self.language_options[self.language_var.get()]["num_operations"], bg=self.color_themes[self.color_theme_var.get()]["bg"], fg=self.color_themes[self.color_theme_var.get()]["fg"])
        self.num_operations_label.pack()

        self.num_operations_entry = tk.Entry(root, textvariable=self.num_operations_var, bg=self.color_themes[self.color_theme_var.get()]["bg"], fg=self.color_themes[self.color_theme_var.get()]["fg"])
        self.num_operations_entry.pack()

        self.min_number_label = tk.Label(root, text=self.language_options[self.language_var.get()]["min_number"], bg=self.color_themes[self.color_theme_var.get()]["bg"], fg=self.color_themes[self.color_theme_var.get()]["fg"])
        self.min_number_label.pack()

        self.min_number_entry = tk.Entry(root, textvariable=self.min_number_var, bg=self.color_themes[self.color_theme_var.get()]["bg"], fg=self.color_themes[self.color_theme_var.get()]["fg"])
        self.min_number_entry.pack()

        self.max_number_label = tk.Label(root, text=self.language_options[self.language_var.get()]["max_number"], bg=self.color_themes[self.color_theme_var.get()]["bg"], fg=self.color_themes[self.color_theme_var.get()]["fg"])
        self.max_number_label.pack()

        self.max_number_entry = tk.Entry(root, textvariable=self.max_number_var, bg=self.color_themes[self.color_theme_var.get()]["bg"], fg=self.color_themes[self.color_theme_var.get()]["fg"])
        self.max_number_entry.pack()

        self.start_button = tk.Button(root, text=self.language_options[self.language_var.get()]["start"], command=self.start_quiz, bg=self.color_themes[self.color_theme_var.get()]["bg"], fg=self.color_themes[self.color_theme_var.get()]["fg"])
        self.start_button.pack()

        self.color_theme_label = tk.Label(root, text=self.language_options[self.language_var.get()]["color_theme"], bg=self.color_themes[self.color_theme_var.get()]["bg"], fg=self.color_themes[self.color_theme_var.get()]["fg"])
        self.color_theme_label.pack()

        self.color_theme_menu = tk.OptionMenu(root, self.color_theme_var, *self.color_themes.keys(), command=self.change_color_theme)
        self.color_theme_menu.config(bg=self.color_themes[self.color_theme_var.get()]["bg"], fg=self.color_themes[self.color_theme_var.get()]["fg"])
        self.color_theme_menu.pack()

        self.language_label = tk.Label(root, text=self.language_options[self.language_var.get()]["language"], bg=self.color_themes[self.color_theme_var.get()]["bg"], fg=self.color_themes[self.color_theme_var.get()]["fg"])
        self.language_label.pack()

        self.language_menu = tk.OptionMenu(root, self.language_var, *self.language_options.keys(), command=self.change_language)
        self.language_menu.config(bg=self.color_themes[self.color_theme_var.get()]["bg"], fg=self.color_themes[self.color_theme_var.get()]["fg"])
        self.language_menu.pack()

        self.quiz_frame = tk.Frame(root, bg=self.color_themes[self.color_theme_var.get()]["bg"])
        self.quiz_frame.pack()
        
        self.question_labels = []
        self.answer_entries = []
        self.questions = []
        self.answers = []

    def generate_question(self):
        num1 = random.randint(self.min_number_var.get(), self.max_number_var.get())
        num2 = random.randint(self.min_number_var.get(), self.max_number_var.get())
        operator = random.choice(["+", "-", "*", "/"])
        question = f"{num1} {operator} {num2}"
        answer = eval(question)
        return question, answer

    def start_quiz(self):
        self.questions = []
        self.answers = []
        for _ in range(self.num_operations_var.get()):
            question, answer = self.generate_question()
            self.questions.append(question)
            self.answers.append(answer)

        self.quiz_frame.destroy()
        self.quiz_frame = tk.Frame(root, bg=self.color_themes[self.color_theme_var.get()]["bg"])
        self.quiz_frame.pack()

        for idx, question in enumerate(self.questions):
            question_label = tk.Label(self.quiz_frame, text=f"Question {idx + 1}: {question}", fg=self.color_themes[self.color_theme_var.get()]["fg"], bg=self.color_themes[self.color_theme_var.get()]["bg"])
            question_label.pack()
            answer_entry = tk.Entry(self.quiz_frame, bg=self.color_themes[self.color_theme_var.get()]["bg"], fg=self.color_themes[self.color_theme_var.get()]["fg"])
            answer_entry.pack()
            self.question_labels.append(question_label)
            self.answer_entries.append(answer_entry)

        self.submit_button = tk.Button(root, text=self.language_options[self.language_var.get()]["start"], command=self.submit_answers, bg=self.color_themes[self.color_theme_var.get()]["bg"], fg=self.color_themes[self.color_theme_var.get()]["fg"])
        self.submit_button.pack()

    def submit_answers(self):
        correct_answers = 0
        for idx, answer_entry in enumerate(self.answer_entries):
            user_answer = answer_entry.get()
            correct_answer = self.answers[idx]
            if user_answer == str(correct_answer):
                correct_answers += 1
        
        total_questions = len(self.questions)
        percentage_correct = (correct_answers / total_questions) * 100

        if percentage_correct < 60:
            grade = "Hinne 2"
        elif 60 <= percentage_correct < 75:
            grade = "Hinne 3"
        elif 75 <= percentage_correct < 90:
            grade = "Hinne 4"
        else:
            grade = "Hinne 5"
        
        result_label = tk.Label(root, text=f"Your grade: {grade}", bg=self.color_themes[self.color_theme_var.get()]["bg"], fg=self.color_themes[self.color_theme_var.get()]["fg"])
        result_label.pack()

    def change_color_theme(self, theme):
        self.root.config(bg=self.color_themes[theme]["bg"])
        for label in self.question_labels:
            label.config(bg=self.color_themes[theme]["bg"], fg=self.color_themes[theme]["fg"])
        for entry in self.answer_entries:
            entry.config(bg=self.color_themes[theme]["bg"], fg=self.color_themes[theme]["fg"])
        self.color_theme_label.config(bg=self.color_themes[theme]["bg"], fg=self.color_themes[theme]["fg"])
        self.start_button.config(bg=self.color_themes[theme]["bg"], fg=self.color_themes[theme]["fg"])
        if hasattr(self, "submit_button"):
            self.submit_button.config(bg=self.color_themes[theme]["bg"], fg=self.color_themes[theme]["fg"])
        self.difficulty_label.config(bg=self.color_themes[theme]["bg"], fg=self.color_themes[theme]["fg"])
        self.num_operations_label.config(bg=self.color_themes[theme]["bg"], fg=self.color_themes[theme]["fg"])
        self.min_number_label.config(bg=self.color_themes[theme]["bg"], fg=self.color_themes[theme]["fg"])
        self.max_number_label.config(bg=self.color_themes[theme]["bg"], fg=self.color_themes[theme]["fg"])
        self.language_label.config(bg=self.color_themes[theme]["bg"], fg=self.color_themes[theme]["fg"])
        self.color_theme_menu.config(bg=self.color_themes[theme]["bg"], fg=self.color_themes[theme]["fg"])
        self.language_menu.config(bg=self.color_themes[theme]["bg"], fg=self.color_themes[theme]["fg"])
        self.difficulty_menu.config(bg=self.color_themes[theme]["bg"], fg=self.color_themes[theme]["fg"])
    
    def change_language(self, language):
        self.difficulty_label.config(text=self.language_options[language]["select_difficulty"])
        self.num_operations_label.config(text=self.language_options[language]["num_operations"])
        self.min_number_label.config(text=self.language_options[language]["min_number"])
        self.max_number_label.config(text=self.language_options[language]["max_number"])
        self.start_button.config(text=self.language_options[language]["start"])
        self.color_theme_label.config(text=self.language_options[language]["color_theme"])
        self.language_label.config(text=self.language_options[language]["language"])

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()
