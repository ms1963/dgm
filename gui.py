import tkinter as tk
from dgm.agent import PromptAgent
from dgm.llm_interface import query_openai

def run_gui():
    agent = PromptAgent()

    def on_submit():
        user_input = prompt_entry.get("1.0", tk.END).strip()
        transformed = agent.act(user_input)
        result = query_openai(transformed)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)

    root = tk.Tk()
    root.title("Darwin-Gödel Machine GUI")

    tk.Label(root, text="Prompt:").pack()
    prompt_entry = tk.Text(root, height=5, width=60)
    prompt_entry.pack()

    tk.Button(root, text="Submit", command=on_submit).pack()

    tk.Label(root, text="LLM Output:").pack()
    output_text = tk.Text(root, height=10, width=60)
    output_text.pack()

    root.mainloop()
