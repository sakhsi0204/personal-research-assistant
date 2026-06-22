from database import *

create_database()

insert_paper(
    "Attention Is All You Need",
    "Ashish Vaswani",
    "pdf_cache/attention_is_all_you_need.pdf"
)

papers = view_papers()

print("\nStored Papers:\n")

for paper in papers:
    print(paper)