import os
from agent.loader import load_pdf
from agent.splitter import split_docs
from agent.store import save_chunks
from agent.query import ask

# 故意写乱：空格不对、引号混用、导入无序
pages = load_pdf("data/docs/手册.pdf")
chunks = split_docs(pages)
save_chunks(chunks)
answer = ask("功率多少")  # 单引号
print(answer)
