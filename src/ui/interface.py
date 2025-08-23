from __future__ import annotations

import gradio as gr

from ..service import invoke_agent


def create_interface() -> gr.Blocks:
    with gr.Blocks(title="Code4all") as demo:
        gr.Markdown("# Code4all")
        with gr.Row():
            query = gr.Textbox(label="Ask a question", placeholder="How do I ... with LangGraph?", lines=3)
        with gr.Row():
            submit = gr.Button("Submit")
        with gr.Row():
            answer = gr.Markdown(label="Answer")
        with gr.Row():
            logs = gr.Markdown(label="Agent Logs")

        def on_submit(q: str) -> tuple[str, str]:
            a, l = invoke_agent(q)
            return a, l

        submit.click(on_submit, inputs=[query], outputs=[answer, logs])
    return demo
