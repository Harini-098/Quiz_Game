import tkinter as tk
from tkinter import messagebox
class QuizGame:
    def __init__(self):
        self.quiz_data = [
            {
                "question":"What is the capital of India?",
                "options":["NewDelhi","Bhopal","Hyderabad","Bengaluru"],
                "correct_answer": 0
            },
            {
                "question":"Which planet is known as the Red Planet?",
                "options":["Jupiter","Mars","Earth","Saturn"],
                "correct_answer": 1
            },
            {
                "question":"How many continents are there in the world?",
                "options":["Seven","six","five","four"],
                "correct_answer": 1
            }
        ]
        self.current_question_index = 0
        self.score = 0
        
        self.window = tk.Tk()
        self.window.title("Quiz Game")
        
        self.question_label = tk.Label(self.window, text = "")
        self.question_label.pack()
        
        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack()
        
        self.options_buttons = []
        for i in range(4):
            button = tk.Button(self.options_frame , text =" " , width = 30, command=lambda i=i:self.check_answer(i))
            button.pack(pady=5)
            self.options_buttons.append(button)
            
        self.next_question_button = tk.Button(self.window, text="next", width=30, command= self.next_question)
        self.next_question_button.pack(pady = 10)
    def check_answer(self, selected_option):
        question_data = self.quiz_data[self.current_question_index]
        answer = question_data["correct_answer"]
        if selected_option == answer:
            self.score = self.score+1
            messagebox.showinfo("Correct","Your answer is correct")
        else:
            messagebox.showinfo("Incorrect","Your answer is wrong")
    def load_question(self):
        question_data= self.quiz_data[self.current_question_index]
        self.question_label.config(text =question_data["question"])
        options = question_data["options"]
        for i in range(4):
            self.options_buttons[i].config(text = options[i])
    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index == len(self.quiz_data):
            messagebox.showinfo("game over", "your score is"+ str(self.score))
            self.window.quit()
        else:
            self.load_question()
    def start_quiz(self):
        self.load_question()
        self.window.mainloop()
    
quiz_game = QuizGame()
quiz_game.start_quiz() 