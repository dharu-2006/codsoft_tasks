# Chatbot Configuration
# Add your custom patterns and responses here

CUSTOM_PATTERNS = {
    # Sports
    r'\b(sports|football|basketball|soccer|tennis|game|match|team|player)\b': [
        "Sports are exciting! What's your favorite sport to watch or play?",
        "I love hearing about sports! Which teams do you follow?",
        "Athletic activities are great for health and fun. Do you play any sports?"
    ],
    
    # Music
    r'\b(music|song|band|artist|concert|guitar|piano|singing|dance)\b': [
        "Music is the universal language! What genre do you enjoy most?",
        "I wish I could hear music! What's your favorite song right now?",
        "Music brings so much joy. Do you play any instruments?"
    ],
    
    # Travel
    r'\b(travel|vacation|trip|country|city|plane|hotel|tourist|visit)\b': [
        "Travel opens our minds to new experiences! Where would you love to visit?",
        "I'd love to hear about your travel adventures! Any favorite destinations?",
        "Exploring new places is amazing. What's the best trip you've ever taken?"
    ],
    
    # Books/Reading
    r'\b(book|read|novel|story|author|library|chapter|page)\b': [
        "Books are windows to other worlds! What's the last book you read?",
        "Reading is such a wonderful hobby. Do you have a favorite author?",
        "I love book discussions! What genre do you prefer?"
    ],
    
    # Technology/Programming
    r'\b(programming|code|computer|software|app|website|developer|python|javascript)\b': [
        "Technology and programming are fascinating! What languages do you work with?",
        "Coding is like modern magic! Are you working on any interesting projects?",
        "The tech world is always evolving. What aspect interests you most?"
    ],
    
    # Health/Fitness
    r'\b(health|fitness|exercise|gym|workout|running|healthy|diet|nutrition)\b': [
        "Health and fitness are so important! What do you do to stay active?",
        "Taking care of yourself is wonderful! Do you have a favorite workout?",
        "Wellness is key to happiness. How do you maintain a healthy lifestyle?"
    ],
    
    # Movies/TV
    r'\b(movie|film|tv|television|show|actor|director|cinema|netflix|watch)\b': [
        "Entertainment is great for relaxation! What's your favorite movie or show?",
        "I love discussing movies and TV! What genre do you prefer?",
        "Screen time can be so enjoyable. Any recent recommendations?"
    ],
    
    # Family/Friends
    r'\b(family|friend|friends|mother|father|sister|brother|parents|kids|children)\b': [
        "Family and friends are precious! How are your loved ones doing?",
        "Relationships are what make life meaningful. Tell me about your family or friends!",
        "The people we care about are so important. What makes your relationships special?"
    ]
}

# Custom responses for specific situations
CUSTOM_RESPONSES = {
    "compliments_received": [
        "You're so kind! I really appreciate that.",
        "Thank you! That brightens my day.",
        "I'm blushing! Well, if I could blush. Thank you!"
    ],
    
    "confusion_expressed": [
        "I understand that can be confusing. Let's break it down together.",
        "No worries! Confusion is just the first step to understanding.",
        "That's totally normal! What specific part is unclear?"
    ],
    
    "encouragement_needed": [
        "You've got this! I believe in you.",
        "Every challenge is an opportunity to grow stronger.",
        "Remember, progress isn't always linear, but you're moving forward!"
    ]
}

# Conversation starters for different times/contexts
CONVERSATION_STARTERS = {
    "general": [
        "What's something interesting that happened to you recently?",
        "If you could have dinner with anyone, who would it be?",
        "What's a skill you'd love to learn?",
        "What always makes you smile?",
        "What's your idea of a perfect day?"
    ],
    
    "creative": [
        "If you could invent something, what would it be?",
        "What's the most creative thing you've ever done?",
        "If you wrote a book, what would it be about?",
        "What's an unusual hobby you'd like to try?"
    ],
    
    "reflective": [
        "What's something you're grateful for today?",
        "What's the best advice you've ever received?",
        "What achievement are you most proud of?",
        "What lesson has life taught you recently?"
    ]
}

# Settings
SETTINGS = {
    "max_conversation_length": 50,  # Maximum turns before suggesting a break
    "response_variation": True,     # Use random response selection
    "show_typing_indicator": False, # Simulate typing (for future enhancement)
    "conversation_starter_frequency": 0.3,  # 30% chance of using conversation starters
    "enable_emoji": True,          # Use emojis in responses
    "case_sensitive": False,       # Pattern matching case sensitivity
}
