import glob
import os
from pathlib import Path

from asyncflows import AsyncFlows

async def main():
    # Load PDFs from the `books` folder
    recipes_glob = os.path.join("documents", "*.pdf")
    document_paths = glob.glob(recipes_glob)

    # Load the chatbot flow
    flow = AsyncFlows.from_file("omniAns.yaml").set_vars(
        pdf_filepaths=document_paths,
    )

    # Keep track of the conversation history
    conversation_history = []

    # Run the flow
    while True:
        # Get the user's query via CLI interface (swap out with whatever input method you use)
        try:
            message = input("What's your essay question: ")
        except EOFError:
            break

        # Set the query and conversation history
        query_flow = flow.set_vars(
            message=message,
            conversation_history=conversation_history
        )

        # Run the flow and get the result
        result = await query_flow.run()
        print(result)

        # Update the conversation history
        conversation_history.extend(
            [
                f"User: {message}",
                f"Assistant: {result}",
            ]
        )


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
