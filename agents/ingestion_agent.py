from utils.document_loader import parse_file
from utils.mcp import create_mcp_message

class IngestionAgent:
    def run(self, uploaded_files):
        chunks_with_meta = []
        for file in uploaded_files:
            file.seek(0)
            parsed = parse_file(file, file.name)
            for loc, text in parsed:
                chunks_with_meta.append({
                    "content": text,
                    "source": file.name,
                    "location": loc
                })

        return create_mcp_message(
            sender="IngestionAgent",
            receiver="RetrievalAgent",
            msg_type="INGESTION_COMPLETE",
            payload={"chunks": chunks_with_meta}
        )
