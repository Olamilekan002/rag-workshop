# Speaker Notes

## Slide 1: Title
Tell them they will **build**, not just watch. Set expectation: by end of session they run a local chat app on their laptop.

## Slide 2: Agenda
Quick roadmap. Mention one 15-minute break around the document pipeline section.

## Slide 3: Who This Is For
Acknowledge mixed audience. Same architecture applies to teaching, research, and industry docs.

## Slide 4: What Is an LLM?
Keep it non-technical. Avoid transformer math. Focus on capabilities and limits.

## Slide 5: Hallucination Problem
Ask: "Who has gotten a confident wrong answer from ChatGPT?" Pause for hands or nods.

## Slide 6: What Is RAG?
One sentence definition. Don't over-explain yet — the diagram is next.

## Slide 7: RAG Architecture
**Most important conceptual slide.** Walk through left-to-right slowly. Say you'll build each box today.

## Slide 8: Real-World Examples
Connect to tools they may know. Emphasize this is production pattern, not a toy.

## Slide 9: Embeddings
Use the car/vehicle/banana example verbally before notebook demo.

## Slide 10: Why Chunk Documents
Explain tradeoff: smaller chunks = precise retrieval, larger chunks = more context per chunk.

## Slide 11: Vector Database
Stress **local** ChromaDB — good for private research documents.

## Slide 12: Demo Preview
2 minutes max. Ask one question, show answer + sources. Don't explain code yet.

## Slide 13: Workshop Stack
Point out: only Gemini needs internet for generation; embeddings run locally after first download.

## Slide 14: Let's Build
Transition moment. Everyone opens notebook Section 2.

## Slide 15: Retrieval Step
Refer back to embedding slide. Retrieval = semantic search, not Ctrl+F.

## Slide 16: Prompt Construction
Show why "answer only from context" reduces hallucination.

## Slide 17: With vs Without RAG
This sets up notebook Section 8 comparison cell.

## Slide 18: Local App Demo
Run `streamlit run app.py`. Emphasize privacy for researchers.

## Slide 19: Use Cases
Ask each group to think of one document set they'd use.

## Slide 20: Make It Yours
Give 10 minutes. Prep 1-2 volunteers during break if demos might be shy.

## Slide 21: What You Built
Recap checklist — they should feel accomplishment.

## Slide 22: Learning Roadmap
Point to `resources/ai_learning_roadmap.md`. Don't overwhelm — one next step is enough.

## Slide 23: Resources
Optional slide — can skip if short on time.

## Slide 24: Q&A
Share repo and feedback form.

## Slide 25: Thank You
Close with: "Take the code. Build something useful in your domain."
