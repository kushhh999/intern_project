# ============================================================
# PROJECT 1: Rule-Based AI Chatbot
# DecodeLabs Industrial Training Kit | Batch 2026
# ============================================================
# WHAT IS THIS?
# A chatbot that uses a DICTIONARY (hash map) to look up
# responses based on what the user types.
# No machine learning. Pure logic. 100% predictable.
# ============================================================

# --- THE KNOWLEDGE BASE (our brain) ---
# This is a Python DICTIONARY: { "key": "value" }
# The KEY  = what the user might type
# The VALUE = what our bot replies
# This is O(1) lookup — instant, no matter how many rules!

responses = {
    # Greetings
    "hello":        "Hey there! 👋 I'm DecoBot. How can I help?",
    "hi":           "Hi! What's on your mind?",
    "hey":          "Hey! 😊 Ask me anything.",

    # Farewells
    "bye":          "Goodbye! Keep building cool things. 🚀",
    "goodbye":      "See you later! Don't forget to push your code. 😄",

    # About the bot
    "who are you":  "I'm DecoBot — a rule-based chatbot built at DecodeLabs!",
    "what are you": "I'm a Python chatbot using if-else logic and dictionaries.",
    "what is your name": "I am DecoBot, built by Madhav Agarwal!",
    "who made you": "Madhav Agarwal — AI Engineer at DecodeLabs!",

    # About AI
    "what is ai":   "AI is making machines simulate human intelligence. You're learning it right now!",
    "what is ml":   "Machine Learning is AI that learns from data. That's Project 2 territory 😉",

    # About DecodeLabs
    "what is decodelabs": "DecodeLabs is your training ground to become a professional AI Engineer!",

    # Fun / personality
    "how are you":  "I'm just code, but I'm running perfectly! 💻",
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "what is python": "Python is the language powering this chatbot — and most of AI/ML!",

    # Help
    "help":         "Try saying: hello, who are you, what is ai, tell me a joke, or bye.",
}

# --- THE EXIT COMMANDS ---
# If user types any of these, we stop the loop
EXIT_COMMANDS = {"exit", "quit", "stop", "q"}

# ============================================================
# THE IPO MODEL (Input → Process → Output)
# ============================================================

def get_clean_input():
    """
    PHASE 1: INPUT & SANITIZATION
    
    raw_input  → "  HeLLo  "  (messy)
    .lower()   → "  hello  "  (lowercase)
    .strip()   → "hello"      (no extra spaces)
    
    This makes our bot case-insensitive and forgiving.
    """
    raw_input = input("You: ")
    clean_input = raw_input.lower().strip()
    return clean_input


def get_response(user_input):
    """
    PHASE 2: PROCESS (Intent Matching)
    
    We use dict.get(key, fallback) — the PROFESSIONAL approach.
    - If key EXISTS  → returns the mapped response
    - If key MISSING → returns the fallback message
    
    This is ONE atomic operation. No if-elif ladder needed!
    """
    return responses.get(user_input, "🤔 I don't understand that yet. Type 'help' to see what I know.")


def run_chatbot():
    """
    PHASE 3: OUTPUT + THE INFINITE LOOP (The Heartbeat)
    
    while True creates an infinite loop — the bot keeps running
    until the user sends an EXIT COMMAND, which triggers `break`.
    """
    print("=" * 50)
    print("  🤖 DecoBot — Rule-Based AI Chatbot")
    print("  DecodeLabs | Project 1 | Batch 2026")
    print("=" * 50)
    print("  Type 'help' for options. Type 'exit' to quit.")
    print("=" * 50)
    print()

    # THE HEARTBEAT — runs forever until break
    while True:
        user_input = get_clean_input()

        # EXIT STRATEGY — the kill command
        if user_input in EXIT_COMMANDS:
            print("Bot: Shutting down... Goodbye, Engineer! 👋")
            break

        # Get and print the response
        reply = get_response(user_input)
        print(f"Bot: {reply}")
        print()  # blank line for readability


# ============================================================
# ENTRY POINT
# This is standard Python — only runs if you execute THIS file
# directly (not when imported as a module).
# ============================================================
if __name__ == "__main__":
    run_chatbot()
