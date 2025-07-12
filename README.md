SnapMap integrates the Google Gemini API to perform advanced AI-based analysis of image content, enabling accurate inference of photo locations—even without embedded GPS metadata.

Features
AI-powered geolocation of images using Google's Gemini API
Generate Google Maps links based on image coordinates
Provide confidence levels for location predictions
Support for additional context and location guesses
Export results to JSON
Handles both local image files and image URLs

Response Format
The API returns a structured JSON response with:
interpretation: Comprehensive analysis of the image
locations: Array of possible locations with:
Country, state, and city information
Confidence level (High/Medium/Low)
Coordinates (latitude/longitude)
Detailed explanation of the reasoning
