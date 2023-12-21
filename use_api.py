import requests

api_endpoint = 'http://localhost:8000/predict'

input_text = """
Graphic Designer

[Company Name] is looking for a talented and creative Graphic Designer to join our team. As a Graphic Designer, you will be responsible for producing visually compelling designs that resonate with our audience and align with our brand identity.

Responsibilities:

Conceptualize and create eye-catching graphics, illustrations, and layouts for various digital and print materials, including but not limited to: marketing collateral, social media content, website assets, and presentations.
Collaborate closely with the marketing and creative teams to understand project requirements and deliver designs that effectively communicate our brand message.
Maintain consistency in design elements and ensure they adhere to brand guidelines across all platforms.
Stay updated with industry trends and incorporate innovative design techniques to enhance visual storytelling.
Manage multiple design projects simultaneously and meet deadlines while maintaining high-quality standards.
Requirements:

Bachelor's degree in Graphic Design, Visual Arts, or related field (or equivalent work experience).
Proficient in graphic design software such as Adobe Creative Suite (Photoshop, Illustrator, InDesign, etc.) and other relevant tools.
Demonstrated portfolio showcasing a diverse range of design projects and creative solutions.
Strong understanding of design principles, typography, color theory, and layout techniques.
Ability to take constructive feedback and iterate designs based on feedback received.
Excellent communication skills and ability to collaborate effectively in a team environment.
Benefits:

Competitive salary commensurate with experience.
Comprehensive benefits package including health insurance and retirement plans.
Opportunities for professional development and skill enhancement.
Collaborative and supportive work environment fostering creativity and innovation.
"""

payload = {"text": input_text}
response = requests.post(api_endpoint, json=payload)

if response.status_code == 200:
    print(response.json())
else:
    print("Prediction failed")