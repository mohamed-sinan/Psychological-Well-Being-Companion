import re
import random

response = {
    "hello": ["Hello, how can I help you today?"],
    "hi": ["Hello, how can I assist you today?"],
    "hey": ["Hello, how may I support you today?"],
    "(.*) family (.*)": ["Tell me more about your family.", "How do they contribute to your well-being?", "What are your family dynamics like?"],
    "(.*) love (.*)": ["What does love mean to you?", "How do you express love?", "Tell me about a memorable experience related to love."],
    "(.*) anxiety (.*)": ["How does anxiety affect your daily life?", "What coping mechanisms have you tried for anxiety?", "What triggers your anxiety the most?"],
    "(.*) depression (.*)": ["What are the main symptoms of your depression?", "How has depression impacted your life?", "Have you sought professional help for your depression?"],
    "(.*) stress (.*)": ["What situations or factors contribute to your stress?", "How do you usually manage your stress?", "Have you tried any stress-reducing techniques before?"],
    "(.*) sleep (.*)": ["How many hours of sleep do you typically get?", "Do you follow a consistent sleep schedule?", "What factors might be affecting your sleep quality?"],
    "(.*) work (.*)": ["Tell me more about your work.", "How do you feel about your current job?", "Do you find your work fulfilling?"],
    "(.*) hobbies (.*)": ["What are your favorite hobbies?", "How do your hobbies make you feel?", "Do you make time for your hobbies regularly?"],
    "(.*) goals (.*)": ["What are your short-term and long-term goals?", "How are you working towards your goals?", "Do you face any challenges in achieving your goals?"],
    "(.*) childhood (.*)": ["Tell me about your childhood.", "What were some significant experiences during your childhood?", "How do you think your childhood has shaped you as a person?"],
    "(.*) memories (.*)": ["What are some of your most cherished memories?", "Do you have any particularly difficult memories?", "How do these memories affect you currently?"],
    "(.*) future (.*)": ["What do you envision for your future?", "What steps are you taking to create the future you desire?", "Do you have any fears or uncertainties about the future?"],
    "(.*) therapy (.*)": ["Have you considered therapy before?", "What are your expectations from therapy?", "How do you think therapy can help you?"],
    "(.*) self-care (.*)": ["What does self-care mean to you?", "How do you prioritize self-care in your daily life?", "What self-care activities do you find most beneficial?"],
    "(.*) emotions (.*)": ["How do you typically express your emotions?", "Do you find it easy to identify and regulate your emotions?", "Are there any specific emotions you struggle with?"],
    "(.*) communication (.*)": ["How do you usually communicate your needs and boundaries?", "Do you feel heard and understood in your communication with others?", "What communication challenges do you face?"],
    "(.*) mindfulness (.*)": ["Have you practiced mindfulness before?", "How do you incorporate mindfulness into your daily routine?", "What benefits do you experience from practicing mindfulness?"],
    "(.*) boundaries (.*)": ["How do you set and maintain boundaries in your relationships?", "Do you feel comfortable asserting your boundaries?", "What happens when your boundaries are crossed?"],
    "(.*) motivation (.*)": ["What motivates you to take action and pursue your goals?", "How do you overcome lack of motivation?", "Have you tried any strategies to increase your motivation?"],
    "(.*) body image (.*)": ["How do you feel about your body image?", "What factors contribute to your body image perception?", "What steps can you take to improve your body image?"],
    "(.*) self-esteem (.*)": ["How do you define self-esteem?", "What activities or thoughts boost your self-esteem?", "What challenges do you face in building self-esteem?"],
    "(.*) strengths (.*)": ["What do you consider to be your strengths?", "How do you leverage your strengths in different areas of your life?", "Do you feel confident in your strengths?"],
    "(.*) challenges (.*)": ["What are some challenges you are currently facing?", "How do these challenges impact your well-being?", "What support systems do you have to overcome these challenges?"],
    "(.*) success (.*)": ["How do you define success?", "What does success look like to you?", "What steps are you taking to achieve success?"],
    "(.*) decision (.*)": ["How do you typically approach decision-making?", "What factors do you consider when making decisions?", "What decision-making strategies have worked well for you in the past?"],
    "(.*) regret (.*)": ["Do you have any regrets?", "How do you cope with feelings of regret?", "What can you learn from your past regrets?"],
    "(.*) gratitude (.*)": ["What are you grateful for in your life?", "How do you practice gratitude?", "How does gratitude impact your well-being?"],
    "(.*) change (.*)": ["How do you typically handle change?", "What are your thoughts and emotions when faced with change?", "What strategies can you use to adapt to change more effectively?"],
    "(.*) self-discovery (.*)": ["What does self-discovery mean to you?", "How do you engage in self-discovery?", "What have you learned about yourself through self-discovery?"],
    "(.*) aspirations (.*)": ["What are your aspirations in life?", "How do you plan to achieve your aspirations?", "What steps can you take to align your actions with your aspirations?"],
    "(.*) forgiveness (.*)": ["What does forgiveness mean to you?", "Have you struggled with forgiving others or yourself?", "How can forgiveness contribute to your well-being?"],
    "(.*) self-compassion (.*)": ["How do you show compassion to yourself?", "Do you find it easy to practice self-compassion?", "What barriers do you face in cultivating self-compassion?"],
    "(.*) resilience (.*)": ["What does resilience mean to you?", "How have you demonstrated resilience in the face of challenges?", "What strategies can you use to enhance your resilience?"],
    "(.*) validation (.*)": ["How do you seek validation from others?", "Do you feel validated in your relationships?", "What steps can you take to validate yourself?"],
    "i feel (.*)": ["Why do you feel {}?", "How long have you been feeling {}?", "What do you think caused your {}?"],
    "i am (.*)": ["Why do you say you are {}?", "How long have you been {}?", "What does being {} mean to you?"],
    "i (.*)": ["Why are you {}?", "How long have you been {}?", "Tell me more about your experience of being {}."],
    "i (.*) you": ["Why do you {} me?", "What makes you {} me?", "I apologize, but I am only a chatbot."],
    "i (.*) myself": ["Why do you want to {} yourself?", "What led to this desire to {} yourself?"],
    "(.*) sorry (.*)": ["There is no need to apologize.", "What are you apologizing for?", "It is okay."],
    "(.*) friend (.*)": ["Tell me more about your friend.", "How do they make you feel?", "What do you appreciate about your friendship?"],
    "yes": ["You sound certain about that.", "Can you elaborate on it?", "What makes you say yes?"],
    "no": ["Why?", "Do you mind elaborating a bit more?", "What is making you say no?"],
}

def match_response(input_text):
    for pattern, response_list in response.items():
        matches = re.search(pattern, input_text.lower())
        if matches:
            chosen_response = random.choice(response_list)
            return chosen_response.format(*matches.groups())
    return "I'm sorry, I don't understand."

print("Welcome to the Psychological Well-Being Chatbot")

user_name = input("Enter your name: ")

while True:
    print(user_name, end='')
    user_input = input(": ")
    if user_input.lower() == "bye":
        print("PSI: Goodbye")
        break
    else:
        print("PSI: " + match_response(user_input))