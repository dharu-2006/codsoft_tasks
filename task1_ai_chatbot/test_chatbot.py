from advanced_chatbot import AdvancedRuleBasedChatbot

def test_chatbot_accuracy():
    """Test the chatbot's pattern matching accuracy"""
    chatbot = AdvancedRuleBasedChatbot()
    
    # Test cases with expected pattern categories
    test_cases = [
        # Greetings
        ("hello", "greeting"),
        ("hi there", "greeting"),
        ("good morning", "greeting"),
        
        # Personal questions
        ("how are you", "personal"),
        ("what's your name", "identity"),
        ("who are you", "identity"),
        
        # Capabilities
        ("what can you do", "capabilities"),
        ("help me", "capabilities"),
        
        # Emotions
        ("i feel sad", "emotions"),
        ("i am happy", "emotions"),
        
        # Technology
        ("artificial intelligence", "tech"),
        ("machine learning", "tech"),
        
        # Thank you
        ("thank you", "thanks"),
        ("thanks a lot", "thanks"),
        
        # Goodbye
        ("goodbye", "goodbye"),
        ("see you later", "goodbye"),
        
        # Agreement
        ("yes", "agreement"),
        ("okay sure", "agreement"),
        
        # Time/Date
        ("what time is it", "time"),
        ("current time", "time"),
        
        # Weather
        ("how's the weather", "weather"),
        ("is it sunny", "weather"),
    ]
    
    print(" Testing Chatbot Accuracy")
    print("=" * 40)
    
    correct_responses = 0
    total_tests = len(test_cases)
    
    for i, (test_input, expected_category) in enumerate(test_cases, 1):
        response = chatbot.get_response(test_input)
        
        # Check if response is not a default/fallback response
        is_specific_response = response not in chatbot.default_responses and \
                             response not in chatbot.conversation_starters
        
        status = " PASS" if is_specific_response else " FAIL"
        
        if is_specific_response:
            correct_responses += 1
        
        print(f"{i:2d}. Input: '{test_input}'")
        print(f"    Expected: {expected_category} response")
        print(f"    Response: '{response}'")
        print(f"    Status: {status}")
        print()
    
    accuracy = (correct_responses / total_tests) * 100
    print(f" ACCURACY RESULTS")
    print(f"   Correct: {correct_responses}/{total_tests}")
    print(f"   Accuracy: {accuracy:.1f}%")
    
    if accuracy >= 90:
        print("   Grade:  EXCELLENT")
    elif accuracy >= 80:
        print("   Grade:  GOOD")
    elif accuracy >= 70:
        print("   Grade:  ACCEPTABLE")
    else:
        print("   Grade:  NEEDS IMPROVEMENT")
    
    return accuracy

def test_preprocessing():
    """Test input preprocessing functionality"""
    chatbot = AdvancedRuleBasedChatbot()
    
    print("\n Testing Input Preprocessing")
    print("=" * 40)
    
    test_cases = [
        ("I'm happy", "i am happy"),
        ("What's up?", "what is up"),
        ("Can't help", "cannot help"),
        ("  HELLO  THERE  ", "hello there"),
        ("You're awesome!", "you are awesome"),
    ]
    
    for original, expected in test_cases:
        processed = chatbot.preprocess_input(original)
        status = " PASS" if processed == expected else " FAIL"
        print(f"'{original}' → '{processed}' (Expected: '{expected}') {status}")

def interactive_test():
    """Interactive testing mode"""
    print("\n Interactive Test Mode")
    print("Type messages to test the chatbot. Type 'exit' to quit.")
    print("=" * 50)
    
    chatbot = AdvancedRuleBasedChatbot()
    
    while True:
        user_input = input("\n Test Input: ").strip()
        
        if user_input.lower() in ['exit', 'quit']:
            break
            
        if not user_input:
            continue
            
        response = chatbot.get_response(user_input)
        is_default = response in chatbot.default_responses or \
                    response in chatbot.conversation_starters
        
        response_type = "Default/Fallback" if is_default else "Pattern Match"
        
        print(f" Response: {response}")
        print(f" Type: {response_type}")

def main():
    """Run all tests"""
    print(" CHATBOT TESTING SUITE")
    print("=" * 50)
    
    # Test accuracy
    accuracy = test_chatbot_accuracy()
    
    # Test preprocessing
    test_preprocessing()
    
    # Ask for interactive testing
    print(f"\n{'='*50}")
    choice = input("Would you like to run interactive tests? (y/n): ").lower()
    if choice in ['y', 'yes']:
        interactive_test()
    
    print(f"\n Final Accuracy Score: {accuracy:.1f}%")
    print("Testing complete!")

if __name__ == "__main__":
    main()
