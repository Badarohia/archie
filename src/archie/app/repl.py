"""Interactive command-line interface for Archie."""

from __future__ import annotations

from archie.brain import Brain, ChatMessage


class REPL:
    """Interactive Read-Eval-Print Loop."""
    _brain: Brain
    
    def __init__(self, brain: Brain) -> None:
        """Initialize the REPL."""
        self._brain = brain

    async def run(self) -> None:
        """Start the interactive session."""

        print()
        print("────────────────────────────")
        print(" Archie")
        print("────────────────────────────")
        print("Type 'exit' or 'quit' to leave.")
        print()

        while True:
            try:
                user_input = input("You > ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye!")
                break

            if not user_input:
                continue

            if user_input.lower() in {"exit", "quit"}:
                print("Goodbye!")
                break

            response = self._brain.generate(
                [
                    ChatMessage(
                        role="user",
                        content=user_input,
                    )
                ]
            )

            print(f"Archie > {response.content}")
            print()