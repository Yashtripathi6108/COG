FROM python:3.11-slim

WORKDIR /app
COPY ExtractImage.py imagenotfound.png langchain_togetherai.py \
    requirements.txt query_results.py SimilarityFinder.py TogetherLLM.py users.pkl /app/    

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["streamlit", "run", "langchain_togetherai.py", "--server.port", "5000"]
