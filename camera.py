import anthropic
import cv2
import base64
from config import ANTHROPIC_API_KEY

def capture_and_analyse():
    print("\n📸 Opening camera in 3 seconds — make sure your environment is visible!")
    
    # Open camera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ Camera not found!")
        return None
    
    print("Press SPACE to take a photo, or Q to quit")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        cv2.imshow("EnviroMusic Camera — Press SPACE to capture", frame)
        
        key = cv2.waitKey(1)
        if key == 32:  # SPACE
            photo_path = "environment.jpg"
            cv2.imwrite(photo_path, frame)
            print("✅ Photo captured!")
            break
        elif key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            return None
    
    cap.release()
    cv2.destroyAllWindows()
    
    # Send photo to Claude for analysis
    print("🤖 Analysing your environment with AI...\n")
    
    with open("environment.jpg", "rb") as f:
        image_data = base64.standard_b64encode(f.read()).decode("utf-8")
    
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": """Analyse this environment and respond with ONLY a JSON object like this:
{
    "environment": "Studying",
    "confidence": "high",
    "reason": "Person is at a desk with books and a laptop"
}
Environment must be exactly one of: Studying, Gym, Relaxing, Commuting, Sleeping, Socialising"""
                    }
                ],
            }
        ],
    )
    
    import json
    import re
    response = message.content[0].text
    
    # Extract JSON even if Claude adds extra text around it
    json_match = re.search(r'\{.*?\}', response, re.DOTALL)
    if json_match:
        result = json.loads(json_match.group())
    else:
        print("Couldn't parse environment, defaulting to Relaxing")
        return "Relaxing"
    
    print(f"🌍 Environment detected: {result['environment']}")
    print(f"📊 Confidence: {result['confidence']}")
    print(f"💭 Reason: {result['reason']}\n")
    
    return result['environment']

if __name__ == "__main__":
    capture_and_analyse()