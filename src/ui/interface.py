from __future__ import annotations

import gradio as gr

from ..service import invoke_agent


def create_interface():
    async def chat_fn(message: str, history: list[tuple[str, str]]):
        # invoke_agent returns a ConversationTurn
        turn = await invoke_agent(message)
        # Convert final_answer blocks to markdown text
        if getattr(turn, "final_answer", None):
            answer = "\n\n".join(block.content for block in turn.final_answer)
        else:
            answer = "(No answer produced)"
        return answer

    demo = gr.ChatInterface(
        fn=chat_fn,
        title="Code4all",
        description="Ask a question about LangGraph",
        examples=[
            ["What is LangGraph?"],
            ["How do I use LangGraph?"],
            ["What are the benefits of LangGraph?"],
        ],
    )
    return demo
