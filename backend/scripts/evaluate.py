"""Evaluates pipeline retrieval and response quality across benchmark questions."""
from pathlib import Path
import sys

# ensure backend root is on sys.path
backend_dir = Path(__file__).resolve().parent.parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

from app.pipeline import pipeline
import json
import time

questions = [
    "How should a beginner break into a weight training program to avoid soreness or injury?",
    "What is the recommended number of sets to perform during the first week and first month of training?",
    "What muscles do bench presses primarily work?",
    "How many sets and reps are prescribed for bench presses in Chart 4's Monday upper body workout?",
    "What is the correct starting position for close-grip bench presses?",
    "What is emphasized when performing lateral raises with bent arms and rotated hands?",
    "What exercises are grouped as supersets in the Monday upper body workout?",
    "What muscles are targeted by close-grip bench presses?",
]
# Debugging flag for pipeline
debug = True


def run_evaluation() -> None:
    """Executes benchmark questions through the RAG pipeline and saves output to disk.

    Steps:
        1. Iterate through benchmark bodybuilding questions.
        2. Execute each question with pipeline in debug mode to collect answers and chunks.
        3. Store question, answer, and chunk metadata into the results list.
        4. Pause briefly between queries to respect LLM API rate limits.
        5. Ensure target data/evaluation folder exists and write results to evaluate.json.

    Args:
        None.

    Returns:
        None.

    Raises:
        Exception: If pipeline execution or file writing encounters an error.
    """
    results = []

    print("Running Questions")

    for i, question in enumerate(questions):
        print(f"Running: {question}")
        answer, chunk_info = pipeline(question, debug=True)

        results.append({
            "question": question,
            "answer": answer,
            "retrieved_chunks": chunk_info,
        })

        # Pausing for rate limit per minute
        if (i + 1) % 1 == 0:
            print("Pausing to respect rate limit...")
            time.sleep(30)

    print("Results Written")

    output_path = Path(__file__).resolve().parent.parent / "data" / "evaluation" / "evaluate.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print("Evaluation complete. Results written to data/evaluation/evaluate.json")


if __name__ == "__main__":
    run_evaluation()