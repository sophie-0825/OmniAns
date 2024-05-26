import glob
import os
from asyncflows import AsyncFlows

class PDFChatbot:
    def __init__(self, document_folder='documents', config_file='chatbot.yaml'):
        self.document_folder = document_folder
        self.config_file = config_file
        self.flow = None
        self.conversation_history = []
        self.load_documents()

    def load_documents(self):
        recipes_glob = os.path.join(self.document_folder, "*.pdf")
        document_paths = glob.glob(recipes_glob)
        self.flow = AsyncFlows.from_file(self.config_file).set_vars(
            pdf_filepaths=document_paths,
        )

    async def ask(self, message):
        query_flow = self.flow.set_vars(
            message=message,
            conversation_history=self.conversation_history,
        )
        result = await query_flow.run()
        self.conversation_history.extend([
            f"User: {message}",
            f"Assistant: {result}",
        ])
        return result

# Usage
# chatbot = PDFChatbot()
# result = await chatbot.ask("Your question")