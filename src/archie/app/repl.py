"""Interactive command-line interface for Archie."""

from __future__ import annotations

from archie.brain import Brain
from archie.conversation import Conversation
from archie.personality import PersonalityManager


class REPL:
    """Interactive Read-Eval-Print Loop."""

    _brain: Brain
    _personality: PersonalityManager

    def __init__(
        self,
        brain: Brain,
        personality: PersonalityManager,
    ) -> None:
        """Initialize the REPL."""

        self._brain = brain
        self._personality = personality

    async def run(self) -> None:
        """Start the interactive session."""

        print()
        print("────────────────────────────")
        print(" Archie")
        print("────────────────────────────")
        print("Type 'exit' or 'quit' to leave.")
        print()

        conversation = Conversation(
            system_prompt=self._personality.prompt,
        )

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

            conversation.add_user_message(user_input)

            response = self._brain.generate(
                conversation.messages,
            )

            conversation.add_assistant_message(
                response.content,
            )

            print(f"Archie > {response.content}")
            print()