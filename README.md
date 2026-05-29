# langchain-langgraph-lab
 
> Learning LangChain and LangGraph by building one small, runnable program at a time.
 
This is my learning lab for the LangChain/LangGraph ecosystem. Each folder is a
self-contained experiment focused on a single idea. The goal is the building, not
the polish.
 
> Verified against: LangChain `1.x`, LangGraph `0.x`. Versions are pinned in
> `requirements.txt` so older programs keep running as the libraries change.
 
## Why one repo for both
 
LangChain 1.x is built on top of LangGraph - LangGraph is the lower-level
orchestration layer, LangChain the higher-level framework above it. They're one
ecosystem, and many programs here touch both (e.g. building an agent in LangChain,
then rebuilding it in LangGraph to see what's underneath), so keeping them
together makes the comparisons easy.

## Stack
 
Python · LangChain · LangGraph · LangSmith (for tracing) · Pydantic
 
