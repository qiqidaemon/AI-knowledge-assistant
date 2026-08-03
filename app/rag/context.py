def build_rag_context(knowledge):
    context=""
    sources=[]
    for item in knowledge:
        context+=(
            f"""
            知识内容：
            {item['content']}
            """
        )
        sources.append(
            {
                "source":item["source"],
                "chunk":item["chunk"]
            }
        )
    return context,sources