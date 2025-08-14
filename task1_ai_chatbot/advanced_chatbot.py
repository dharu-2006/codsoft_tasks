import re
import random
from datetime import datetime

class AdvancedRuleBasedChatbot:
    def __init__(self):
        # Enhanced patterns with more sophisticated matching
        self.patterns = {
            # Greetings with context awareness
            r'\b(hello|hi|hey|greetings|good morning|good afternoon|good evening)\b.*': [
                "Hello! How can I help you today?",
                "Hi there! What's on your mind?",
                "Hey! Great to see you. How may I assist you?"
            ],
            
            # Personal questions
            r'\b(how are you|how\'s it going|how do you do|what\'s up|how you doing)\b': [
                "I'm doing fantastic, thank you! How are you feeling today?",
                "I'm running smoothly! What brings you here today?",
                "All good on my end! How about you?"
            ],
            
            # Identity questions
            r'\b(what is your name|what\'s your name|who are you|your name|tell me about yourself)\b': [
                "I'm an AI chatbot designed to have conversations with you!",
                "You can call me ChatBot. I'm here to chat and help however I can!",
                "I'm your AI conversation partner. Nice to meet you!"
            ],
            
            # Age/creation questions
            r'\b(how old are you|when were you created|your age)\b': [
                "I was just created today! I'm brand new and ready to chat.",
                "I'm timeless in a way - I exist in the moment of our conversation!",
                "Age is just a number for AI like me. I'm here and ready to help!"
            ],
            
            # Capability questions
            r'\b(what can you do|your capabilities|features|abilities|help me)\b': [
                "I can chat with you, answer questions, and have meaningful conversations!",
                "I'm great at understanding what you're saying and responding appropriately.",
                "I can discuss various topics and try to be helpful in our conversation!"
            ],
            
            # Feelings/emotions
            r'\b(i feel|i am (sad|happy|excited|angry|frustrated|tired|good|bad|great))\b': [
                "I appreciate you sharing how you feel. Would you like to talk about it?",
                "Emotions are important. I'm here to listen if you want to share more.",
                "Thank you for being open with me. How can I help you feel better?"
            ],
            
            # Compliments
            r'\b(you are (good|great|awesome|amazing|smart|helpful|nice))\b': [
                "Thank you so much! That means a lot to me.",
                "I really appreciate your kind words!",
                "You're very kind! I'm just trying my best to be helpful."
            ],
            
            # Questions about AI/technology
            r'\b(artificial intelligence|machine learning|technology|computer|robot)\b': [
                "Technology is fascinating! I'm a simple rule-based system, but AI is evolving rapidly.",
                "I love discussing technology! What aspect interests you most?",
                "AI and technology are exciting fields. What would you like to know?"
            ],
            
            # Learning questions
            r'\b(can you learn|do you learn|machine learning|getting smarter)\b': [
                "I don't learn from our conversation, but I try to respond as best I can!",
                "I'm rule-based, so I don't learn new things, but I aim to be helpful!",
                "My responses are pre-programmed, but I strive to be useful in every chat!"
            ],
            
            # Time-related
            r'\b(what time|current time|time is it|date|today)\b': [
                f"I don't have real-time access, but I can tell you I was started around {datetime.now().strftime('%I:%M %p')}!",
                "Time flies when we're chatting! Check your device for the current time.",
                "I wish I could tell you the exact time, but your device knows better than I do!"
            ],
            
            # Weather
            r'\b(weather|temperature|rain|sunny|cloudy|hot|cold|snow)\b': [
                "I can't check the weather, but I hope it's nice where you are!",
                "Weather talk! I'd love to know if it's a beautiful day where you are.",
                "I don't have weather data, but you can check your local weather app!"
            ],
            
            # Food/eating
            r'\b(food|eat|hungry|dinner|lunch|breakfast|cooking|recipe)\b': [
                "Food is such a great topic! What's your favorite type of cuisine?",
                "I wish I could taste food! What are you thinking of eating?",
                "Cooking and food bring people together. Do you enjoy cooking?"
            ],
            
            # Hobbies/interests
            r'\b(hobby|hobbies|interests|like to do|free time|fun)\b': [
                "Hobbies are wonderful! What do you enjoy doing in your spare time?",
                "I'd love to hear about what interests you most!",
                "Everyone needs something fun to do. What brings you joy?"
            ],
            
            # Work/school
            r'\b(work|job|school|study|student|employee|career)\b': [
                "Work and studies keep us busy! How are things going for you?",
                "Whether work or school, I hope things are going well for you!",
                "Career and education are important. What field are you in?"
            ],
            
            # Thank you
            r'\b(thank you|thanks|appreciate|grateful|thx)\b': [
                "You're absolutely welcome!",
                "My pleasure! Always happy to help!",
                "Thank you for being so polite! Anything else I can do?"
            ],
            
            # Apologies
            r'\b(sorry|apologize|my bad|excuse me)\b': [
                "No need to apologize! You're perfectly fine.",
                "Don't worry about it at all!",
                "No apologies necessary! We're just having a friendly chat."
            ],
            
            # Agreement
            r'\b(yes|yeah|yep|sure|okay|ok|right|exactly|true|correct)\b': [
                "Great! I'm glad we're on the same page.",
                "Wonderful! What would you like to explore next?",
                "Perfect! How can I help you further?"
            ],
            
            # Disagreement
            r'\b(no|nope|not really|nah|wrong|incorrect|disagree)\b': [
                "That's totally fine! Different perspectives make conversations interesting.",
                "I understand. What's your take on it?",
                "Fair enough! I'm always open to different viewpoints."
            ],
            
            # Goodbye
            r'\b(bye|goodbye|see you|farewell|take care|later|exit|quit)\b': [
                "Goodbye! It was wonderful chatting with you!",
                "See you later! Take care and have a fantastic day!",
                "Farewell! Thanks for the great conversation!"
            ]
        }
        
        # Context-aware default responses
        self.default_responses = [
            "That's interesting! Can you tell me more about that?",
            "I'm not sure I fully understand, but I'd love to learn more!",
            "That's a unique way to put it! Could you elaborate?",
            "I find that fascinating! What made you think of that?",
            "I'm still processing that. Can you help me understand better?",
            "That's something I haven't encountered before. Tell me more!",
            "Interesting perspective! What else would you like to discuss?"
        ]
        
        # Conversation starters for when chat gets quiet
        self.conversation_starters = [
            "What's something that made you smile today?",
            "If you could learn any new skill, what would it be?",
            "What's your favorite way to spend a weekend?",
            "Is there a book or movie you'd recommend?",
            "What's something you're looking forward to?"
        ]
    
    def preprocess_input(self, user_input):
        """Enhanced preprocessing for better accuracy"""
        # Convert to lowercase and strip
        processed = user_input.lower().strip()
        # Remove extra whitespace
        processed = re.sub(r'\s+', ' ', processed)
        # Handle contractions
        contractions = {
            "i'm": "i am", "you're": "you are", "it's": "it is",
            "that's": "that is", "what's": "what is", "who's": "who is",
            "how's": "how is", "where's": "where is", "when's": "when is",
            "why's": "why is", "can't": "cannot", "won't": "will not",
            "don't": "do not", "isn't": "is not", "aren't": "are not"
        }
        for contraction, expansion in contractions.items():
            processed = processed.replace(contraction, expansion)
        return processed
    
    def get_response(self, user_input):
        """Enhanced response generation with pattern scoring"""
        processed_input = self.preprocess_input(user_input)
        
        # Score patterns based on match quality
        best_match = None
        best_score = 0
        
        for pattern, responses in self.patterns.items():
            match = re.search(pattern, processed_input, re.IGNORECASE)
            if match:
                # Score based on match length and position
                match_length = len(match.group(0))
                match_position = 1 - (match.start() / len(processed_input))
                score = match_length * match_position
                
                if score > best_score:
                    best_score = score
                    best_match = responses
        
        if best_match:
            return random.choice(best_match)
        
        # If no pattern matches, occasionally ask conversation starters
        if random.random() < 0.3:  # 30% chance
            return random.choice(self.conversation_starters)
        
        return random.choice(self.default_responses)
    
    def chat(self):
        """Enhanced chat loop with better user experience"""
        print(" Advanced ChatBot: Hello! I'm an advanced rule-based chatbot.")
        print("   I'm here to have meaningful conversations with you!")
        print("   Type 'quit' or 'bye' when you want to leave.")
        print("=" * 65)
        
        conversation_count = 0
        
        while True:
            try:
                user_input = input("\n You: ").strip()
                
                if not user_input:
                    print(" ChatBot: I'm listening... what would you like to talk about?")
                    continue
                
                conversation_count += 1
                
                # Check for exit commands
                if re.search(r'\b(quit|exit|bye|goodbye)\b', user_input.lower()):
                    if conversation_count > 5:
                        print(" ChatBot: We had a great conversation! Thanks for chatting with me!")
                    else:
                        print(" ChatBot: Goodbye! Hope to chat with you again soon!")
                    break
                
                response = self.get_response(user_input)
                print(f" ChatBot: {response}")
                
                # Occasionally encourage continuation
                if conversation_count % 7 == 0:
                    print("           (I'm really enjoying our conversation!)")
                
            except KeyboardInterrupt:
                print("\n ChatBot: Thanks for the chat! Have a wonderful day!")
                break
            except Exception:
                print(f" ChatBot: Oops! Something went wrong, but I'm still here to chat!")

def main():
    """Main function"""
    print(" Starting Advanced Rule-Based Chatbot...")
    chatbot = AdvancedRuleBasedChatbot()
    chatbot.chat()

if __name__ == "__main__":
    main()
