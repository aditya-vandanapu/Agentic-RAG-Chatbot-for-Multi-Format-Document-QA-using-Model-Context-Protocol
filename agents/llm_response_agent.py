from utils.mcp import create_mcp_message
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class LLMResponseAgent:
    def generate_response(self, retrieved_chunks, query):
        context = "\n\n".join(
            [f"[{c['source']} - {c['location']}]: {c['content']}" for c in retrieved_chunks]
        )
        prompt = f"Context:\n{context}\n\nQuestion: {query}"

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response.choices[0].message.content.strip()
        except Exception as e:
            answer = f"⚠️ OpenAI Error: {str(e)}"

        return create_mcp_message(
            sender="LLMResponseAgent",
            receiver="UI",
            msg_type="FINAL_RESPONSE",
            payload={
                "answer": answer,
                "source": retrieved_chunks
            }
        )
